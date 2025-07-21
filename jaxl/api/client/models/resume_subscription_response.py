"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar

import attr


T = TypeVar("T", bound="ResumeSubscriptionResponse")


@attr.s(auto_attribs=True)
class ResumeSubscriptionResponse:
    """
    Attributes:
        provider_plan_id (str):
        app_account_token (str):
        order_id (int):
    """

    provider_plan_id: str
    app_account_token: str
    order_id: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        provider_plan_id = self.provider_plan_id
        app_account_token = self.app_account_token
        order_id = self.order_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider_plan_id": provider_plan_id,
                "app_account_token": app_account_token,
                "order_id": order_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        provider_plan_id = d.pop("provider_plan_id")

        app_account_token = d.pop("app_account_token")

        order_id = d.pop("order_id")

        resume_subscription_response = cls(
            provider_plan_id=provider_plan_id,
            app_account_token=app_account_token,
            order_id=order_id,
        )

        resume_subscription_response.additional_properties = d
        return resume_subscription_response

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
