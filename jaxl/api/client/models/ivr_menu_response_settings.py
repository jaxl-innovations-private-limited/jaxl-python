"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="IVRMenuResponseSettings")


@attr.s(auto_attribs=True)
class IVRMenuResponseSettings:
    """Adhoc key-value pairs storing ivr settings. Stores following dynamic settings: 1) speak_greeting -- Defaults to
    true. 2) ask_for_input -- Request called input before CTA execution. 3) confirm_input -- Whether to confirm user
    input before proceeding with CTA. 4) callback_url -- Pre-CTA callback URL.  IVR CTA is executed if url returns 200
    OK. 5) callback_url_method -- Method to use then invoking callback_url e.g. GET or POST.6) cta -- Fully validated
    runtime CTA to execute. 7) status_callback_url -- A callback url invoked with call flow status changes. 8)
    status_callback_url_method -- Method to use then invoking status_callback_url_method e.g. GET or POST.

    """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ivr_menu_response_settings = cls()

        ivr_menu_response_settings.additional_properties = d
        return ivr_menu_response_settings

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
