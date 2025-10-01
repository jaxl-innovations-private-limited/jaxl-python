"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PaymentGatewayFeesInfo")


@attr.s(auto_attribs=True)
class PaymentGatewayFeesInfo:
    """
    Attributes:
        fees_percentage (float):
        fees_amount (float):
    """

    fees_percentage: float
    fees_amount: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fees_percentage = self.fees_percentage
        fees_amount = self.fees_amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fees_percentage": fees_percentage,
                "fees_amount": fees_amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fees_percentage = d.pop("fees_percentage")

        fees_amount = d.pop("fees_amount")

        payment_gateway_fees_info = cls(
            fees_percentage=fees_percentage,
            fees_amount=fees_amount,
        )

        payment_gateway_fees_info.additional_properties = d
        return payment_gateway_fees_info

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
