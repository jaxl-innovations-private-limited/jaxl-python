"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.emoji import Emoji
    from ..models.reaction_by import ReactionBy


T = TypeVar("T", bound="EmojiReaction")


@attr.s(auto_attribs=True)
class EmojiReaction:
    """
    Attributes:
        emoji (Emoji):
        by (List['ReactionBy']):
    """

    emoji: "Emoji"
    by: List["ReactionBy"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        emoji = self.emoji.to_dict()

        by = []
        for by_item_data in self.by:
            by_item = by_item_data.to_dict()

            by.append(by_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "emoji": emoji,
                "by": by,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.emoji import Emoji
        from ..models.reaction_by import ReactionBy

        d = src_dict.copy()
        emoji = Emoji.from_dict(d.pop("emoji"))

        by = []
        _by = d.pop("by")
        for by_item_data in _by:
            by_item = ReactionBy.from_dict(by_item_data)

            by.append(by_item)

        emoji_reaction = cls(
            emoji=emoji,
            by=by,
        )

        emoji_reaction.additional_properties = d
        return emoji_reaction

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
