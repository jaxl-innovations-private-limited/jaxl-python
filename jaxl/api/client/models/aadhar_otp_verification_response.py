"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.kyc import Kyc


T = TypeVar("T", bound="AadharOtpVerificationResponse")


@attr.s(auto_attribs=True)
class AadharOtpVerificationResponse:
    """
    Attributes:
        verified (bool):
        kyc (Kyc): Adds a 'jaxlid' field which contains signed ID information.
    """

    verified: bool
    kyc: "Kyc"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        verified = self.verified
        kyc = self.kyc.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "verified": verified,
                "kyc": kyc,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.kyc import Kyc

        d = src_dict.copy()
        verified = d.pop("verified")

        kyc = Kyc.from_dict(d.pop("kyc"))

        aadhar_otp_verification_response = cls(
            verified=verified,
            kyc=kyc,
        )

        aadhar_otp_verification_response.additional_properties = d
        return aadhar_otp_verification_response

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
