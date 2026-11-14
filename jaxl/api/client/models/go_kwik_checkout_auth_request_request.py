"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoKwikCheckoutAuthRequestRequest")


@attr.s(auto_attribs=True)
class GoKwikCheckoutAuthRequestRequest:
    """
    Attributes:
        shop_domain (str): Shopify shop domain (e.g. 'my-store.myshopify.com') of an already-connected Shopify
            org_provider running GoKwik checkout.
        webhook_secret (Union[Unset, None, str]): Unused: GoKwik sends no signature header at all (confirmed against
            real deliveries), so there is nothing to verify. Accepted so a future scheme needs no API change.
    """

    shop_domain: str
    webhook_secret: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shop_domain = self.shop_domain
        webhook_secret = self.webhook_secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shop_domain": shop_domain,
            }
        )
        if webhook_secret is not UNSET:
            field_dict["webhook_secret"] = webhook_secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        shop_domain = d.pop("shop_domain")

        webhook_secret = d.pop("webhook_secret", UNSET)

        go_kwik_checkout_auth_request_request = cls(
            shop_domain=shop_domain,
            webhook_secret=webhook_secret,
        )

        go_kwik_checkout_auth_request_request.additional_properties = d
        return go_kwik_checkout_auth_request_request

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
