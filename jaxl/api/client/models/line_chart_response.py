"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.resolution_enum import ResolutionEnum


if TYPE_CHECKING:
    from ..models.point_response import PointResponse


T = TypeVar("T", bound="LineChartResponse")


@attr.s(auto_attribs=True)
class LineChartResponse:
    """
    Attributes:
        points (List['PointResponse']):
        resolution (ResolutionEnum):
    """

    points: List["PointResponse"]
    resolution: ResolutionEnum
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        points = []
        for points_item_data in self.points:
            points_item = points_item_data.to_dict()

            points.append(points_item)

        resolution = self.resolution.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "points": points,
                "resolution": resolution,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.point_response import PointResponse

        d = src_dict.copy()
        points = []
        _points = d.pop("points")
        for points_item_data in _points:
            points_item = PointResponse.from_dict(points_item_data)

            points.append(points_item)

        resolution = ResolutionEnum(d.pop("resolution"))

        line_chart_response = cls(
            points=points,
            resolution=resolution,
        )

        line_chart_response.additional_properties = d
        return line_chart_response

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
