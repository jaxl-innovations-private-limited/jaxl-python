"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset


T = TypeVar("T", bound="PhoneNumberCheckResponse")


@attr.s(auto_attribs=True)
class PhoneNumberCheckResponse:
    """
    Attributes:
        access (Union[Unset, None, str]):
        refresh (Union[Unset, None, str]):
        reason (Union[Unset, None, str]):
    """

    access: Union[Unset, None, str] = UNSET
    refresh: Union[Unset, None, str] = UNSET
    reason: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access = self.access
        refresh = self.refresh
        reason = self.reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access is not UNSET:
            field_dict["access"] = access
        if refresh is not UNSET:
            field_dict["refresh"] = refresh
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access = d.pop("access", UNSET)

        refresh = d.pop("refresh", UNSET)

        reason = d.pop("reason", UNSET)

        phone_number_check_response = cls(
            access=access,
            refresh=refresh,
            reason=reason,
        )

        phone_number_check_response.additional_properties = d
        return phone_number_check_response

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
