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

from ..types import UNSET, Unset


T = TypeVar("T", bound="Credit")


@attr.s(auto_attribs=True)
class Credit:
    """
    Attributes:
        id (int):
        amount (str):
        currency (int): Currency in which credit was paid.
        reason (str):
        created_on (datetime.datetime): Datetime when this object was created
        agent (Union[Unset, None, int]):
    """

    id: int
    amount: str
    currency: int
    reason: str
    created_on: datetime.datetime
    agent: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        amount = self.amount
        currency = self.currency
        reason = self.reason
        created_on = self.created_on.isoformat()

        agent = self.agent

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "amount": amount,
                "currency": currency,
                "reason": reason,
                "created_on": created_on,
            }
        )
        if agent is not UNSET:
            field_dict["agent"] = agent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        amount = d.pop("amount")

        currency = d.pop("currency")

        reason = d.pop("reason")

        created_on = isoparse(d.pop("created_on"))

        agent = d.pop("agent", UNSET)

        credit = cls(
            id=id,
            amount=amount,
            currency=currency,
            reason=reason,
            created_on=created_on,
            agent=agent,
        )

        credit.additional_properties = d
        return credit

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
