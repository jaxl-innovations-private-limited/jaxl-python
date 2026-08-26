"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.kind_enum import KindEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="KbSearchRequest")


@attr.s(auto_attribs=True)
class KbSearchRequest:
    """
    Attributes:
        call_id (int):
        query (str):
        kind (Union[Unset, KindEnum]):  Default: KindEnum.PRODUCTS.
        limit (Union[Unset, int]):  Default: 5.
    """

    call_id: int
    query: str
    kind: Union[Unset, KindEnum] = KindEnum.PRODUCTS
    limit: Union[Unset, int] = 5
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        call_id = self.call_id
        query = self.query
        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        limit = self.limit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "call_id": call_id,
                "query": query,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        call_id = d.pop("call_id")

        query = d.pop("query")

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, KindEnum]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = KindEnum(_kind)

        limit = d.pop("limit", UNSET)

        kb_search_request = cls(
            call_id=call_id,
            query=query,
            kind=kind,
            limit=limit,
        )

        kb_search_request.additional_properties = d
        return kb_search_request

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
