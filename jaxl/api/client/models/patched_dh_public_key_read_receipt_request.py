"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset


T = TypeVar("T", bound="PatchedDHPublicKeyReadReceiptRequest")


@attr.s(auto_attribs=True)
class PatchedDHPublicKeyReadReceiptRequest:
    """Read receipts are sent for the last PK that user device has seen/read.

    NOTE: "to_key" is acknowledging read receipt for all messages until primary key "till"
    received "from_key" user.

        Attributes:
            till (Union[Unset, int]): ID till which this device has read messages received from_key
            from_key (Union[Unset, str]): The discovery key from whom messages were received and are now being acked
            to_key (Union[Unset, str]): The discovery key to whom messages were sent and is now acking
    """

    till: Union[Unset, int] = UNSET
    from_key: Union[Unset, str] = UNSET
    to_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        till = self.till
        from_key = self.from_key
        to_key = self.to_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if till is not UNSET:
            field_dict["till"] = till
        if from_key is not UNSET:
            field_dict["from_key"] = from_key
        if to_key is not UNSET:
            field_dict["to_key"] = to_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        till = d.pop("till", UNSET)

        from_key = d.pop("from_key", UNSET)

        to_key = d.pop("to_key", UNSET)

        patched_dh_public_key_read_receipt_request = cls(
            till=till,
            from_key=from_key,
            to_key=to_key,
        )

        patched_dh_public_key_read_receipt_request.additional_properties = d
        return patched_dh_public_key_read_receipt_request

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
