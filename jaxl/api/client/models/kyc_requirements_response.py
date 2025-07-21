"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.additional_fields import AdditionalFields
    from ..models.address_requirement import AddressRequirement
    from ..models.identity_requirement import IdentityRequirement
    from ..models.proofs_requirement import ProofsRequirement


T = TypeVar("T", bound="KycRequirementsResponse")


@attr.s(auto_attribs=True)
class KycRequirementsResponse:
    """
    Attributes:
        identity (IdentityRequirement):
        address (AddressRequirement):
        proofs (ProofsRequirement):
        additional_fields (List['AdditionalFields']):
    """

    identity: "IdentityRequirement"
    address: "AddressRequirement"
    proofs: "ProofsRequirement"
    additional_fields: List["AdditionalFields"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identity = self.identity.to_dict()

        address = self.address.to_dict()

        proofs = self.proofs.to_dict()

        additional_fields = []
        for additional_fields_item_data in self.additional_fields:
            additional_fields_item = additional_fields_item_data.to_dict()

            additional_fields.append(additional_fields_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identity": identity,
                "address": address,
                "proofs": proofs,
                "additional_fields": additional_fields,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.additional_fields import AdditionalFields
        from ..models.address_requirement import AddressRequirement
        from ..models.identity_requirement import IdentityRequirement
        from ..models.proofs_requirement import ProofsRequirement

        d = src_dict.copy()
        identity = IdentityRequirement.from_dict(d.pop("identity"))

        address = AddressRequirement.from_dict(d.pop("address"))

        proofs = ProofsRequirement.from_dict(d.pop("proofs"))

        additional_fields = []
        _additional_fields = d.pop("additional_fields")
        for additional_fields_item_data in _additional_fields:
            additional_fields_item = AdditionalFields.from_dict(
                additional_fields_item_data
            )

            additional_fields.append(additional_fields_item)

        kyc_requirements_response = cls(
            identity=identity,
            address=address,
            proofs=proofs,
            additional_fields=additional_fields,
        )

        kyc_requirements_response.additional_properties = d
        return kyc_requirements_response

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
