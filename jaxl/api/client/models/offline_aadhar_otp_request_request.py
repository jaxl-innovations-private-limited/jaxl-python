"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar

import attr

from ..types import Unset


T = TypeVar("T", bound="OfflineAadharOtpRequestRequest")


@attr.s(auto_attribs=True)
class OfflineAadharOtpRequestRequest:
    """
    Attributes:
        phone_number (str):
        aadhar_number (str):
        kyc_id (int):
    """

    phone_number: str
    aadhar_number: str
    kyc_id: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        phone_number = self.phone_number
        aadhar_number = self.aadhar_number
        kyc_id = self.kyc_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "phone_number": phone_number,
                "aadhar_number": aadhar_number,
                "kyc_id": kyc_id,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        phone_number = (
            self.phone_number
            if isinstance(self.phone_number, Unset)
            else (None, str(self.phone_number).encode(), "text/plain")
        )
        aadhar_number = (
            self.aadhar_number
            if isinstance(self.aadhar_number, Unset)
            else (None, str(self.aadhar_number).encode(), "text/plain")
        )
        kyc_id = (
            self.kyc_id
            if isinstance(self.kyc_id, Unset)
            else (None, str(self.kyc_id).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                key: (None, str(value).encode(), "text/plain")
                for key, value in self.additional_properties.items()
            }
        )
        field_dict.update(
            {
                "phone_number": phone_number,
                "aadhar_number": aadhar_number,
                "kyc_id": kyc_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        phone_number = d.pop("phone_number")

        aadhar_number = d.pop("aadhar_number")

        kyc_id = d.pop("kyc_id")

        offline_aadhar_otp_request_request = cls(
            phone_number=phone_number,
            aadhar_number=aadhar_number,
            kyc_id=kyc_id,
        )

        offline_aadhar_otp_request_request.additional_properties = d
        return offline_aadhar_otp_request_request

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
