"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.country import Country


T = TypeVar("T", bound="AppCountry")


@attr.s(auto_attribs=True)
class AppCountry:
    """Adds a 'jaxlid' field which contains signed ID information.

    Attributes:
        app (int):
        country (Country): Adds a 'jaxlid' field which contains signed ID information.
        price_currency_id (int):
        jaxlid (Optional[str]):
    """

    app: int
    country: "Country"
    price_currency_id: int
    jaxlid: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        app = self.app
        country = self.country.to_dict()

        price_currency_id = self.price_currency_id
        jaxlid = self.jaxlid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app": app,
                "country": country,
                "price_currency_id": price_currency_id,
                "jaxlid": jaxlid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.country import Country

        d = src_dict.copy()
        app = d.pop("app")

        country = Country.from_dict(d.pop("country"))

        price_currency_id = d.pop("price_currency_id")

        jaxlid = d.pop("jaxlid")

        app_country = cls(
            app=app,
            country=country,
            price_currency_id=price_currency_id,
            jaxlid=jaxlid,
        )

        app_country.additional_properties = d
        return app_country

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
