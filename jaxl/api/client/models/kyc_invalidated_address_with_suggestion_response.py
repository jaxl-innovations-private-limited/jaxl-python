"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.kyc_invalidated_address_with_suggestion_response_suggested_address import (
        KycInvalidatedAddressWithSuggestionResponseSuggestedAddress,
    )


T = TypeVar("T", bound="KycInvalidatedAddressWithSuggestionResponse")


@attr.s(auto_attribs=True)
class KycInvalidatedAddressWithSuggestionResponse:
    """
    Attributes:
        message (str):
        suggested_address (KycInvalidatedAddressWithSuggestionResponseSuggestedAddress):
    """

    message: str
    suggested_address: "KycInvalidatedAddressWithSuggestionResponseSuggestedAddress"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        suggested_address = self.suggested_address.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "suggested_address": suggested_address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.kyc_invalidated_address_with_suggestion_response_suggested_address import (
            KycInvalidatedAddressWithSuggestionResponseSuggestedAddress,
        )

        d = src_dict.copy()
        message = d.pop("message")

        suggested_address = (
            KycInvalidatedAddressWithSuggestionResponseSuggestedAddress.from_dict(
                d.pop("suggested_address")
            )
        )

        kyc_invalidated_address_with_suggestion_response = cls(
            message=message,
            suggested_address=suggested_address,
        )

        kyc_invalidated_address_with_suggestion_response.additional_properties = d
        return kyc_invalidated_address_with_suggestion_response

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
