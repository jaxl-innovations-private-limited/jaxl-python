"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import json
from io import BytesIO
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..types import File


if TYPE_CHECKING:
    from ..models.aadhar_attributes_request import AadharAttributesRequest


T = TypeVar("T", bound="AadharUploadRequest")


@attr.s(auto_attribs=True)
class AadharUploadRequest:
    """
    Attributes:
        aadhar_card_back (File):
        aadhar_card_front (File):
        attributes (AadharAttributesRequest):
    """

    aadhar_card_back: File
    aadhar_card_front: File
    attributes: "AadharAttributesRequest"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aadhar_card_back = self.aadhar_card_back.to_tuple()

        aadhar_card_front = self.aadhar_card_front.to_tuple()

        attributes = self.attributes.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aadhar_card_back": aadhar_card_back,
                "aadhar_card_front": aadhar_card_front,
                "attributes": attributes,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        aadhar_card_back = self.aadhar_card_back.to_tuple()

        aadhar_card_front = self.aadhar_card_front.to_tuple()

        attributes = (
            None,
            json.dumps(self.attributes.to_dict()).encode(),
            "application/json",
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                key: (None, str(value).encode(), "text/plain")
                for key, value in self.additional_properties.items()
            }
        )
        field_dict.update(
            {
                "aadhar_card_back": aadhar_card_back,
                "aadhar_card_front": aadhar_card_front,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.aadhar_attributes_request import AadharAttributesRequest

        d = src_dict.copy()
        aadhar_card_back = File(payload=BytesIO(d.pop("aadhar_card_back")))

        aadhar_card_front = File(payload=BytesIO(d.pop("aadhar_card_front")))

        attributes = AadharAttributesRequest.from_dict(d.pop("attributes"))

        aadhar_upload_request = cls(
            aadhar_card_back=aadhar_card_back,
            aadhar_card_front=aadhar_card_front,
            attributes=attributes,
        )

        aadhar_upload_request.additional_properties = d
        return aadhar_upload_request

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
