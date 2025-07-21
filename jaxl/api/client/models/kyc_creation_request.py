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
    from ..models.proof_id_request import ProofIdRequest


T = TypeVar("T", bound="KycCreationRequest")


@attr.s(auto_attribs=True)
class KycCreationRequest:
    """
    Attributes:
        iso_country (IsoCountryEnum):
        address_id (int):
        useridentity_id (int):
        resource (Union[None, ResourceEnum, Unset]):
        proofs (Union[Unset, None, List['ProofIdRequest']]):
        friendly_name (Union[Unset, None, str]):
        parent_id (Union[Unset, None, int]): ID of the KYC being edited
    """

    iso_country: IsoCountryEnum
    address_id: int
    useridentity_id: int
    resource: Union[None, ResourceEnum, Unset] = UNSET
    proofs: Union[Unset, None, List["ProofIdRequest"]] = UNSET
    friendly_name: Union[Unset, None, str] = UNSET
    parent_id: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        iso_country = self.iso_country.value

        address_id = self.address_id
        useridentity_id = self.useridentity_id
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

        proofs: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.proofs, Unset):
            if self.proofs is None:
                proofs = None
            else:
                proofs = []
                for proofs_item_data in self.proofs:
                    proofs_item = proofs_item_data.to_dict()

                    proofs.append(proofs_item)

        friendly_name = self.friendly_name
        parent_id = self.parent_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "iso_country": iso_country,
                "address_id": address_id,
                "useridentity_id": useridentity_id,
            }
        )
        if resource is not UNSET:
            field_dict["resource"] = resource
        if proofs is not UNSET:
            field_dict["proofs"] = proofs
        if friendly_name is not UNSET:
            field_dict["friendly_name"] = friendly_name
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.proof_id_request import ProofIdRequest

        d = src_dict.copy()
        iso_country = IsoCountryEnum(d.pop("iso_country"))

        address_id = d.pop("address_id")

        useridentity_id = d.pop("useridentity_id")

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

        proofs = []
        _proofs = d.pop("proofs", UNSET)
        for proofs_item_data in _proofs or []:
            proofs_item = ProofIdRequest.from_dict(proofs_item_data)

            proofs.append(proofs_item)

        friendly_name = d.pop("friendly_name", UNSET)

        parent_id = d.pop("parent_id", UNSET)

        kyc_creation_request = cls(
            iso_country=iso_country,
            address_id=address_id,
            useridentity_id=useridentity_id,
            resource=resource,
            proofs=proofs,
            friendly_name=friendly_name,
            parent_id=parent_id,
        )

        kyc_creation_request.additional_properties = d
        return kyc_creation_request

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
