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
    from ..models.order_attributes_attributes import OrderAttributesAttributes


T = TypeVar("T", bound="OrderAttributes")


@attr.s(auto_attribs=True)
class OrderAttributes:
    """
    Attributes:
        sku_label (Union[Unset, None, str]):
        sku_hex_color (Union[Unset, None, str]):
        attributes (Union[Unset, None, OrderAttributesAttributes]):
    """

    sku_label: Union[Unset, None, str] = UNSET
    sku_hex_color: Union[Unset, None, str] = UNSET
    attributes: Union[Unset, None, "OrderAttributesAttributes"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sku_label = self.sku_label
        sku_hex_color = self.sku_hex_color
        attributes: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict() if self.attributes else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sku_label is not UNSET:
            field_dict["sku_label"] = sku_label
        if sku_hex_color is not UNSET:
            field_dict["sku_hex_color"] = sku_hex_color
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_attributes_attributes import (
            OrderAttributesAttributes,
        )

        d = src_dict.copy()
        sku_label = d.pop("sku_label", UNSET)

        sku_hex_color = d.pop("sku_hex_color", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, None, OrderAttributesAttributes]
        if _attributes is None:
            attributes = None
        elif isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = OrderAttributesAttributes.from_dict(_attributes)

        order_attributes = cls(
            sku_label=sku_label,
            sku_hex_color=sku_hex_color,
            attributes=attributes,
        )

        order_attributes.additional_properties = d
        return order_attributes

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
