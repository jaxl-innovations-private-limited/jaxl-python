"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CallScheduleRequest")


@attr.s(auto_attribs=True)
class CallScheduleRequest:
    """F-167a K-1b — `POST /v1/calls/schedule/`: schedule a standalone
    outbound call for a future time (no prior call / tag needed).
    E.164 numbers; `run_at` ISO-8601 with timezone; `ivr_id` decides what
    the callee lands in on answer (required — same rule as calls create).

        Attributes:
            from_number (str):
            to_number (str):
            ivr_id (int):
            run_at (datetime.datetime):
            reason (Union[Unset, None, str]):
    """

    from_number: str
    to_number: str
    ivr_id: int
    run_at: datetime.datetime
    reason: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_number = self.from_number
        to_number = self.to_number
        ivr_id = self.ivr_id
        run_at = self.run_at.isoformat()

        reason = self.reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from_number": from_number,
                "to_number": to_number,
                "ivr_id": ivr_id,
                "run_at": run_at,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        from_number = d.pop("from_number")

        to_number = d.pop("to_number")

        ivr_id = d.pop("ivr_id")

        run_at = isoparse(d.pop("run_at"))

        reason = d.pop("reason", UNSET)

        call_schedule_request = cls(
            from_number=from_number,
            to_number=to_number,
            ivr_id=ivr_id,
            run_at=run_at,
            reason=reason,
        )

        call_schedule_request.additional_properties = d
        return call_schedule_request

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
