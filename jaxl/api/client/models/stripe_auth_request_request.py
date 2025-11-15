"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="StripeAuthRequestRequest")


@attr.s(auto_attribs=True)
class StripeAuthRequestRequest:
    """
    Attributes:
        publishable_key (Union[Unset, None, str]):
        secret_key (Union[Unset, None, str]):
        webhook_signing_secret (Union[Unset, None, str]):
    """

    publishable_key: Union[Unset, None, str] = UNSET
    secret_key: Union[Unset, None, str] = UNSET
    webhook_signing_secret: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        publishable_key = self.publishable_key
        secret_key = self.secret_key
        webhook_signing_secret = self.webhook_signing_secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if publishable_key is not UNSET:
            field_dict["publishable_key"] = publishable_key
        if secret_key is not UNSET:
            field_dict["secret_key"] = secret_key
        if webhook_signing_secret is not UNSET:
            field_dict["webhook_signing_secret"] = webhook_signing_secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        publishable_key = d.pop("publishable_key", UNSET)

        secret_key = d.pop("secret_key", UNSET)

        webhook_signing_secret = d.pop("webhook_signing_secret", UNSET)

        stripe_auth_request_request = cls(
            publishable_key=publishable_key,
            secret_key=secret_key,
            webhook_signing_secret=webhook_signing_secret,
        )

        stripe_auth_request_request.additional_properties = d
        return stripe_auth_request_request

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
