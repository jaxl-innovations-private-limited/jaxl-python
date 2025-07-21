"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.language_enum import LanguageEnum
from ..models.voice_enum import VoiceEnum
from ..types import UNSET, Unset


T = TypeVar("T", bound="TtsRequestRequest")


@attr.s(auto_attribs=True)
class TtsRequestRequest:
    """
    Attributes:
        text (str):
        language (Union[Unset, LanguageEnum]):
        voice (Union[Unset, VoiceEnum]):
    """

    text: str
    language: Union[Unset, LanguageEnum] = UNSET
    voice: Union[Unset, VoiceEnum] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text
        language: Union[Unset, str] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.value

        voice: Union[Unset, str] = UNSET
        if not isinstance(self.voice, Unset):
            voice = self.voice.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
            }
        )
        if language is not UNSET:
            field_dict["language"] = language
        if voice is not UNSET:
            field_dict["voice"] = voice

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text")

        _language = d.pop("language", UNSET)
        language: Union[Unset, LanguageEnum]
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = LanguageEnum(_language)

        _voice = d.pop("voice", UNSET)
        voice: Union[Unset, VoiceEnum]
        if isinstance(_voice, Unset):
            voice = UNSET
        else:
            voice = VoiceEnum(_voice)

        tts_request_request = cls(
            text=text,
            language=language,
            voice=voice,
        )

        tts_request_request.additional_properties = d
        return tts_request_request

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
