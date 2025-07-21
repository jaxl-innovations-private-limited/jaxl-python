"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.locale_enum import LocaleEnum
from ..types import UNSET, Unset


T = TypeVar("T", bound="CallTranscribeRequest")


@attr.s(auto_attribs=True)
class CallTranscribeRequest:
    """
    Attributes:
        locale (Union[Unset, LocaleEnum]):
        currency (Union[Unset, None, str]):
        total_recharge (Union[Unset, None, str]):
    """

    locale: Union[Unset, LocaleEnum] = UNSET
    currency: Union[Unset, None, str] = UNSET
    total_recharge: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        locale: Union[Unset, str] = UNSET
        if not isinstance(self.locale, Unset):
            locale = self.locale.value

        currency = self.currency
        total_recharge = self.total_recharge

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if locale is not UNSET:
            field_dict["locale"] = locale
        if currency is not UNSET:
            field_dict["currency"] = currency
        if total_recharge is not UNSET:
            field_dict["total_recharge"] = total_recharge

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _locale = d.pop("locale", UNSET)
        locale: Union[Unset, LocaleEnum]
        if isinstance(_locale, Unset):
            locale = UNSET
        else:
            locale = LocaleEnum(_locale)

        currency = d.pop("currency", UNSET)

        total_recharge = d.pop("total_recharge", UNSET)

        call_transcribe_request = cls(
            locale=locale,
            currency=currency,
            total_recharge=total_recharge,
        )

        call_transcribe_request.additional_properties = d
        return call_transcribe_request

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
