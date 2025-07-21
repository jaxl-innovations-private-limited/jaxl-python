"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset


T = TypeVar("T", bound="PatchedOrganizationGroupUpdateRequest")


@attr.s(auto_attribs=True)
class PatchedOrganizationGroupUpdateRequest:
    """
    Attributes:
        name (Union[Unset, None, str]):
        add_employees (Union[Unset, List[int]]):
        remove_employees (Union[Unset, List[int]]):
    """

    name: Union[Unset, None, str] = UNSET
    add_employees: Union[Unset, List[int]] = UNSET
    remove_employees: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        add_employees: Union[Unset, List[int]] = UNSET
        if not isinstance(self.add_employees, Unset):
            add_employees = self.add_employees

        remove_employees: Union[Unset, List[int]] = UNSET
        if not isinstance(self.remove_employees, Unset):
            remove_employees = self.remove_employees

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if add_employees is not UNSET:
            field_dict["add_employees"] = add_employees
        if remove_employees is not UNSET:
            field_dict["remove_employees"] = remove_employees

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        add_employees = cast(List[int], d.pop("add_employees", UNSET))

        remove_employees = cast(List[int], d.pop("remove_employees", UNSET))

        patched_organization_group_update_request = cls(
            name=name,
            add_employees=add_employees,
            remove_employees=remove_employees,
        )

        patched_organization_group_update_request.additional_properties = d
        return patched_organization_group_update_request

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
