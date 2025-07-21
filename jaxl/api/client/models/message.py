"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.quoted import Quoted


T = TypeVar("T", bound="Message")


@attr.s(auto_attribs=True)
class Message:
    """
    Attributes:
        id (int):
        sender (str):
        conversation_id (str):
        thread_id (str):
        message (str):
        created_on (datetime.datetime): Datetime when this object was created
        quote_message (Union[Unset, None, Quoted]):
    """

    id: int
    sender: str
    conversation_id: str
    thread_id: str
    message: str
    created_on: datetime.datetime
    quote_message: Union[Unset, None, "Quoted"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        sender = self.sender
        conversation_id = self.conversation_id
        thread_id = self.thread_id
        message = self.message
        created_on = self.created_on.isoformat()

        quote_message: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.quote_message, Unset):
            quote_message = self.quote_message.to_dict() if self.quote_message else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "sender": sender,
                "conversation_id": conversation_id,
                "thread_id": thread_id,
                "message": message,
                "created_on": created_on,
            }
        )
        if quote_message is not UNSET:
            field_dict["quote_message"] = quote_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.quoted import Quoted

        d = src_dict.copy()
        id = d.pop("id")

        sender = d.pop("sender")

        conversation_id = d.pop("conversation_id")

        thread_id = d.pop("thread_id")

        _message = d.pop("message")

        created_on = isoparse(d.pop("created_on"))

        _quote_message = d.pop("quote_message", UNSET)
        quote_message: Union[Unset, None, Quoted]
        if _quote_message is None:
            quote_message = None
        elif isinstance(_quote_message, Unset):
            quote_message = UNSET
        else:
            quote_message = Quoted.from_dict(_quote_message)

        message = cls(
            id=id,
            sender=sender,
            conversation_id=conversation_id,
            thread_id=thread_id,
            message=_message,
            created_on=created_on,
            quote_message=quote_message,
        )

        message.additional_properties = d
        return message

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
