"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_preferences import OrganizationPreferences


T = TypeVar("T", bound="Organization")


@attr.s(auto_attribs=True)
class Organization:
    """Adds a 'jaxlid' field which contains signed ID information.

    Attributes:
        id (int):
        name (str): Name of the organization
        preferences (OrganizationPreferences): Organization owner preferences
        domain (Union[Unset, None, str]): Organization domain
        owner (Union[Unset, None, int]): AppUser who owns this organization
        phone_number (Union[Unset, None, str]): Organization cellular number provided by organization
        jaxlid (Optional[str]):
    """

    id: int
    name: str
    preferences: "OrganizationPreferences"
    jaxlid: Optional[str]
    domain: Union[Unset, None, str] = UNSET
    owner: Union[Unset, None, int] = UNSET
    phone_number: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        preferences = self.preferences.to_dict()

        domain = self.domain
        owner = self.owner
        phone_number = self.phone_number
        jaxlid = self.jaxlid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "preferences": preferences,
                "jaxlid": jaxlid,
            }
        )
        if domain is not UNSET:
            field_dict["domain"] = domain
        if owner is not UNSET:
            field_dict["owner"] = owner
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.organization_preferences import OrganizationPreferences

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        preferences = OrganizationPreferences.from_dict(d.pop("preferences"))

        domain = d.pop("domain", UNSET)

        owner = d.pop("owner", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        jaxlid = d.pop("jaxlid")

        organization = cls(
            id=id,
            name=name,
            preferences=preferences,
            domain=domain,
            owner=owner,
            phone_number=phone_number,
            jaxlid=jaxlid,
        )

        organization.additional_properties = d
        return organization

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
