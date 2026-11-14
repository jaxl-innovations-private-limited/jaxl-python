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
    from ..models.cta import CTA


T = TypeVar("T", bound="IVROptionsResponse")


@attr.s(auto_attribs=True)
class IVROptionsResponse:
    """
    Attributes:
        id (int):
        name (str): Public name of this option
        menu (int): IVR Menu to which this option belongs to
        input_ (str): Input required to visit this options sub-menu or invoke CTA
        enabled (bool):
        next_ (Union[Unset, None, int]): Optionally, next menu to present after receiving input
        cta (Union[Unset, CTA]):
        needs_data_prompt (Union[Unset, None, str]): Provide iff system must prompt user with the provided text for more
            input after they have chosen this option
        confirmation (Union[Unset, None, bool]): Whether to ask for confirmation to verify input data. Can only be
            enabled when needs_data_prompt is non-null.
        webhook_url (Union[Unset, None, str]): When provided, Jaxl IVR system will make a POST API on this URL, return
            200 OK to execute configure CTA, return any other response code to hangup the call.
    """

    id: int
    name: str
    menu: int
    input_: str
    enabled: bool
    next_: Union[Unset, None, int] = UNSET
    cta: Union[Unset, "CTA"] = UNSET
    needs_data_prompt: Union[Unset, None, str] = UNSET
    confirmation: Union[Unset, None, bool] = UNSET
    webhook_url: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        menu = self.menu
        input_ = self.input_
        enabled = self.enabled
        next_ = self.next_
        cta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cta, Unset):
            cta = self.cta.to_dict()

        needs_data_prompt = self.needs_data_prompt
        confirmation = self.confirmation
        webhook_url = self.webhook_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "menu": menu,
                "input": input_,
                "enabled": enabled,
            }
        )
        if next_ is not UNSET:
            field_dict["next"] = next_
        if cta is not UNSET:
            field_dict["cta"] = cta
        if needs_data_prompt is not UNSET:
            field_dict["needs_data_prompt"] = needs_data_prompt
        if confirmation is not UNSET:
            field_dict["confirmation"] = confirmation
        if webhook_url is not UNSET:
            field_dict["webhook_url"] = webhook_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cta import CTA

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        menu = d.pop("menu")

        input_ = d.pop("input")

        enabled = d.pop("enabled")

        next_ = d.pop("next", UNSET)

        _cta = d.pop("cta", UNSET)
        cta: Union[Unset, CTA]
        if isinstance(_cta, Unset) or _cta is None:
            cta = UNSET
        else:
            cta = CTA.from_dict(_cta)

        needs_data_prompt = d.pop("needs_data_prompt", UNSET)

        confirmation = d.pop("confirmation", UNSET)

        webhook_url = d.pop("webhook_url", UNSET)

        ivr_options_response = cls(
            id=id,
            name=name,
            menu=menu,
            input_=input_,
            enabled=enabled,
            next_=next_,
            cta=cta,
            needs_data_prompt=needs_data_prompt,
            confirmation=confirmation,
            webhook_url=webhook_url,
        )

        ivr_options_response.additional_properties = d
        return ivr_options_response

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
