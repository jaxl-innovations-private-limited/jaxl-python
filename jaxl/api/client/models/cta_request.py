"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ivr_collection_request import IVRCollectionRequest


T = TypeVar("T", bound="CTARequest")


@attr.s(auto_attribs=True)
class CTARequest:
    """
    Attributes:
        phone_number (Union[Unset, None, str]):
        devices (Union[Unset, None, List[int]]):
        appusers (Union[Unset, None, List[int]]):
        collections (Union[Unset, None, IVRCollectionRequest]):
        webhook (Union[Unset, None, str]):
    """

    phone_number: Union[Unset, None, str] = UNSET
    devices: Union[Unset, None, List[int]] = UNSET
    appusers: Union[Unset, None, List[int]] = UNSET
    collections: Union[Unset, None, "IVRCollectionRequest"] = UNSET
    webhook: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        phone_number = self.phone_number
        devices: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.devices, Unset):
            if self.devices is None:
                devices = None
            else:
                devices = self.devices

        appusers: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.appusers, Unset):
            if self.appusers is None:
                appusers = None
            else:
                appusers = self.appusers

        collections: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.collections, Unset):
            collections = self.collections.to_dict() if self.collections else None

        webhook = self.webhook

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if devices is not UNSET:
            field_dict["devices"] = devices
        if appusers is not UNSET:
            field_dict["appusers"] = appusers
        if collections is not UNSET:
            field_dict["collections"] = collections
        if webhook is not UNSET:
            field_dict["webhook"] = webhook

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ivr_collection_request import IVRCollectionRequest

        d = src_dict.copy()
        phone_number = d.pop("phone_number", UNSET)

        devices = cast(List[int], d.pop("devices", UNSET))

        appusers = cast(List[int], d.pop("appusers", UNSET))

        _collections = d.pop("collections", UNSET)
        collections: Union[Unset, None, IVRCollectionRequest]
        if _collections is None:
            collections = None
        elif isinstance(_collections, Unset):
            collections = UNSET
        else:
            collections = IVRCollectionRequest.from_dict(_collections)

        webhook = d.pop("webhook", UNSET)

        cta_request = cls(
            phone_number=phone_number,
            devices=devices,
            appusers=appusers,
            collections=collections,
            webhook=webhook,
        )

        cta_request.additional_properties = d
        return cta_request

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
