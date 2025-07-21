"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

from ..models.current_status_enum import CurrentStatusEnum


T = TypeVar("T", bound="FamilyMembership")


@attr.s(auto_attribs=True)
class FamilyMembership:
    """Adds a 'jaxlid' field which contains signed ID information.

    Attributes:
        id (int):
        member (int):
        status (CurrentStatusEnum):
        jaxlid (Optional[str]):
    """

    id: int
    member: int
    status: CurrentStatusEnum
    jaxlid: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        member = self.member
        status = self.status.value

        jaxlid = self.jaxlid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "member": member,
                "status": status,
                "jaxlid": jaxlid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        member = d.pop("member")

        status = CurrentStatusEnum(d.pop("status"))

        jaxlid = d.pop("jaxlid")

        family_membership = cls(
            id=id,
            member=member,
            status=status,
            jaxlid=jaxlid,
        )

        family_membership.additional_properties = d
        return family_membership

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
