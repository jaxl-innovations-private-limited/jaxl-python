"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.role_enum import RoleEnum
from ..types import UNSET, Unset


T = TypeVar("T", bound="PatchedOrganizationMemberUpdateRequest")


@attr.s(auto_attribs=True)
class PatchedOrganizationMemberUpdateRequest:
    """
    Attributes:
        role (Union[Unset, List[RoleEnum]]):
        action (Union[Unset, bool]): When true, roles are added, when false, roles are removed Default: True.
    """

    role: Union[Unset, List[RoleEnum]] = UNSET
    action: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role: Union[Unset, List[str]] = UNSET
        if not isinstance(self.role, Unset):
            role = []
            for role_item_data in self.role:
                role_item = role_item_data.value

                role.append(role_item)

        action = self.action

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role is not UNSET:
            field_dict["role"] = role
        if action is not UNSET:
            field_dict["action"] = action

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        role = []
        _role = d.pop("role", UNSET)
        for role_item_data in _role or []:
            role_item = RoleEnum(role_item_data)

            role.append(role_item)

        action = d.pop("action", UNSET)

        patched_organization_member_update_request = cls(
            role=role,
            action=action,
        )

        patched_organization_member_update_request.additional_properties = d
        return patched_organization_member_update_request

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
