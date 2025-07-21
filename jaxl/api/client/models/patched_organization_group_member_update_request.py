"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.roles_enum import RolesEnum
from ..types import UNSET, Unset


T = TypeVar("T", bound="PatchedOrganizationGroupMemberUpdateRequest")


@attr.s(auto_attribs=True)
class PatchedOrganizationGroupMemberUpdateRequest:
    """
    Attributes:
        roles (Union[Unset, List[RolesEnum]]):
        action (Union[Unset, bool]): When true, roles are added, when false, roles are removed Default: True.
    """

    roles: Union[Unset, List[RolesEnum]] = UNSET
    action: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        roles: Union[Unset, List[int]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.value

                roles.append(roles_item)

        action = self.action

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if roles is not UNSET:
            field_dict["roles"] = roles
        if action is not UNSET:
            field_dict["action"] = action

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        roles = []
        _roles = d.pop("roles", UNSET)
        for roles_item_data in _roles or []:
            roles_item = RolesEnum(roles_item_data)

            roles.append(roles_item)

        action = d.pop("action", UNSET)

        patched_organization_group_member_update_request = cls(
            roles=roles,
            action=action,
        )

        patched_organization_group_member_update_request.additional_properties = d
        return patched_organization_group_member_update_request

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
