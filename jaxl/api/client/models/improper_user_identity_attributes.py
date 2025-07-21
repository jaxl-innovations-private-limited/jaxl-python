"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.improper_user_identity_attributes_errors import (
        ImproperUserIdentityAttributesErrors,
    )


T = TypeVar("T", bound="ImproperUserIdentityAttributes")


@attr.s(auto_attribs=True)
class ImproperUserIdentityAttributes:
    """
    Attributes:
        field_errors (ImproperUserIdentityAttributesErrors):
    """

    field_errors: "ImproperUserIdentityAttributesErrors"
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
        from ..models.improper_user_identity_attributes_errors import (
            ImproperUserIdentityAttributesErrors,
        )

        d = src_dict.copy()
        field_errors = ImproperUserIdentityAttributesErrors.from_dict(d.pop("_errors"))

        improper_user_identity_attributes = cls(
            field_errors=field_errors,
        )

        improper_user_identity_attributes.additional_properties = d
        return improper_user_identity_attributes

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
