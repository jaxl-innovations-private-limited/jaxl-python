"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.call_date_response import CallDateResponse


T = TypeVar("T", bound="CallDatesResponse")


@attr.s(auto_attribs=True)
class CallDatesResponse:
    """
    Attributes:
        dates (List['CallDateResponse']):
    """

    dates: List["CallDateResponse"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dates = []
        for dates_item_data in self.dates:
            dates_item = dates_item_data.to_dict()

            dates.append(dates_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dates": dates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.call_date_response import CallDateResponse

        d = src_dict.copy()
        dates = []
        _dates = d.pop("dates")
        for dates_item_data in _dates:
            dates_item = CallDateResponse.from_dict(dates_item_data)

            dates.append(dates_item)

        call_dates_response = cls(
            dates=dates,
        )

        call_dates_response.additional_properties = d
        return call_dates_response

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
