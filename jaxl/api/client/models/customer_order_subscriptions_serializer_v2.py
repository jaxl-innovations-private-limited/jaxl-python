"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.customer_order_subscriptions_serializer_v2_status_enum import (
    CustomerOrderSubscriptionsSerializerV2StatusEnum,
)
from ..models.order_status_enum import OrderStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.can_user_resubscribe_plan import CanUserResubscribePlan
    from ..models.customer_provider_serializer_v2 import CustomerProviderSerializerV2
    from ..models.item import Item
    from ..models.payment_gateway_fees_info import PaymentGatewayFeesInfo
    from ..models.plan import Plan
    from ..models.plan_cancel_info import PlanCancelInfo
    from ..models.plan_expiry_timestamp import PlanExpiryTimestamp


T = TypeVar("T", bound="CustomerOrderSubscriptionsSerializerV2")


@attr.s(auto_attribs=True)
class CustomerOrderSubscriptionsSerializerV2:
    """Adds a 'jaxlid' field which contains signed ID information.

    Attributes:
        id (int):
        plan_id (int):
        provider_plan_id (str):
        name (str):
        status (CustomerOrderSubscriptionsSerializerV2StatusEnum):
        order_status (OrderStatusEnum):
        provider (CustomerProviderSerializerV2):
        plan (Plan):
        can_resubscribe (CanUserResubscribePlan):
        can_resubscribe_sku (bool):
        expiry_timestamp (PlanExpiryTimestamp):
        cancel_timestamp (PlanCancelInfo):
        cost (float):
        fees (PaymentGatewayFeesInfo):
        symbol (str):
        item (Item):
        tags (List[str]):
        includes (List['CustomerOrderSubscriptionsSerializerV2']):
        reason (Union[Unset, None, str]): reason why sku is not eligible for resubscription.
        next_invoice_timestamp (Union[Unset, None, datetime.datetime]): next renewal timestamp
        jaxlid (Optional[str]):
    """

    id: int
    plan_id: int
    provider_plan_id: str
    name: str
    status: CustomerOrderSubscriptionsSerializerV2StatusEnum
    order_status: OrderStatusEnum
    provider: "CustomerProviderSerializerV2"
    plan: "Plan"
    can_resubscribe: "CanUserResubscribePlan"
    can_resubscribe_sku: bool
    expiry_timestamp: "PlanExpiryTimestamp"
    cancel_timestamp: "PlanCancelInfo"
    cost: float
    fees: "PaymentGatewayFeesInfo"
    symbol: str
    item: "Item"
    tags: List[str]
    includes: List["CustomerOrderSubscriptionsSerializerV2"]
    jaxlid: Optional[str]
    reason: Union[Unset, None, str] = UNSET
    next_invoice_timestamp: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        plan_id = self.plan_id
        provider_plan_id = self.provider_plan_id
        name = self.name
        status = self.status.value

        order_status = self.order_status.value

        provider = self.provider.to_dict()

        plan = self.plan.to_dict()

        can_resubscribe = self.can_resubscribe.to_dict()

        can_resubscribe_sku = self.can_resubscribe_sku
        expiry_timestamp = self.expiry_timestamp.to_dict()

        cancel_timestamp = self.cancel_timestamp.to_dict()

        cost = self.cost
        fees = self.fees.to_dict()

        symbol = self.symbol
        item = self.item.to_dict()

        tags = self.tags

        includes = []
        for includes_item_data in self.includes:
            includes_item = includes_item_data.to_dict()

            includes.append(includes_item)

        reason = self.reason
        next_invoice_timestamp: Union[Unset, None, str] = UNSET
        if not isinstance(self.next_invoice_timestamp, Unset):
            next_invoice_timestamp = (
                self.next_invoice_timestamp.isoformat()
                if self.next_invoice_timestamp
                else None
            )

        jaxlid = self.jaxlid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "plan_id": plan_id,
                "provider_plan_id": provider_plan_id,
                "name": name,
                "status": status,
                "order_status": order_status,
                "provider": provider,
                "plan": plan,
                "can_resubscribe": can_resubscribe,
                "can_resubscribe_sku": can_resubscribe_sku,
                "expiry_timestamp": expiry_timestamp,
                "cancel_timestamp": cancel_timestamp,
                "cost": cost,
                "fees": fees,
                "symbol": symbol,
                "item": item,
                "tags": tags,
                "includes": includes,
                "jaxlid": jaxlid,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason
        if next_invoice_timestamp is not UNSET:
            field_dict["next_invoice_timestamp"] = next_invoice_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.can_user_resubscribe_plan import CanUserResubscribePlan
        from ..models.customer_provider_serializer_v2 import (
            CustomerProviderSerializerV2,
        )
        from ..models.item import Item
        from ..models.payment_gateway_fees_info import PaymentGatewayFeesInfo
        from ..models.plan import Plan
        from ..models.plan_cancel_info import PlanCancelInfo
        from ..models.plan_expiry_timestamp import PlanExpiryTimestamp

        d = src_dict.copy()
        id = d.pop("id")

        plan_id = d.pop("plan_id")

        provider_plan_id = d.pop("provider_plan_id")

        name = d.pop("name")

        status = CustomerOrderSubscriptionsSerializerV2StatusEnum(d.pop("status"))

        order_status = OrderStatusEnum(d.pop("order_status"))

        provider = CustomerProviderSerializerV2.from_dict(d.pop("provider"))

        plan = Plan.from_dict(d.pop("plan"))

        can_resubscribe = CanUserResubscribePlan.from_dict(d.pop("can_resubscribe"))

        can_resubscribe_sku = d.pop("can_resubscribe_sku")

        expiry_timestamp = PlanExpiryTimestamp.from_dict(d.pop("expiry_timestamp"))

        cancel_timestamp = PlanCancelInfo.from_dict(d.pop("cancel_timestamp"))

        cost = d.pop("cost")

        fees = PaymentGatewayFeesInfo.from_dict(d.pop("fees"))

        symbol = d.pop("symbol")

        item = Item.from_dict(d.pop("item"))

        tags = cast(List[str], d.pop("tags"))

        includes = []
        _includes = d.pop("includes")
        for includes_item_data in _includes:
            includes_item = CustomerOrderSubscriptionsSerializerV2.from_dict(
                includes_item_data
            )

            includes.append(includes_item)

        reason = d.pop("reason", UNSET)

        _next_invoice_timestamp = d.pop("next_invoice_timestamp", UNSET)
        next_invoice_timestamp: Union[Unset, None, datetime.datetime]
        if _next_invoice_timestamp is None:
            next_invoice_timestamp = None
        elif isinstance(_next_invoice_timestamp, Unset):
            next_invoice_timestamp = UNSET
        else:
            next_invoice_timestamp = isoparse(_next_invoice_timestamp)

        jaxlid = d.pop("jaxlid")

        customer_order_subscriptions_serializer_v2 = cls(
            id=id,
            plan_id=plan_id,
            provider_plan_id=provider_plan_id,
            name=name,
            status=status,
            order_status=order_status,
            provider=provider,
            plan=plan,
            can_resubscribe=can_resubscribe,
            can_resubscribe_sku=can_resubscribe_sku,
            expiry_timestamp=expiry_timestamp,
            cancel_timestamp=cancel_timestamp,
            cost=cost,
            fees=fees,
            symbol=symbol,
            item=item,
            tags=tags,
            includes=includes,
            reason=reason,
            next_invoice_timestamp=next_invoice_timestamp,
            jaxlid=jaxlid,
        )

        customer_order_subscriptions_serializer_v2.additional_properties = d
        return customer_order_subscriptions_serializer_v2

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
