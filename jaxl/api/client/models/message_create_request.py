"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset


T = TypeVar("T", bound="MessageCreateRequest")


@attr.s(auto_attribs=True)
class MessageCreateRequest:
    """
    Attributes:
        conversation_id (str):
        message (str):
        thread_id (Union[Unset, str]):
        quoted_message_id (Union[Unset, str]):
    """

    conversation_id: str
    message: str
    thread_id: Union[Unset, str] = UNSET
    quoted_message_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        conversation_id = self.conversation_id
        message = self.message
        thread_id = self.thread_id
        quoted_message_id = self.quoted_message_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conversation_id": conversation_id,
                "message": message,
            }
        )
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id
        if quoted_message_id is not UNSET:
            field_dict["quoted_message_id"] = quoted_message_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        conversation_id = d.pop("conversation_id")

        message = d.pop("message")

        thread_id = d.pop("thread_id", UNSET)

        quoted_message_id = d.pop("quoted_message_id", UNSET)

        message_create_request = cls(
            conversation_id=conversation_id,
            message=message,
            thread_id=thread_id,
            quoted_message_id=quoted_message_id,
        )

        message_create_request.additional_properties = d
        return message_create_request

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
