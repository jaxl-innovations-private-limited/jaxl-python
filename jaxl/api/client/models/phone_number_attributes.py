"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PhoneNumberAttributes")


@attr.s(auto_attribs=True)
class PhoneNumberAttributes:
    """
    Attributes:
        sku_label (Union[Unset, None, str]):
        sku_hex_color (Union[Unset, None, str]):
    """

    sku_label: Union[Unset, None, str] = UNSET
    sku_hex_color: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sku_label = self.sku_label
        sku_hex_color = self.sku_hex_color

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sku_label is not UNSET:
            field_dict["sku_label"] = sku_label
        if sku_hex_color is not UNSET:
            field_dict["sku_hex_color"] = sku_hex_color

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sku_label = d.pop("sku_label", UNSET)

        sku_hex_color = d.pop("sku_hex_color", UNSET)

        phone_number_attributes = cls(
            sku_label=sku_label,
            sku_hex_color=sku_hex_color,
        )

        phone_number_attributes.additional_properties = d
        return phone_number_attributes

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
