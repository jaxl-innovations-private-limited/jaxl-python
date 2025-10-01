"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_agent import UserAgent


T = TypeVar("T", bound="Connection")


@attr.s(auto_attribs=True)
class Connection:
    """Adds a 'jaxlid' field which contains signed ID information.

    Attributes:
        useragent (UserAgent):
        connected_on (datetime.datetime): Datetime when this connection was established
        disconnected_on (Union[Unset, None, datetime.datetime]): Datetime when this connection got disconnected
        jaxlid (Optional[str]):
    """

    useragent: "UserAgent"
    connected_on: datetime.datetime
    jaxlid: Optional[str]
    disconnected_on: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        useragent = self.useragent.to_dict()

        connected_on = self.connected_on.isoformat()

        disconnected_on: Union[Unset, None, str] = UNSET
        if not isinstance(self.disconnected_on, Unset):
            disconnected_on = (
                self.disconnected_on.isoformat() if self.disconnected_on else None
            )

        jaxlid = self.jaxlid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "useragent": useragent,
                "connected_on": connected_on,
                "jaxlid": jaxlid,
            }
        )
        if disconnected_on is not UNSET:
            field_dict["disconnected_on"] = disconnected_on

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_agent import UserAgent

        d = src_dict.copy()
        useragent = UserAgent.from_dict(d.pop("useragent"))

        connected_on = isoparse(d.pop("connected_on"))

        _disconnected_on = d.pop("disconnected_on", UNSET)
        disconnected_on: Union[Unset, None, datetime.datetime]
        if _disconnected_on is None:
            disconnected_on = None
        elif isinstance(_disconnected_on, Unset):
            disconnected_on = UNSET
        else:
            disconnected_on = isoparse(_disconnected_on)

        jaxlid = d.pop("jaxlid")

        connection = cls(
            useragent=useragent,
            connected_on=connected_on,
            disconnected_on=disconnected_on,
            jaxlid=jaxlid,
        )

        connection.additional_properties = d
        return connection

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
