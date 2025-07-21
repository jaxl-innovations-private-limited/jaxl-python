"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.iso_country_enum import IsoCountryEnum
from ..models.resource_enum import ResourceEnum
from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.proof_field_request import ProofFieldRequest


T = TypeVar("T", bound="KycProofUploadDataRequest")


@attr.s(auto_attribs=True)
class KycProofUploadDataRequest:
    """
    Attributes:
        useridentity_id (int):
        address_id (int):
        proof_fields (List['ProofFieldRequest']):
        friendly_name (str):
        document_type (str): Type of document eg: passport, business_registration, government_issued_document,
            residence_permit etc
        iso_country (IsoCountryEnum):
        resource (Union[None, ResourceEnum, Unset]):
    """

    useridentity_id: int
    address_id: int
    proof_fields: List["ProofFieldRequest"]
    friendly_name: str
    document_type: str
    iso_country: IsoCountryEnum
    resource: Union[None, ResourceEnum, Unset] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        useridentity_id = self.useridentity_id
        address_id = self.address_id
        proof_fields = []
        for proof_fields_item_data in self.proof_fields:
            proof_fields_item = proof_fields_item_data.to_dict()

            proof_fields.append(proof_fields_item)

        friendly_name = self.friendly_name
        document_type = self.document_type
        iso_country = self.iso_country.value

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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "useridentity_id": useridentity_id,
                "address_id": address_id,
                "proof_fields": proof_fields,
                "friendly_name": friendly_name,
                "document_type": document_type,
                "iso_country": iso_country,
            }
        )
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.proof_field_request import ProofFieldRequest

        d = src_dict.copy()
        useridentity_id = d.pop("useridentity_id")

        address_id = d.pop("address_id")

        proof_fields = []
        _proof_fields = d.pop("proof_fields")
        for proof_fields_item_data in _proof_fields:
            proof_fields_item = ProofFieldRequest.from_dict(proof_fields_item_data)

            proof_fields.append(proof_fields_item)

        friendly_name = d.pop("friendly_name")

        document_type = d.pop("document_type")

        iso_country = IsoCountryEnum(d.pop("iso_country"))

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

        kyc_proof_upload_data_request = cls(
            useridentity_id=useridentity_id,
            address_id=address_id,
            proof_fields=proof_fields,
            friendly_name=friendly_name,
            document_type=document_type,
            iso_country=iso_country,
            resource=resource,
        )

        kyc_proof_upload_data_request.additional_properties = d
        return kyc_proof_upload_data_request

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
