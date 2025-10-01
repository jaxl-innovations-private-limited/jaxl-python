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

T = TypeVar("T", bound="Analytic")


@attr.s(auto_attribs=True)
class Analytic:
    """
    Attributes:
        normalized_value (float):
        actual_value (int):
        start_time (datetime.datetime):
        end_time (datetime.datetime):
    """

    normalized_value: float
    actual_value: int
    start_time: datetime.datetime
    end_time: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        normalized_value = self.normalized_value
        actual_value = self.actual_value
        start_time = self.start_time.isoformat()

        end_time = self.end_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "normalized_value": normalized_value,
                "actual_value": actual_value,
                "start_time": start_time,
                "end_time": end_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        normalized_value = d.pop("normalized_value")

        actual_value = d.pop("actual_value")

        start_time = isoparse(d.pop("start_time"))

        end_time = isoparse(d.pop("end_time"))

        analytic = cls(
            normalized_value=normalized_value,
            actual_value=actual_value,
            start_time=start_time,
            end_time=end_time,
        )

        analytic.additional_properties = d
        return analytic

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
