"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr

from ..models.organization_employee_status_enum import OrganizationEmployeeStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_employee_preferences import (
        OrganizationEmployeePreferences,
    )
    from ..models.organization_group_inline import OrganizationGroupInline


T = TypeVar("T", bound="OrganizationEmployee")


@attr.s(auto_attribs=True)
class OrganizationEmployee:
    """Adds a 'jaxlid' field which contains signed ID information.

    Attributes:
        id (int):
        user_id (int):
        app_user_id (int):
        email (str):
        groups (List['OrganizationGroupInline']):
        status (OrganizationEmployeeStatusEnum):
        permissions (List[str]):
        preferences (Union[Unset, OrganizationEmployeePreferences]):
        invited_by (Union[Unset, None, int]): Organization employee who invited this employee to their organization
        removed_by (Union[Unset, None, int]): Organization employee who remove this employee from the organization
        phone_number (Union[Unset, None, str]): Employee cellular number provided by organization
        jaxlid (Optional[str]):
    """

    id: int
    user_id: int
    app_user_id: int
    email: str
    groups: List["OrganizationGroupInline"]
    status: OrganizationEmployeeStatusEnum
    permissions: List[str]
    jaxlid: Optional[str]
    preferences: Union[Unset, "OrganizationEmployeePreferences"] = UNSET
    invited_by: Union[Unset, None, int] = UNSET
    removed_by: Union[Unset, None, int] = UNSET
    phone_number: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        user_id = self.user_id
        app_user_id = self.app_user_id
        email = self.email
        groups = []
        for groups_item_data in self.groups:
            groups_item = groups_item_data.to_dict()

            groups.append(groups_item)

        status = self.status.value

        permissions = self.permissions

        preferences: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preferences, Unset):
            preferences = self.preferences.to_dict()

        invited_by = self.invited_by
        removed_by = self.removed_by
        phone_number = self.phone_number
        jaxlid = self.jaxlid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "app_user_id": app_user_id,
                "email": email,
                "groups": groups,
                "status": status,
                "permissions": permissions,
                "jaxlid": jaxlid,
            }
        )
        if preferences is not UNSET:
            field_dict["preferences"] = preferences
        if invited_by is not UNSET:
            field_dict["invited_by"] = invited_by
        if removed_by is not UNSET:
            field_dict["removed_by"] = removed_by
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.organization_employee_preferences import (
            OrganizationEmployeePreferences,
        )
        from ..models.organization_group_inline import OrganizationGroupInline

        d = src_dict.copy()
        id = d.pop("id")

        user_id = d.pop("user_id")

        app_user_id = d.pop("app_user_id")

        email = d.pop("email")

        groups = []
        _groups = d.pop("groups")
        for groups_item_data in _groups:
            groups_item = OrganizationGroupInline.from_dict(groups_item_data)

            groups.append(groups_item)

        status = OrganizationEmployeeStatusEnum(d.pop("status"))

        permissions = cast(List[str], d.pop("permissions"))

        _preferences = d.pop("preferences", UNSET)
        preferences: Union[Unset, OrganizationEmployeePreferences]
        if isinstance(_preferences, Unset):
            preferences = UNSET
        else:
            preferences = OrganizationEmployeePreferences.from_dict(_preferences)

        invited_by = d.pop("invited_by", UNSET)

        removed_by = d.pop("removed_by", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        jaxlid = d.pop("jaxlid")

        organization_employee = cls(
            id=id,
            user_id=user_id,
            app_user_id=app_user_id,
            email=email,
            groups=groups,
            status=status,
            permissions=permissions,
            preferences=preferences,
            invited_by=invited_by,
            removed_by=removed_by,
            phone_number=phone_number,
            jaxlid=jaxlid,
        )

        organization_employee.additional_properties = d
        return organization_employee

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
