"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

T = TypeVar("T", bound="Country")


@attr.s(auto_attribs=True)
class Country:
    """Adds a 'jaxlid' field which contains signed ID information.

    Attributes:
        name (str):
        iso_country_code (str): The ISO country codes are internationally recognized codes that designate every country
            and most of the dependent areas a two-letter combination. eg: IN, US, AU, CN, DE etc.
        iso_alpha3_country_code (str): The Alpha3 ISO country codes are internationally recognized codes that designate
            every country and most of the dependent areas a three-letter combination. eg: IND, USA, AUS, CAN, DEU etc.
        iso_currency (str): ISO currency codes are the three-letter alphabetic codes that represent the various
            currencies used throughout the world. eg: INR, USD, AUD, CNY, EUR, etc.
        currency_symbol (str): A currency symbol or currency sign is a graphic symbol used as a shorthand for a
            currency's name. eg: ₹ (India), € (European Union), CA$ (Canada), د.إ; (UAE) etc.
        isd_code (int):
        emoji_unicode (str):
        flag_image_url (str):
        jaxlid (Optional[str]):
    """

    name: str
    iso_country_code: str
    iso_alpha3_country_code: str
    iso_currency: str
    currency_symbol: str
    isd_code: int
    emoji_unicode: str
    flag_image_url: str
    jaxlid: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        iso_country_code = self.iso_country_code
        iso_alpha3_country_code = self.iso_alpha3_country_code
        iso_currency = self.iso_currency
        currency_symbol = self.currency_symbol
        isd_code = self.isd_code
        emoji_unicode = self.emoji_unicode
        flag_image_url = self.flag_image_url
        jaxlid = self.jaxlid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "iso_country_code": iso_country_code,
                "iso_alpha3_country_code": iso_alpha3_country_code,
                "iso_currency": iso_currency,
                "currency_symbol": currency_symbol,
                "isd_code": isd_code,
                "emoji_unicode": emoji_unicode,
                "flag_image_url": flag_image_url,
                "jaxlid": jaxlid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        iso_country_code = d.pop("iso_country_code")

        iso_alpha3_country_code = d.pop("iso_alpha3_country_code")

        iso_currency = d.pop("iso_currency")

        currency_symbol = d.pop("currency_symbol")

        isd_code = d.pop("isd_code")

        emoji_unicode = d.pop("emoji_unicode")

        flag_image_url = d.pop("flag_image_url")

        jaxlid = d.pop("jaxlid")

        country = cls(
            name=name,
            iso_country_code=iso_country_code,
            iso_alpha3_country_code=iso_alpha3_country_code,
            iso_currency=iso_currency,
            currency_symbol=currency_symbol,
            isd_code=isd_code,
            emoji_unicode=emoji_unicode,
            flag_image_url=flag_image_url,
            jaxlid=jaxlid,
        )

        country.additional_properties = d
        return country

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
