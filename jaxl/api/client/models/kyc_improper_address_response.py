"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.kyc_improper_address_response_errors import (
        KycImproperAddressResponseErrors,
    )


T = TypeVar("T", bound="KycImproperAddressResponse")


@attr.s(auto_attribs=True)
class KycImproperAddressResponse:
    """
    Attributes:
        field_errors (KycImproperAddressResponseErrors):
    """

    field_errors: "KycImproperAddressResponseErrors"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_errors = self.field_errors.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_errors": field_errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.kyc_improper_address_response_errors import (
            KycImproperAddressResponseErrors,
        )

        d = src_dict.copy()
        field_errors = KycImproperAddressResponseErrors.from_dict(d.pop("_errors"))

        kyc_improper_address_response = cls(
            field_errors=field_errors,
        )

        kyc_improper_address_response.additional_properties = d
        return kyc_improper_address_response

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
