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
    from ..models.transport_packet_request import TransportPacketRequest


T = TypeVar("T", bound="DeviceTransportRequest")


@attr.s(auto_attribs=True)
class DeviceTransportRequest:
    """
    Attributes:
        timeout (Union[Unset, None, int]): Timeout when None means no timeout.  A value == 0 would mean, don't poll at
            all.  In such scenarios its important to provide a packet.  A positive value means, wait for timeout seconds
            expecting a transport push or response packet
        delay (Union[Unset, None, str]):
        request (Union[Unset, None, TransportPacketRequest]): Transport has a universal packet structure with following
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

    timeout: Union[Unset, None, int] = UNSET
    delay: Union[Unset, None, str] = UNSET
    request: Union[Unset, None, "TransportPacketRequest"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timeout = self.timeout
        delay = self.delay
        request: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.request, Unset):
            request = self.request.to_dict() if self.request else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if delay is not UNSET:
            field_dict["delay"] = delay
        if request is not UNSET:
            field_dict["request"] = request

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.transport_packet_request import TransportPacketRequest

        d = src_dict.copy()
        timeout = d.pop("timeout", UNSET)

        delay = d.pop("delay", UNSET)

        _request = d.pop("request", UNSET)
        request: Union[Unset, None, TransportPacketRequest]
        if _request is None:
            request = None
        elif isinstance(_request, Unset):
            request = UNSET
        else:
            request = TransportPacketRequest.from_dict(_request)

        device_transport_request = cls(
            timeout=timeout,
            delay=delay,
            request=request,
        )

        device_transport_request.additional_properties = d
        return device_transport_request

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
