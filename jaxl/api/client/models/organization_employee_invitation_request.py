"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.organization_employee_invite_request import (
        OrganizationEmployeeInviteRequest,
    )


T = TypeVar("T", bound="OrganizationEmployeeInvitationRequest")


@attr.s(auto_attribs=True)
class OrganizationEmployeeInvitationRequest:
    """
    Attributes:
        emails (List['OrganizationEmployeeInviteRequest']):
    """

    emails: List["OrganizationEmployeeInviteRequest"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        emails = []
        for emails_item_data in self.emails:
            emails_item = emails_item_data.to_dict()

            emails.append(emails_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "emails": emails,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.organization_employee_invite_request import (
            OrganizationEmployeeInviteRequest,
        )

        d = src_dict.copy()
        emails = []
        _emails = d.pop("emails")
        for emails_item_data in _emails:
            emails_item = OrganizationEmployeeInviteRequest.from_dict(emails_item_data)

            emails.append(emails_item)

        organization_employee_invitation_request = cls(
            emails=emails,
        )

        organization_employee_invitation_request.additional_properties = d
        return organization_employee_invitation_request

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
