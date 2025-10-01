"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.phone_number import PhoneNumber


T = TypeVar("T", bound="PaginatedPhoneNumberList")


@attr.s(auto_attribs=True)
class PaginatedPhoneNumberList:
    """
    Attributes:
        count (int):  Example: 123.
        results (List['PhoneNumber']):
        next_ (Union[Unset, None, str]):  Example: http://api.example.org/accounts/?offset=400&limit=100.
        previous (Union[Unset, None, str]):  Example: http://api.example.org/accounts/?offset=200&limit=100.
    """

    count: int
    results: List["PhoneNumber"]
    next_: Union[Unset, None, str] = UNSET
    previous: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()

            results.append(results_item)

        next_ = self.next_
        previous = self.previous

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "results": results,
            }
        )
        if next_ is not UNSET:
            field_dict["next"] = next_
        if previous is not UNSET:
            field_dict["previous"] = previous

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.phone_number import PhoneNumber

        d = src_dict.copy()
        count = d.pop("count")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = PhoneNumber.from_dict(results_item_data)

            results.append(results_item)

        next_ = d.pop("next", UNSET)

        previous = d.pop("previous", UNSET)

        paginated_phone_number_list = cls(
            count=count,
            results=results,
            next_=next_,
            previous=previous,
        )

        paginated_phone_number_list.additional_properties = d
        return paginated_phone_number_list

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
