"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.iso_country_enum import IsoCountryEnum


T = TypeVar("T", bound="AddressCreationRequest")


@attr.s(auto_attribs=True)
class AddressCreationRequest:
    """
    Attributes:
        friendly_name (str):
        customer_name (str):
        street (str):
        city (str):
        region (str):
        postal_code (str):
        iso_country (IsoCountryEnum):
    """

    friendly_name: str
    customer_name: str
    street: str
    city: str
    region: str
    postal_code: str
    iso_country: IsoCountryEnum
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        friendly_name = self.friendly_name
        customer_name = self.customer_name
        street = self.street
        city = self.city
        region = self.region
        postal_code = self.postal_code
        iso_country = self.iso_country.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "friendly_name": friendly_name,
                "customer_name": customer_name,
                "street": street,
                "city": city,
                "region": region,
                "postal_code": postal_code,
                "iso_country": iso_country,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        friendly_name = d.pop("friendly_name")

        customer_name = d.pop("customer_name")

        street = d.pop("street")

        city = d.pop("city")

        region = d.pop("region")

        postal_code = d.pop("postal_code")

        iso_country = IsoCountryEnum(d.pop("iso_country"))

        address_creation_request = cls(
            friendly_name=friendly_name,
            customer_name=customer_name,
            street=street,
            city=city,
            region=region,
            postal_code=postal_code,
            iso_country=iso_country,
        )

        address_creation_request.additional_properties = d
        return address_creation_request

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
