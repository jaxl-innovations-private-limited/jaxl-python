"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.address_provider import AddressProvider
    from ..models.proof import Proof
    from ..models.user_identity import UserIdentity


T = TypeVar("T", bound="KycDocumentResponse")


@attr.s(auto_attribs=True)
class KycDocumentResponse:
    """
    Attributes:
        proofs (List['Proof']):
        user_identity (UserIdentity):
        address (AddressProvider):
    """

    proofs: List["Proof"]
    user_identity: "UserIdentity"
    address: "AddressProvider"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        proofs = []
        for proofs_item_data in self.proofs:
            proofs_item = proofs_item_data.to_dict()

            proofs.append(proofs_item)

        user_identity = self.user_identity.to_dict()

        address = self.address.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proofs": proofs,
                "user_identity": user_identity,
                "address": address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address_provider import AddressProvider
        from ..models.proof import Proof
        from ..models.user_identity import UserIdentity

        d = src_dict.copy()
        proofs = []
        _proofs = d.pop("proofs")
        for proofs_item_data in _proofs:
            proofs_item = Proof.from_dict(proofs_item_data)

            proofs.append(proofs_item)

        user_identity = UserIdentity.from_dict(d.pop("user_identity"))

        address = AddressProvider.from_dict(d.pop("address"))

        kyc_document_response = cls(
            proofs=proofs,
            user_identity=user_identity,
            address=address,
        )

        kyc_document_response.additional_properties = d
        return kyc_document_response

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
