"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset


T = TypeVar("T", bound="AadharAttributesRequest")


@attr.s(auto_attribs=True)
class AadharAttributesRequest:
    """
    Attributes:
        signature (str):
        csek (str):
        email (str):
        phone_number (str):
        vat (Union[Unset, None, str]):
        business_registration_number (Union[Unset, None, str]):
    """

    signature: str
    csek: str
    email: str
    phone_number: str
    vat: Union[Unset, None, str] = UNSET
    business_registration_number: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        signature = self.signature
        csek = self.csek
        email = self.email
        phone_number = self.phone_number
        vat = self.vat
        business_registration_number = self.business_registration_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "signature": signature,
                "csek": csek,
                "email": email,
                "phone_number": phone_number,
            }
        )
        if vat is not UNSET:
            field_dict["vat"] = vat
        if business_registration_number is not UNSET:
            field_dict["business_registration_number"] = business_registration_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        signature = d.pop("signature")

        csek = d.pop("csek")

        email = d.pop("email")

        phone_number = d.pop("phone_number")

        vat = d.pop("vat", UNSET)

        business_registration_number = d.pop("business_registration_number", UNSET)

        aadhar_attributes_request = cls(
            signature=signature,
            csek=csek,
            email=email,
            phone_number=phone_number,
            vat=vat,
            business_registration_number=business_registration_number,
        )

        aadhar_attributes_request.additional_properties = d
        return aadhar_attributes_request

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
