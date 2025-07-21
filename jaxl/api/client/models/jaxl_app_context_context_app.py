"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..models.environment_enum import EnvironmentEnum
from ..models.jaxl_app_context_context_app_type_enum import (
    JaxlAppContextContextAppTypeEnum,
)
from ..types import UNSET, Unset


T = TypeVar("T", bound="JaxlAppContextContextApp")


@attr.s(auto_attribs=True)
class JaxlAppContextContextApp:
    """
    Attributes:
        environment (EnvironmentEnum):
        id (int):
        type (JaxlAppContextContextAppTypeEnum):
        token_ttl (int):
        vapid_key (Optional[str]):
        appstore (Union[Unset, None, str]):
        playstore (Union[Unset, None, str]):
        static_url (Optional[str]):
        api_key (Optional[str]):
        api_token (Optional[str]):
        csrf_token (Optional[str]):
    """

    environment: EnvironmentEnum
    id: int
    type: JaxlAppContextContextAppTypeEnum
    token_ttl: int
    vapid_key: Optional[str]
    static_url: Optional[str]
    api_key: Optional[str]
    api_token: Optional[str]
    csrf_token: Optional[str]
    appstore: Union[Unset, None, str] = UNSET
    playstore: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        environment = self.environment.value

        id = self.id
        type = self.type.value

        token_ttl = self.token_ttl
        vapid_key = self.vapid_key
        appstore = self.appstore
        playstore = self.playstore
        static_url = self.static_url
        api_key = self.api_key
        api_token = self.api_token
        csrf_token = self.csrf_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "environment": environment,
                "id": id,
                "type": type,
                "token_ttl": token_ttl,
                "vapid_key": vapid_key,
                "static_url": static_url,
                "api_key": api_key,
                "api_token": api_token,
                "csrf_token": csrf_token,
            }
        )
        if appstore is not UNSET:
            field_dict["appstore"] = appstore
        if playstore is not UNSET:
            field_dict["playstore"] = playstore

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        environment = EnvironmentEnum(d.pop("environment"))

        id = d.pop("id")

        type = JaxlAppContextContextAppTypeEnum(d.pop("type"))

        token_ttl = d.pop("token_ttl")

        vapid_key = d.pop("vapid_key")

        appstore = d.pop("appstore", UNSET)

        playstore = d.pop("playstore", UNSET)

        static_url = d.pop("static_url")

        api_key = d.pop("api_key")

        api_token = d.pop("api_token")

        csrf_token = d.pop("csrf_token")

        jaxl_app_context_context_app = cls(
            environment=environment,
            id=id,
            type=type,
            token_ttl=token_ttl,
            vapid_key=vapid_key,
            appstore=appstore,
            playstore=playstore,
            static_url=static_url,
            api_key=api_key,
            api_token=api_token,
            csrf_token=csrf_token,
        )

        jaxl_app_context_context_app.additional_properties = d
        return jaxl_app_context_context_app

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
