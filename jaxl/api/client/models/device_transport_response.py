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
    from ..models.transport_packet import TransportPacket


T = TypeVar("T", bound="DeviceTransportResponse")


@attr.s(auto_attribs=True)
class DeviceTransportResponse:
    """
    Attributes:
        packet (TransportPacket): Transport has a universal packet structure with following specification:

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
        response (Union[Unset, None, TransportPacket]): Transport has a universal packet structure with following
            specification:

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
    """

    packet: "TransportPacket"
    response: Union[Unset, None, "TransportPacket"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        packet = self.packet.to_dict()

        response: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.response, Unset):
            response = self.response.to_dict() if self.response else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "packet": packet,
            }
        )
        if response is not UNSET:
            field_dict["response"] = response

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.transport_packet import TransportPacket

        d = src_dict.copy()
        packet = TransportPacket.from_dict(d.pop("packet"))

        _response = d.pop("response", UNSET)
        response: Union[Unset, None, TransportPacket]
        if _response is None:
            response = None
        elif isinstance(_response, Unset):
            response = UNSET
        else:
            response = TransportPacket.from_dict(_response)

        device_transport_response = cls(
            packet=packet,
            response=response,
        )

        device_transport_response.additional_properties = d
        return device_transport_response

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
