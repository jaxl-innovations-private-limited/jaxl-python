"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Optional, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="OrganizationGroupResponse")


@attr.s(auto_attribs=True)
class OrganizationGroupResponse:
    """Adds a 'jaxlid' field which contains signed ID information.

    Attributes:
        id (int):
        name (str): Group name
        phone_numbers (List[str]): List of phone numbers UID assigned to this team
        admins (List[int]):
        employees (List[int]):
        jaxlid (Optional[str]):
    """

    id: int
    name: str
    phone_numbers: List[str]
    admins: List[int]
    employees: List[int]
    jaxlid: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        phone_numbers = self.phone_numbers

        admins = self.admins

        employees = self.employees

        jaxlid = self.jaxlid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "phone_numbers": phone_numbers,
                "admins": admins,
                "employees": employees,
                "jaxlid": jaxlid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        phone_numbers = cast(List[str], d.pop("phone_numbers"))

        admins = cast(List[int], d.pop("admins"))

        employees = cast(List[int], d.pop("employees"))

        jaxlid = d.pop("jaxlid")

        organization_group_response = cls(
            id=id,
            name=name,
            phone_numbers=phone_numbers,
            admins=admins,
            employees=employees,
            jaxlid=jaxlid,
        )

        organization_group_response.additional_properties = d
        return organization_group_response

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
