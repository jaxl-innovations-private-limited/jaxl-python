"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.integrations_request_provider_enum import IntegrationsRequestProviderEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.integrations_properties_request import IntegrationsPropertiesRequest


T = TypeVar("T", bound="IntegrationsRequestRequest")


@attr.s(auto_attribs=True)
class IntegrationsRequestRequest:
    """
    Attributes:
        provider (IntegrationsRequestProviderEnum):
        properties (IntegrationsPropertiesRequest):
        success_url (Union[Unset, None, str]):
        failure_url (Union[Unset, None, str]):
    """

    provider: IntegrationsRequestProviderEnum
    properties: "IntegrationsPropertiesRequest"
    success_url: Union[Unset, None, str] = UNSET
    failure_url: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        provider = self.provider.value

        properties = self.properties.to_dict()

        success_url = self.success_url
        failure_url = self.failure_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "properties": properties,
            }
        )
        if success_url is not UNSET:
            field_dict["success_url"] = success_url
        if failure_url is not UNSET:
            field_dict["failure_url"] = failure_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.integrations_properties_request import (
            IntegrationsPropertiesRequest,
        )

        d = src_dict.copy()
        provider = IntegrationsRequestProviderEnum(d.pop("provider"))

        properties = IntegrationsPropertiesRequest.from_dict(d.pop("properties"))

        success_url = d.pop("success_url", UNSET)

        failure_url = d.pop("failure_url", UNSET)

        integrations_request_request = cls(
            provider=provider,
            properties=properties,
            success_url=success_url,
            failure_url=failure_url,
        )

        integrations_request_request.additional_properties = d
        return integrations_request_request

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
