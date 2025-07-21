"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from io import BytesIO
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.format_enum import FormatEnum
from ..types import UNSET, File, Unset


T = TypeVar("T", bound="PdfImageConversionRequest")


@attr.s(auto_attribs=True)
class PdfImageConversionRequest:
    """
    Attributes:
        pdf (File):
        password (Union[Unset, str]):
        format_ (Union[Unset, FormatEnum]):  Default: FormatEnum.JPEG.
    """

    pdf: File
    password: Union[Unset, str] = UNSET
    format_: Union[Unset, FormatEnum] = FormatEnum.JPEG
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pdf = self.pdf.to_tuple()

        password = self.password
        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pdf": pdf,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password
        if format_ is not UNSET:
            field_dict["format"] = format_

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        pdf = self.pdf.to_tuple()

        password = (
            self.password
            if isinstance(self.password, Unset)
            else (None, str(self.password).encode(), "text/plain")
        )
        format_: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = (None, str(self.format_.value).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                key: (None, str(value).encode(), "text/plain")
                for key, value in self.additional_properties.items()
            }
        )
        field_dict.update(
            {
                "pdf": pdf,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password
        if format_ is not UNSET:
            field_dict["format"] = format_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pdf = File(payload=BytesIO(d.pop("pdf")))

        password = d.pop("password", UNSET)

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, FormatEnum]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = FormatEnum(_format_)

        pdf_image_conversion_request = cls(
            pdf=pdf,
            password=password,
            format_=format_,
        )

        pdf_image_conversion_request.additional_properties = d
        return pdf_image_conversion_request

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
