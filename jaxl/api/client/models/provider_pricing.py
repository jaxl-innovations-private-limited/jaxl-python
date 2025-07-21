"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset


T = TypeVar("T", bound="ProviderPricing")


@attr.s(auto_attribs=True)
class ProviderPricing:
    """
    Attributes:
        ios (Union[Unset, None, float]):
        android (Union[Unset, None, float]):
        web (Union[Unset, None, float]):
    """

    ios: Union[Unset, None, float] = UNSET
    android: Union[Unset, None, float] = UNSET
    web: Union[Unset, None, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ios = self.ios
        android = self.android
        web = self.web

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ios is not UNSET:
            field_dict["ios"] = ios
        if android is not UNSET:
            field_dict["android"] = android
        if web is not UNSET:
            field_dict["web"] = web

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ios = d.pop("ios", UNSET)

        android = d.pop("android", UNSET)

        web = d.pop("web", UNSET)

        provider_pricing = cls(
            ios=ios,
            android=android,
            web=web,
        )

        provider_pricing.additional_properties = d
        return provider_pricing

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
