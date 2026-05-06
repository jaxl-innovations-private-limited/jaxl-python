"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from collections import deque
from typing import Deque, Optional


# pylint: disable=too-many-instance-attributes
class SilenceDetector:
    """Edge-triggered VAD wrapper around py-webrtcvad.

    Streaming contract: feed PCM16 mono audio one chunk at a time via
    ``process()``. The method returns:

    - ``True`` once on the speech-start edge
    - ``False`` once on the speech-end edge
    - ``None`` while no edge has been detected on this call

    Preroll buffer (FIX for head clipping)
    --------------------------------------
    By design, ``speech_frame_threshold`` consecutive speech frames must
    elapse before the detector declares speech-start. Those trigger
    frames carry the actual onset of the user's utterance (e.g. the "h"
    in "haan") and previously had no public surface for callers to
    recover them — at best the caller kept a tiny rolling preroll that
    was smaller than the trigger window, and the very first speech frame
    was always lost.

    The detector now maintains its own ``preroll`` deque that captures
    every processed frame. When speech-start fires, the caller MUST call
    ``consume_preroll()`` to retrieve those frames and prepend them to
    the audio it forwards to ASR. ``consume_preroll`` returns the bytes
    AND clears the buffer, so subsequent calls within the same speech
    segment are safe (return empty).

    The preroll size is configurable but defaults to a slightly larger
    window than ``speech_frame_threshold`` so the caller also receives a
    small amount of audio captured just BEFORE the trigger window — this
    catches consonant onsets that webrtcvad sometimes fails to flag as
    speech (e.g. "h", "f", "s") but still belong to the utterance.
    """

    # pylint: disable=too-many-positional-arguments
    def __init__(
        self,
        sample_rate: int = 8000,
        frame_duration_ms: int = 20,
        aggressiveness: int = 2,
        silence_frame_threshold: int = 12,  # ~240ms
        speech_frame_threshold: int = 5,  # ~100ms
        preroll_frames: Optional[int] = None,
    ):
        import webrtcvad

        self.sample_rate = sample_rate
        self.frame_duration_ms = frame_duration_ms
        self.aggressiveness = aggressiveness
        self.frame_size = int(self.sample_rate * self.frame_duration_ms / 1000)
        self.vad = webrtcvad.Vad(self.aggressiveness)

        self.speech_frame_threshold = speech_frame_threshold
        self.silence_frame_threshold = silence_frame_threshold

        # Preroll covers AT LEAST the trigger window plus a few extra frames
        # of pre-trigger audio, so the caller never sees a truncated onset.
        # Five extra frames (~100ms) is enough to recover voiceless
        # consonants that VAD initially missed while keeping memory tiny.
        if preroll_frames is None:
            preroll_frames = speech_frame_threshold + 5

        self.is_talking = False
        self.speech_frames = 0
        self.silence_frames = 0
        self.buffer = b""
        self.last_frame_is_speech: Optional[bool] = None
        self._preroll: Deque[bytes] = deque(maxlen=preroll_frames)

    def process(self, slin16: bytes) -> Optional[bool]:
        """Process PCM16 mono audio. Returns:
        - True once on speech start
        - False once on speech end
        - None if no change

        Side-effect: every fully formed frame is appended to the preroll
        buffer. On the speech-start edge the caller should call
        ``consume_preroll()`` to retrieve the trigger frames.
        """
        self.buffer += slin16
        change = None

        while len(self.buffer) >= self.frame_size * 2:
            frame, self.buffer = (
                self.buffer[: self.frame_size * 2],
                self.buffer[self.frame_size * 2 :],
            )

            # Always preserve the frame in the preroll. Bounded by maxlen,
            # so memory is O(preroll_frames) regardless of call duration.
            self._preroll.append(frame)

            is_speech = self.vad.is_speech(frame, self.sample_rate)
            self.last_frame_is_speech = is_speech

            if is_speech:
                self.speech_frames += 1
                self.silence_frames = 0
                if (
                    not self.is_talking
                    and self.speech_frames >= self.speech_frame_threshold
                ):
                    change = True  # silence -> speech
                    self.is_talking = True
            else:
                self.silence_frames += 1
                self.speech_frames = 0
                if (
                    self.is_talking
                    and self.silence_frames >= self.silence_frame_threshold
                ):
                    change = False  # speech -> silence
                    self.is_talking = False

        return change

    def consume_preroll(self) -> bytes:
        """Return the preroll buffer as concatenated PCM16 bytes and clear it.

        Call this immediately after ``process()`` returns ``True`` (the
        speech-start edge). The returned bytes contain the frames that
        triggered the start plus a few preceding frames for context, and
        should be prepended to the audio stream forwarded to ASR.

        Subsequent calls within the same speech segment return ``b""``.
        """
        out = b"".join(self._preroll)
        self._preroll.clear()
        return out

    def reset(self) -> None:
        self.buffer = b""
        self.silence_frames = 0
        self.speech_frames = 0
        self.is_talking = False
        self.last_frame_is_speech = None
        self._preroll.clear()
