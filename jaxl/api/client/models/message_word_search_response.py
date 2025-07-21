"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.message_word_position_response import (
        MessageWordPositionResponse,
    )


T = TypeVar("T", bound="MessageWordSearchResponse")


@attr.s(auto_attribs=True)
class MessageWordSearchResponse:
    """
    Attributes:
        hs (MessageWordPositionResponse):
        he (MessageWordPositionResponse):
        score (float):
    """

    hs: "MessageWordPositionResponse"
    he: "MessageWordPositionResponse"
    score: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hs = self.hs.to_dict()

        he = self.he.to_dict()

        score = self.score

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hs": hs,
                "he": he,
                "score": score,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.message_word_position_response import (
            MessageWordPositionResponse,
        )

        d = src_dict.copy()
        hs = MessageWordPositionResponse.from_dict(d.pop("hs"))

        he = MessageWordPositionResponse.from_dict(d.pop("he"))

        score = d.pop("score")

        message_word_search_response = cls(
            hs=hs,
            he=he,
            score=score,
        )

        message_word_search_response.additional_properties = d
        return message_word_search_response

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
