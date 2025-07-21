"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from io import BytesIO
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.greeting_type_enum import GreetingTypeEnum
from ..models.language_enum import LanguageEnum
from ..models.scenario_enum import ScenarioEnum
from ..models.voice_enum import VoiceEnum
from ..types import UNSET, File, FileJsonType, Unset


T = TypeVar("T", bound="GreetingCreationRequestRequest")


@attr.s(auto_attribs=True)
class GreetingCreationRequestRequest:
    """
    Attributes:
        scenario (ScenarioEnum):
        greeting_type (GreetingTypeEnum):
        text (Union[Unset, None, str]): Text message of the greeting. Can only be used with text greeting type
        language (Union[Unset, LanguageEnum]):
        repeat_after (Union[Unset, int]): Number of seconds in between greeting repetitions
        scenario_key (Union[Unset, str]):
        voice (Union[Unset, VoiceEnum]):
        library_id (Union[Unset, None, int]): UserUpload pk of existing audio that has been picked from the library
        silence_audio_id (Union[Unset, None, int]): Greeting pk of silence audio (Greeting) that has been picked from
            the library
        file (Union[Unset, File]):
    """

    scenario: ScenarioEnum
    greeting_type: GreetingTypeEnum
    text: Union[Unset, None, str] = UNSET
    language: Union[Unset, LanguageEnum] = UNSET
    repeat_after: Union[Unset, int] = UNSET
    scenario_key: Union[Unset, str] = UNSET
    voice: Union[Unset, VoiceEnum] = UNSET
    library_id: Union[Unset, None, int] = UNSET
    silence_audio_id: Union[Unset, None, int] = UNSET
    file: Union[Unset, File] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scenario = self.scenario.value

        greeting_type = self.greeting_type.value

        text = self.text
        language: Union[Unset, str] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.value

        repeat_after = self.repeat_after
        scenario_key = self.scenario_key
        voice: Union[Unset, str] = UNSET
        if not isinstance(self.voice, Unset):
            voice = self.voice.value

        library_id = self.library_id
        silence_audio_id = self.silence_audio_id
        file: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scenario": scenario,
                "greeting_type": greeting_type,
            }
        )
        if text is not UNSET:
            field_dict["text"] = text
        if language is not UNSET:
            field_dict["language"] = language
        if repeat_after is not UNSET:
            field_dict["repeat_after"] = repeat_after
        if scenario_key is not UNSET:
            field_dict["scenario_key"] = scenario_key
        if voice is not UNSET:
            field_dict["voice"] = voice
        if library_id is not UNSET:
            field_dict["library_id"] = library_id
        if silence_audio_id is not UNSET:
            field_dict["silence_audio_id"] = silence_audio_id
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        scenario = (None, str(self.scenario.value).encode(), "text/plain")

        greeting_type = (None, str(self.greeting_type.value).encode(), "text/plain")

        text = (
            self.text
            if isinstance(self.text, Unset)
            else (None, str(self.text).encode(), "text/plain")
        )
        language: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.language, Unset):
            language = (None, str(self.language.value).encode(), "text/plain")

        repeat_after = (
            self.repeat_after
            if isinstance(self.repeat_after, Unset)
            else (None, str(self.repeat_after).encode(), "text/plain")
        )
        scenario_key = (
            self.scenario_key
            if isinstance(self.scenario_key, Unset)
            else (None, str(self.scenario_key).encode(), "text/plain")
        )
        voice: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.voice, Unset):
            voice = (None, str(self.voice.value).encode(), "text/plain")

        library_id = (
            self.library_id
            if isinstance(self.library_id, Unset)
            else (None, str(self.library_id).encode(), "text/plain")
        )
        silence_audio_id = (
            self.silence_audio_id
            if isinstance(self.silence_audio_id, Unset)
            else (None, str(self.silence_audio_id).encode(), "text/plain")
        )
        file: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                key: (None, str(value).encode(), "text/plain")
                for key, value in self.additional_properties.items()
            }
        )
        field_dict.update(
            {
                "scenario": scenario,
                "greeting_type": greeting_type,
            }
        )
        if text is not UNSET:
            field_dict["text"] = text
        if language is not UNSET:
            field_dict["language"] = language
        if repeat_after is not UNSET:
            field_dict["repeat_after"] = repeat_after
        if scenario_key is not UNSET:
            field_dict["scenario_key"] = scenario_key
        if voice is not UNSET:
            field_dict["voice"] = voice
        if library_id is not UNSET:
            field_dict["library_id"] = library_id
        if silence_audio_id is not UNSET:
            field_dict["silence_audio_id"] = silence_audio_id
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        scenario = ScenarioEnum(d.pop("scenario"))

        greeting_type = GreetingTypeEnum(d.pop("greeting_type"))

        text = d.pop("text", UNSET)

        _language = d.pop("language", UNSET)
        language: Union[Unset, LanguageEnum]
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = LanguageEnum(_language)

        repeat_after = d.pop("repeat_after", UNSET)

        scenario_key = d.pop("scenario_key", UNSET)

        _voice = d.pop("voice", UNSET)
        voice: Union[Unset, VoiceEnum]
        if isinstance(_voice, Unset):
            voice = UNSET
        else:
            voice = VoiceEnum(_voice)

        library_id = d.pop("library_id", UNSET)

        silence_audio_id = d.pop("silence_audio_id", UNSET)

        _file = d.pop("file", UNSET)
        file: Union[Unset, File]
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = File(payload=BytesIO(_file))

        greeting_creation_request_request = cls(
            scenario=scenario,
            greeting_type=greeting_type,
            text=text,
            language=language,
            repeat_after=repeat_after,
            scenario_key=scenario_key,
            voice=voice,
            library_id=library_id,
            silence_audio_id=silence_audio_id,
            file=file,
        )

        greeting_creation_request_request.additional_properties = d
        return greeting_creation_request_request

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
