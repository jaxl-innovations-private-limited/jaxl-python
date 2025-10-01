"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.call_usage_stats_response import CallUsageStatsResponse


T = TypeVar("T", bound="CallUsageByCurrencyResponse")


@attr.s(auto_attribs=True)
class CallUsageByCurrencyResponse:
    """
    Attributes:
        signed (str):
        num_calls (int):
        call_time (int):
        start_time (datetime.datetime):
        end_time (datetime.datetime):
        stats (List['CallUsageStatsResponse']):
        cost (Union[Unset, None, float]):
        currency (Union[Unset, None, str]):
    """

    signed: str
    num_calls: int
    call_time: int
    start_time: datetime.datetime
    end_time: datetime.datetime
    stats: List["CallUsageStatsResponse"]
    cost: Union[Unset, None, float] = UNSET
    currency: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        signed = self.signed
        num_calls = self.num_calls
        call_time = self.call_time
        start_time = self.start_time.isoformat()

        end_time = self.end_time.isoformat()

        stats = []
        for stats_item_data in self.stats:
            stats_item = stats_item_data.to_dict()

            stats.append(stats_item)

        cost = self.cost
        currency = self.currency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "signed": signed,
                "num_calls": num_calls,
                "call_time": call_time,
                "start_time": start_time,
                "end_time": end_time,
                "stats": stats,
            }
        )
        if cost is not UNSET:
            field_dict["cost"] = cost
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.call_usage_stats_response import CallUsageStatsResponse

        d = src_dict.copy()
        signed = d.pop("signed")

        num_calls = d.pop("num_calls")

        call_time = d.pop("call_time")

        start_time = isoparse(d.pop("start_time"))

        end_time = isoparse(d.pop("end_time"))

        stats = []
        _stats = d.pop("stats")
        for stats_item_data in _stats:
            stats_item = CallUsageStatsResponse.from_dict(stats_item_data)

            stats.append(stats_item)

        cost = d.pop("cost", UNSET)

        currency = d.pop("currency", UNSET)

        call_usage_by_currency_response = cls(
            signed=signed,
            num_calls=num_calls,
            call_time=call_time,
            start_time=start_time,
            end_time=end_time,
            stats=stats,
            cost=cost,
            currency=currency,
        )

        call_usage_by_currency_response.additional_properties = d
        return call_usage_by_currency_response

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
