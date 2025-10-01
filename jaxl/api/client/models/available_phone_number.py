"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.available_phone_number_provider_enum import (
    AvailablePhoneNumberProviderEnum,
)
from ..models.intent_enum import IntentEnum
from ..models.rental_currency_enum import RentalCurrencyEnum
from ..models.resource_enum import ResourceEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.available_phone_number_capabilities import (
        AvailablePhoneNumberCapabilities,
    )


T = TypeVar("T", bound="AvailablePhoneNumber")


@attr.s(auto_attribs=True)
class AvailablePhoneNumber:
    """
    Attributes:
        display_name (str):
        phone_number (str):
        iso_country (str):
        capabilities (AvailablePhoneNumberCapabilities):
        region (str):
        locality (str):
        resource (ResourceEnum):
        rental_currency (RentalCurrencyEnum):
        signature (str):
        provider (AvailablePhoneNumberProviderEnum):
        intent (IntentEnum):
        rental_price (Union[Unset, None, float]):
    """

    display_name: str
    phone_number: str
    iso_country: str
    capabilities: "AvailablePhoneNumberCapabilities"
    region: str
    locality: str
    resource: ResourceEnum
    rental_currency: RentalCurrencyEnum
    signature: str
    provider: AvailablePhoneNumberProviderEnum
    intent: IntentEnum
    rental_price: Union[Unset, None, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        phone_number = self.phone_number
        iso_country = self.iso_country
        capabilities = self.capabilities.to_dict()

        region = self.region
        locality = self.locality
        resource = self.resource.value

        rental_currency = self.rental_currency.value

        signature = self.signature
        provider = self.provider.value

        intent = self.intent.value

        rental_price = self.rental_price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "display_name": display_name,
                "phone_number": phone_number,
                "iso_country": iso_country,
                "capabilities": capabilities,
                "region": region,
                "locality": locality,
                "resource": resource,
                "rental_currency": rental_currency,
                "signature": signature,
                "provider": provider,
                "intent": intent,
            }
        )
        if rental_price is not UNSET:
            field_dict["rental_price"] = rental_price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.available_phone_number_capabilities import (
            AvailablePhoneNumberCapabilities,
        )

        d = src_dict.copy()
        display_name = d.pop("display_name")

        phone_number = d.pop("phone_number")

        iso_country = d.pop("iso_country")

        capabilities = AvailablePhoneNumberCapabilities.from_dict(d.pop("capabilities"))

        region = d.pop("region")

        locality = d.pop("locality")

        resource = ResourceEnum(d.pop("resource"))

        rental_currency = RentalCurrencyEnum(d.pop("rental_currency"))

        signature = d.pop("signature")

        provider = AvailablePhoneNumberProviderEnum(d.pop("provider"))

        intent = IntentEnum(d.pop("intent"))

        rental_price = d.pop("rental_price", UNSET)

        available_phone_number = cls(
            display_name=display_name,
            phone_number=phone_number,
            iso_country=iso_country,
            capabilities=capabilities,
            region=region,
            locality=locality,
            resource=resource,
            rental_currency=rental_currency,
            signature=signature,
            provider=provider,
            intent=intent,
            rental_price=rental_price,
        )

        available_phone_number.additional_properties = d
        return available_phone_number

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
