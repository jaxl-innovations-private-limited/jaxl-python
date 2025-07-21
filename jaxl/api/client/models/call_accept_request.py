"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset


T = TypeVar("T", bound="CallAcceptRequest")


@attr.s(auto_attribs=True)
class CallAcceptRequest:
    """
    Attributes:
        session_id (Union[Unset, None, str]): Only applicable for call type 2, 3, 4
        to_channel (Union[Unset, None, str]): Only applicable for call type 2.  When provided 'rtc.invite' equivalent is
            automatically performed by backend, so that client don't need to send another request
    """

    session_id: Union[Unset, None, str] = UNSET
    to_channel: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        session_id = self.session_id
        to_channel = self.to_channel

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if to_channel is not UNSET:
            field_dict["to_channel"] = to_channel

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        session_id = d.pop("session_id", UNSET)

        to_channel = d.pop("to_channel", UNSET)

        call_accept_request = cls(
            session_id=session_id,
            to_channel=to_channel,
        )

        call_accept_request.additional_properties = d
        return call_accept_request

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
