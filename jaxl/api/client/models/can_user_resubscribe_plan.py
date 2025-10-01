"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CanUserResubscribePlan")


@attr.s(auto_attribs=True)
class CanUserResubscribePlan:
    """
    Attributes:
        eligible (bool):
        reason (str):
    """

    eligible: bool
    reason: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        eligible = self.eligible
        reason = self.reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eligible": eligible,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        eligible = d.pop("eligible")

        reason = d.pop("reason")

        can_user_resubscribe_plan = cls(
            eligible=eligible,
            reason=reason,
        )

        can_user_resubscribe_plan.additional_properties = d
        return can_user_resubscribe_plan

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
