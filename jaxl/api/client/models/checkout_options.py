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
    from ..models.razor_pay_checkout_options import RazorPayCheckoutOptions


T = TypeVar("T", bound="CheckoutOptions")


@attr.s(auto_attribs=True)
class CheckoutOptions:
    """
    Attributes:
        provider_plan_id (str):
        url (Union[Unset, str]):
        app_account_token (Union[Unset, str]):
        provider_payload (Union[Unset, RazorPayCheckoutOptions]):
    """

    provider_plan_id: str
    url: Union[Unset, str] = UNSET
    app_account_token: Union[Unset, str] = UNSET
    provider_payload: Union[Unset, "RazorPayCheckoutOptions"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        provider_plan_id = self.provider_plan_id
        url = self.url
        app_account_token = self.app_account_token
        provider_payload: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.provider_payload, Unset):
            provider_payload = self.provider_payload.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider_plan_id": provider_plan_id,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if app_account_token is not UNSET:
            field_dict["app_account_token"] = app_account_token
        if provider_payload is not UNSET:
            field_dict["provider_payload"] = provider_payload

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.razor_pay_checkout_options import RazorPayCheckoutOptions

        d = src_dict.copy()
        provider_plan_id = d.pop("provider_plan_id")

        url = d.pop("url", UNSET)

        app_account_token = d.pop("app_account_token", UNSET)

        _provider_payload = d.pop("provider_payload", UNSET)
        provider_payload: Union[Unset, RazorPayCheckoutOptions]
        if isinstance(_provider_payload, Unset):
            provider_payload = UNSET
        else:
            provider_payload = RazorPayCheckoutOptions.from_dict(_provider_payload)

        checkout_options = cls(
            provider_plan_id=provider_plan_id,
            url=url,
            app_account_token=app_account_token,
            provider_payload=provider_payload,
        )

        checkout_options.additional_properties = d
        return checkout_options

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
