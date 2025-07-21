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
    from ..models.user_identity_uploaded_data_request import (
        UserIdentityUploadedDataRequest,
    )


T = TypeVar("T", bound="UserIdentityCreationRequest")


@attr.s(auto_attribs=True)
class UserIdentityCreationRequest:
    """
    Attributes:
        payload (UserIdentityUploadedDataRequest):
        csek (Union[Unset, None, str]):
        signature (Union[Unset, None, str]):
    """

    payload: "UserIdentityUploadedDataRequest"
    csek: Union[Unset, None, str] = UNSET
    signature: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payload = self.payload.to_dict()

        csek = self.csek
        signature = self.signature

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payload": payload,
            }
        )
        if csek is not UNSET:
            field_dict["csek"] = csek
        if signature is not UNSET:
            field_dict["signature"] = signature

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_identity_uploaded_data_request import (
            UserIdentityUploadedDataRequest,
        )

        d = src_dict.copy()
        payload = UserIdentityUploadedDataRequest.from_dict(d.pop("payload"))

        csek = d.pop("csek", UNSET)

        signature = d.pop("signature", UNSET)

        user_identity_creation_request = cls(
            payload=payload,
            csek=csek,
            signature=signature,
        )

        user_identity_creation_request.additional_properties = d
        return user_identity_creation_request

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
