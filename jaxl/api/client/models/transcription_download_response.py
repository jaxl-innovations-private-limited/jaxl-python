"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.locale_enum import LocaleEnum


T = TypeVar("T", bound="TranscriptionDownloadResponse")


@attr.s(auto_attribs=True)
class TranscriptionDownloadResponse:
    """
    Attributes:
        encrypted (str):
        mimetype (str):
        sha (str):
        size (int):
        transcription_id (int):
        locale (LocaleEnum):
    """

    encrypted: str
    mimetype: str
    sha: str
    size: int
    transcription_id: int
    locale: LocaleEnum
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        encrypted = self.encrypted
        mimetype = self.mimetype
        sha = self.sha
        size = self.size
        transcription_id = self.transcription_id
        locale = self.locale.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "encrypted": encrypted,
                "mimetype": mimetype,
                "sha": sha,
                "size": size,
                "transcription_id": transcription_id,
                "locale": locale,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        encrypted = d.pop("encrypted")

        mimetype = d.pop("mimetype")

        sha = d.pop("sha")

        size = d.pop("size")

        transcription_id = d.pop("transcription_id")

        locale = LocaleEnum(d.pop("locale"))

        transcription_download_response = cls(
            encrypted=encrypted,
            mimetype=mimetype,
            sha=sha,
            size=size,
            transcription_id=transcription_id,
            locale=locale,
        )

        transcription_download_response.additional_properties = d
        return transcription_download_response

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
