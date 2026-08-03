"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="NimbusPostAuthRequestRequest")


@attr.s(auto_attribs=True)
class NimbusPostAuthRequestRequest:
    """
    Attributes:
        api_key (str):
        api_secret (str):
        webhook_secret (Union[Unset, None, str]):
    """

    api_key: str
    api_secret: str
    webhook_secret: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api_key = self.api_key
        api_secret = self.api_secret
        webhook_secret = self.webhook_secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "api_key": api_key,
                "api_secret": api_secret,
            }
        )
        if webhook_secret is not UNSET:
            field_dict["webhook_secret"] = webhook_secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        api_key = d.pop("api_key")

        api_secret = d.pop("api_secret")

        webhook_secret = d.pop("webhook_secret", UNSET)

        nimbus_post_auth_request_request = cls(
            api_key=api_key,
            api_secret=api_secret,
            webhook_secret=webhook_secret,
        )

        nimbus_post_auth_request_request.additional_properties = d
        return nimbus_post_auth_request_request

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
