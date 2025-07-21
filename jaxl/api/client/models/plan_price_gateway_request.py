"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.plan_price_gateway_request_attributes import (
        PlanPriceGatewayRequestAttributes,
    )


T = TypeVar("T", bound="PlanPriceGatewayRequest")


@attr.s(auto_attribs=True)
class PlanPriceGatewayRequest:
    """
    Attributes:
        plan (int):
        price (int):
        gateway (Union[Unset, int]):
        sku (Union[Unset, None, str]): Stock keeping unit pertaining to the item being purchased as part of this order.
            eg: phone number
        attributes (Union[Unset, None, PlanPriceGatewayRequestAttributes]):
        bundle (Union[Unset, List['PlanPriceGatewayRequest']]):
    """

    plan: int
    price: int
    gateway: Union[Unset, int] = UNSET
    sku: Union[Unset, None, str] = UNSET
    attributes: Union[Unset, None, "PlanPriceGatewayRequestAttributes"] = UNSET
    bundle: Union[Unset, List["PlanPriceGatewayRequest"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        plan = self.plan
        price = self.price
        gateway = self.gateway
        sku = self.sku
        attributes: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict() if self.attributes else None

        bundle: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.bundle, Unset):
            bundle = []
            for bundle_item_data in self.bundle:
                bundle_item = bundle_item_data.to_dict()

                bundle.append(bundle_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plan": plan,
                "price": price,
            }
        )
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if sku is not UNSET:
            field_dict["sku"] = sku
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if bundle is not UNSET:
            field_dict["bundle"] = bundle

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.plan_price_gateway_request_attributes import (
            PlanPriceGatewayRequestAttributes,
        )

        d = src_dict.copy()
        plan = d.pop("plan")

        price = d.pop("price")

        gateway = d.pop("gateway", UNSET)

        sku = d.pop("sku", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, None, PlanPriceGatewayRequestAttributes]
        if _attributes is None:
            attributes = None
        elif isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = PlanPriceGatewayRequestAttributes.from_dict(_attributes)

        bundle = []
        _bundle = d.pop("bundle", UNSET)
        for bundle_item_data in _bundle or []:
            bundle_item = PlanPriceGatewayRequest.from_dict(bundle_item_data)

            bundle.append(bundle_item)

        plan_price_gateway_request = cls(
            plan=plan,
            price=price,
            gateway=gateway,
            sku=sku,
            attributes=attributes,
            bundle=bundle,
        )

        plan_price_gateway_request.additional_properties = d
        return plan_price_gateway_request

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
