"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.greeting_configuration_response import (
        GreetingConfigurationResponse,
    )
    from ..models.upload import Upload


T = TypeVar("T", bound="GreetingCreationResponse")


@attr.s(auto_attribs=True)
class GreetingCreationResponse:
    """
    Attributes:
        greeting_configuration (GreetingConfigurationResponse):
        upload (Upload):
    """

    greeting_configuration: "GreetingConfigurationResponse"
    upload: "Upload"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        greeting_configuration = self.greeting_configuration.to_dict()

        upload = self.upload.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "greeting_configuration": greeting_configuration,
                "upload": upload,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.greeting_configuration_response import (
            GreetingConfigurationResponse,
        )
        from ..models.upload import Upload

        d = src_dict.copy()
        greeting_configuration = GreetingConfigurationResponse.from_dict(
            d.pop("greeting_configuration")
        )

        upload = Upload.from_dict(d.pop("upload"))

        greeting_creation_response = cls(
            greeting_configuration=greeting_configuration,
            upload=upload,
        )

        greeting_creation_response.additional_properties = d
        return greeting_creation_response

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
