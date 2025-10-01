"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.device_attestation_error_reason_enum import (
    DeviceAttestationErrorReasonEnum,
)

T = TypeVar("T", bound="DeviceAttestationError")


@attr.s(auto_attribs=True)
class DeviceAttestationError:
    """
    Attributes:
        reason (DeviceAttestationErrorReasonEnum):
    """

    reason: DeviceAttestationErrorReasonEnum
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reason = self.reason.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reason = DeviceAttestationErrorReasonEnum(d.pop("reason"))

        device_attestation_error = cls(
            reason=reason,
        )

        device_attestation_error.additional_properties = d
        return device_attestation_error

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
