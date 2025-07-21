"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar

import attr


T = TypeVar("T", bound="NonCompliantKycResponse")


@attr.s(auto_attribs=True)
class NonCompliantKycResponse:
    """
    Attributes:
        name (str):
        title (str):
        error_code (int):
        description (str):
        field_type (int):
    """

    name: str
    title: str
    error_code: int
    description: str
    field_type: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        title = self.title
        error_code = self.error_code
        description = self.description
        field_type = self.field_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "title": title,
                "error_code": error_code,
                "description": description,
                "field_type": field_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        title = d.pop("title")

        error_code = d.pop("error_code")

        description = d.pop("description")

        field_type = d.pop("field_type")

        non_compliant_kyc_response = cls(
            name=name,
            title=title,
            error_code=error_code,
            description=description,
            field_type=field_type,
        )

        non_compliant_kyc_response.additional_properties = d
        return non_compliant_kyc_response

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
