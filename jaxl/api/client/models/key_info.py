"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.key_info_type_enum import KeyInfoTypeEnum


if TYPE_CHECKING:
    from ..models.information import Information


T = TypeVar("T", bound="KeyInfo")


@attr.s(auto_attribs=True)
class KeyInfo:
    """
    Attributes:
        name (str):
        type (KeyInfoTypeEnum):
        info (Information):
    """

    name: str
    type: KeyInfoTypeEnum
    info: "Information"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type = self.type.value

        info = self.info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type,
                "info": info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.information import Information

        d = src_dict.copy()
        name = d.pop("name")

        type = KeyInfoTypeEnum(d.pop("type"))

        info = Information.from_dict(d.pop("info"))

        key_info = cls(
            name=name,
            type=type,
            info=info,
        )

        key_info.additional_properties = d
        return key_info

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
