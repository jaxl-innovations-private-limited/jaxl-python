"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.razor_pay_config_display import RazorPayConfigDisplay


T = TypeVar("T", bound="RazorPayConfig")


@attr.s(auto_attribs=True)
class RazorPayConfig:
    """
    Attributes:
        display (RazorPayConfigDisplay):
    """

    display: "RazorPayConfigDisplay"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display = self.display.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "display": display,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.razor_pay_config_display import RazorPayConfigDisplay

        d = src_dict.copy()
        display = RazorPayConfigDisplay.from_dict(d.pop("display"))

        razor_pay_config = cls(
            display=display,
        )

        razor_pay_config.additional_properties = d
        return razor_pay_config

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
