"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="CallUsageStatsResponse")


@attr.s(auto_attribs=True)
class CallUsageStatsResponse:
    """
    Attributes:
        day (datetime.datetime):
        num_calls (int):
        call_time (int):
        total_cost (float):
    """

    day: datetime.datetime
    num_calls: int
    call_time: int
    total_cost: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        day = self.day.isoformat()

        num_calls = self.num_calls
        call_time = self.call_time
        total_cost = self.total_cost

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "day": day,
                "num_calls": num_calls,
                "call_time": call_time,
                "total_cost": total_cost,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        day = isoparse(d.pop("day"))

        num_calls = d.pop("num_calls")

        call_time = d.pop("call_time")

        total_cost = d.pop("total_cost")

        call_usage_stats_response = cls(
            day=day,
            num_calls=num_calls,
            call_time=call_time,
            total_cost=total_cost,
        )

        call_usage_stats_response.additional_properties = d
        return call_usage_stats_response

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
