"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PhoneNumberCapabilities")


@attr.s(auto_attribs=True)
class PhoneNumberCapabilities:
    """
    Attributes:
        voice (bool):
        mms (bool):
        sms (bool):
    """

    voice: bool
    mms: bool
    sms: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        voice = self.voice
        mms = self.mms
        sms = self.sms

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "voice": voice,
                "mms": mms,
                "sms": sms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        voice = d.pop("voice")

        mms = d.pop("mms")

        sms = d.pop("sms")

        phone_number_capabilities = cls(
            voice=voice,
            mms=mms,
            sms=sms,
        )

        phone_number_capabilities.additional_properties = d
        return phone_number_capabilities

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
