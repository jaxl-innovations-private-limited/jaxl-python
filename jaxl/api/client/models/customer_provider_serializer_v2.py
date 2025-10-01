"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.currency_enum import CurrencyEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerProviderSerializerV2")


@attr.s(auto_attribs=True)
class CustomerProviderSerializerV2:
    """
    Attributes:
        customer (int):
        provider (int):
        provider_customer_id (Union[Unset, None, str]): Provider assigned customer ID. This field is an artifact of
            creating a customer object at the provider end, which is a mandatory requirement across 99% payment gateways.
            Currently, only with APPLE_PAY, no provider generated customer ID is mandatory or even available.  Our payment
            system don't need a provider generated customer ID, when our client app can persist jxl-cust-acnt cookie at
            their end.
        currency (Union[Unset, CurrencyEnum]):
    """

    customer: int
    provider: int
    provider_customer_id: Union[Unset, None, str] = UNSET
    currency: Union[Unset, CurrencyEnum] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer = self.customer
        provider = self.provider
        provider_customer_id = self.provider_customer_id
        currency: Union[Unset, int] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customer": customer,
                "provider": provider,
            }
        )
        if provider_customer_id is not UNSET:
            field_dict["provider_customer_id"] = provider_customer_id
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        customer = d.pop("customer")

        provider = d.pop("provider")

        provider_customer_id = d.pop("provider_customer_id", UNSET)

        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, CurrencyEnum]
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = CurrencyEnum(_currency)

        customer_provider_serializer_v2 = cls(
            customer=customer,
            provider=provider,
            provider_customer_id=provider_customer_id,
            currency=currency,
        )

        customer_provider_serializer_v2.additional_properties = d
        return customer_provider_serializer_v2

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
