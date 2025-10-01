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
    from ..models.next_or_cta_request import NextOrCTARequest


T = TypeVar("T", bound="IVROptionsRequest")


@attr.s(auto_attribs=True)
class IVROptionsRequest:
    """
    Attributes:
        name (str): Public name of this option
        input_ (str): Input required to visit this options sub-menu or invoke CTA
        next_or_cta (NextOrCTARequest):
        enabled (Union[Unset, bool]): Whether this object is currently enabled or disabled
        needs_data_prompt (Union[Unset, None, str]): Provide iff system must prompt user with the provided text for more
            input after they have chosen this option
        confirmation (Union[Unset, None, bool]): Whether to ask for confirmation to verify input data. Can only be
            enabled when needs_data_prompt is non-null.
        webhook_url (Union[Unset, None, str]): When provided, Jaxl IVR system will make a POST API on this URL, return
            200 OK to execute configure CTA, return any other response code to hangup the call.
    """

    name: str
    input_: str
    next_or_cta: "NextOrCTARequest"
    enabled: Union[Unset, bool] = UNSET
    needs_data_prompt: Union[Unset, None, str] = UNSET
    confirmation: Union[Unset, None, bool] = UNSET
    webhook_url: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        input_ = self.input_
        next_or_cta = self.next_or_cta.to_dict()

        enabled = self.enabled
        needs_data_prompt = self.needs_data_prompt
        confirmation = self.confirmation
        webhook_url = self.webhook_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "input": input_,
                "next_or_cta": next_or_cta,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if needs_data_prompt is not UNSET:
            field_dict["needs_data_prompt"] = needs_data_prompt
        if confirmation is not UNSET:
            field_dict["confirmation"] = confirmation
        if webhook_url is not UNSET:
            field_dict["webhook_url"] = webhook_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.next_or_cta_request import NextOrCTARequest

        d = src_dict.copy()
        name = d.pop("name")

        input_ = d.pop("input")

        next_or_cta = NextOrCTARequest.from_dict(d.pop("next_or_cta"))

        enabled = d.pop("enabled", UNSET)

        needs_data_prompt = d.pop("needs_data_prompt", UNSET)

        confirmation = d.pop("confirmation", UNSET)

        webhook_url = d.pop("webhook_url", UNSET)

        ivr_options_request = cls(
            name=name,
            input_=input_,
            next_or_cta=next_or_cta,
            enabled=enabled,
            needs_data_prompt=needs_data_prompt,
            confirmation=confirmation,
            webhook_url=webhook_url,
        )

        ivr_options_request.additional_properties = d
        return ivr_options_request

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
