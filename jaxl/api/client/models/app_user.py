"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..models.platform_enum import PlatformEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppUser")


@attr.s(auto_attribs=True)
class AppUser:
    """Adds a 'jaxlid' field which contains signed ID information.

    Attributes:
        id (int):
        user (int):
        platform (PlatformEnum):
        account (Union[Unset, int]): Defaults to 0.  This value gets incremented when a user creates a new account on
            the app after deleting their previous app user accounts.
        verified (Union[Unset, bool]): Whether user email has been verified.
        jaxlid (Optional[str]):
    """

    id: int
    user: int
    platform: PlatformEnum
    jaxlid: Optional[str]
    account: Union[Unset, int] = UNSET
    verified: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        user = self.user
        platform = self.platform.value

        account = self.account
        verified = self.verified
        jaxlid = self.jaxlid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user": user,
                "platform": platform,
                "jaxlid": jaxlid,
            }
        )
        if account is not UNSET:
            field_dict["account"] = account
        if verified is not UNSET:
            field_dict["verified"] = verified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        user = d.pop("user")

        platform = PlatformEnum(d.pop("platform"))

        account = d.pop("account", UNSET)

        verified = d.pop("verified", UNSET)

        jaxlid = d.pop("jaxlid")

        app_user = cls(
            id=id,
            user=user,
            platform=platform,
            account=account,
            verified=verified,
            jaxlid=jaxlid,
        )

        app_user.additional_properties = d
        return app_user

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
