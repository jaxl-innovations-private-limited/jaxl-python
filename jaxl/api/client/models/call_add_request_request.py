"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CallAddRequestRequest")


@attr.s(auto_attribs=True)
class CallAddRequestRequest:
    """
    Attributes:
        e164 (Union[Unset, None, str]): Phone number in E.164 format, e.g. +14155552671
        from_e164 (Union[Unset, None, str]): Phone number in E.164 format, e.g. +14155552671
        email (Union[Unset, None, str]): Email address of the participant
    """

    e164: Union[Unset, None, str] = UNSET
    from_e164: Union[Unset, None, str] = UNSET
    email: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        e164 = self.e164
        from_e164 = self.from_e164
        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if e164 is not UNSET:
            field_dict["e164"] = e164
        if from_e164 is not UNSET:
            field_dict["from_e164"] = from_e164
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        e164 = d.pop("e164", UNSET)

        from_e164 = d.pop("from_e164", UNSET)

        email = d.pop("email", UNSET)

        call_add_request_request = cls(
            e164=e164,
            from_e164=from_e164,
            email=email,
        )

        call_add_request_request.additional_properties = d
        return call_add_request_request

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
