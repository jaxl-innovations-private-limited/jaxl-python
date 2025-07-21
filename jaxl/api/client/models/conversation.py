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

from ..models.conversation_type_enum import ConversationTypeEnum
from ..types import UNSET, Unset


T = TypeVar("T", bound="Conversation")


@attr.s(auto_attribs=True)
class Conversation:
    """This is a serializer for Message model

    Attributes:
        id (str): Unique key generated for this conversation. For peer-to-peer we generate a stable UUID.For group
            conversations, this is a UUID
        name (str):
        created_on (datetime.datetime): Datetime when this object was created
        modified_on (datetime.datetime): Datetime when this object was last modified
        num_unread (int):
        sender (Union[Unset, str]):
        latest_activity (Union[Unset, str]):
        type (Union[Unset, ConversationTypeEnum]):
    """

    id: str
    name: str
    created_on: datetime.datetime
    modified_on: datetime.datetime
    num_unread: int
    sender: Union[Unset, str] = UNSET
    latest_activity: Union[Unset, str] = UNSET
    type: Union[Unset, ConversationTypeEnum] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        created_on = self.created_on.isoformat()

        modified_on = self.modified_on.isoformat()

        num_unread = self.num_unread
        sender = self.sender
        latest_activity = self.latest_activity
        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "created_on": created_on,
                "modified_on": modified_on,
                "num_unread": num_unread,
            }
        )
        if sender is not UNSET:
            field_dict["sender"] = sender
        if latest_activity is not UNSET:
            field_dict["latest_activity"] = latest_activity
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        created_on = isoparse(d.pop("created_on"))

        modified_on = isoparse(d.pop("modified_on"))

        num_unread = d.pop("num_unread")

        sender = d.pop("sender", UNSET)

        latest_activity = d.pop("latest_activity", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ConversationTypeEnum]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ConversationTypeEnum(_type)

        conversation = cls(
            id=id,
            name=name,
            created_on=created_on,
            modified_on=modified_on,
            num_unread=num_unread,
            sender=sender,
            latest_activity=latest_activity,
            type=type,
        )

        conversation.additional_properties = d
        return conversation

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
