"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.iso_country_enum import IsoCountryEnum
from ..models.proof_status_enum import ProofStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kyc_upload_metadata import KycUploadMetadata


T = TypeVar("T", bound="Proof")


@attr.s(auto_attribs=True)
class Proof:
    """
    Attributes:
        id (int):
        document_type (str):
        status (ProofStatusEnum):
        iso_country (IsoCountryEnum):
        sid (Union[Unset, None, str]): Upstream provider SID
        signature (Union[Unset, None, str]):
        document (Union[Unset, None, KycUploadMetadata]):
        metadata (Union[Unset, None, KycUploadMetadata]):
    """

    id: int
    document_type: str
    status: ProofStatusEnum
    iso_country: IsoCountryEnum
    sid: Union[Unset, None, str] = UNSET
    signature: Union[Unset, None, str] = UNSET
    document: Union[Unset, None, "KycUploadMetadata"] = UNSET
    metadata: Union[Unset, None, "KycUploadMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        document_type = self.document_type
        status = self.status.value

        iso_country = self.iso_country.value

        sid = self.sid
        signature = self.signature
        document: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.document, Unset):
            document = self.document.to_dict() if self.document else None

        metadata: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict() if self.metadata else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "document_type": document_type,
                "status": status,
                "iso_country": iso_country,
            }
        )
        if sid is not UNSET:
            field_dict["sid"] = sid
        if signature is not UNSET:
            field_dict["signature"] = signature
        if document is not UNSET:
            field_dict["document"] = document
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.kyc_upload_metadata import KycUploadMetadata

        d = src_dict.copy()
        id = d.pop("id")

        document_type = d.pop("document_type")

        status = ProofStatusEnum(d.pop("status"))

        iso_country = IsoCountryEnum(d.pop("iso_country"))

        sid = d.pop("sid", UNSET)

        signature = d.pop("signature", UNSET)

        _document = d.pop("document", UNSET)
        document: Union[Unset, None, KycUploadMetadata]
        if _document is None:
            document = None
        elif isinstance(_document, Unset):
            document = UNSET
        else:
            document = KycUploadMetadata.from_dict(_document)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, None, KycUploadMetadata]
        if _metadata is None:
            metadata = None
        elif isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = KycUploadMetadata.from_dict(_metadata)

        proof = cls(
            id=id,
            document_type=document_type,
            status=status,
            iso_country=iso_country,
            sid=sid,
            signature=signature,
            document=document,
            metadata=metadata,
        )

        proof.additional_properties = d
        return proof

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
