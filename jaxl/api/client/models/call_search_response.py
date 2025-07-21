"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse


if TYPE_CHECKING:
    from ..models.call import Call


T = TypeVar("T", bound="CallSearchResponse")


@attr.s(auto_attribs=True)
class CallSearchResponse:
    """
    Attributes:
        number (str):
        count (int):
        last_activity (datetime.datetime):
        latest_call (Call):
    """

    number: str
    count: int
    last_activity: datetime.datetime
    latest_call: "Call"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number = self.number
        count = self.count
        last_activity = self.last_activity.isoformat()

        latest_call = self.latest_call.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "number": number,
                "count": count,
                "last_activity": last_activity,
                "latest_call": latest_call,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.call import Call

        d = src_dict.copy()
        number = d.pop("number")

        count = d.pop("count")

        last_activity = isoparse(d.pop("last_activity"))

        latest_call = Call.from_dict(d.pop("latest_call"))

        call_search_response = cls(
            number=number,
            count=count,
            last_activity=last_activity,
            latest_call=latest_call,
        )

        call_search_response.additional_properties = d
        return call_search_response

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
