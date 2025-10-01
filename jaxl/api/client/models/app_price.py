"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppPrice")


@attr.s(auto_attribs=True)
class AppPrice:
    """
    Attributes:
        id (int):
        app_id (int): Primary key of the App related to this object
        price (int):
        symbol (Union[Unset, str]):
        cost_per_year (Union[Unset, float]):
        cost_by_100 (Union[Unset, float]):
    """

    id: int
    app_id: int
    price: int
    symbol: Union[Unset, str] = UNSET
    cost_per_year: Union[Unset, float] = UNSET
    cost_by_100: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        app_id = self.app_id
        price = self.price
        symbol = self.symbol
        cost_per_year = self.cost_per_year
        cost_by_100 = self.cost_by_100

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "app_id": app_id,
                "price": price,
            }
        )
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if cost_per_year is not UNSET:
            field_dict["cost_per_year"] = cost_per_year
        if cost_by_100 is not UNSET:
            field_dict["cost_by_100"] = cost_by_100

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        app_id = d.pop("app_id")

        price = d.pop("price")

        symbol = d.pop("symbol", UNSET)

        cost_per_year = d.pop("cost_per_year", UNSET)

        cost_by_100 = d.pop("cost_by_100", UNSET)

        app_price = cls(
            id=id,
            app_id=app_id,
            price=price,
            symbol=symbol,
            cost_per_year=cost_per_year,
            cost_by_100=cost_by_100,
        )

        app_price.additional_properties = d
        return app_price

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
