"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.next_or_cta_request import NextOrCTARequest


T = TypeVar("T", bound="CallTransferRequestRequest")


@attr.s(auto_attribs=True)
class CallTransferRequestRequest:
    """
    Attributes:
        next_or_cta (NextOrCTARequest):
    """

    next_or_cta: "NextOrCTARequest"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        next_or_cta = self.next_or_cta.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "next_or_cta": next_or_cta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.next_or_cta_request import NextOrCTARequest

        d = src_dict.copy()
        next_or_cta = NextOrCTARequest.from_dict(d.pop("next_or_cta"))

        call_transfer_request_request = cls(
            next_or_cta=next_or_cta,
        )

        call_transfer_request_request.additional_properties = d
        return call_transfer_request_request

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
