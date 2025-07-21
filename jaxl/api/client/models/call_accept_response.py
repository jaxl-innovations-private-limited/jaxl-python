"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.call_accept_response_reason_enum import (
    CallAcceptResponseReasonEnum,
)
from ..types import UNSET, Unset


T = TypeVar("T", bound="CallAcceptResponse")


@attr.s(auto_attribs=True)
class CallAcceptResponse:
    """
    Attributes:
        accepted (bool):
        reason (Union[CallAcceptResponseReasonEnum, None, Unset]):
        device_id (Union[Unset, None, int]):
    """

    accepted: bool
    reason: Union[CallAcceptResponseReasonEnum, None, Unset] = UNSET
    device_id: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        accepted = self.accepted
        reason: Union[None, Unset, str]
        if isinstance(self.reason, Unset):
            reason = UNSET
        elif self.reason is None:
            reason = None

        elif isinstance(self.reason, CallAcceptResponseReasonEnum):
            reason = UNSET
            if not isinstance(self.reason, Unset):
                reason = self.reason.value

        else:
            reason = self.reason

        device_id = self.device_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accepted": accepted,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason
        if device_id is not UNSET:
            field_dict["device_id"] = device_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        accepted = d.pop("accepted")

        def _parse_reason(
            data: object,
        ) -> Union[CallAcceptResponseReasonEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _reason_type_0 = data
                reason_type_0: Union[Unset, CallAcceptResponseReasonEnum]
                if isinstance(_reason_type_0, Unset):
                    reason_type_0 = UNSET
                else:
                    reason_type_0 = CallAcceptResponseReasonEnum(_reason_type_0)

                return reason_type_0
            except:  # noqa: E722
                pass
            return cast(Union[CallAcceptResponseReasonEnum, None, Unset], data)

        reason = _parse_reason(d.pop("reason", UNSET))

        device_id = d.pop("device_id", UNSET)

        call_accept_response = cls(
            accepted=accepted,
            reason=reason,
            device_id=device_id,
        )

        call_accept_response.additional_properties = d
        return call_accept_response

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
