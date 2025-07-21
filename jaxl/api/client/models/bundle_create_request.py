"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.individual_plan_request import IndividualPlanRequest


T = TypeVar("T", bound="BundleCreateRequest")


@attr.s(auto_attribs=True)
class BundleCreateRequest:
    """
    Attributes:
        includes (List['IndividualPlanRequest']):
        name (Union[Unset, str]):
        release (Union[Unset, bool]):  Default: True.
        publish (Union[Unset, bool]):  Default: True.
    """

    includes: List["IndividualPlanRequest"]
    name: Union[Unset, str] = UNSET
    release: Union[Unset, bool] = True
    publish: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        includes = []
        for includes_item_data in self.includes:
            includes_item = includes_item_data.to_dict()

            includes.append(includes_item)

        name = self.name
        release = self.release
        publish = self.publish

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "includes": includes,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if release is not UNSET:
            field_dict["release"] = release
        if publish is not UNSET:
            field_dict["publish"] = publish

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.individual_plan_request import IndividualPlanRequest

        d = src_dict.copy()
        includes = []
        _includes = d.pop("includes")
        for includes_item_data in _includes:
            includes_item = IndividualPlanRequest.from_dict(includes_item_data)

            includes.append(includes_item)

        name = d.pop("name", UNSET)

        release = d.pop("release", UNSET)

        publish = d.pop("publish", UNSET)

        bundle_create_request = cls(
            includes=includes,
            name=name,
            release=release,
            publish=publish,
        )

        bundle_create_request.additional_properties = d
        return bundle_create_request

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
