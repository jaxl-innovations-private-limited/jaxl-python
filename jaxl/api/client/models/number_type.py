"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.provider_pricing import ProviderPricing


T = TypeVar("T", bound="NumberType")


@attr.s(auto_attribs=True)
class NumberType:
    """
    Attributes:
        monthly (ProviderPricing):
        quarterly (ProviderPricing):
        half_yearly (ProviderPricing):
        yearly (ProviderPricing):
        sms (bool):
        voice (bool):
        recording (bool):
        incoming_per_min (Optional[float]):
        incoming_sms_price (Optional[float]):
        outgoing_sms_price_min (Optional[float]):
        outgoing_sms_price_max (Optional[float]):
        recording_price (Optional[float]):
    """

    monthly: "ProviderPricing"
    quarterly: "ProviderPricing"
    half_yearly: "ProviderPricing"
    yearly: "ProviderPricing"
    sms: bool
    voice: bool
    recording: bool
    incoming_per_min: Optional[float]
    incoming_sms_price: Optional[float]
    outgoing_sms_price_min: Optional[float]
    outgoing_sms_price_max: Optional[float]
    recording_price: Optional[float]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        monthly = self.monthly.to_dict()

        quarterly = self.quarterly.to_dict()

        half_yearly = self.half_yearly.to_dict()

        yearly = self.yearly.to_dict()

        sms = self.sms
        voice = self.voice
        recording = self.recording
        incoming_per_min = self.incoming_per_min
        incoming_sms_price = self.incoming_sms_price
        outgoing_sms_price_min = self.outgoing_sms_price_min
        outgoing_sms_price_max = self.outgoing_sms_price_max
        recording_price = self.recording_price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "monthly": monthly,
                "quarterly": quarterly,
                "half_yearly": half_yearly,
                "yearly": yearly,
                "sms": sms,
                "voice": voice,
                "recording": recording,
                "incoming_per_min": incoming_per_min,
                "incoming_sms_price": incoming_sms_price,
                "outgoing_sms_price_min": outgoing_sms_price_min,
                "outgoing_sms_price_max": outgoing_sms_price_max,
                "recording_price": recording_price,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.provider_pricing import ProviderPricing

        d = src_dict.copy()
        monthly = ProviderPricing.from_dict(d.pop("monthly"))

        quarterly = ProviderPricing.from_dict(d.pop("quarterly"))

        half_yearly = ProviderPricing.from_dict(d.pop("half_yearly"))

        yearly = ProviderPricing.from_dict(d.pop("yearly"))

        sms = d.pop("sms")

        voice = d.pop("voice")

        recording = d.pop("recording")

        incoming_per_min = d.pop("incoming_per_min")

        incoming_sms_price = d.pop("incoming_sms_price")

        outgoing_sms_price_min = d.pop("outgoing_sms_price_min")

        outgoing_sms_price_max = d.pop("outgoing_sms_price_max")

        recording_price = d.pop("recording_price")

        number_type = cls(
            monthly=monthly,
            quarterly=quarterly,
            half_yearly=half_yearly,
            yearly=yearly,
            sms=sms,
            voice=voice,
            recording=recording,
            incoming_per_min=incoming_per_min,
            incoming_sms_price=incoming_sms_price,
            outgoing_sms_price_min=outgoing_sms_price_min,
            outgoing_sms_price_max=outgoing_sms_price_max,
            recording_price=recording_price,
        )

        number_type.additional_properties = d
        return number_type

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
