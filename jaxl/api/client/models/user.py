"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset


T = TypeVar("T", bound="User")


@attr.s(auto_attribs=True)
class User:
    """Adds a 'jaxlid' field which contains signed ID information.

    Attributes:
        id (int):
        url (str):
        username (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
        email (Union[Unset, str]):
        jaxlid (Optional[str]):
    """

    id: int
    url: str
    username: str
    jaxlid: Optional[str]
    email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        username = self.username
        email = self.email
        jaxlid = self.jaxlid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "username": username,
                "jaxlid": jaxlid,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        username = d.pop("username")

        email = d.pop("email", UNSET)

        jaxlid = d.pop("jaxlid")

        user = cls(
            id=id,
            url=url,
            username=username,
            email=email,
            jaxlid=jaxlid,
        )

        user.additional_properties = d
        return user

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
