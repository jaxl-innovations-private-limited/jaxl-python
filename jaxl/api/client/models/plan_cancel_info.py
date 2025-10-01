"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.canceled_by_enum import CanceledByEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlanCancelInfo")


@attr.s(auto_attribs=True)
class PlanCancelInfo:
    """
    Attributes:
        is_canceled (bool):
        canceled_by (CanceledByEnum):
        canceled_at (Union[Unset, None, datetime.datetime]):
    """

    is_canceled: bool
    canceled_by: CanceledByEnum
    canceled_at: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_canceled = self.is_canceled
        canceled_by = self.canceled_by.value

        canceled_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.canceled_at, Unset):
            canceled_at = self.canceled_at.isoformat() if self.canceled_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "is_canceled": is_canceled,
                "canceled_by": canceled_by,
            }
        )
        if canceled_at is not UNSET:
            field_dict["canceled_at"] = canceled_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_canceled = d.pop("is_canceled")

        canceled_by = CanceledByEnum(d.pop("canceled_by"))

        _canceled_at = d.pop("canceled_at", UNSET)
        canceled_at: Union[Unset, None, datetime.datetime]
        if _canceled_at is None:
            canceled_at = None
        elif isinstance(_canceled_at, Unset):
            canceled_at = UNSET
        else:
            canceled_at = isoparse(_canceled_at)

        plan_cancel_info = cls(
            is_canceled=is_canceled,
            canceled_by=canceled_by,
            canceled_at=canceled_at,
        )

        plan_cancel_info.additional_properties = d
        return plan_cancel_info

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
