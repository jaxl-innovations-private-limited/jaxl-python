"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.key_chain_set_request import KeyChainSetRequest


T = TypeVar("T", bound="KeyChainMultiSetRequest")


@attr.s(auto_attribs=True)
class KeyChainMultiSetRequest:
    """
    Attributes:
        keyvalues (List['KeyChainSetRequest']):
    """

    keyvalues: List["KeyChainSetRequest"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        keyvalues = []
        for keyvalues_item_data in self.keyvalues:
            keyvalues_item = keyvalues_item_data.to_dict()

            keyvalues.append(keyvalues_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keyvalues": keyvalues,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.key_chain_set_request import KeyChainSetRequest

        d = src_dict.copy()
        keyvalues = []
        _keyvalues = d.pop("keyvalues")
        for keyvalues_item_data in _keyvalues:
            keyvalues_item = KeyChainSetRequest.from_dict(keyvalues_item_data)

            keyvalues.append(keyvalues_item)

        key_chain_multi_set_request = cls(
            keyvalues=keyvalues,
        )

        key_chain_multi_set_request.additional_properties = d
        return key_chain_multi_set_request

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
