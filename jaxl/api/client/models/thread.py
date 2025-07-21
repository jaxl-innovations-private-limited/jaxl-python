"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse


T = TypeVar("T", bound="Thread")


@attr.s(auto_attribs=True)
class Thread:
    """
    Attributes:
        id (str): Randomly generated ID for this thread. There can ever be a single thread for peer-to-peer
            conversations. For group conversations there can be multiple threads.
        created_by (str):
        conversation (str): Unique key generated for this conversation. For peer-to-peer we generate a stable UUID.For
            group conversations, this is a UUID
        created_on (datetime.datetime): Datetime when this object was created
    """

    id: str
    created_by: str
    conversation: str
    created_on: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        created_by = self.created_by
        conversation = self.conversation
        created_on = self.created_on.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_by": created_by,
                "conversation": conversation,
                "created_on": created_on,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        created_by = d.pop("created_by")

        conversation = d.pop("conversation")

        created_on = isoparse(d.pop("created_on"))

        thread = cls(
            id=id,
            created_by=created_by,
            conversation=conversation,
            created_on=created_on,
        )

        thread.additional_properties = d
        return thread

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
