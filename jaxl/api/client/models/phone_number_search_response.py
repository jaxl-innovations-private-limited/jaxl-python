"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

import attr

from ..models.resource_enum import ResourceEnum

if TYPE_CHECKING:
    from ..models.available_phone_number import AvailablePhoneNumber


T = TypeVar("T", bound="PhoneNumberSearchResponse")


@attr.s(auto_attribs=True)
class PhoneNumberSearchResponse:
    """
    Attributes:
        results (List['AvailablePhoneNumber']):
        resource (ResourceEnum):
        resources (List[str]):
    """

    results: List["AvailablePhoneNumber"]
    resource: ResourceEnum
    resources: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()

            results.append(results_item)

        resource = self.resource.value

        resources = self.resources

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "resource": resource,
                "resources": resources,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.available_phone_number import AvailablePhoneNumber

        d = src_dict.copy()
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = AvailablePhoneNumber.from_dict(results_item_data)

            results.append(results_item)

        resource = ResourceEnum(d.pop("resource"))

        resources = cast(List[str], d.pop("resources"))

        phone_number_search_response = cls(
            results=results,
            resource=resource,
            resources=resources,
        )

        phone_number_search_response.additional_properties = d
        return phone_number_search_response

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
