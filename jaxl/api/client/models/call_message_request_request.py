"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.call_message_request_type_enum import CallMessageRequestTypeEnum
from ..models.why_enum import WhyEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="CallMessageRequestRequest")


@attr.s(auto_attribs=True)
class CallMessageRequestRequest:
    """
    Attributes:
        text (str): Text encrypted with attestation key
        timestamp (datetime.datetime): When this message activity happened.
        why (WhyEnum):
        type (Union[Unset, CallMessageRequestTypeEnum]):  Default: CallMessageRequestTypeEnum.VALUE_10.
    """

    text: str
    timestamp: datetime.datetime
    why: WhyEnum
    type: Union[Unset, CallMessageRequestTypeEnum] = CallMessageRequestTypeEnum.VALUE_10
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text
        timestamp = self.timestamp.isoformat()

        why = self.why.value

        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "timestamp": timestamp,
                "why": why,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text")

        timestamp = isoparse(d.pop("timestamp"))

        why = WhyEnum(d.pop("why"))

        _type = d.pop("type", UNSET)
        type: Union[Unset, CallMessageRequestTypeEnum]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CallMessageRequestTypeEnum(_type)

        call_message_request_request = cls(
            text=text,
            timestamp=timestamp,
            why=why,
            type=type,
        )

        call_message_request_request.additional_properties = d
        return call_message_request_request

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
