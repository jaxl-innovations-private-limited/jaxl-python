"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.transcription_word_position_response import (
        TranscriptionWordPositionResponse,
    )


T = TypeVar("T", bound="TranscriptionWordSearchResponse")


@attr.s(auto_attribs=True)
class TranscriptionWordSearchResponse:
    """
    Attributes:
        hs (TranscriptionWordPositionResponse):
        he (TranscriptionWordPositionResponse):
        start_time (str):
        end_time (str):
        channel_tag (int):
        language_code (str):
        score (float):
    """

    hs: "TranscriptionWordPositionResponse"
    he: "TranscriptionWordPositionResponse"
    start_time: str
    end_time: str
    channel_tag: int
    language_code: str
    score: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hs = self.hs.to_dict()

        he = self.he.to_dict()

        start_time = self.start_time
        end_time = self.end_time
        channel_tag = self.channel_tag
        language_code = self.language_code
        score = self.score

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hs": hs,
                "he": he,
                "start_time": start_time,
                "end_time": end_time,
                "channel_tag": channel_tag,
                "language_code": language_code,
                "score": score,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.transcription_word_position_response import (
            TranscriptionWordPositionResponse,
        )

        d = src_dict.copy()
        hs = TranscriptionWordPositionResponse.from_dict(d.pop("hs"))

        he = TranscriptionWordPositionResponse.from_dict(d.pop("he"))

        start_time = d.pop("start_time")

        end_time = d.pop("end_time")

        channel_tag = d.pop("channel_tag")

        language_code = d.pop("language_code")

        score = d.pop("score")

        transcription_word_search_response = cls(
            hs=hs,
            he=he,
            start_time=start_time,
            end_time=end_time,
            channel_tag=channel_tag,
            language_code=language_code,
            score=score,
        )

        transcription_word_search_response.additional_properties = d
        return transcription_word_search_response

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
