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
    from ..models.transcription_alternatives import TranscriptionAlternatives


T = TypeVar("T", bound="TranscriptionResult")


@attr.s(auto_attribs=True)
class TranscriptionResult:
    """
    Attributes:
        alternatives (Union[Unset, List['TranscriptionAlternatives']]):
        channel_tag (Union[Unset, int]):
        language_code (Union[Unset, str]):
        result_end_time (Union[Unset, str]):
    """

    alternatives: Union[Unset, List["TranscriptionAlternatives"]] = UNSET
    channel_tag: Union[Unset, int] = UNSET
    language_code: Union[Unset, str] = UNSET
    result_end_time: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alternatives: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.alternatives, Unset):
            alternatives = []
            for alternatives_item_data in self.alternatives:
                alternatives_item = alternatives_item_data.to_dict()

                alternatives.append(alternatives_item)

        channel_tag = self.channel_tag
        language_code = self.language_code
        result_end_time = self.result_end_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alternatives is not UNSET:
            field_dict["alternatives"] = alternatives
        if channel_tag is not UNSET:
            field_dict["channelTag"] = channel_tag
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code
        if result_end_time is not UNSET:
            field_dict["resultEndTime"] = result_end_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.transcription_alternatives import (
            TranscriptionAlternatives,
        )

        d = src_dict.copy()
        alternatives = []
        _alternatives = d.pop("alternatives", UNSET)
        for alternatives_item_data in _alternatives or []:
            alternatives_item = TranscriptionAlternatives.from_dict(
                alternatives_item_data
            )

            alternatives.append(alternatives_item)

        channel_tag = d.pop("channelTag", UNSET)

        language_code = d.pop("languageCode", UNSET)

        result_end_time = d.pop("resultEndTime", UNSET)

        transcription_result = cls(
            alternatives=alternatives,
            channel_tag=channel_tag,
            language_code=language_code,
            result_end_time=result_end_time,
        )

        transcription_result.additional_properties = d
        return transcription_result

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
