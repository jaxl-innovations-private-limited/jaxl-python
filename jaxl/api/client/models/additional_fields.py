"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.additional_fields_type_enum import AdditionalFieldsTypeEnum
from ..types import UNSET, Unset


T = TypeVar("T", bound="AdditionalFields")


@attr.s(auto_attribs=True)
class AdditionalFields:
    """
    Attributes:
        name (str):
        title (str):
        type (AdditionalFieldsTypeEnum):
        description (Union[Unset, None, str]):
        options (Union[Unset, None, List[str]]):
        value (Union[Unset, None, str]):
    """

    name: str
    title: str
    type: AdditionalFieldsTypeEnum
    description: Union[Unset, None, str] = UNSET
    options: Union[Unset, None, List[str]] = UNSET
    value: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        title = self.title
        type = self.type.value

        description = self.description
        options: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.options, Unset):
            if self.options is None:
                options = None
            else:
                options = self.options

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "title": title,
                "type": type,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if options is not UNSET:
            field_dict["options"] = options
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        title = d.pop("title")

        type = AdditionalFieldsTypeEnum(d.pop("type"))

        description = d.pop("description", UNSET)

        options = cast(List[str], d.pop("options", UNSET))

        value = d.pop("value", UNSET)

        additional_fields = cls(
            name=name,
            title=title,
            type=type,
            description=description,
            options=options,
            value=value,
        )

        additional_fields.additional_properties = d
        return additional_fields

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
