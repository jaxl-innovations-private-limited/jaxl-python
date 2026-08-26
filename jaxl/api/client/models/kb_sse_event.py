"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KbSseEvent")


@attr.s(auto_attribs=True)
class KbSseEvent:
    """The schema of EACH `text/event-stream` event on the kb endpoint
    (the OpenAPI SSE-documentation shape — one chunk schema for the
    stream): a `result` event carries `line`; the terminal `done` event
    carries `count`.

        Attributes:
            line (Union[Unset, str]): `result` events only — one compact catalogue line, e.g. `[id:7101] Aloe Vera Face Wash
                — ₹299 (2 options) — Skincare`.
            count (Union[Unset, int]): `done` event only — total result lines streamed.
    """

    line: Union[Unset, str] = UNSET
    count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line = self.line
        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line is not UNSET:
            field_dict["line"] = line
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        line = d.pop("line", UNSET)

        count = d.pop("count", UNSET)

        kb_sse_event = cls(
            line=line,
            count=count,
        )

        kb_sse_event.additional_properties = d
        return kb_sse_event

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
