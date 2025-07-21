"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.transport_token import TransportToken


T = TypeVar("T", bound="VerifyResponse")


@attr.s(auto_attribs=True)
class VerifyResponse:
    """
    Attributes:
        verified (bool):
        signature (Union[Unset, None, str]):
        transport (Union[Unset, None, TransportToken]):
        identifier (Union[Unset, None, str]):
        app_user_id (Union[Unset, None, int]):
    """

    verified: bool
    signature: Union[Unset, None, str] = UNSET
    transport: Union[Unset, None, "TransportToken"] = UNSET
    identifier: Union[Unset, None, str] = UNSET
    app_user_id: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        verified = self.verified
        signature = self.signature
        transport: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.transport, Unset):
            transport = self.transport.to_dict() if self.transport else None

        identifier = self.identifier
        app_user_id = self.app_user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "verified": verified,
            }
        )
        if signature is not UNSET:
            field_dict["signature"] = signature
        if transport is not UNSET:
            field_dict["transport"] = transport
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if app_user_id is not UNSET:
            field_dict["app_user_id"] = app_user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.transport_token import TransportToken

        d = src_dict.copy()
        verified = d.pop("verified")

        signature = d.pop("signature", UNSET)

        _transport = d.pop("transport", UNSET)
        transport: Union[Unset, None, TransportToken]
        if _transport is None:
            transport = None
        elif isinstance(_transport, Unset):
            transport = UNSET
        else:
            transport = TransportToken.from_dict(_transport)

        identifier = d.pop("identifier", UNSET)

        app_user_id = d.pop("app_user_id", UNSET)

        verify_response = cls(
            verified=verified,
            signature=signature,
            transport=transport,
            identifier=identifier,
            app_user_id=app_user_id,
        )

        verify_response.additional_properties = d
        return verify_response

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
