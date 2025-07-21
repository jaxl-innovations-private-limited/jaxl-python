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

from ..types import File, Unset


if TYPE_CHECKING:
    from ..models.kyc_proof_upload_data_request import (
        KycProofUploadDataRequest,
    )


T = TypeVar("T", bound="KycProofUploadRequest")


@attr.s(auto_attribs=True)
class KycProofUploadRequest:
    """
    Attributes:
        file (File):
        payload (KycProofUploadDataRequest):
        csek (str):
        signature (str):
    """

    file: File
    payload: "KycProofUploadDataRequest"
    csek: str
    signature: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file = self.file.to_tuple()

        payload = self.payload.to_dict()

        csek = self.csek
        signature = self.signature

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
                "payload": payload,
                "csek": csek,
                "signature": signature,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        file = self.file.to_tuple()

        payload = (
            None,
            json.dumps(self.payload.to_dict()).encode(),
            "application/json",
        )

        csek = (
            self.csek
            if isinstance(self.csek, Unset)
            else (None, str(self.csek).encode(), "text/plain")
        )
        signature = (
            self.signature
            if isinstance(self.signature, Unset)
            else (None, str(self.signature).encode(), "text/plain")
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
                "file": file,
                "payload": payload,
                "csek": csek,
                "signature": signature,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.kyc_proof_upload_data_request import (
            KycProofUploadDataRequest,
        )

        d = src_dict.copy()
        file = File(payload=BytesIO(d.pop("file")))

        payload = KycProofUploadDataRequest.from_dict(d.pop("payload"))

        csek = d.pop("csek")

        signature = d.pop("signature")

        kyc_proof_upload_request = cls(
            file=file,
            payload=payload,
            csek=csek,
            signature=signature,
        )

        kyc_proof_upload_request.additional_properties = d
        return kyc_proof_upload_request

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
