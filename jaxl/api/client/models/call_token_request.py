"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.call_type_enum import CallTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="CallTokenRequest")


@attr.s(auto_attribs=True)
class CallTokenRequest:
    """
    Attributes:
        from_number (str):
        to_number (str):
        session_id (str):
        call_type (CallTypeEnum):
        balance (str):
        currency (str):
        provider (Union[Unset, None, int]):
        ivr_id (Union[Unset, None, int]):
        total_recharge (Union[Unset, None, str]):
        cid (Union[Unset, None, int]): Call ID which acted as source for this outgoing call
    """

    from_number: str
    to_number: str
    session_id: str
    call_type: CallTypeEnum
    balance: str
    currency: str
    provider: Union[Unset, None, int] = UNSET
    ivr_id: Union[Unset, None, int] = UNSET
    total_recharge: Union[Unset, None, str] = UNSET
    cid: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_number = self.from_number
        to_number = self.to_number
        session_id = self.session_id
        call_type = self.call_type.value

        balance = self.balance
        currency = self.currency
        provider = self.provider
        ivr_id = self.ivr_id
        total_recharge = self.total_recharge
        cid = self.cid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from_number": from_number,
                "to_number": to_number,
                "session_id": session_id,
                "call_type": call_type,
                "balance": balance,
                "currency": currency,
            }
        )
        if provider is not UNSET:
            field_dict["provider"] = provider
        if ivr_id is not UNSET:
            field_dict["ivr_id"] = ivr_id
        if total_recharge is not UNSET:
            field_dict["total_recharge"] = total_recharge
        if cid is not UNSET:
            field_dict["cid"] = cid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        from_number = d.pop("from_number")

        to_number = d.pop("to_number")

        session_id = d.pop("session_id")

        call_type = CallTypeEnum(d.pop("call_type"))

        balance = d.pop("balance")

        currency = d.pop("currency")

        provider = d.pop("provider", UNSET)

        ivr_id = d.pop("ivr_id", UNSET)

        total_recharge = d.pop("total_recharge", UNSET)

        cid = d.pop("cid", UNSET)

        call_token_request = cls(
            from_number=from_number,
            to_number=to_number,
            session_id=session_id,
            call_type=call_type,
            balance=balance,
            currency=currency,
            provider=provider,
            ivr_id=ivr_id,
            total_recharge=total_recharge,
            cid=cid,
        )

        call_token_request.additional_properties = d
        return call_token_request

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
