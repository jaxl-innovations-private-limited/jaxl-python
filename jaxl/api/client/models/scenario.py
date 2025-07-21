"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.scenario_enum import ScenarioEnum
from ..types import UNSET, Unset


T = TypeVar("T", bound="Scenario")


@attr.s(auto_attribs=True)
class Scenario:
    """
    Attributes:
        scenario (ScenarioEnum):
        scenario_key (Union[Unset, str]):
    """

    scenario: ScenarioEnum
    scenario_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scenario = self.scenario.value

        scenario_key = self.scenario_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scenario": scenario,
            }
        )
        if scenario_key is not UNSET:
            field_dict["scenario_key"] = scenario_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _scenario = ScenarioEnum(d.pop("scenario"))

        scenario_key = d.pop("scenario_key", UNSET)

        scenario = cls(
            scenario=_scenario,
            scenario_key=scenario_key,
        )

        scenario.additional_properties = d
        return scenario

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
