"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar

import attr


T = TypeVar("T", bound="SmsRequestRequest")


@attr.s(auto_attribs=True)
class SmsRequestRequest:
    """
    Attributes:
        from_number (str):
        to_number (str):
        message (str): Encrypted with attestation key
        encrypted (str): Encrypted with self key
    """

    from_number: str
    to_number: str
    message: str
    encrypted: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_number = self.from_number
        to_number = self.to_number
        message = self.message
        encrypted = self.encrypted

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from_number": from_number,
                "to_number": to_number,
                "message": message,
                "encrypted": encrypted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        from_number = d.pop("from_number")

        to_number = d.pop("to_number")

        message = d.pop("message")

        encrypted = d.pop("encrypted")

        sms_request_request = cls(
            from_number=from_number,
            to_number=to_number,
            message=message,
            encrypted=encrypted,
        )

        sms_request_request.additional_properties = d
        return sms_request_request

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
