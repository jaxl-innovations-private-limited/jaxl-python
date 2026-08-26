"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KwikEngageAuthRequestRequest")


@attr.s(auto_attribs=True)
class KwikEngageAuthRequestRequest:
    """
    Attributes:
        api_key (str): Kwik Engage API key
        merchant_id (str): Kwik Engage merchant ID
        waba_id (str): WhatsApp Business Account ID
        phone_number_id (str): WhatsApp phone number ID
        webhook_secret (Union[Unset, None, str]): Kwik Engage webhook secret
    """

    api_key: str
    merchant_id: str
    waba_id: str
    phone_number_id: str
    webhook_secret: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api_key = self.api_key
        merchant_id = self.merchant_id
        waba_id = self.waba_id
        phone_number_id = self.phone_number_id
        webhook_secret = self.webhook_secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "api_key": api_key,
                "merchant_id": merchant_id,
                "waba_id": waba_id,
                "phone_number_id": phone_number_id,
            }
        )
        if webhook_secret is not UNSET:
            field_dict["webhook_secret"] = webhook_secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        api_key = d.pop("api_key")

        merchant_id = d.pop("merchant_id")

        waba_id = d.pop("waba_id")

        phone_number_id = d.pop("phone_number_id")

        webhook_secret = d.pop("webhook_secret", UNSET)

        kwik_engage_auth_request_request = cls(
            api_key=api_key,
            merchant_id=merchant_id,
            waba_id=waba_id,
            phone_number_id=phone_number_id,
            webhook_secret=webhook_secret,
        )

        kwik_engage_auth_request_request.additional_properties = d
        return kwik_engage_auth_request_request

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
