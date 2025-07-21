"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.device_token_provider_enum import DeviceTokenProviderEnum


T = TypeVar("T", bound="DeviceTokenRequest")


@attr.s(auto_attribs=True)
class DeviceTokenRequest:
    """
    Attributes:
        provider (DeviceTokenProviderEnum):
        token (str): FCM tokens are max 255, while APNS tokens are 160 char in length
    """

    provider: DeviceTokenProviderEnum
    token: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        provider = self.provider.value

        token = self.token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "token": token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        provider = DeviceTokenProviderEnum(d.pop("provider"))

        token = d.pop("token")

        device_token_request = cls(
            provider=provider,
            token=token,
        )

        device_token_request.additional_properties = d
        return device_token_request

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
