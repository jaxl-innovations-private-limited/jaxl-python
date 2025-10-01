"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.iso_country_enum import IsoCountryEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kyc_upload_metadata import KycUploadMetadata


T = TypeVar("T", bound="UserIdentity")


@attr.s(auto_attribs=True)
class UserIdentity:
    """
    Attributes:
        id (int):
        iso_country (IsoCountryEnum):
        sid (Union[Unset, None, str]): Upstream provider SID
        signature (Union[Unset, None, str]):
        upload_metadata (Union[Unset, None, KycUploadMetadata]):
    """

    id: int
    iso_country: IsoCountryEnum
    sid: Union[Unset, None, str] = UNSET
    signature: Union[Unset, None, str] = UNSET
    upload_metadata: Union[Unset, None, "KycUploadMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        iso_country = self.iso_country.value

        sid = self.sid
        signature = self.signature
        upload_metadata: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.upload_metadata, Unset):
            upload_metadata = (
                self.upload_metadata.to_dict() if self.upload_metadata else None
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "iso_country": iso_country,
            }
        )
        if sid is not UNSET:
            field_dict["sid"] = sid
        if signature is not UNSET:
            field_dict["signature"] = signature
        if upload_metadata is not UNSET:
            field_dict["upload_metadata"] = upload_metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.kyc_upload_metadata import KycUploadMetadata

        d = src_dict.copy()
        id = d.pop("id")

        iso_country = IsoCountryEnum(d.pop("iso_country"))

        sid = d.pop("sid", UNSET)

        signature = d.pop("signature", UNSET)

        _upload_metadata = d.pop("upload_metadata", UNSET)
        upload_metadata: Union[Unset, None, KycUploadMetadata]
        if _upload_metadata is None:
            upload_metadata = None
        elif isinstance(_upload_metadata, Unset):
            upload_metadata = UNSET
        else:
            upload_metadata = KycUploadMetadata.from_dict(_upload_metadata)

        user_identity = cls(
            id=id,
            iso_country=iso_country,
            sid=sid,
            signature=signature,
            upload_metadata=upload_metadata,
        )

        user_identity.additional_properties = d
        return user_identity

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
