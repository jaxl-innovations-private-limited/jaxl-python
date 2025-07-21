"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar

import attr


T = TypeVar("T", bound="TranscriptionWord")


@attr.s(auto_attribs=True)
class TranscriptionWord:
    """
    Attributes:
        end_time (str):
        start_time (str):
        word (str):
    """

    end_time: str
    start_time: str
    word: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        end_time = self.end_time
        start_time = self.start_time
        word = self.word

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endTime": end_time,
                "startTime": start_time,
                "word": word,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        end_time = d.pop("endTime")

        start_time = d.pop("startTime")

        word = d.pop("word")

        transcription_word = cls(
            end_time=end_time,
            start_time=start_time,
            word=word,
        )

        transcription_word.additional_properties = d
        return transcription_word

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
