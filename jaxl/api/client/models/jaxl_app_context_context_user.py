"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Optional, Type, TypeVar

import attr


T = TypeVar("T", bound="JaxlAppContextContextUser")


@attr.s(auto_attribs=True)
class JaxlAppContextContextUser:
    """
    Attributes:
        id (Optional[int]):
        app_user_id (Optional[int]):
        is_logged_in (Optional[bool]):
    """

    id: Optional[int]
    app_user_id: Optional[int]
    is_logged_in: Optional[bool]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        app_user_id = self.app_user_id
        is_logged_in = self.is_logged_in

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "app_user_id": app_user_id,
                "is_logged_in": is_logged_in,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        app_user_id = d.pop("app_user_id")

        is_logged_in = d.pop("is_logged_in")

        jaxl_app_context_context_user = cls(
            id=id,
            app_user_id=app_user_id,
            is_logged_in=is_logged_in,
        )

        jaxl_app_context_context_user.additional_properties = d
        return jaxl_app_context_context_user

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
