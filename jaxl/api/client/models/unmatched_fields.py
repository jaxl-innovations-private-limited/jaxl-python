"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.additional_fields import AdditionalFields


T = TypeVar("T", bound="UnmatchedFields")


@attr.s(auto_attribs=True)
class UnmatchedFields:
    """
    Attributes:
        unmatched_fields (List['AdditionalFields']):
        message (str):
    """

    unmatched_fields: List["AdditionalFields"]
    message: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unmatched_fields = []
        for unmatched_fields_item_data in self.unmatched_fields:
            unmatched_fields_item = unmatched_fields_item_data.to_dict()

            unmatched_fields.append(unmatched_fields_item)

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unmatched_fields": unmatched_fields,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.additional_fields import AdditionalFields

        d = src_dict.copy()
        __unmatched_fields = []
        _unmatched_fields = d.pop("unmatched_fields")
        for unmatched_fields_item_data in _unmatched_fields:
            unmatched_fields_item = AdditionalFields.from_dict(
                unmatched_fields_item_data
            )

            __unmatched_fields.append(unmatched_fields_item)

        message = d.pop("message")

        unmatched_fields = cls(
            unmatched_fields=__unmatched_fields,
            message=message,
        )

        unmatched_fields.additional_properties = d
        return unmatched_fields

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
