"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShiprocketDeliveryAuthRequestRequest")


@attr.s(auto_attribs=True)
class ShiprocketDeliveryAuthRequestRequest:
    """Push-only from Shiprocket's side -- no credentials are needed to
    receive the webhook, just a URL pasted into their dashboard.
    webhook_secret is reserved for future signature verification.

        Attributes:
            webhook_secret (Union[Unset, None, str]):
            shop_domain (Union[Unset, None, str]): Optional Shopify shop domain (e.g. 'my-store.myshopify.com') to associate
                this provider with an already-connected Shopify org_provider in the organization.
    """

    webhook_secret: Union[Unset, None, str] = UNSET
    shop_domain: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        webhook_secret = self.webhook_secret
        shop_domain = self.shop_domain

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if webhook_secret is not UNSET:
            field_dict["webhook_secret"] = webhook_secret
        if shop_domain is not UNSET:
            field_dict["shop_domain"] = shop_domain

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        webhook_secret = d.pop("webhook_secret", UNSET)

        shop_domain = d.pop("shop_domain", UNSET)

        shiprocket_delivery_auth_request_request = cls(
            webhook_secret=webhook_secret,
            shop_domain=shop_domain,
        )

        shiprocket_delivery_auth_request_request.additional_properties = d
        return shiprocket_delivery_auth_request_request

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
