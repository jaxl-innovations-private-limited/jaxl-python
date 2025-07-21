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
    from ..models.app_user_preferences_request_preferences import (
        AppUserPreferencesRequestPreferences,
    )


T = TypeVar("T", bound="AppUserPreferencesRequest")


@attr.s(auto_attribs=True)
class AppUserPreferencesRequest:
    """
    Attributes:
        preferences (Union[Unset, AppUserPreferencesRequestPreferences]): Adhoc key-value pairs storing app user
            preferences & settings
    """

    preferences: Union[Unset, "AppUserPreferencesRequestPreferences"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        preferences: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preferences, Unset):
            preferences = self.preferences.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if preferences is not UNSET:
            field_dict["preferences"] = preferences

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.app_user_preferences_request_preferences import (
            AppUserPreferencesRequestPreferences,
        )

        d = src_dict.copy()
        _preferences = d.pop("preferences", UNSET)
        preferences: Union[Unset, AppUserPreferencesRequestPreferences]
        if isinstance(_preferences, Unset):
            preferences = UNSET
        else:
            preferences = AppUserPreferencesRequestPreferences.from_dict(_preferences)

        app_user_preferences_request = cls(
            preferences=preferences,
        )

        app_user_preferences_request.additional_properties = d
        return app_user_preferences_request

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
