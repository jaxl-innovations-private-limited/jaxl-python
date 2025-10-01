"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.capabilities import Capabilities
    from ..models.country import Country


T = TypeVar("T", bound="PlanItem")


@attr.s(auto_attribs=True)
class PlanItem:
    """
    Attributes:
        name (str):
        country (Union[Unset, Country]): Adds a 'jaxlid' field which contains signed ID information.
        number_type (Union[Unset, str]): Type of number eg: Tollfree, Phone, Landline
        capabilities (Union[Unset, Capabilities]):
    """

    name: str
    country: Union[Unset, "Country"] = UNSET
    number_type: Union[Unset, str] = UNSET
    capabilities: Union[Unset, "Capabilities"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        country: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.to_dict()

        number_type = self.number_type
        capabilities: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if country is not UNSET:
            field_dict["country"] = country
        if number_type is not UNSET:
            field_dict["number_type"] = number_type
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.capabilities import Capabilities
        from ..models.country import Country

        d = src_dict.copy()
        name = d.pop("name")

        _country = d.pop("country", UNSET)
        country: Union[Unset, Country]
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = Country.from_dict(_country)

        number_type = d.pop("number_type", UNSET)

        _capabilities = d.pop("capabilities", UNSET)
        capabilities: Union[Unset, Capabilities]
        if isinstance(_capabilities, Unset):
            capabilities = UNSET
        else:
            capabilities = Capabilities.from_dict(_capabilities)

        plan_item = cls(
            name=name,
            country=country,
            number_type=number_type,
            capabilities=capabilities,
        )

        plan_item.additional_properties = d
        return plan_item

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
