"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.campaign_v2_status_enum import CampaignV2StatusEnum
from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.campaign_stats_v2 import CampaignStatsV2
    from ..models.campaign_tag import CampaignTag


T = TypeVar("T", bound="CampaignV2")


@attr.s(auto_attribs=True)
class CampaignV2:
    """
    Attributes:
        id (int):
        name (str):
        status (CampaignV2StatusEnum):
        started_by (int):
        stats (CampaignStatsV2):
        tags (List['CampaignTag']):
        created_on (datetime.datetime): Datetime when this object was created
        in_window (bool):
        auto_retry (bool):
        parent (Union[Unset, None, int]): Campaign from which this campaign was cloned.
    """

    id: int
    name: str
    status: CampaignV2StatusEnum
    started_by: int
    stats: "CampaignStatsV2"
    tags: List["CampaignTag"]
    created_on: datetime.datetime
    in_window: bool
    auto_retry: bool
    parent: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        status = self.status.value

        started_by = self.started_by
        stats = self.stats.to_dict()

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()

            tags.append(tags_item)

        created_on = self.created_on.isoformat()

        in_window = self.in_window
        auto_retry = self.auto_retry
        parent = self.parent

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
                "started_by": started_by,
                "stats": stats,
                "tags": tags,
                "created_on": created_on,
                "in_window": in_window,
                "auto_retry": auto_retry,
            }
        )
        if parent is not UNSET:
            field_dict["parent"] = parent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.campaign_stats_v2 import CampaignStatsV2
        from ..models.campaign_tag import CampaignTag

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        status = CampaignV2StatusEnum(d.pop("status"))

        started_by = d.pop("started_by")

        stats = CampaignStatsV2.from_dict(d.pop("stats"))

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = CampaignTag.from_dict(tags_item_data)

            tags.append(tags_item)

        created_on = isoparse(d.pop("created_on"))

        in_window = d.pop("in_window")

        auto_retry = d.pop("auto_retry")

        parent = d.pop("parent", UNSET)

        campaign_v2 = cls(
            id=id,
            name=name,
            status=status,
            started_by=started_by,
            stats=stats,
            tags=tags,
            created_on=created_on,
            in_window=in_window,
            auto_retry=auto_retry,
            parent=parent,
        )

        campaign_v2.additional_properties = d
        return campaign_v2

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
