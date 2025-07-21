"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.checkout_options import CheckoutOptions


T = TypeVar("T", bound="OrderCheckoutResponse")


@attr.s(auto_attribs=True)
class OrderCheckoutResponse:
    """
    Attributes:
        id (int):
        checkout_options (CheckoutOptions):
        gateway (int):
    """

    id: int
    checkout_options: "CheckoutOptions"
    gateway: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        checkout_options = self.checkout_options.to_dict()

        gateway = self.gateway

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "checkout_options": checkout_options,
                "gateway": gateway,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checkout_options import CheckoutOptions

        d = src_dict.copy()
        id = d.pop("id")

        checkout_options = CheckoutOptions.from_dict(d.pop("checkout_options"))

        gateway = d.pop("gateway")

        order_checkout_response = cls(
            id=id,
            checkout_options=checkout_options,
            gateway=gateway,
        )

        order_checkout_response.additional_properties = d
        return order_checkout_response

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
