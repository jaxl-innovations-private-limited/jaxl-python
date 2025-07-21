"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Optional,
    Type,
    TypeVar,
    cast,
)

import attr


if TYPE_CHECKING:
    from ..models.family_membership import FamilyMembership


T = TypeVar("T", bound="Family")


@attr.s(auto_attribs=True)
class Family:
    """Adds a 'jaxlid' field which contains signed ID information.

    Attributes:
        id (int):
        name (str): Family name
        created_by (int): Family owner
        members (List['FamilyMembership']):
        groups (List[int]): Permission groups assigned to this family members
        jaxlid (Optional[str]):
    """

    id: int
    name: str
    created_by: int
    members: List["FamilyMembership"]
    groups: List[int]
    jaxlid: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        created_by = self.created_by
        members = []
        for members_item_data in self.members:
            members_item = members_item_data.to_dict()

            members.append(members_item)

        groups = self.groups

        jaxlid = self.jaxlid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "created_by": created_by,
                "members": members,
                "groups": groups,
                "jaxlid": jaxlid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.family_membership import FamilyMembership

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        created_by = d.pop("created_by")

        members = []
        _members = d.pop("members")
        for members_item_data in _members:
            members_item = FamilyMembership.from_dict(members_item_data)

            members.append(members_item)

        groups = cast(List[int], d.pop("groups"))

        jaxlid = d.pop("jaxlid")

        family = cls(
            id=id,
            name=name,
            created_by=created_by,
            members=members,
            groups=groups,
            jaxlid=jaxlid,
        )

        family.additional_properties = d
        return family

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
