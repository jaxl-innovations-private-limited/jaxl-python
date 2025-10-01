"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAgentPlatform")


@attr.s(auto_attribs=True)
class UserAgentPlatform:
    """
    Attributes:
        name (str):
        version (Union[Unset, None, str]):
        manufacturer (Union[Unset, None, str]):
    """

    name: str
    version: Union[Unset, None, str] = UNSET
    manufacturer: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        version = self.version
        manufacturer = self.manufacturer

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if version is not UNSET:
            field_dict["version"] = version
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        version = d.pop("version", UNSET)

        manufacturer = d.pop("manufacturer", UNSET)

        user_agent_platform = cls(
            name=name,
            version=version,
            manufacturer=manufacturer,
        )

        user_agent_platform.additional_properties = d
        return user_agent_platform

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
