"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.greeting_type_enum import GreetingTypeEnum
from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.upload import Upload


T = TypeVar("T", bound="Greeting")


@attr.s(auto_attribs=True)
class Greeting:
    """
    Attributes:
        app_user_id (int): AppUser who created this greeting
        device_id (int): Device on which this greeting was created
        upload (Upload):
        greeting_type (GreetingTypeEnum):
        created_on (datetime.datetime): Datetime when this object was created
        modified_on (datetime.datetime): Datetime when this object was last modified
        text (Union[Unset, Upload]):
    """

    app_user_id: int
    device_id: int
    upload: "Upload"
    greeting_type: GreetingTypeEnum
    created_on: datetime.datetime
    modified_on: datetime.datetime
    text: Union[Unset, "Upload"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        app_user_id = self.app_user_id
        device_id = self.device_id
        upload = self.upload.to_dict()

        greeting_type = self.greeting_type.value

        created_on = self.created_on.isoformat()

        modified_on = self.modified_on.isoformat()

        text: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.text, Unset):
            text = self.text.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_user_id": app_user_id,
                "device_id": device_id,
                "upload": upload,
                "greeting_type": greeting_type,
                "created_on": created_on,
                "modified_on": modified_on,
            }
        )
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.upload import Upload

        d = src_dict.copy()
        app_user_id = d.pop("app_user_id")

        device_id = d.pop("device_id")

        upload = Upload.from_dict(d.pop("upload"))

        greeting_type = GreetingTypeEnum(d.pop("greeting_type"))

        created_on = isoparse(d.pop("created_on"))

        modified_on = isoparse(d.pop("modified_on"))

        _text = d.pop("text", UNSET)
        text: Union[Unset, Upload]
        if isinstance(_text, Unset):
            text = UNSET
        else:
            text = Upload.from_dict(_text)

        greeting = cls(
            app_user_id=app_user_id,
            device_id=device_id,
            upload=upload,
            greeting_type=greeting_type,
            created_on=created_on,
            modified_on=modified_on,
            text=text,
        )

        greeting.additional_properties = d
        return greeting

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
