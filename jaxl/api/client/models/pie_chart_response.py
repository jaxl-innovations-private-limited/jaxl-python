"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.key_info import KeyInfo


T = TypeVar("T", bound="PieChartResponse")


@attr.s(auto_attribs=True)
class PieChartResponse:
    """
    Attributes:
        pies (List['KeyInfo']):
    """

    pies: List["KeyInfo"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pies = []
        for pies_item_data in self.pies:
            pies_item = pies_item_data.to_dict()

            pies.append(pies_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pies": pies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.key_info import KeyInfo

        d = src_dict.copy()
        pies = []
        _pies = d.pop("pies")
        for pies_item_data in _pies:
            pies_item = KeyInfo.from_dict(pies_item_data)

            pies.append(pies_item)

        pie_chart_response = cls(
            pies=pies,
        )

        pie_chart_response.additional_properties = d
        return pie_chart_response

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
