"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar

import attr


T = TypeVar("T", bound="CampaignUsageSummary")


@attr.s(auto_attribs=True)
class CampaignUsageSummary:
    """
    Attributes:
        cost (float):
        currency (str):
        num_calls (int):
        call_time (int):
    """

    cost: float
    currency: str
    num_calls: int
    call_time: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cost = self.cost
        currency = self.currency
        num_calls = self.num_calls
        call_time = self.call_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cost": cost,
                "currency": currency,
                "num_calls": num_calls,
                "call_time": call_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cost = d.pop("cost")

        currency = d.pop("currency")

        num_calls = d.pop("num_calls")

        call_time = d.pop("call_time")

        campaign_usage_summary = cls(
            cost=cost,
            currency=currency,
            num_calls=num_calls,
            call_time=call_time,
        )

        campaign_usage_summary.additional_properties = d
        return campaign_usage_summary

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
