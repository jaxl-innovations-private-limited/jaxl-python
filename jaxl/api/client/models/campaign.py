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

from ..models.cta_type_enum import CtaTypeEnum
from ..types import UNSET, Unset


T = TypeVar("T", bound="Campaign")


@attr.s(auto_attribs=True)
class Campaign:
    """
    Attributes:
        id (int):
        cta_type (CtaTypeEnum):
        cta_id (int): Campaign CTA ID
        run_at (Union[Unset, None, datetime.datetime]): Available only for scheduled campaigns
    """

    id: int
    cta_type: CtaTypeEnum
    cta_id: int
    run_at: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        cta_type = self.cta_type.value

        cta_id = self.cta_id
        run_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.run_at, Unset):
            run_at = self.run_at.isoformat() if self.run_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "cta_type": cta_type,
                "cta_id": cta_id,
            }
        )
        if run_at is not UNSET:
            field_dict["run_at"] = run_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        cta_type = CtaTypeEnum(d.pop("cta_type"))

        cta_id = d.pop("cta_id")

        _run_at = d.pop("run_at", UNSET)
        run_at: Union[Unset, None, datetime.datetime]
        if _run_at is None:
            run_at = None
        elif isinstance(_run_at, Unset):
            run_at = UNSET
        else:
            run_at = isoparse(_run_at)

        campaign = cls(
            id=id,
            cta_type=cta_type,
            cta_id=cta_id,
            run_at=run_at,
        )

        campaign.additional_properties = d
        return campaign

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
