"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, cast

import attr


T = TypeVar("T", bound="PlanCountryNumberTypes")


@attr.s(auto_attribs=True)
class PlanCountryNumberTypes:
    """
    Attributes:
        iso_country_code (str):
        number_types (List[str]):
    """

    iso_country_code: str
    number_types: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        iso_country_code = self.iso_country_code
        number_types = self.number_types

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "iso_country_code": iso_country_code,
                "number_types": number_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        iso_country_code = d.pop("iso_country_code")

        number_types = cast(List[str], d.pop("number_types"))

        plan_country_number_types = cls(
            iso_country_code=iso_country_code,
            number_types=number_types,
        )

        plan_country_number_types.additional_properties = d
        return plan_country_number_types

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
