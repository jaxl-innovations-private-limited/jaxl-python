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
    from ..models.key_info import KeyInfo


T = TypeVar("T", bound="PointResponse")


@attr.s(auto_attribs=True)
class PointResponse:
    """
    Attributes:
        datetime_ (datetime.datetime):
        payload (List['KeyInfo']):
    """

    datetime_: datetime.datetime
    payload: List["KeyInfo"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        datetime_ = self.datetime_.isoformat()

        payload = []
        for payload_item_data in self.payload:
            payload_item = payload_item_data.to_dict()

            payload.append(payload_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datetime": datetime_,
                "payload": payload,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.key_info import KeyInfo

        d = src_dict.copy()
        datetime_ = isoparse(d.pop("datetime"))

        payload = []
        _payload = d.pop("payload")
        for payload_item_data in _payload:
            payload_item = KeyInfo.from_dict(payload_item_data)

            payload.append(payload_item)

        point_response = cls(
            datetime_=datetime_,
            payload=payload,
        )

        point_response.additional_properties = d
        return point_response

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
