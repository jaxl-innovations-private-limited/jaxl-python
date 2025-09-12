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


T = TypeVar("T", bound="Payment")


@attr.s(auto_attribs=True)
class Payment:
    """
    Attributes:
        id (int):
        order_id (int):
        paid_by (str):
        plan_name (str):
        provider_plan_id (str):
        transaction_id (int):
        amount (float):
        currency_symbol (str):
        transaction_timestamp (datetime.datetime):
        status (str):
        item_type (str): Item for example PHONE_NUMBER, LINKED_DEVICE, BUNDLE, RECHARGE etc
        period (str):
        includes (List['Payment']):
        interval (Union[Unset, int]):
        sku (Union[Unset, str]):
        subscription_type (Union[Unset, str]):
    """

    id: int
    order_id: int
    paid_by: str
    plan_name: str
    provider_plan_id: str
    transaction_id: int
    amount: float
    currency_symbol: str
    transaction_timestamp: datetime.datetime
    status: str
    item_type: str
    period: str
    includes: List["Payment"]
    interval: Union[Unset, int] = UNSET
    sku: Union[Unset, str] = UNSET
    subscription_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        order_id = self.order_id
        paid_by = self.paid_by
        plan_name = self.plan_name
        provider_plan_id = self.provider_plan_id
        transaction_id = self.transaction_id
        amount = self.amount
        currency_symbol = self.currency_symbol
        transaction_timestamp = self.transaction_timestamp.isoformat()

        status = self.status
        item_type = self.item_type
        period = self.period
        includes = []
        for includes_item_data in self.includes:
            includes_item = includes_item_data.to_dict()

            includes.append(includes_item)

        interval = self.interval
        sku = self.sku
        subscription_type = self.subscription_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "order_id": order_id,
                "paid_by": paid_by,
                "plan_name": plan_name,
                "provider_plan_id": provider_plan_id,
                "transaction_id": transaction_id,
                "amount": amount,
                "currency_symbol": currency_symbol,
                "transaction_timestamp": transaction_timestamp,
                "status": status,
                "item_type": item_type,
                "period": period,
                "includes": includes,
            }
        )
        if interval is not UNSET:
            field_dict["interval"] = interval
        if sku is not UNSET:
            field_dict["sku"] = sku
        if subscription_type is not UNSET:
            field_dict["subscription_type"] = subscription_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        order_id = d.pop("order_id")

        paid_by = d.pop("paid_by")

        plan_name = d.pop("plan_name")

        provider_plan_id = d.pop("provider_plan_id")

        transaction_id = d.pop("transaction_id")

        amount = d.pop("amount")

        currency_symbol = d.pop("currency_symbol")

        transaction_timestamp = isoparse(d.pop("transaction_timestamp"))

        status = d.pop("status")

        item_type = d.pop("item_type")

        period = d.pop("period")

        includes = []
        _includes = d.pop("includes")
        for includes_item_data in _includes:
            includes_item = Payment.from_dict(includes_item_data)

            includes.append(includes_item)

        interval = d.pop("interval", UNSET)

        sku = d.pop("sku", UNSET)

        subscription_type = d.pop("subscription_type", UNSET)

        payment = cls(
            id=id,
            order_id=order_id,
            paid_by=paid_by,
            plan_name=plan_name,
            provider_plan_id=provider_plan_id,
            transaction_id=transaction_id,
            amount=amount,
            currency_symbol=currency_symbol,
            transaction_timestamp=transaction_timestamp,
            status=status,
            item_type=item_type,
            period=period,
            includes=includes,
            interval=interval,
            sku=sku,
            subscription_type=subscription_type,
        )

        payment.additional_properties = d
        return payment

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
