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


T = TypeVar("T", bound="ListMember")


@attr.s(auto_attribs=True)
class ListMember:
    """
    Attributes:
        identity (str):
        created_on (datetime.datetime): Datetime when this object was created
        is_admin (Union[Unset, None, bool]):
        left_at (Union[Unset, None, datetime.datetime]):
    """

    identity: str
    created_on: datetime.datetime
    is_admin: Union[Unset, None, bool] = UNSET
    left_at: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identity = self.identity
        created_on = self.created_on.isoformat()

        is_admin = self.is_admin
        left_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.left_at, Unset):
            left_at = self.left_at.isoformat() if self.left_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identity": identity,
                "created_on": created_on,
            }
        )
        if is_admin is not UNSET:
            field_dict["is_admin"] = is_admin
        if left_at is not UNSET:
            field_dict["left_at"] = left_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        identity = d.pop("identity")

        created_on = isoparse(d.pop("created_on"))

        is_admin = d.pop("is_admin", UNSET)

        _left_at = d.pop("left_at", UNSET)
        left_at: Union[Unset, None, datetime.datetime]
        if _left_at is None:
            left_at = None
        elif isinstance(_left_at, Unset):
            left_at = UNSET
        else:
            left_at = isoparse(_left_at)

        list_member = cls(
            identity=identity,
            created_on=created_on,
            is_admin=is_admin,
            left_at=left_at,
        )

        list_member.additional_properties = d
        return list_member

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
