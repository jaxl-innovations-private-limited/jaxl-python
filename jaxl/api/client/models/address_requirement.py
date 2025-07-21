"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.requirement_enum import RequirementEnum


T = TypeVar("T", bound="AddressRequirement")


@attr.s(auto_attribs=True)
class AddressRequirement:
    """
    Attributes:
        requirement (RequirementEnum):
        is_required (bool):
    """

    requirement: RequirementEnum
    is_required: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        requirement = self.requirement.value

        is_required = self.is_required

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requirement": requirement,
                "is_required": is_required,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        requirement = RequirementEnum(d.pop("requirement"))

        is_required = d.pop("is_required")

        address_requirement = cls(
            requirement=requirement,
            is_required=is_required,
        )

        address_requirement.additional_properties = d
        return address_requirement

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
