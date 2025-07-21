"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar

import attr


T = TypeVar("T", bound="Outbound")


@attr.s(auto_attribs=True)
class Outbound:
    """
    Attributes:
        iso (str):
        country (str):
        min_outgoing_per_min (float):
        max_outgoing_per_min (float):
    """

    iso: str
    country: str
    min_outgoing_per_min: float
    max_outgoing_per_min: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        iso = self.iso
        country = self.country
        min_outgoing_per_min = self.min_outgoing_per_min
        max_outgoing_per_min = self.max_outgoing_per_min

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "iso": iso,
                "country": country,
                "min_outgoing_per_min": min_outgoing_per_min,
                "max_outgoing_per_min": max_outgoing_per_min,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        iso = d.pop("iso")

        country = d.pop("country")

        min_outgoing_per_min = d.pop("min_outgoing_per_min")

        max_outgoing_per_min = d.pop("max_outgoing_per_min")

        outbound = cls(
            iso=iso,
            country=country,
            min_outgoing_per_min=min_outgoing_per_min,
            max_outgoing_per_min=max_outgoing_per_min,
        )

        outbound.additional_properties = d
        return outbound

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
