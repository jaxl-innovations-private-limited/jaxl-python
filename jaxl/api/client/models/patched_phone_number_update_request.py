"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.ringing_strategy_enum import RingingStrategyEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patched_phone_number_update_request_frontdesk import (
        PatchedPhoneNumberUpdateRequestFrontdesk,
    )


T = TypeVar("T", bound="PatchedPhoneNumberUpdateRequest")


@attr.s(auto_attribs=True)
class PatchedPhoneNumberUpdateRequest:
    """OpenAPI request body for PATCH /v1/phonenumbers/{id}/.

    The view handles these keys itself (`ringing_strategy` is not a model
    field — it lives in OrganizationSetting), so this serializer keeps the
    generated client contract honest; it does not drive validation.

        Attributes:
            ivr (Union[Unset, None, int]): Optional IVR for all incoming calls to this number
            frontdesk (Union[Unset, None, PatchedPhoneNumberUpdateRequestFrontdesk]): Save front desk key
            ringing_strategy (Union[None, RingingStrategyEnum, Unset]): Per-number ringing strategy override (B2B only).
                null removes the override — runtime falls back to the default (BROADCAST).
    """

    ivr: Union[Unset, None, int] = UNSET
    frontdesk: Union[Unset, None, "PatchedPhoneNumberUpdateRequestFrontdesk"] = UNSET
    ringing_strategy: Union[None, RingingStrategyEnum, Unset] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ivr = self.ivr
        frontdesk: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.frontdesk, Unset):
            frontdesk = self.frontdesk.to_dict() if self.frontdesk else None

        ringing_strategy: Union[None, Unset, str]
        if isinstance(self.ringing_strategy, Unset):
            ringing_strategy = UNSET
        elif self.ringing_strategy is None:
            ringing_strategy = None

        elif isinstance(self.ringing_strategy, RingingStrategyEnum):
            ringing_strategy = UNSET
            if not isinstance(self.ringing_strategy, Unset):
                ringing_strategy = self.ringing_strategy.value

        else:
            ringing_strategy = self.ringing_strategy

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ivr is not UNSET:
            field_dict["ivr"] = ivr
        if frontdesk is not UNSET:
            field_dict["frontdesk"] = frontdesk
        if ringing_strategy is not UNSET:
            field_dict["ringing_strategy"] = ringing_strategy

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patched_phone_number_update_request_frontdesk import (
            PatchedPhoneNumberUpdateRequestFrontdesk,
        )

        d = src_dict.copy()
        ivr = d.pop("ivr", UNSET)

        _frontdesk = d.pop("frontdesk", UNSET)
        frontdesk: Union[Unset, None, PatchedPhoneNumberUpdateRequestFrontdesk]
        if _frontdesk is None:
            frontdesk = None
        elif isinstance(_frontdesk, Unset):
            frontdesk = UNSET
        else:
            frontdesk = PatchedPhoneNumberUpdateRequestFrontdesk.from_dict(_frontdesk)

        def _parse_ringing_strategy(
            data: object,
        ) -> Union[None, RingingStrategyEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _ringing_strategy_type_0 = data
                ringing_strategy_type_0: Union[Unset, RingingStrategyEnum]
                if isinstance(_ringing_strategy_type_0, Unset):
                    ringing_strategy_type_0 = UNSET
                else:
                    ringing_strategy_type_0 = RingingStrategyEnum(
                        _ringing_strategy_type_0
                    )

                return ringing_strategy_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, RingingStrategyEnum, Unset], data)

        ringing_strategy = _parse_ringing_strategy(d.pop("ringing_strategy", UNSET))

        patched_phone_number_update_request = cls(
            ivr=ivr,
            frontdesk=frontdesk,
            ringing_strategy=ringing_strategy,
        )

        patched_phone_number_update_request.additional_properties = d
        return patched_phone_number_update_request

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
