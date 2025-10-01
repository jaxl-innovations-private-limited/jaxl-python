"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, cast

import attr

from ..models.id_enum import IdEnum

T = TypeVar("T", bound="IVRCollectionRequest")


@attr.s(auto_attribs=True)
class IVRCollectionRequest:
    """
    Attributes:
        collection_ids (List[int]):
        type (IdEnum):
    """

    collection_ids: List[int]
    type: IdEnum
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        collection_ids = self.collection_ids

        type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_ids": collection_ids,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        collection_ids = cast(List[int], d.pop("collection_ids"))

        type = IdEnum(d.pop("type"))

        ivr_collection_request = cls(
            collection_ids=collection_ids,
            type=type,
        )

        ivr_collection_request.additional_properties = d
        return ivr_collection_request

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
