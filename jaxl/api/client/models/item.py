"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Item")


@attr.s(auto_attribs=True)
class Item:
    """
    Attributes:
        type (str):
        sku (Union[Unset, None, str]):
        sku_label (Union[Unset, None, str]):
        sku_hex_color (Union[Unset, None, str]):
        country_name (Union[Unset, None, str]):
        iso_country_code (Union[Unset, None, str]):
        iso_alpha3_country_code (Union[Unset, None, str]):
        flag_url (Union[Unset, None, str]):
        intent (Union[Unset, None, str]):
    """

    type: str
    sku: Union[Unset, None, str] = UNSET
    sku_label: Union[Unset, None, str] = UNSET
    sku_hex_color: Union[Unset, None, str] = UNSET
    country_name: Union[Unset, None, str] = UNSET
    iso_country_code: Union[Unset, None, str] = UNSET
    iso_alpha3_country_code: Union[Unset, None, str] = UNSET
    flag_url: Union[Unset, None, str] = UNSET
    intent: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        sku = self.sku
        sku_label = self.sku_label
        sku_hex_color = self.sku_hex_color
        country_name = self.country_name
        iso_country_code = self.iso_country_code
        iso_alpha3_country_code = self.iso_alpha3_country_code
        flag_url = self.flag_url
        intent = self.intent

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if sku is not UNSET:
            field_dict["sku"] = sku
        if sku_label is not UNSET:
            field_dict["sku_label"] = sku_label
        if sku_hex_color is not UNSET:
            field_dict["sku_hex_color"] = sku_hex_color
        if country_name is not UNSET:
            field_dict["country_name"] = country_name
        if iso_country_code is not UNSET:
            field_dict["iso_country_code"] = iso_country_code
        if iso_alpha3_country_code is not UNSET:
            field_dict["iso_alpha3_country_code"] = iso_alpha3_country_code
        if flag_url is not UNSET:
            field_dict["flag_url"] = flag_url
        if intent is not UNSET:
            field_dict["intent"] = intent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        sku = d.pop("sku", UNSET)

        sku_label = d.pop("sku_label", UNSET)

        sku_hex_color = d.pop("sku_hex_color", UNSET)

        country_name = d.pop("country_name", UNSET)

        iso_country_code = d.pop("iso_country_code", UNSET)

        iso_alpha3_country_code = d.pop("iso_alpha3_country_code", UNSET)

        flag_url = d.pop("flag_url", UNSET)

        intent = d.pop("intent", UNSET)

        item = cls(
            type=type,
            sku=sku,
            sku_label=sku_label,
            sku_hex_color=sku_hex_color,
            country_name=country_name,
            iso_country_code=iso_country_code,
            iso_alpha3_country_code=iso_alpha3_country_code,
            flag_url=flag_url,
            intent=intent,
        )

        item.additional_properties = d
        return item

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
