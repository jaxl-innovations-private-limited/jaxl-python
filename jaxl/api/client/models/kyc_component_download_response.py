"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.kyc_upload_metadata import KycUploadMetadata


T = TypeVar("T", bound="KycComponentDownloadResponse")


@attr.s(auto_attribs=True)
class KycComponentDownloadResponse:
    """
    Attributes:
        encrypted (str):
        metadata (KycUploadMetadata):
    """

    encrypted: str
    metadata: "KycUploadMetadata"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        encrypted = self.encrypted
        metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "encrypted": encrypted,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.kyc_upload_metadata import KycUploadMetadata

        d = src_dict.copy()
        encrypted = d.pop("encrypted")

        metadata = KycUploadMetadata.from_dict(d.pop("metadata"))

        kyc_component_download_response = cls(
            encrypted=encrypted,
            metadata=metadata,
        )

        kyc_component_download_response.additional_properties = d
        return kyc_component_download_response

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
