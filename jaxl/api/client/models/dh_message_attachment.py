"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="DHMessageAttachment")


@attr.s(auto_attribs=True)
class DHMessageAttachment:
    """
    Attributes:
        id (int):
        size (int):
        mimetype (str):
        sha256 (str):
        uploaded_on (Optional[datetime.datetime]):
        signature (Optional[str]):
    """

    id: int
    size: int
    mimetype: str
    sha256: str
    uploaded_on: Optional[datetime.datetime]
    signature: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        size = self.size
        mimetype = self.mimetype
        sha256 = self.sha256
        uploaded_on = self.uploaded_on.isoformat() if self.uploaded_on else None

        signature = self.signature

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "size": size,
                "mimetype": mimetype,
                "sha256": sha256,
                "uploaded_on": uploaded_on,
                "signature": signature,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        size = d.pop("size")

        mimetype = d.pop("mimetype")

        sha256 = d.pop("sha256")

        _uploaded_on = d.pop("uploaded_on")
        uploaded_on: Optional[datetime.datetime]
        if _uploaded_on is None:
            uploaded_on = None
        else:
            uploaded_on = isoparse(_uploaded_on)

        signature = d.pop("signature")

        dh_message_attachment = cls(
            id=id,
            size=size,
            mimetype=mimetype,
            sha256=sha256,
            uploaded_on=uploaded_on,
            signature=signature,
        )

        dh_message_attachment.additional_properties = d
        return dh_message_attachment

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
