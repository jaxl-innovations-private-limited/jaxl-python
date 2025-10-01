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
    from ..models.app_price import AppPrice
    from ..models.payment_gateway_fees_info import PaymentGatewayFeesInfo
    from ..models.plan_extra_details import PlanExtraDetails
    from ..models.plan_item import PlanItem
    from ..models.plan_type import PlanType
    from ..models.product_group import ProductGroup


T = TypeVar("T", bound="Plan")


@attr.s(auto_attribs=True)
class Plan:
    """
    Attributes:
        id (int):
        app_id (int): Primary key of the App related to this object
        name (str): Plan name must only contain characters allowed by integrated payment providers.  <br/>Provided plan
            name will be used to automatically create plans across various providers.
        type (PlanType):
        item (PlanItem):
        price (AppPrice):
        fees (PaymentGatewayFeesInfo):
        extra_details (PlanExtraDetails):
        includes (List['Plan']):
        product_ids (List['ProductGroup']):
        label (Union[Unset, str]): Label for a plan eg: Most Popular, Best Value Saver etc.
        message (Union[Unset, str]): Description for localization in App Store Connect
        is_bundle (Union[Unset, bool]): Whether this plan is a bundle or single plan
        enabled (Union[Unset, bool]): Whether this object is currently enabled or disabled
        public (Union[Unset, bool]): Public means that all necessary plans have been created on provider end.<br/>Once
            made public, a plan can only be disabled.
        release (Union[Unset, bool]): Release means a plan is available in list plans API i.e. visible inmobile and web
            apps. During creation, a plan can be manually un-marked for release. However, it has to be manually marked for
            release again.<br/> Once marked for release manually, a plan cannot be un-marked again.
    """

    id: int
    app_id: int
    name: str
    type: "PlanType"
    item: "PlanItem"
    price: "AppPrice"
    fees: "PaymentGatewayFeesInfo"
    extra_details: "PlanExtraDetails"
    includes: List["Plan"]
    product_ids: List["ProductGroup"]
    label: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    is_bundle: Union[Unset, bool] = UNSET
    enabled: Union[Unset, bool] = UNSET
    public: Union[Unset, bool] = UNSET
    release: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        app_id = self.app_id
        name = self.name
        type = self.type.to_dict()

        item = self.item.to_dict()

        price = self.price.to_dict()

        fees = self.fees.to_dict()

        extra_details = self.extra_details.to_dict()

        includes = []
        for includes_item_data in self.includes:
            includes_item = includes_item_data.to_dict()

            includes.append(includes_item)

        product_ids = []
        for product_ids_item_data in self.product_ids:
            product_ids_item = product_ids_item_data.to_dict()

            product_ids.append(product_ids_item)

        label = self.label
        message = self.message
        is_bundle = self.is_bundle
        enabled = self.enabled
        public = self.public
        release = self.release

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "app_id": app_id,
                "name": name,
                "type": type,
                "item": item,
                "price": price,
                "fees": fees,
                "extra_details": extra_details,
                "includes": includes,
                "product_ids": product_ids,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if message is not UNSET:
            field_dict["message"] = message
        if is_bundle is not UNSET:
            field_dict["is_bundle"] = is_bundle
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if public is not UNSET:
            field_dict["public"] = public
        if release is not UNSET:
            field_dict["release"] = release

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.app_price import AppPrice
        from ..models.payment_gateway_fees_info import PaymentGatewayFeesInfo
        from ..models.plan_extra_details import PlanExtraDetails
        from ..models.plan_item import PlanItem
        from ..models.plan_type import PlanType
        from ..models.product_group import ProductGroup

        d = src_dict.copy()
        id = d.pop("id")

        app_id = d.pop("app_id")

        name = d.pop("name")

        type = PlanType.from_dict(d.pop("type"))

        item = PlanItem.from_dict(d.pop("item"))

        price = AppPrice.from_dict(d.pop("price"))

        fees = PaymentGatewayFeesInfo.from_dict(d.pop("fees"))

        extra_details = PlanExtraDetails.from_dict(d.pop("extra_details"))

        includes = []
        _includes = d.pop("includes")
        for includes_item_data in _includes:
            includes_item = Plan.from_dict(includes_item_data)

            includes.append(includes_item)

        product_ids = []
        _product_ids = d.pop("product_ids")
        for product_ids_item_data in _product_ids:
            product_ids_item = ProductGroup.from_dict(product_ids_item_data)

            product_ids.append(product_ids_item)

        label = d.pop("label", UNSET)

        message = d.pop("message", UNSET)

        is_bundle = d.pop("is_bundle", UNSET)

        enabled = d.pop("enabled", UNSET)

        public = d.pop("public", UNSET)

        release = d.pop("release", UNSET)

        plan = cls(
            id=id,
            app_id=app_id,
            name=name,
            type=type,
            item=item,
            price=price,
            fees=fees,
            extra_details=extra_details,
            includes=includes,
            product_ids=product_ids,
            label=label,
            message=message,
            is_bundle=is_bundle,
            enabled=enabled,
            public=public,
            release=release,
        )

        plan.additional_properties = d
        return plan

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
