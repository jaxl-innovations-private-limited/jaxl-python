"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.unit_enum import UnitEnum
from ..types import UNSET, Unset


T = TypeVar("T", bound="Information")


@attr.s(auto_attribs=True)
class Information:
    """
    Attributes:
        value (Any):
        color (Union[Unset, None, str]):
        unit (Union[Unset, UnitEnum]):
    """

    value: Any
    color: Union[Unset, None, str] = UNSET
    unit: Union[Unset, UnitEnum] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value = self.value
        color = self.color
        unit: Union[Unset, str] = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value")

        color = d.pop("color", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: Union[Unset, UnitEnum]
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = UnitEnum(_unit)

        information = cls(
            value=value,
            color=color,
            unit=unit,
        )

        information.additional_properties = d
        return information

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
