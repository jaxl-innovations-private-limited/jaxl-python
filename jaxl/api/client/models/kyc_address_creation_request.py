"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.resource_enum import ResourceEnum
from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.address_creation_request import AddressCreationRequest


T = TypeVar("T", bound="KycAddressCreationRequest")


@attr.s(auto_attribs=True)
class KycAddressCreationRequest:
    """
    Attributes:
        useridentity_id (int):
        address (AddressCreationRequest):
        csek (str):
        signature (str):
        resource (Union[None, ResourceEnum, Unset]):
    """

    useridentity_id: int
    address: "AddressCreationRequest"
    csek: str
    signature: str
    resource: Union[None, ResourceEnum, Unset] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        useridentity_id = self.useridentity_id
        address = self.address.to_dict()

        csek = self.csek
        signature = self.signature
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
                "address": address,
                "csek": csek,
                "signature": signature,
            }
        )
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address_creation_request import AddressCreationRequest

        d = src_dict.copy()
        useridentity_id = d.pop("useridentity_id")

        address = AddressCreationRequest.from_dict(d.pop("address"))

        csek = d.pop("csek")

        signature = d.pop("signature")

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

        kyc_address_creation_request = cls(
            useridentity_id=useridentity_id,
            address=address,
            csek=csek,
            signature=signature,
            resource=resource,
        )

        kyc_address_creation_request.additional_properties = d
        return kyc_address_creation_request

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
