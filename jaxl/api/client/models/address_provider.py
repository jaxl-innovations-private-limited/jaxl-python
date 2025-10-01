"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.address_provider_status_enum import AddressProviderStatusEnum
from ..models.resource_enum import ResourceEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kyc_upload_metadata import KycUploadMetadata


T = TypeVar("T", bound="AddressProvider")


@attr.s(auto_attribs=True)
class AddressProvider:
    """
    Attributes:
        id (int):
        friendly_name_sha (str):
        iso_country (str):
        status (AddressProviderStatusEnum):
        useridentity_id (int):
        sid (Union[Unset, None, str]):
        resource (Union[None, ResourceEnum, Unset]):
        signature (Union[Unset, None, str]):
        upload_metadata (Union[Unset, None, KycUploadMetadata]):
    """

    id: int
    friendly_name_sha: str
    iso_country: str
    status: AddressProviderStatusEnum
    useridentity_id: int
    sid: Union[Unset, None, str] = UNSET
    resource: Union[None, ResourceEnum, Unset] = UNSET
    signature: Union[Unset, None, str] = UNSET
    upload_metadata: Union[Unset, None, "KycUploadMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        friendly_name_sha = self.friendly_name_sha
        iso_country = self.iso_country
        status = self.status.value

        useridentity_id = self.useridentity_id
        sid = self.sid
        resource: Union[None, Unset, str]
        if isinstance(self.resource, Unset):
            resource = UNSET
        elif self.resource is None:
            resource = None

        elif isinstance(self.resource, ResourceEnum):
            resource = UNSET
            if not isinstance(self.resource, Unset):
                resource = self.resource.value

        else:
            resource = self.resource

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
                "friendly_name_sha": friendly_name_sha,
                "iso_country": iso_country,
                "status": status,
                "useridentity_id": useridentity_id,
            }
        )
        if sid is not UNSET:
            field_dict["sid"] = sid
        if resource is not UNSET:
            field_dict["resource"] = resource
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

        friendly_name_sha = d.pop("friendly_name_sha")

        iso_country = d.pop("iso_country")

        status = AddressProviderStatusEnum(d.pop("status"))

        useridentity_id = d.pop("useridentity_id")

        sid = d.pop("sid", UNSET)

        def _parse_resource(data: object) -> Union[None, ResourceEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _resource_type_0 = data
                resource_type_0: Union[Unset, ResourceEnum]
                if isinstance(_resource_type_0, Unset):
                    resource_type_0 = UNSET
                else:
                    resource_type_0 = ResourceEnum(_resource_type_0)

                return resource_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, ResourceEnum, Unset], data)

        resource = _parse_resource(d.pop("resource", UNSET))

        signature = d.pop("signature", UNSET)

        _upload_metadata = d.pop("upload_metadata", UNSET)
        upload_metadata: Union[Unset, None, KycUploadMetadata]
        if _upload_metadata is None:
            upload_metadata = None
        elif isinstance(_upload_metadata, Unset):
            upload_metadata = UNSET
        else:
            upload_metadata = KycUploadMetadata.from_dict(_upload_metadata)

        address_provider = cls(
            id=id,
            friendly_name_sha=friendly_name_sha,
            iso_country=iso_country,
            status=status,
            useridentity_id=useridentity_id,
            sid=sid,
            resource=resource,
            signature=signature,
            upload_metadata=upload_metadata,
        )

        address_provider.additional_properties = d
        return address_provider

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
