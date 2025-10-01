"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.id_enum import IdEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plan_type_cycle import PlanTypeCycle


T = TypeVar("T", bound="PlanType")


@attr.s(auto_attribs=True)
class PlanType:
    """
    Attributes:
        id (IdEnum):
        cycle (Union[Unset, PlanTypeCycle]):
    """

    id: IdEnum
    cycle: Union[Unset, "PlanTypeCycle"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id.value

        cycle: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cycle, Unset):
            cycle = self.cycle.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if cycle is not UNSET:
            field_dict["cycle"] = cycle

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.plan_type_cycle import PlanTypeCycle

        d = src_dict.copy()
        id = IdEnum(d.pop("id"))

        _cycle = d.pop("cycle", UNSET)
        cycle: Union[Unset, PlanTypeCycle]
        if isinstance(_cycle, Unset):
            cycle = UNSET
        else:
            cycle = PlanTypeCycle.from_dict(_cycle)

        plan_type = cls(
            id=id,
            cycle=cycle,
        )

        plan_type.additional_properties = d
        return plan_type

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
