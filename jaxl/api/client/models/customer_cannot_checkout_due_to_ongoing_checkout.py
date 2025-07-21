"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset


T = TypeVar("T", bound="CustomerCannotCheckoutDueToOngoingCheckout")


@attr.s(auto_attribs=True)
class CustomerCannotCheckoutDueToOngoingCheckout:
    """
    Attributes:
        order_id (Union[Unset, int]):
        device_id (Union[Unset, int]):
    """

    order_id: Union[Unset, int] = UNSET
    device_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_id = self.order_id
        device_id = self.device_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if device_id is not UNSET:
            field_dict["device_id"] = device_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        order_id = d.pop("order_id", UNSET)

        device_id = d.pop("device_id", UNSET)

        customer_cannot_checkout_due_to_ongoing_checkout = cls(
            order_id=order_id,
            device_id=device_id,
        )

        customer_cannot_checkout_due_to_ongoing_checkout.additional_properties = d
        return customer_cannot_checkout_due_to_ongoing_checkout

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
