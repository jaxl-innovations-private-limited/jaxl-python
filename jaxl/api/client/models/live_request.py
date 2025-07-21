"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.purpose_enum import PurposeEnum
from ..types import UNSET, Unset


T = TypeVar("T", bound="LiveRequest")


@attr.s(auto_attribs=True)
class LiveRequest:
    """
    Attributes:
        from_identity (str):
        from_device_id (Union[Unset, None, int]): Only allowed from /try/ browsers
        to_identity (Union[Unset, None, str]):
        purpose (Union[Unset, PurposeEnum]):
    """

    from_identity: str
    from_device_id: Union[Unset, None, int] = UNSET
    to_identity: Union[Unset, None, str] = UNSET
    purpose: Union[Unset, PurposeEnum] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_identity = self.from_identity
        from_device_id = self.from_device_id
        to_identity = self.to_identity
        purpose: Union[Unset, str] = UNSET
        if not isinstance(self.purpose, Unset):
            purpose = self.purpose.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from_identity": from_identity,
            }
        )
        if from_device_id is not UNSET:
            field_dict["from_device_id"] = from_device_id
        if to_identity is not UNSET:
            field_dict["to_identity"] = to_identity
        if purpose is not UNSET:
            field_dict["purpose"] = purpose

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        from_identity = d.pop("from_identity")

        from_device_id = d.pop("from_device_id", UNSET)

        to_identity = d.pop("to_identity", UNSET)

        _purpose = d.pop("purpose", UNSET)
        purpose: Union[Unset, PurposeEnum]
        if isinstance(_purpose, Unset):
            purpose = UNSET
        else:
            purpose = PurposeEnum(_purpose)

        live_request = cls(
            from_identity=from_identity,
            from_device_id=from_device_id,
            to_identity=to_identity,
            purpose=purpose,
        )

        live_request.additional_properties = d
        return live_request

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
