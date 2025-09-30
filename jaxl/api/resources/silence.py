"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Optional


# pylint: disable=too-many-instance-attributes
class SilenceDetector:
    """Edge-triggered VAD wrapper around py-webrtcvad."""

    # pylint: disable=too-many-positional-arguments
    def __init__(
        self,
        sample_rate: int = 8000,
        frame_duration_ms: int = 20,
        aggressiveness: int = 2,
        silence_frame_threshold: int = 15,  # ~300ms
        speech_frame_threshold: int = 20,  # ~400ms
    ):
        import webrtcvad

        self.sample_rate = sample_rate
        self.frame_duration_ms = frame_duration_ms
        self.aggressiveness = aggressiveness
        self.frame_size = int(self.sample_rate * self.frame_duration_ms / 1000)
        self.vad = webrtcvad.Vad(self.aggressiveness)

        self.speech_frame_threshold = speech_frame_threshold
        self.silence_frame_threshold = silence_frame_threshold
        self.is_talking = False
        self.speech_frames = 0
        self.silence_frames = 0
        self.buffer = b""

    def process(self, slin16: bytes) -> Optional[bool]:
        """Process PCM16 mono audio. Returns:
        - True once on speech start
        - False once on speech end
        - None if no change
        """
        self.buffer += slin16
        change = None

        while len(self.buffer) >= self.frame_size * 2:
            frame, self.buffer = (
                self.buffer[: self.frame_size * 2],
                self.buffer[self.frame_size * 2 :],
            )

            is_speech = self.vad.is_speech(frame, self.sample_rate)

            if is_speech:
                self.speech_frames += 1
                self.silence_frames = 0
                if (
                    not self.is_talking
                    and self.speech_frames > self.speech_frame_threshold
                ):
                    change = True  # silence -> speech
                    self.is_talking = True
            else:
                self.silence_frames += 1
                self.speech_frames = 0
                if (
                    self.is_talking
                    and self.silence_frames > self.silence_frame_threshold
                ):
                    change = False  # speech -> silence
                    self.is_talking = False

        return change

    def reset(self) -> None:
        self.buffer = b""
        self.silence_frames = 0
        self.speech_frames = 0
        self.is_talking = False
