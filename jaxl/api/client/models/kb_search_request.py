"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.kb_search_mode_enum import KbSearchModeEnum
from ..models.kind_enum import KindEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="KbSearchRequest")


@attr.s(auto_attribs=True)
class KbSearchRequest:
    """
    Attributes:
        call_id (int):
        kind (Union[Unset, KindEnum]):  Default: KindEnum.PRODUCTS.
        query (Union[Unset, str]):  Default: ''.
        limit (Union[Unset, int]):  Default: 5.
        mode (Union[Unset, KbSearchModeEnum]):  Default: KbSearchModeEnum.SPECIFIC.
        category (Union[Unset, str]):  Default: ''.
    """

    call_id: int
    kind: Union[Unset, KindEnum] = KindEnum.PRODUCTS
    query: Union[Unset, str] = ""
    limit: Union[Unset, int] = 5
    mode: Union[Unset, KbSearchModeEnum] = KbSearchModeEnum.SPECIFIC
    category: Union[Unset, str] = ""
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        call_id = self.call_id
        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        query = self.query
        limit = self.limit
        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        category = self.category

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "call_id": call_id,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if query is not UNSET:
            field_dict["query"] = query
        if limit is not UNSET:
            field_dict["limit"] = limit
        if mode is not UNSET:
            field_dict["mode"] = mode
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        call_id = d.pop("call_id")

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, KindEnum]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = KindEnum(_kind)

        query = d.pop("query", UNSET)

        limit = d.pop("limit", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, KbSearchModeEnum]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = KbSearchModeEnum(_mode)

        category = d.pop("category", UNSET)

        kb_search_request = cls(
            call_id=call_id,
            kind=kind,
            query=query,
            limit=limit,
            mode=mode,
            category=category,
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
