"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.chart_type_enum import ChartTypeEnum


T = TypeVar("T", bound="AnalyticsSlugResponse")


@attr.s(auto_attribs=True)
class AnalyticsSlugResponse:
    """
    Attributes:
        title (str):
        slug (str):
        chart_type (ChartTypeEnum):
    """

    title: str
    slug: str
    chart_type: ChartTypeEnum
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        slug = self.slug
        chart_type = self.chart_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "slug": slug,
                "chart_type": chart_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        slug = d.pop("slug")

        chart_type = ChartTypeEnum(d.pop("chart_type"))

        analytics_slug_response = cls(
            title=title,
            slug=slug,
            chart_type=chart_type,
        )

        analytics_slug_response.additional_properties = d
        return analytics_slug_response

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
