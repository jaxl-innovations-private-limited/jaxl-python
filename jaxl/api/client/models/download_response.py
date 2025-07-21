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
    from ..models.download_response_headers import DownloadResponseHeaders
    from ..models.upload import Upload


T = TypeVar("T", bound="DownloadResponse")


@attr.s(auto_attribs=True)
class DownloadResponse:
    """
    Attributes:
        encrypted (str):
        metadata (Upload):
        headers (Union[Unset, None, DownloadResponseHeaders]):
    """

    encrypted: str
    metadata: "Upload"
    headers: Union[Unset, None, "DownloadResponseHeaders"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        encrypted = self.encrypted
        metadata = self.metadata.to_dict()

        headers: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict() if self.headers else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "encrypted": encrypted,
                "metadata": metadata,
            }
        )
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.download_response_headers import DownloadResponseHeaders
        from ..models.upload import Upload

        d = src_dict.copy()
        encrypted = d.pop("encrypted")

        metadata = Upload.from_dict(d.pop("metadata"))

        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, None, DownloadResponseHeaders]
        if _headers is None:
            headers = None
        elif isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = DownloadResponseHeaders.from_dict(_headers)

        download_response = cls(
            encrypted=encrypted,
            metadata=metadata,
            headers=headers,
        )

        download_response.additional_properties = d
        return download_response

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
