"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset


T = TypeVar("T", bound="PatchedIVRMenuRequest")


@attr.s(auto_attribs=True)
class PatchedIVRMenuRequest:
    """
    Attributes:
        name (Union[Unset, str]): Name of this IVR menu as shown/spoken to user before following up with options
        hangup (Union[Unset, bool]): Whether the call should be ended after speaking out the greeting message
    """

    name: Union[Unset, str] = UNSET
    hangup: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        hangup = self.hangup

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if hangup is not UNSET:
            field_dict["hangup"] = hangup

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        hangup = d.pop("hangup", UNSET)

        patched_ivr_menu_request = cls(
            name=name,
            hangup=hangup,
        )

        patched_ivr_menu_request.additional_properties = d
        return patched_ivr_menu_request

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
