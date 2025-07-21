"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.campaign_usage_summary import CampaignUsageSummary


T = TypeVar("T", bound="CampaignStatsV2")


@attr.s(auto_attribs=True)
class CampaignStatsV2:
    """
    Attributes:
        total (CampaignUsageSummary):
        successful (CampaignUsageSummary):
        failed (CampaignUsageSummary):
        missed (CampaignUsageSummary):
        pending (CampaignUsageSummary):
    """

    total: "CampaignUsageSummary"
    successful: "CampaignUsageSummary"
    failed: "CampaignUsageSummary"
    missed: "CampaignUsageSummary"
    pending: "CampaignUsageSummary"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total = self.total.to_dict()

        successful = self.successful.to_dict()

        failed = self.failed.to_dict()

        missed = self.missed.to_dict()

        pending = self.pending.to_dict()

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
        from ..models.campaign_usage_summary import CampaignUsageSummary

        d = src_dict.copy()
        total = CampaignUsageSummary.from_dict(d.pop("total"))

        successful = CampaignUsageSummary.from_dict(d.pop("successful"))

        failed = CampaignUsageSummary.from_dict(d.pop("failed"))

        missed = CampaignUsageSummary.from_dict(d.pop("missed"))

        pending = CampaignUsageSummary.from_dict(d.pop("pending"))

        campaign_stats_v2 = cls(
            total=total,
            successful=successful,
            failed=failed,
            missed=missed,
            pending=pending,
        )

        campaign_stats_v2.additional_properties = d
        return campaign_stats_v2

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
