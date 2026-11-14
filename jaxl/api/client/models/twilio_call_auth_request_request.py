"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="TwilioCallAuthRequestRequest")


@attr.s(auto_attribs=True)
class TwilioCallAuthRequestRequest:
    """F-171 BYO call provider: the org's OWN Twilio account.

    Attributes:
        account_sid (str): Twilio Account SID (AC…)
        auth_token (str): Twilio Auth Token
    """

    account_sid: str
    auth_token: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_sid = self.account_sid
        auth_token = self.auth_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_sid": account_sid,
                "auth_token": auth_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_sid = d.pop("account_sid")

        auth_token = d.pop("auth_token")

        twilio_call_auth_request_request = cls(
            account_sid=account_sid,
            auth_token=auth_token,
        )

        twilio_call_auth_request_request.additional_properties = d
        return twilio_call_auth_request_request

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
