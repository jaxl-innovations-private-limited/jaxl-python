"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Optional, Type, TypeVar

import attr


T = TypeVar("T", bound="JaxlAppDetailContextApp")


@attr.s(auto_attribs=True)
class JaxlAppDetailContextApp:
    """
    Attributes:
        name (str):
        title (Optional[str]):
        subtitle (Optional[str]):
        description (Optional[str]):
    """

    name: str
    title: Optional[str]
    subtitle: Optional[str]
    description: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        title = self.title
        subtitle = self.subtitle
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "title": title,
                "subtitle": subtitle,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        title = d.pop("title")

        subtitle = d.pop("subtitle")

        description = d.pop("description")

        jaxl_app_detail_context_app = cls(
            name=name,
            title=title,
            subtitle=subtitle,
            description=description,
        )

        jaxl_app_detail_context_app.additional_properties = d
        return jaxl_app_detail_context_app

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
