"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExotelAuthRequestRequest")


@attr.s(auto_attribs=True)
class ExotelAuthRequestRequest:
    """
    Attributes:
        api_key (Union[Unset, None, str]):
        api_token (Union[Unset, None, str]):
        tenant_id (Union[Unset, None, str]):
        flow_id (Union[Unset, None, int]):
    """

    api_key: Union[Unset, None, str] = UNSET
    api_token: Union[Unset, None, str] = UNSET
    tenant_id: Union[Unset, None, str] = UNSET
    flow_id: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api_key = self.api_key
        api_token = self.api_token
        tenant_id = self.tenant_id
        flow_id = self.flow_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if api_token is not UNSET:
            field_dict["api_token"] = api_token
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id
        if flow_id is not UNSET:
            field_dict["flow_id"] = flow_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        api_key = d.pop("api_key", UNSET)

        api_token = d.pop("api_token", UNSET)

        tenant_id = d.pop("tenant_id", UNSET)

        flow_id = d.pop("flow_id", UNSET)

        exotel_auth_request_request = cls(
            api_key=api_key,
            api_token=api_token,
            tenant_id=tenant_id,
            flow_id=flow_id,
        )

        exotel_auth_request_request.additional_properties = d
        return exotel_auth_request_request

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
