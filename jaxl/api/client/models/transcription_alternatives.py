"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.transcription_word import TranscriptionWord


T = TypeVar("T", bound="TranscriptionAlternatives")


@attr.s(auto_attribs=True)
class TranscriptionAlternatives:
    """
    Attributes:
        words (List['TranscriptionWord']):
        confidence (Union[Unset, float]):
        transcript (Union[Unset, str]):
    """

    words: List["TranscriptionWord"]
    confidence: Union[Unset, float] = UNSET
    transcript: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        words = []
        for words_item_data in self.words:
            words_item = words_item_data.to_dict()

            words.append(words_item)

        confidence = self.confidence
        transcript = self.transcript

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "words": words,
            }
        )
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if transcript is not UNSET:
            field_dict["transcript"] = transcript

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.transcription_word import TranscriptionWord

        d = src_dict.copy()
        words = []
        _words = d.pop("words")
        for words_item_data in _words:
            words_item = TranscriptionWord.from_dict(words_item_data)

            words.append(words_item)

        confidence = d.pop("confidence", UNSET)

        transcript = d.pop("transcript", UNSET)

        transcription_alternatives = cls(
            words=words,
            confidence=confidence,
            transcript=transcript,
        )

        transcription_alternatives.additional_properties = d
        return transcription_alternatives

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
