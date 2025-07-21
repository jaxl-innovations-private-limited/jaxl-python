"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.language_enum import LanguageEnum
from ..models.scenario_enum import ScenarioEnum
from ..models.voice_enum import VoiceEnum
from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.greeting import Greeting
    from ..models.upload import Upload


T = TypeVar("T", bound="GreetingConfigurationResponse")


@attr.s(auto_attribs=True)
class GreetingConfigurationResponse:
    """
    Attributes:
        id (int):
        greeting (Greeting):
        active (bool):
        scenario (ScenarioEnum):
        created_on (datetime.datetime):
        modified_on (datetime.datetime):
        voice (Union[Unset, VoiceEnum]):
        language (Union[Unset, LanguageEnum]):
        repeat_after (Union[Unset, int]):
        silence_audio (Union[Unset, Upload]):
        scenario_key (Union[Unset, str]):
    """

    id: int
    greeting: "Greeting"
    active: bool
    scenario: ScenarioEnum
    created_on: datetime.datetime
    modified_on: datetime.datetime
    voice: Union[Unset, VoiceEnum] = UNSET
    language: Union[Unset, LanguageEnum] = UNSET
    repeat_after: Union[Unset, int] = UNSET
    silence_audio: Union[Unset, "Upload"] = UNSET
    scenario_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        greeting = self.greeting.to_dict()

        active = self.active
        scenario = self.scenario.value

        created_on = self.created_on.isoformat()

        modified_on = self.modified_on.isoformat()

        voice: Union[Unset, str] = UNSET
        if not isinstance(self.voice, Unset):
            voice = self.voice.value

        language: Union[Unset, str] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.value

        repeat_after = self.repeat_after
        silence_audio: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.silence_audio, Unset):
            silence_audio = self.silence_audio.to_dict()

        scenario_key = self.scenario_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "greeting": greeting,
                "active": active,
                "scenario": scenario,
                "created_on": created_on,
                "modified_on": modified_on,
            }
        )
        if voice is not UNSET:
            field_dict["voice"] = voice
        if language is not UNSET:
            field_dict["language"] = language
        if repeat_after is not UNSET:
            field_dict["repeat_after"] = repeat_after
        if silence_audio is not UNSET:
            field_dict["silence_audio"] = silence_audio
        if scenario_key is not UNSET:
            field_dict["scenario_key"] = scenario_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.greeting import Greeting
        from ..models.upload import Upload

        d = src_dict.copy()
        id = d.pop("id")

        greeting = Greeting.from_dict(d.pop("greeting"))

        active = d.pop("active")

        scenario = ScenarioEnum(d.pop("scenario"))

        created_on = isoparse(d.pop("created_on"))

        modified_on = isoparse(d.pop("modified_on"))

        _voice = d.pop("voice", UNSET)
        voice: Union[Unset, VoiceEnum]
        if isinstance(_voice, Unset):
            voice = UNSET
        else:
            voice = VoiceEnum(_voice)

        _language = d.pop("language", UNSET)
        language: Union[Unset, LanguageEnum]
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = LanguageEnum(_language)

        repeat_after = d.pop("repeat_after", UNSET)

        _silence_audio = d.pop("silence_audio", UNSET)
        silence_audio: Union[Unset, Upload]
        if isinstance(_silence_audio, Unset):
            silence_audio = UNSET
        else:
            silence_audio = Upload.from_dict(_silence_audio)

        scenario_key = d.pop("scenario_key", UNSET)

        greeting_configuration_response = cls(
            id=id,
            greeting=greeting,
            active=active,
            scenario=scenario,
            created_on=created_on,
            modified_on=modified_on,
            voice=voice,
            language=language,
            repeat_after=repeat_after,
            silence_audio=silence_audio,
            scenario_key=scenario_key,
        )

        greeting_configuration_response.additional_properties = d
        return greeting_configuration_response

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
