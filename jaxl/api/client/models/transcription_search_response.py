"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.transcription_word_search_response import (
        TranscriptionWordSearchResponse,
    )


T = TypeVar("T", bound="TranscriptionSearchResponse")


@attr.s(auto_attribs=True)
class TranscriptionSearchResponse:
    """
    Attributes:
        call_id (int):
        max_score (float):
        min_score (float):
        results (List['TranscriptionWordSearchResponse']):
    """

    call_id: int
    max_score: float
    min_score: float
    results: List["TranscriptionWordSearchResponse"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        call_id = self.call_id
        max_score = self.max_score
        min_score = self.min_score
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()

            results.append(results_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "call_id": call_id,
                "max_score": max_score,
                "min_score": min_score,
                "results": results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.transcription_word_search_response import (
            TranscriptionWordSearchResponse,
        )

        d = src_dict.copy()
        call_id = d.pop("call_id")

        max_score = d.pop("max_score")

        min_score = d.pop("min_score")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = TranscriptionWordSearchResponse.from_dict(results_item_data)

            results.append(results_item)

        transcription_search_response = cls(
            call_id=call_id,
            max_score=max_score,
            min_score=min_score,
            results=results,
        )

        transcription_search_response.additional_properties = d
        return transcription_search_response

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
