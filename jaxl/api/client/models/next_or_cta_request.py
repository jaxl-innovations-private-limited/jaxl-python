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
    from ..models.cta_request import CTARequest


T = TypeVar("T", bound="NextOrCTARequest")


@attr.s(auto_attribs=True)
class NextOrCTARequest:
    """
    Attributes:
        next_ (Union[Unset, None, int]):
        cta (Union[Unset, None, CTARequest]):
    """

    next_: Union[Unset, None, int] = UNSET
    cta: Union[Unset, None, "CTARequest"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        next_ = self.next_
        cta: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.cta, Unset):
            cta = self.cta.to_dict() if self.cta else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_ is not UNSET:
            field_dict["next"] = next_
        if cta is not UNSET:
            field_dict["cta"] = cta

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cta_request import CTARequest

        d = src_dict.copy()
        next_ = d.pop("next", UNSET)

        _cta = d.pop("cta", UNSET)
        cta: Union[Unset, None, CTARequest]
        if _cta is None:
            cta = None
        elif isinstance(_cta, Unset):
            cta = UNSET
        else:
            cta = CTARequest.from_dict(_cta)

        next_or_cta_request = cls(
            next_=next_,
            cta=cta,
        )

        next_or_cta_request.additional_properties = d
        return next_or_cta_request

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
