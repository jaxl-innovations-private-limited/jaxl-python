"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.kyc_component_download_response import (
        KycComponentDownloadResponse,
    )


T = TypeVar("T", bound="ProofDownloadResponse")


@attr.s(auto_attribs=True)
class ProofDownloadResponse:
    """
    Attributes:
        document (KycComponentDownloadResponse):
        metadata (KycComponentDownloadResponse):
    """

    document: "KycComponentDownloadResponse"
    metadata: "KycComponentDownloadResponse"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        document = self.document.to_dict()

        metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "document": document,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.kyc_component_download_response import (
            KycComponentDownloadResponse,
        )

        d = src_dict.copy()
        document = KycComponentDownloadResponse.from_dict(d.pop("document"))

        metadata = KycComponentDownloadResponse.from_dict(d.pop("metadata"))

        proof_download_response = cls(
            document=document,
            metadata=metadata,
        )

        proof_download_response.additional_properties = d
        return proof_download_response

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
