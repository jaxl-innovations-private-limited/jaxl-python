"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar

import attr


T = TypeVar("T", bound="KeyChainMultiGetResponse")


@attr.s(auto_attribs=True)
class KeyChainMultiGetResponse:
    """
    Attributes:
        id (int):
        key (str):
        encrypted (str): Encrypted value.  Devices must encrypt the values using self (app user level) DH keypairs.
            This DH keypair is backed up in SDDS storage and all devices of an appuser will be able to access their self
            keypair from SDDS storage.
        sha256 (str): SHA256 of the original value.  This is stored mostly for achieving efficiency by client and
            server.  E.g. current value's sha256 sum can be matched with this value to know whether current value is
            different from the value stored in the keychain db.
    """

    id: int
    key: str
    encrypted: str
    sha256: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        key = self.key
        encrypted = self.encrypted
        sha256 = self.sha256

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "key": key,
                "encrypted": encrypted,
                "sha256": sha256,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        key = d.pop("key")

        encrypted = d.pop("encrypted")

        sha256 = d.pop("sha256")

        key_chain_multi_get_response = cls(
            id=id,
            key=key,
            encrypted=encrypted,
            sha256=sha256,
        )

        key_chain_multi_get_response.additional_properties = d
        return key_chain_multi_get_response

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
