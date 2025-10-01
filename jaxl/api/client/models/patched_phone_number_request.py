"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedPhoneNumberRequest")


@attr.s(auto_attribs=True)
class PatchedPhoneNumberRequest:
    """Adds a 'jaxlid' field which contains signed ID information.

    Attributes:
        ivr (Union[Unset, None, int]): Optional IVR for all incoming calls to this number
    """

    ivr: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ivr = self.ivr

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ivr is not UNSET:
            field_dict["ivr"] = ivr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ivr = d.pop("ivr", UNSET)

        patched_phone_number_request = cls(
            ivr=ivr,
        )

        patched_phone_number_request.additional_properties = d
        return patched_phone_number_request

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
