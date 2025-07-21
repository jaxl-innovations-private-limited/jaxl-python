"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset


T = TypeVar("T", bound="VerifyTokenRequest")


@attr.s(auto_attribs=True)
class VerifyTokenRequest:
    """
    Attributes:
        token (str):
        ticket (Union[Unset, None, str]):
        check_parent (Union[Unset, None, bool]):
    """

    token: str
    ticket: Union[Unset, None, str] = UNSET
    check_parent: Union[Unset, None, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token = self.token
        ticket = self.ticket
        check_parent = self.check_parent

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
            }
        )
        if ticket is not UNSET:
            field_dict["ticket"] = ticket
        if check_parent is not UNSET:
            field_dict["check_parent"] = check_parent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token")

        ticket = d.pop("ticket", UNSET)

        check_parent = d.pop("check_parent", UNSET)

        verify_token_request = cls(
            token=token,
            ticket=ticket,
            check_parent=check_parent,
        )

        verify_token_request.additional_properties = d
        return verify_token_request

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
