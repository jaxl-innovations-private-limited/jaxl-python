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


T = TypeVar("T", bound="IVRState")


@attr.s(auto_attribs=True)
class IVRState:
    """
    Attributes:
        timeout_url (str):
        url (Union[Unset, None, str]):
        cta (Union[Unset, None, CTA]):
        wait_for (Union[Unset, None, str]):
        min_input_character_length (Union[Unset, None, int]):
    """

    timeout_url: str
    url: Union[Unset, None, str] = UNSET
    cta: Union[Unset, None, "CTA"] = UNSET
    wait_for: Union[Unset, None, str] = UNSET
    min_input_character_length: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timeout_url = self.timeout_url
        url = self.url
        cta: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.cta, Unset):
            cta = self.cta.to_dict() if self.cta else None

        wait_for = self.wait_for
        min_input_character_length = self.min_input_character_length

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timeout_url": timeout_url,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if cta is not UNSET:
            field_dict["cta"] = cta
        if wait_for is not UNSET:
            field_dict["wait_for"] = wait_for
        if min_input_character_length is not UNSET:
            field_dict["min_input_character_length"] = min_input_character_length

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cta import CTA

        d = src_dict.copy()
        timeout_url = d.pop("timeout_url")

        url = d.pop("url", UNSET)

        _cta = d.pop("cta", UNSET)
        cta: Union[Unset, None, CTA]
        if _cta is None:
            cta = None
        elif isinstance(_cta, Unset):
            cta = UNSET
        else:
            cta = CTA.from_dict(_cta)

        wait_for = d.pop("wait_for", UNSET)

        min_input_character_length = d.pop("min_input_character_length", UNSET)

        ivr_state = cls(
            timeout_url=timeout_url,
            url=url,
            cta=cta,
            wait_for=wait_for,
            min_input_character_length=min_input_character_length,
        )

        ivr_state.additional_properties = d
        return ivr_state

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
