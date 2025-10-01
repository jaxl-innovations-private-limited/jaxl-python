"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.ivr_menu_response_status_enum import IVRMenuResponseStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analytic import Analytic


T = TypeVar("T", bound="IVRMenuResponse")


@attr.s(auto_attribs=True)
class IVRMenuResponse:
    """
    Attributes:
        id (int):
        name (str): Name of this IVR menu as shown/spoken to user before following up with options
        status (IVRMenuResponseStatusEnum):
        avg_time_spent (int):
        analytics (List['Analytic']):
        created_by (int):
        hangup (Union[Unset, bool]): Whether the call should be ended after speaking out the greeting message
        phone (Union[Unset, List[int]]):
    """

    id: int
    name: str
    status: IVRMenuResponseStatusEnum
    avg_time_spent: int
    analytics: List["Analytic"]
    created_by: int
    hangup: Union[Unset, bool] = UNSET
    phone: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        status = self.status.value

        avg_time_spent = self.avg_time_spent
        analytics = []
        for analytics_item_data in self.analytics:
            analytics_item = analytics_item_data.to_dict()

            analytics.append(analytics_item)

        created_by = self.created_by
        hangup = self.hangup
        phone: Union[Unset, List[int]] = UNSET
        if not isinstance(self.phone, Unset):
            phone = self.phone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
                "avg_time_spent": avg_time_spent,
                "analytics": analytics,
                "created_by": created_by,
            }
        )
        if hangup is not UNSET:
            field_dict["hangup"] = hangup
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.analytic import Analytic

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        status = IVRMenuResponseStatusEnum(d.pop("status"))

        avg_time_spent = d.pop("avg_time_spent")

        analytics = []
        _analytics = d.pop("analytics")
        for analytics_item_data in _analytics:
            analytics_item = Analytic.from_dict(analytics_item_data)

            analytics.append(analytics_item)

        created_by = d.pop("created_by")

        hangup = d.pop("hangup", UNSET)

        phone = cast(List[int], d.pop("phone", UNSET))

        ivr_menu_response = cls(
            id=id,
            name=name,
            status=status,
            avg_time_spent=avg_time_spent,
            analytics=analytics,
            created_by=created_by,
            hangup=hangup,
            phone=phone,
        )

        ivr_menu_response.additional_properties = d
        return ivr_menu_response

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
