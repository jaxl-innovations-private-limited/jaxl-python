"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.order_attributes import OrderAttributes


T = TypeVar("T", bound="CustomerOrderSku")


@attr.s(auto_attribs=True)
class CustomerOrderSku:
    """
    Attributes:
        id (int):
        sku (str):
        attributes (OrderAttributes):
    """

    id: int
    sku: str
    attributes: "OrderAttributes"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        sku = self.sku
        attributes = self.attributes.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "sku": sku,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_attributes import OrderAttributes

        d = src_dict.copy()
        id = d.pop("id")

        sku = d.pop("sku")

        attributes = OrderAttributes.from_dict(d.pop("attributes"))

        customer_order_sku = cls(
            id=id,
            sku=sku,
            attributes=attributes,
        )

        customer_order_sku.additional_properties = d
        return customer_order_sku

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
