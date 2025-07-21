"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar

import attr


T = TypeVar("T", bound="BusinessAttributesRequest")


@attr.s(auto_attribs=True)
class BusinessAttributesRequest:
    """
    Attributes:
        business_name (str):
        business_registration_number (str):
        vat (str):
    """

    business_name: str
    business_registration_number: str
    vat: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        business_name = self.business_name
        business_registration_number = self.business_registration_number
        vat = self.vat

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "business_name": business_name,
                "business_registration_number": business_registration_number,
                "vat": vat,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        business_name = d.pop("business_name")

        business_registration_number = d.pop("business_registration_number")

        vat = d.pop("vat")

        business_attributes_request = cls(
            business_name=business_name,
            business_registration_number=business_registration_number,
            vat=vat,
        )

        business_attributes_request.additional_properties = d
        return business_attributes_request

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
