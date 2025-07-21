"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.duration_enum import DurationEnum
from ..models.gateway_enum import GatewayEnum
from ..models.iso_country_enum import IsoCountryEnum
from ..models.plan_create_type_enum import PlanCreateTypeEnum
from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.plan_create_request_item_attributes import (
        PlanCreateRequestItemAttributes,
    )


T = TypeVar("T", bound="PlanCreateRequest")


@attr.s(auto_attribs=True)
class PlanCreateRequest:
    """
    Attributes:
        item (str): Enter item_slug
        iso_country (IsoCountryEnum):
        selling_price (float):
        type (Union[Unset, PlanCreateTypeEnum]):  Default: PlanCreateTypeEnum.CONSUMABLE.
        gateway (Union[Unset, List[GatewayEnum]]):
        alternate_selling_price (Union[Unset, float]):
        android_selling_price (Union[Unset, float]):
        name (Union[Unset, str]):
        duration (Union[Unset, DurationEnum]):
        message (Union[Unset, str]):
        release (Union[Unset, bool]):  Default: True.
        publish (Union[Unset, bool]):  Default: True.
        item_attributes (Union[Unset, PlanCreateRequestItemAttributes]):
    """

    item: str
    iso_country: IsoCountryEnum
    selling_price: float
    type: Union[Unset, PlanCreateTypeEnum] = PlanCreateTypeEnum.CONSUMABLE
    gateway: Union[Unset, List[GatewayEnum]] = UNSET
    alternate_selling_price: Union[Unset, float] = UNSET
    android_selling_price: Union[Unset, float] = UNSET
    name: Union[Unset, str] = UNSET
    duration: Union[Unset, DurationEnum] = UNSET
    message: Union[Unset, str] = UNSET
    release: Union[Unset, bool] = True
    publish: Union[Unset, bool] = True
    item_attributes: Union[Unset, "PlanCreateRequestItemAttributes"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item = self.item
        iso_country = self.iso_country.value

        selling_price = self.selling_price
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        gateway: Union[Unset, List[int]] = UNSET
        if not isinstance(self.gateway, Unset):
            gateway = []
            for gateway_item_data in self.gateway:
                gateway_item = gateway_item_data.value

                gateway.append(gateway_item)

        alternate_selling_price = self.alternate_selling_price
        android_selling_price = self.android_selling_price
        name = self.name
        duration: Union[Unset, str] = UNSET
        if not isinstance(self.duration, Unset):
            duration = self.duration.value

        message = self.message
        release = self.release
        publish = self.publish
        item_attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.item_attributes, Unset):
            item_attributes = self.item_attributes.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item": item,
                "iso_country": iso_country,
                "selling_price": selling_price,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if alternate_selling_price is not UNSET:
            field_dict["alternate_selling_price"] = alternate_selling_price
        if android_selling_price is not UNSET:
            field_dict["android_selling_price"] = android_selling_price
        if name is not UNSET:
            field_dict["name"] = name
        if duration is not UNSET:
            field_dict["duration"] = duration
        if message is not UNSET:
            field_dict["message"] = message
        if release is not UNSET:
            field_dict["release"] = release
        if publish is not UNSET:
            field_dict["publish"] = publish
        if item_attributes is not UNSET:
            field_dict["item_attributes"] = item_attributes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.plan_create_request_item_attributes import (
            PlanCreateRequestItemAttributes,
        )

        d = src_dict.copy()
        item = d.pop("item")

        iso_country = IsoCountryEnum(d.pop("iso_country"))

        selling_price = d.pop("selling_price")

        _type = d.pop("type", UNSET)
        type: Union[Unset, PlanCreateTypeEnum]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = PlanCreateTypeEnum(_type)

        gateway = []
        _gateway = d.pop("gateway", UNSET)
        for gateway_item_data in _gateway or []:
            gateway_item = GatewayEnum(gateway_item_data)

            gateway.append(gateway_item)

        alternate_selling_price = d.pop("alternate_selling_price", UNSET)

        android_selling_price = d.pop("android_selling_price", UNSET)

        name = d.pop("name", UNSET)

        _duration = d.pop("duration", UNSET)
        duration: Union[Unset, DurationEnum]
        if isinstance(_duration, Unset):
            duration = UNSET
        else:
            duration = DurationEnum(_duration)

        message = d.pop("message", UNSET)

        release = d.pop("release", UNSET)

        publish = d.pop("publish", UNSET)

        _item_attributes = d.pop("item_attributes", UNSET)
        item_attributes: Union[Unset, PlanCreateRequestItemAttributes]
        if isinstance(_item_attributes, Unset):
            item_attributes = UNSET
        else:
            item_attributes = PlanCreateRequestItemAttributes.from_dict(
                _item_attributes
            )

        plan_create_request = cls(
            item=item,
            iso_country=iso_country,
            selling_price=selling_price,
            type=type,
            gateway=gateway,
            alternate_selling_price=alternate_selling_price,
            android_selling_price=android_selling_price,
            name=name,
            duration=duration,
            message=message,
            release=release,
            publish=publish,
            item_attributes=item_attributes,
        )

        plan_create_request.additional_properties = d
        return plan_create_request

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
