"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.campaign_update_status_enum import CampaignUpdateStatusEnum
from ..types import UNSET, Unset


T = TypeVar("T", bound="PatchedCampaignUpdateRequest")


@attr.s(auto_attribs=True)
class PatchedCampaignUpdateRequest:
    """
    Attributes:
        status (Union[Unset, CampaignUpdateStatusEnum]):
        recharge (Union[Unset, str]):
        currency (Union[Unset, int]):
    """

    status: Union[Unset, CampaignUpdateStatusEnum] = UNSET
    recharge: Union[Unset, str] = UNSET
    currency: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        recharge = self.recharge
        currency = self.currency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if recharge is not UNSET:
            field_dict["recharge"] = recharge
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, CampaignUpdateStatusEnum]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CampaignUpdateStatusEnum(_status)

        recharge = d.pop("recharge", UNSET)

        currency = d.pop("currency", UNSET)

        patched_campaign_update_request = cls(
            status=status,
            recharge=recharge,
            currency=currency,
        )

        patched_campaign_update_request.additional_properties = d
        return patched_campaign_update_request

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
