"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Optional, Type, TypeVar

import attr


T = TypeVar("T", bound="JaxlAppTransportContext")


@attr.s(auto_attribs=True)
class JaxlAppTransportContext:
    """
    Attributes:
        url (str):
        addr (str):
        ticket (Optional[str]):
    """

    url: str
    addr: str
    ticket: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        addr = self.addr
        ticket = self.ticket

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "addr": addr,
                "ticket": ticket,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        addr = d.pop("addr")

        ticket = d.pop("ticket")

        jaxl_app_transport_context = cls(
            url=url,
            addr=addr,
            ticket=ticket,
        )

        jaxl_app_transport_context.additional_properties = d
        return jaxl_app_transport_context

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
