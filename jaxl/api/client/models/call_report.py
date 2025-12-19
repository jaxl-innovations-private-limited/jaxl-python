"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.call_report_status_enum import CallReportStatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="CallReport")


@attr.s(auto_attribs=True)
class CallReport:
    """
    Attributes:
        id (int):
        status (Union[Unset, CallReportStatusEnum]):
    """

    id: int
    status: Union[Unset, CallReportStatusEnum] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        _status = d.pop("status", UNSET)
        status: Union[Unset, CallReportStatusEnum]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CallReportStatusEnum(_status)

        call_report = cls(
            id=id,
            status=status,
        )

        call_report.additional_properties = d
        return call_report

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
