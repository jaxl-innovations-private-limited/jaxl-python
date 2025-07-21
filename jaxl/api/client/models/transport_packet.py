"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.t_enum import TEnum
from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.transport_packet_d import TransportPacketD


T = TypeVar("T", bound="TransportPacket")


@attr.s(auto_attribs=True)
class TransportPacket:
    """Transport has a universal packet structure with following specification:

    {
        "i": "... unique packet ID for this websocket connection ...",
        "t": "... type of packet, one of (request|response|push|ack) ...",
        "m": "... module which must handle this packet ...",
        "a": "... action to be taken by the module ...",
        "d": "... payload for module action ...",
    }

    NOTE:
    1) "response" type packets don't have "a" and "m" attributes defined.
       This is so because client already knows "a" and "m" from original request.

        Attributes:
            i (int): Integer ID for the packet. Response packet IDs matches corresponding request packet IDs
            t (TEnum):
            d (Union[Unset, None, TransportPacketD]): Optional payload associated with the packet
            m (Union[Unset, None, str]): Transport module name that must handle this packet
            a (Union[Unset, None, str]): Transport module action that must handle this packet
    """

    i: int
    t: TEnum
    d: Union[Unset, None, "TransportPacketD"] = UNSET
    m: Union[Unset, None, str] = UNSET
    a: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        i = self.i
        t = self.t.value

        d: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.d, Unset):
            d = self.d.to_dict() if self.d else None

        m = self.m
        a = self.a

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "i": i,
                "t": t,
            }
        )
        if d is not UNSET:
            field_dict["d"] = d
        if m is not UNSET:
            field_dict["m"] = m
        if a is not UNSET:
            field_dict["a"] = a

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.transport_packet_d import TransportPacketD

        d = src_dict.copy()
        i = d.pop("i")

        t = TEnum(d.pop("t"))

        __d = d.pop("d", UNSET)
        _d: Union[Unset, None, TransportPacketD]
        if __d is None:
            _d = None
        elif isinstance(__d, Unset):
            _d = UNSET
        else:
            _d = TransportPacketD.from_dict(__d)

        m = d.pop("m", UNSET)

        a = d.pop("a", UNSET)

        transport_packet = cls(
            i=i,
            t=t,
            d=_d,
            m=m,
            a=a,
        )

        transport_packet.additional_properties = d
        return transport_packet

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
