"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Capabilities")


@attr.s(auto_attribs=True)
class Capabilities:
    """
    Attributes:
        sms_enabled (Union[Unset, None, bool]):
        sms_price (Union[Unset, None, float]):
        incoming_price (Union[Unset, None, float]):
        outgoing_price (Union[Unset, None, float]):
        voice_enabled (Union[Unset, None, bool]):
        recording_enabled (Union[Unset, None, bool]):
        recording_price (Union[Unset, None, float]):
    """

    sms_enabled: Union[Unset, None, bool] = UNSET
    sms_price: Union[Unset, None, float] = UNSET
    incoming_price: Union[Unset, None, float] = UNSET
    outgoing_price: Union[Unset, None, float] = UNSET
    voice_enabled: Union[Unset, None, bool] = UNSET
    recording_enabled: Union[Unset, None, bool] = UNSET
    recording_price: Union[Unset, None, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sms_enabled = self.sms_enabled
        sms_price = self.sms_price
        incoming_price = self.incoming_price
        outgoing_price = self.outgoing_price
        voice_enabled = self.voice_enabled
        recording_enabled = self.recording_enabled
        recording_price = self.recording_price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sms_enabled is not UNSET:
            field_dict["sms_enabled"] = sms_enabled
        if sms_price is not UNSET:
            field_dict["sms_price"] = sms_price
        if incoming_price is not UNSET:
            field_dict["incoming_price"] = incoming_price
        if outgoing_price is not UNSET:
            field_dict["outgoing_price"] = outgoing_price
        if voice_enabled is not UNSET:
            field_dict["voice_enabled"] = voice_enabled
        if recording_enabled is not UNSET:
            field_dict["recording_enabled"] = recording_enabled
        if recording_price is not UNSET:
            field_dict["recording_price"] = recording_price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sms_enabled = d.pop("sms_enabled", UNSET)

        sms_price = d.pop("sms_price", UNSET)

        incoming_price = d.pop("incoming_price", UNSET)

        outgoing_price = d.pop("outgoing_price", UNSET)

        voice_enabled = d.pop("voice_enabled", UNSET)

        recording_enabled = d.pop("recording_enabled", UNSET)

        recording_price = d.pop("recording_price", UNSET)

        capabilities = cls(
            sms_enabled=sms_enabled,
            sms_price=sms_price,
            incoming_price=incoming_price,
            outgoing_price=outgoing_price,
            voice_enabled=voice_enabled,
            recording_enabled=recording_enabled,
            recording_price=recording_price,
        )

        capabilities.additional_properties = d
        return capabilities

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
