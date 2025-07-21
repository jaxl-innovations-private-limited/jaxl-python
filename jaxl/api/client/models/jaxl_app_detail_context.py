"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.jaxl_app_detail_context_app import JaxlAppDetailContextApp
    from ..models.jaxl_app_detail_context_endpoints import (
        JaxlAppDetailContextEndpoints,
    )


T = TypeVar("T", bound="JaxlAppDetailContext")


@attr.s(auto_attribs=True)
class JaxlAppDetailContext:
    """
    Attributes:
        app (JaxlAppDetailContextApp):
        endpoints (JaxlAppDetailContextEndpoints):
    """

    app: "JaxlAppDetailContextApp"
    endpoints: "JaxlAppDetailContextEndpoints"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        app = self.app.to_dict()

        endpoints = self.endpoints.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app": app,
                "endpoints": endpoints,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.jaxl_app_detail_context_app import (
            JaxlAppDetailContextApp,
        )
        from ..models.jaxl_app_detail_context_endpoints import (
            JaxlAppDetailContextEndpoints,
        )

        d = src_dict.copy()
        app = JaxlAppDetailContextApp.from_dict(d.pop("app"))

        endpoints = JaxlAppDetailContextEndpoints.from_dict(d.pop("endpoints"))

        jaxl_app_detail_context = cls(
            app=app,
            endpoints=endpoints,
        )

        jaxl_app_detail_context.additional_properties = d
        return jaxl_app_detail_context

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
