"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset


T = TypeVar("T", bound="CustomerCannotPurchaseItem")


@attr.s(auto_attribs=True)
class CustomerCannotPurchaseItem:
    """
    Attributes:
        max_limit (Union[Unset, int]):
        sku (Union[Unset, str]):
        reason (Union[Unset, str]):
    """

    max_limit: Union[Unset, int] = UNSET
    sku: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_limit = self.max_limit
        sku = self.sku
        reason = self.reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_limit is not UNSET:
            field_dict["max_limit"] = max_limit
        if sku is not UNSET:
            field_dict["sku"] = sku
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        max_limit = d.pop("max_limit", UNSET)

        sku = d.pop("sku", UNSET)

        reason = d.pop("reason", UNSET)

        customer_cannot_purchase_item = cls(
            max_limit=max_limit,
            sku=sku,
            reason=reason,
        )

        customer_cannot_purchase_item.additional_properties = d
        return customer_cannot_purchase_item

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
