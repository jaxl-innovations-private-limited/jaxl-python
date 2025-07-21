"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.organization_employee import OrganizationEmployee


T = TypeVar("T", bound="OrganizationEmployeeInviteResponse")


@attr.s(auto_attribs=True)
class OrganizationEmployeeInviteResponse:
    """
    Attributes:
        invites (List['OrganizationEmployee']):
        num_invited (Union[Unset, int]):
    """

    invites: List["OrganizationEmployee"]
    num_invited: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invites = []
        for invites_item_data in self.invites:
            invites_item = invites_item_data.to_dict()

            invites.append(invites_item)

        num_invited = self.num_invited

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invites": invites,
            }
        )
        if num_invited is not UNSET:
            field_dict["num_invited"] = num_invited

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.organization_employee import OrganizationEmployee

        d = src_dict.copy()
        invites = []
        _invites = d.pop("invites")
        for invites_item_data in _invites:
            invites_item = OrganizationEmployee.from_dict(invites_item_data)

            invites.append(invites_item)

        num_invited = d.pop("num_invited", UNSET)

        organization_employee_invite_response = cls(
            invites=invites,
            num_invited=num_invited,
        )

        organization_employee_invite_response.additional_properties = d
        return organization_employee_invite_response

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
