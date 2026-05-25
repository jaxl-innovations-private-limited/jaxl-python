"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationProvider")


@attr.s(auto_attribs=True)
class OrganizationProvider:
    """
    Attributes:
        id (int):
        provider_name (str): Name of provider like for exotel it is jaxl61 for shopify it is shop domain
        provider_type (str):
        ivr_id (Union[Unset, None, int]): Ivr id assigned to this
    """

    id: int
    provider_name: str
    provider_type: str
    ivr_id: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        provider_name = self.provider_name
        provider_type = self.provider_type
        ivr_id = self.ivr_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "provider_name": provider_name,
                "provider_type": provider_type,
            }
        )
        if ivr_id is not UNSET:
            field_dict["ivr_id"] = ivr_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        provider_name = d.pop("provider_name")

        provider_type = d.pop("provider_type")

        ivr_id = d.pop("ivr_id", UNSET)

        organization_provider = cls(
            id=id,
            provider_name=provider_name,
            provider_type=provider_type,
            ivr_id=ivr_id,
        )

        organization_provider.additional_properties = d
        return organization_provider

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
