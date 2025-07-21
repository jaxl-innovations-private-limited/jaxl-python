"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Optional, Type, TypeVar

import attr


T = TypeVar("T", bound="ReceiptValidateSerializerV2Request")


@attr.s(auto_attribs=True)
class ReceiptValidateSerializerV2Request:
    """
    Attributes:
        product_id (str):
        receipt (str):
        status (str):
        transaction_id (Optional[str]):
        transaction_date (Optional[str]):
    """

    product_id: str
    receipt: str
    status: str
    transaction_id: Optional[str]
    transaction_date: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        product_id = self.product_id
        receipt = self.receipt
        status = self.status
        transaction_id = self.transaction_id
        transaction_date = self.transaction_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product_id": product_id,
                "receipt": receipt,
                "status": status,
                "transaction_id": transaction_id,
                "transaction_date": transaction_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        product_id = d.pop("product_id")

        receipt = d.pop("receipt")

        status = d.pop("status")

        transaction_id = d.pop("transaction_id")

        transaction_date = d.pop("transaction_date")

        receipt_validate_serializer_v2_request = cls(
            product_id=product_id,
            receipt=receipt,
            status=status,
            transaction_id=transaction_id,
            transaction_date=transaction_date,
        )

        receipt_validate_serializer_v2_request.additional_properties = d
        return receipt_validate_serializer_v2_request

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
