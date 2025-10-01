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
    from ..models.user_agent_browser import UserAgentBrowser
    from ..models.user_agent_device import UserAgentDevice
    from ..models.user_agent_operating_system import UserAgentOperatingSystem
    from ..models.user_agent_platform import UserAgentPlatform


T = TypeVar("T", bound="UserAgent")


@attr.s(auto_attribs=True)
class UserAgent:
    """
    Attributes:
        platform (UserAgentPlatform):
        browser (UserAgentBrowser):
        os (UserAgentOperatingSystem):
        device (Union[Unset, None, UserAgentDevice]):
    """

    platform: "UserAgentPlatform"
    browser: "UserAgentBrowser"
    os: "UserAgentOperatingSystem"
    device: Union[Unset, None, "UserAgentDevice"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        platform = self.platform.to_dict()

        browser = self.browser.to_dict()

        os = self.os.to_dict()

        device: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.device, Unset):
            device = self.device.to_dict() if self.device else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platform": platform,
                "browser": browser,
                "os": os,
            }
        )
        if device is not UNSET:
            field_dict["device"] = device

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_agent_browser import UserAgentBrowser
        from ..models.user_agent_device import UserAgentDevice
        from ..models.user_agent_operating_system import UserAgentOperatingSystem
        from ..models.user_agent_platform import UserAgentPlatform

        d = src_dict.copy()
        platform = UserAgentPlatform.from_dict(d.pop("platform"))

        browser = UserAgentBrowser.from_dict(d.pop("browser"))

        os = UserAgentOperatingSystem.from_dict(d.pop("os"))

        _device = d.pop("device", UNSET)
        device: Union[Unset, None, UserAgentDevice]
        if _device is None:
            device = None
        elif isinstance(_device, Unset):
            device = UNSET
        else:
            device = UserAgentDevice.from_dict(_device)

        user_agent = cls(
            platform=platform,
            browser=browser,
            os=os,
            device=device,
        )

        user_agent.additional_properties = d
        return user_agent

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
