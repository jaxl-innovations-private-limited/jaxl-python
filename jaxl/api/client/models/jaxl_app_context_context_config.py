"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.jaxl_app_context_context_config_firebase import (
        JaxlAppContextContextConfigFirebase,
    )


T = TypeVar("T", bound="JaxlAppContextContextConfig")


@attr.s(auto_attribs=True)
class JaxlAppContextContextConfig:
    """
    Attributes:
        firebase (Optional[JaxlAppContextContextConfigFirebase]):
    """

    firebase: Optional["JaxlAppContextContextConfigFirebase"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        firebase = self.firebase.to_dict() if self.firebase else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "firebase": firebase,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.jaxl_app_context_context_config_firebase import (
            JaxlAppContextContextConfigFirebase,
        )

        d = src_dict.copy()
        _firebase = d.pop("firebase")
        firebase: Optional[JaxlAppContextContextConfigFirebase]
        if _firebase is None:
            firebase = None
        else:
            firebase = JaxlAppContextContextConfigFirebase.from_dict(_firebase)

        jaxl_app_context_context_config = cls(
            firebase=firebase,
        )

        jaxl_app_context_context_config.additional_properties = d
        return jaxl_app_context_context_config

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
