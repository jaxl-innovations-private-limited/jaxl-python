"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadMetadata")


@attr.s(auto_attribs=True)
class UploadMetadata:
    """
    Attributes:
        expires_on (Union[Unset, None, datetime.datetime]): Datetime after which backend will delete the upload from
            infrastructure
        expired_on (Union[Unset, None, datetime.datetime]): Datetime when this file was marked as expired by the
            infrastructure
    """

    expires_on: Union[Unset, None, datetime.datetime] = UNSET
    expired_on: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        expires_on: Union[Unset, None, str] = UNSET
        if not isinstance(self.expires_on, Unset):
            expires_on = self.expires_on.isoformat() if self.expires_on else None

        expired_on: Union[Unset, None, str] = UNSET
        if not isinstance(self.expired_on, Unset):
            expired_on = self.expired_on.isoformat() if self.expired_on else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expires_on is not UNSET:
            field_dict["expires_on"] = expires_on
        if expired_on is not UNSET:
            field_dict["expired_on"] = expired_on

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _expires_on = d.pop("expires_on", UNSET)
        expires_on: Union[Unset, None, datetime.datetime]
        if _expires_on is None:
            expires_on = None
        elif isinstance(_expires_on, Unset):
            expires_on = UNSET
        else:
            expires_on = isoparse(_expires_on)

        _expired_on = d.pop("expired_on", UNSET)
        expired_on: Union[Unset, None, datetime.datetime]
        if _expired_on is None:
            expired_on = None
        elif isinstance(_expired_on, Unset):
            expired_on = UNSET
        else:
            expired_on = isoparse(_expired_on)

        upload_metadata = cls(
            expires_on=expires_on,
            expired_on=expired_on,
        )

        upload_metadata.additional_properties = d
        return upload_metadata

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
