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


T = TypeVar("T", bound="PatchedIVROptionsUpdateRequest")


@attr.s(auto_attribs=True)
class PatchedIVROptionsUpdateRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        enabled (Union[Unset, bool]): Whether this object is currently enabled or disabled
        needs_data_prompt (Union[Unset, None, str]): Provide iff system must prompt user with the provided text for more
            input after they have chosen this option
        next_or_cta (Union[Unset, NextOrCTARequest]):
        confirmation (Union[Unset, None, bool]): Whether to ask for confirmation to verify input data. Can only be
            enabled when needs_data_prompt is non-null.
        webhook_url (Union[Unset, None, str]): When provided, Jaxl IVR system will make a POST API on this URL, return
            200 OK to execute configure CTA, return any other response code to hangup the call.
    """

    name: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    needs_data_prompt: Union[Unset, None, str] = UNSET
    next_or_cta: Union[Unset, "NextOrCTARequest"] = UNSET
    confirmation: Union[Unset, None, bool] = UNSET
    webhook_url: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        enabled = self.enabled
        needs_data_prompt = self.needs_data_prompt
        next_or_cta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.next_or_cta, Unset):
            next_or_cta = self.next_or_cta.to_dict()

        confirmation = self.confirmation
        webhook_url = self.webhook_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if needs_data_prompt is not UNSET:
            field_dict["needs_data_prompt"] = needs_data_prompt
        if next_or_cta is not UNSET:
            field_dict["next_or_cta"] = next_or_cta
        if confirmation is not UNSET:
            field_dict["confirmation"] = confirmation
        if webhook_url is not UNSET:
            field_dict["webhook_url"] = webhook_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.next_or_cta_request import NextOrCTARequest

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        enabled = d.pop("enabled", UNSET)

        needs_data_prompt = d.pop("needs_data_prompt", UNSET)

        _next_or_cta = d.pop("next_or_cta", UNSET)
        next_or_cta: Union[Unset, NextOrCTARequest]
        if isinstance(_next_or_cta, Unset):
            next_or_cta = UNSET
        else:
            next_or_cta = NextOrCTARequest.from_dict(_next_or_cta)

        confirmation = d.pop("confirmation", UNSET)

        webhook_url = d.pop("webhook_url", UNSET)

        patched_ivr_options_update_request = cls(
            name=name,
            enabled=enabled,
            needs_data_prompt=needs_data_prompt,
            next_or_cta=next_or_cta,
            confirmation=confirmation,
            webhook_url=webhook_url,
        )

        patched_ivr_options_update_request.additional_properties = d
        return patched_ivr_options_update_request

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
