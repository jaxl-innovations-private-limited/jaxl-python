"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar

import attr


T = TypeVar("T", bound="AadharOtpRequestRequest")


@attr.s(auto_attribs=True)
class AadharOtpRequestRequest:
    """
    Attributes:
        aadhar_number (str):
        kyc_id (int):
    """

    aadhar_number: str
    kyc_id: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aadhar_number = self.aadhar_number
        kyc_id = self.kyc_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aadhar_number": aadhar_number,
                "kyc_id": kyc_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        aadhar_number = d.pop("aadhar_number")

        kyc_id = d.pop("kyc_id")

        aadhar_otp_request_request = cls(
            aadhar_number=aadhar_number,
            kyc_id=kyc_id,
        )

        aadhar_otp_request_request.additional_properties = d
        return aadhar_otp_request_request

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
