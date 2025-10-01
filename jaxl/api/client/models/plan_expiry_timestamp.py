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

from ..models.plan_expiry_timestamp_type_enum import PlanExpiryTimestampTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlanExpiryTimestamp")


@attr.s(auto_attribs=True)
class PlanExpiryTimestamp:
    """
    Attributes:
        type (PlanExpiryTimestampTypeEnum):
        timestamp (Union[Unset, None, datetime.datetime]): Timestamp when plan will expire
        time_left_days (Union[Unset, None, int]): Time left in days for plan to expire
    """

    type: PlanExpiryTimestampTypeEnum
    timestamp: Union[Unset, None, datetime.datetime] = UNSET
    time_left_days: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        timestamp: Union[Unset, None, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat() if self.timestamp else None

        time_left_days = self.time_left_days

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if time_left_days is not UNSET:
            field_dict["time_left_days"] = time_left_days

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PlanExpiryTimestampTypeEnum(d.pop("type"))

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, None, datetime.datetime]
        if _timestamp is None:
            timestamp = None
        elif isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        time_left_days = d.pop("time_left_days", UNSET)

        plan_expiry_timestamp = cls(
            type=type,
            timestamp=timestamp,
            time_left_days=time_left_days,
        )

        plan_expiry_timestamp.additional_properties = d
        return plan_expiry_timestamp

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
