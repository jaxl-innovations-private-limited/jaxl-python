"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.emoji_reaction import EmojiReaction


T = TypeVar("T", bound="DHMessageReaction")


@attr.s(auto_attribs=True)
class DHMessageReaction:
    """
    Attributes:
        last_modified_on (datetime.datetime):
        emojis (List['EmojiReaction']):
    """

    last_modified_on: datetime.datetime
    emojis: List["EmojiReaction"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        last_modified_on = self.last_modified_on.isoformat()

        emojis = []
        for emojis_item_data in self.emojis:
            emojis_item = emojis_item_data.to_dict()

            emojis.append(emojis_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "last_modified_on": last_modified_on,
                "emojis": emojis,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.emoji_reaction import EmojiReaction

        d = src_dict.copy()
        last_modified_on = isoparse(d.pop("last_modified_on"))

        emojis = []
        _emojis = d.pop("emojis")
        for emojis_item_data in _emojis:
            emojis_item = EmojiReaction.from_dict(emojis_item_data)

            emojis.append(emojis_item)

        dh_message_reaction = cls(
            last_modified_on=last_modified_on,
            emojis=emojis,
        )

        dh_message_reaction.additional_properties = d
        return dh_message_reaction

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
