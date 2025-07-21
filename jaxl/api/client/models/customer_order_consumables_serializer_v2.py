"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.order_status_enum import OrderStatusEnum


if TYPE_CHECKING:
    from ..models.customer_provider_serializer_v2 import (
        CustomerProviderSerializerV2,
    )
    from ..models.payment_gateway_fees_info import PaymentGatewayFeesInfo


T = TypeVar("T", bound="CustomerOrderConsumablesSerializerV2")


@attr.s(auto_attribs=True)
class CustomerOrderConsumablesSerializerV2:
    """
    Attributes:
        id (int):
        plan_id (int):
        name (str):
        order_status (OrderStatusEnum):
        provider (CustomerProviderSerializerV2):
        cost (float):
        fees (PaymentGatewayFeesInfo):
        symbol (str):
    """

    id: int
    plan_id: int
    name: str
    order_status: OrderStatusEnum
    provider: "CustomerProviderSerializerV2"
    cost: float
    fees: "PaymentGatewayFeesInfo"
    symbol: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        plan_id = self.plan_id
        name = self.name
        order_status = self.order_status.value

        provider = self.provider.to_dict()

        cost = self.cost
        fees = self.fees.to_dict()

        symbol = self.symbol

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "plan_id": plan_id,
                "name": name,
                "order_status": order_status,
                "provider": provider,
                "cost": cost,
                "fees": fees,
                "symbol": symbol,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer_provider_serializer_v2 import (
            CustomerProviderSerializerV2,
        )
        from ..models.payment_gateway_fees_info import PaymentGatewayFeesInfo

        d = src_dict.copy()
        id = d.pop("id")

        plan_id = d.pop("plan_id")

        name = d.pop("name")

        order_status = OrderStatusEnum(d.pop("order_status"))

        provider = CustomerProviderSerializerV2.from_dict(d.pop("provider"))

        cost = d.pop("cost")

        fees = PaymentGatewayFeesInfo.from_dict(d.pop("fees"))

        symbol = d.pop("symbol")

        customer_order_consumables_serializer_v2 = cls(
            id=id,
            plan_id=plan_id,
            name=name,
            order_status=order_status,
            provider=provider,
            cost=cost,
            fees=fees,
            symbol=symbol,
        )

        customer_order_consumables_serializer_v2.additional_properties = d
        return customer_order_consumables_serializer_v2

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
