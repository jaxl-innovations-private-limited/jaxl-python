"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.resource_enum import ResourceEnum


if TYPE_CHECKING:
    from ..models.country import Country


T = TypeVar("T", bound="KycCountries")


@attr.s(auto_attribs=True)
class KycCountries:
    """
    Attributes:
        country (Country): Adds a 'jaxlid' field which contains signed ID information.
        resource (List[ResourceEnum]):
    """

    country: "Country"
    resource: List[ResourceEnum]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        country = self.country.to_dict()

        resource = []
        for resource_item_data in self.resource:
            resource_item = resource_item_data.value

            resource.append(resource_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "country": country,
                "resource": resource,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.country import Country

        d = src_dict.copy()
        country = Country.from_dict(d.pop("country"))

        resource = []
        _resource = d.pop("resource")
        for resource_item_data in _resource:
            resource_item = ResourceEnum(resource_item_data)

            resource.append(resource_item)

        kyc_countries = cls(
            country=country,
            resource=resource,
        )

        kyc_countries.additional_properties = d
        return kyc_countries

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
