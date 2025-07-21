"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.otp_provider_enum import OtpProviderEnum
from ..models.platform_enum import PlatformEnum


T = TypeVar("T", bound="OtpRequest")


@attr.s(auto_attribs=True)
class OtpRequest:
    """
    Attributes:
        identifier (str):
        platform (PlatformEnum):
        provider (OtpProviderEnum):
    """

    identifier: str
    platform: PlatformEnum
    provider: OtpProviderEnum
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identifier = self.identifier
        platform = self.platform.value

        provider = self.provider.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "platform": platform,
                "provider": provider,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        identifier = d.pop("identifier")

        platform = PlatformEnum(d.pop("platform"))

        provider = OtpProviderEnum(d.pop("provider"))

        otp_request = cls(
            identifier=identifier,
            platform=platform,
            provider=provider,
        )

        otp_request.additional_properties = d
        return otp_request

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
