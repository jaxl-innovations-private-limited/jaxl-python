"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CampaignStats")


@attr.s(auto_attribs=True)
class CampaignStats:
    """
    Attributes:
        total (int):
        successful (int):
        failed (int):
        missed (int):
        pending (int):
    """

    total: int
    successful: int
    failed: int
    missed: int
    pending: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total = self.total
        successful = self.successful
        failed = self.failed
        missed = self.missed
        pending = self.pending

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "successful": successful,
                "failed": failed,
                "missed": missed,
                "pending": pending,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total = d.pop("total")

        successful = d.pop("successful")

        failed = d.pop("failed")

        missed = d.pop("missed")

        pending = d.pop("pending")

        campaign_stats = cls(
            total=total,
            successful=successful,
            failed=failed,
            missed=missed,
            pending=pending,
        )

        campaign_stats.additional_properties = d
        return campaign_stats

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
