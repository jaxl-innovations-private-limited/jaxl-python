"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.iso_country_enum import IsoCountryEnum
from ..models.kyc_status_enum import KycStatusEnum
from ..models.provider_status_enum import ProviderStatusEnum
from ..models.resource_enum import ResourceEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_provider import AddressProvider
    from ..models.proof import Proof
    from ..models.user_identity import UserIdentity


T = TypeVar("T", bound="Kyc")


@attr.s(auto_attribs=True)
class Kyc:
    """Adds a 'jaxlid' field which contains signed ID information.

    Attributes:
        id (int):
        address (AddressProvider):
        useridentity (UserIdentity):
        proofs (List['Proof']):
        iso_country (IsoCountryEnum):
        provider_status (ProviderStatusEnum):
        status (KycStatusEnum):
        can_edit (bool):
        friendly_name (str):
        created_on (datetime.datetime):
        modified_on (datetime.datetime):
        resource (Union[None, ResourceEnum, Unset]):
        parent_id (Union[Unset, None, int]):
        jaxlid (Optional[str]):
    """

    id: int
    address: "AddressProvider"
    useridentity: "UserIdentity"
    proofs: List["Proof"]
    iso_country: IsoCountryEnum
    provider_status: ProviderStatusEnum
    status: KycStatusEnum
    can_edit: bool
    friendly_name: str
    created_on: datetime.datetime
    modified_on: datetime.datetime
    jaxlid: Optional[str]
    resource: Union[None, ResourceEnum, Unset] = UNSET
    parent_id: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        address = self.address.to_dict()

        useridentity = self.useridentity.to_dict()

        proofs = []
        for proofs_item_data in self.proofs:
            proofs_item = proofs_item_data.to_dict()

            proofs.append(proofs_item)

        iso_country = self.iso_country.value

        provider_status = self.provider_status.value

        status = self.status.value

        can_edit = self.can_edit
        friendly_name = self.friendly_name
        created_on = self.created_on.isoformat()

        modified_on = self.modified_on.isoformat()

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

        parent_id = self.parent_id
        jaxlid = self.jaxlid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "address": address,
                "useridentity": useridentity,
                "proofs": proofs,
                "iso_country": iso_country,
                "provider_status": provider_status,
                "status": status,
                "can_edit": can_edit,
                "friendly_name": friendly_name,
                "created_on": created_on,
                "modified_on": modified_on,
                "jaxlid": jaxlid,
            }
        )
        if resource is not UNSET:
            field_dict["resource"] = resource
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address_provider import AddressProvider
        from ..models.proof import Proof
        from ..models.user_identity import UserIdentity

        d = src_dict.copy()
        id = d.pop("id")

        address = AddressProvider.from_dict(d.pop("address"))

        useridentity = UserIdentity.from_dict(d.pop("useridentity"))

        proofs = []
        _proofs = d.pop("proofs")
        for proofs_item_data in _proofs:
            proofs_item = Proof.from_dict(proofs_item_data)

            proofs.append(proofs_item)

        iso_country = IsoCountryEnum(d.pop("iso_country"))

        provider_status = ProviderStatusEnum(d.pop("provider_status"))

        status = KycStatusEnum(d.pop("status"))

        can_edit = d.pop("can_edit")

        friendly_name = d.pop("friendly_name")

        created_on = isoparse(d.pop("created_on"))

        modified_on = isoparse(d.pop("modified_on"))

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

        parent_id = d.pop("parent_id", UNSET)

        jaxlid = d.pop("jaxlid")

        kyc = cls(
            id=id,
            address=address,
            useridentity=useridentity,
            proofs=proofs,
            iso_country=iso_country,
            provider_status=provider_status,
            status=status,
            can_edit=can_edit,
            friendly_name=friendly_name,
            created_on=created_on,
            modified_on=modified_on,
            resource=resource,
            parent_id=parent_id,
            jaxlid=jaxlid,
        )

        kyc.additional_properties = d
        return kyc

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
