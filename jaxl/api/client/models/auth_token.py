"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar

import attr
from dateutil.parser import isoparse


T = TypeVar("T", bound="AuthToken")


@attr.s(auto_attribs=True)
class AuthToken:
    """
    Attributes:
        id (int):
        name (str): Name assigned to this auth token.
        expires_on (datetime.datetime): Datetime when this token expires
        token (Optional[str]):
    """

    id: int
    name: str
    expires_on: datetime.datetime
    token: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        expires_on = self.expires_on.isoformat()

        token = self.token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "expires_on": expires_on,
                "token": token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        expires_on = isoparse(d.pop("expires_on"))

        token = d.pop("token")

        auth_token = cls(
            id=id,
            name=name,
            expires_on=expires_on,
            token=token,
        )

        auth_token.additional_properties = d
        return auth_token

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
