"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

import attr

from ..models.iso_country_enum import IsoCountryEnum
from ..models.provider_status_enum import ProviderStatusEnum


if TYPE_CHECKING:
    from ..models.address_provider import AddressProvider


T = TypeVar("T", bound="KycSummary")


@attr.s(auto_attribs=True)
class KycSummary:
    """Adds a 'jaxlid' field which contains signed ID information.

    Attributes:
        id (int):
        address (AddressProvider):
        iso_country (IsoCountryEnum):
        provider_status (ProviderStatusEnum):
        friendly_name (str):
        jaxlid (Optional[str]):
    """

    id: int
    address: "AddressProvider"
    iso_country: IsoCountryEnum
    provider_status: ProviderStatusEnum
    friendly_name: str
    jaxlid: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        address = self.address.to_dict()

        iso_country = self.iso_country.value

        provider_status = self.provider_status.value

        friendly_name = self.friendly_name
        jaxlid = self.jaxlid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "address": address,
                "iso_country": iso_country,
                "provider_status": provider_status,
                "friendly_name": friendly_name,
                "jaxlid": jaxlid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address_provider import AddressProvider

        d = src_dict.copy()
        id = d.pop("id")

        address = AddressProvider.from_dict(d.pop("address"))

        iso_country = IsoCountryEnum(d.pop("iso_country"))

        provider_status = ProviderStatusEnum(d.pop("provider_status"))

        friendly_name = d.pop("friendly_name")

        jaxlid = d.pop("jaxlid")

        kyc_summary = cls(
            id=id,
            address=address,
            iso_country=iso_country,
            provider_status=provider_status,
            friendly_name=friendly_name,
            jaxlid=jaxlid,
        )

        kyc_summary.additional_properties = d
        return kyc_summary

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
