"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset


T = TypeVar("T", bound="RazorPayModel")


@attr.s(auto_attribs=True)
class RazorPayModel:
    """
    Attributes:
        backdropclose (Union[Unset, bool]):
        escape (Union[Unset, bool]):
        handleback (Union[Unset, bool]):
        confirm_close (Union[Unset, bool]):
        animation (Union[Unset, bool]):
    """

    backdropclose: Union[Unset, bool] = UNSET
    escape: Union[Unset, bool] = UNSET
    handleback: Union[Unset, bool] = UNSET
    confirm_close: Union[Unset, bool] = UNSET
    animation: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        backdropclose = self.backdropclose
        escape = self.escape
        handleback = self.handleback
        confirm_close = self.confirm_close
        animation = self.animation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backdropclose is not UNSET:
            field_dict["backdropclose"] = backdropclose
        if escape is not UNSET:
            field_dict["escape"] = escape
        if handleback is not UNSET:
            field_dict["handleback"] = handleback
        if confirm_close is not UNSET:
            field_dict["confirm_close"] = confirm_close
        if animation is not UNSET:
            field_dict["animation"] = animation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        backdropclose = d.pop("backdropclose", UNSET)

        escape = d.pop("escape", UNSET)

        handleback = d.pop("handleback", UNSET)

        confirm_close = d.pop("confirm_close", UNSET)

        animation = d.pop("animation", UNSET)

        razor_pay_model = cls(
            backdropclose=backdropclose,
            escape=escape,
            handleback=handleback,
            confirm_close=confirm_close,
            animation=animation,
        )

        razor_pay_model.additional_properties = d
        return razor_pay_model

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
