"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.jaxl_app_context_context_app import JaxlAppContextContextApp
    from ..models.jaxl_app_context_context_config import (
        JaxlAppContextContextConfig,
    )
    from ..models.jaxl_app_context_context_device import (
        JaxlAppContextContextDevice,
    )
    from ..models.jaxl_app_context_context_user import (
        JaxlAppContextContextUser,
    )


T = TypeVar("T", bound="JaxlAppContextContext")


@attr.s(auto_attribs=True)
class JaxlAppContextContext:
    """
    Attributes:
        app (JaxlAppContextContextApp):
        user (JaxlAppContextContextUser):
        device (JaxlAppContextContextDevice):
        config (JaxlAppContextContextConfig):
    """

    app: "JaxlAppContextContextApp"
    user: "JaxlAppContextContextUser"
    device: "JaxlAppContextContextDevice"
    config: "JaxlAppContextContextConfig"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        app = self.app.to_dict()

        user = self.user.to_dict()

        device = self.device.to_dict()

        config = self.config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app": app,
                "user": user,
                "device": device,
                "config": config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.jaxl_app_context_context_app import (
            JaxlAppContextContextApp,
        )
        from ..models.jaxl_app_context_context_config import (
            JaxlAppContextContextConfig,
        )
        from ..models.jaxl_app_context_context_device import (
            JaxlAppContextContextDevice,
        )
        from ..models.jaxl_app_context_context_user import (
            JaxlAppContextContextUser,
        )

        d = src_dict.copy()
        app = JaxlAppContextContextApp.from_dict(d.pop("app"))

        user = JaxlAppContextContextUser.from_dict(d.pop("user"))

        device = JaxlAppContextContextDevice.from_dict(d.pop("device"))

        config = JaxlAppContextContextConfig.from_dict(d.pop("config"))

        jaxl_app_context_context = cls(
            app=app,
            user=user,
            device=device,
            config=config,
        )

        jaxl_app_context_context.additional_properties = d
        return jaxl_app_context_context

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
