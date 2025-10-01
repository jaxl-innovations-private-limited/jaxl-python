"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.call import Call


T = TypeVar("T", bound="CallTokenResponse")


@attr.s(auto_attribs=True)
class CallTokenResponse:
    """
    Attributes:
        reason (Union[Unset, None, str]):
        token (Union[Unset, None, str]):
        to_number (Union[Unset, None, str]):
        call (Union[Unset, None, Call]):
        session_id (Union[Unset, None, str]):
        call_id (Union[Unset, None, int]):
        time_limit (Union[Unset, None, int]):
        provider (Union[Unset, None, int]):
        balance (Union[Unset, None, str]):
    """

    reason: Union[Unset, None, str] = UNSET
    token: Union[Unset, None, str] = UNSET
    to_number: Union[Unset, None, str] = UNSET
    call: Union[Unset, None, "Call"] = UNSET
    session_id: Union[Unset, None, str] = UNSET
    call_id: Union[Unset, None, int] = UNSET
    time_limit: Union[Unset, None, int] = UNSET
    provider: Union[Unset, None, int] = UNSET
    balance: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reason = self.reason
        token = self.token
        to_number = self.to_number
        call: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.call, Unset):
            call = self.call.to_dict() if self.call else None

        session_id = self.session_id
        call_id = self.call_id
        time_limit = self.time_limit
        provider = self.provider
        balance = self.balance

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reason is not UNSET:
            field_dict["reason"] = reason
        if token is not UNSET:
            field_dict["token"] = token
        if to_number is not UNSET:
            field_dict["to_number"] = to_number
        if call is not UNSET:
            field_dict["call"] = call
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if call_id is not UNSET:
            field_dict["call_id"] = call_id
        if time_limit is not UNSET:
            field_dict["time_limit"] = time_limit
        if provider is not UNSET:
            field_dict["provider"] = provider
        if balance is not UNSET:
            field_dict["balance"] = balance

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.call import Call

        d = src_dict.copy()
        reason = d.pop("reason", UNSET)

        token = d.pop("token", UNSET)

        to_number = d.pop("to_number", UNSET)

        _call = d.pop("call", UNSET)
        call: Union[Unset, None, Call]
        if _call is None:
            call = None
        elif isinstance(_call, Unset):
            call = UNSET
        else:
            call = Call.from_dict(_call)

        session_id = d.pop("session_id", UNSET)

        call_id = d.pop("call_id", UNSET)

        time_limit = d.pop("time_limit", UNSET)

        provider = d.pop("provider", UNSET)

        balance = d.pop("balance", UNSET)

        call_token_response = cls(
            reason=reason,
            token=token,
            to_number=to_number,
            call=call,
            session_id=session_id,
            call_id=call_id,
            time_limit=time_limit,
            provider=provider,
            balance=balance,
        )

        call_token_response.additional_properties = d
        return call_token_response

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
