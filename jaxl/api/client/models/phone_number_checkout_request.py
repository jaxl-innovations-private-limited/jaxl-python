"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.state_enum import StateEnum


T = TypeVar("T", bound="PhoneNumberCheckoutRequest")


@attr.s(auto_attribs=True)
class PhoneNumberCheckoutRequest:
    """
    Attributes:
        state (StateEnum):
        signature (str): Signature returned by a prior search API for NEW state. jaxlid of current order_id for
            REPURCHASE state
    """

    state: StateEnum
    signature: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state = self.state.value

        signature = self.signature

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
                "signature": signature,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        state = StateEnum(d.pop("state"))

        signature = d.pop("signature")

        phone_number_checkout_request = cls(
            state=state,
            signature=signature,
        )

        phone_number_checkout_request.additional_properties = d
        return phone_number_checkout_request

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
