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
    from ..models.provider_notes import ProviderNotes
    from ..models.razor_pay_config import RazorPayConfig
    from ..models.razor_pay_model import RazorPayModel
    from ..models.razor_pay_read_only import RazorPayReadOnly
    from ..models.razor_pay_retry import RazorPayRetry


T = TypeVar("T", bound="RazorPayCheckoutOptions")


@attr.s(auto_attribs=True)
class RazorPayCheckoutOptions:
    """
    Attributes:
        provider (str):
        key (str):
        name (str):
        description (str):
        remember_customer (bool):
        notes (ProviderNotes):
        callback_url (str):
        modal (RazorPayModel):
        retry (RazorPayRetry):
        order_id (Union[Unset, str]):
        customer_id (Union[Unset, str]):
        provider_order_id (Union[Unset, str]):
        readonly (Union[Unset, RazorPayReadOnly]):
        config (Union[Unset, RazorPayConfig]):
    """

    provider: str
    key: str
    name: str
    description: str
    remember_customer: bool
    notes: "ProviderNotes"
    callback_url: str
    modal: "RazorPayModel"
    retry: "RazorPayRetry"
    order_id: Union[Unset, str] = UNSET
    customer_id: Union[Unset, str] = UNSET
    provider_order_id: Union[Unset, str] = UNSET
    readonly: Union[Unset, "RazorPayReadOnly"] = UNSET
    config: Union[Unset, "RazorPayConfig"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        provider = self.provider
        key = self.key
        name = self.name
        description = self.description
        remember_customer = self.remember_customer
        notes = self.notes.to_dict()

        callback_url = self.callback_url
        modal = self.modal.to_dict()

        retry = self.retry.to_dict()

        order_id = self.order_id
        customer_id = self.customer_id
        provider_order_id = self.provider_order_id
        readonly: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.readonly, Unset):
            readonly = self.readonly.to_dict()

        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "key": key,
                "name": name,
                "description": description,
                "remember_customer": remember_customer,
                "notes": notes,
                "callback_url": callback_url,
                "modal": modal,
                "retry": retry,
            }
        )
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if customer_id is not UNSET:
            field_dict["customer_id"] = customer_id
        if provider_order_id is not UNSET:
            field_dict["provider_order_id"] = provider_order_id
        if readonly is not UNSET:
            field_dict["readonly"] = readonly
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.provider_notes import ProviderNotes
        from ..models.razor_pay_config import RazorPayConfig
        from ..models.razor_pay_model import RazorPayModel
        from ..models.razor_pay_read_only import RazorPayReadOnly
        from ..models.razor_pay_retry import RazorPayRetry

        d = src_dict.copy()
        provider = d.pop("provider")

        key = d.pop("key")

        name = d.pop("name")

        description = d.pop("description")

        remember_customer = d.pop("remember_customer")

        notes = ProviderNotes.from_dict(d.pop("notes"))

        callback_url = d.pop("callback_url")

        modal = RazorPayModel.from_dict(d.pop("modal"))

        retry = RazorPayRetry.from_dict(d.pop("retry"))

        order_id = d.pop("order_id", UNSET)

        customer_id = d.pop("customer_id", UNSET)

        provider_order_id = d.pop("provider_order_id", UNSET)

        _readonly = d.pop("readonly", UNSET)
        readonly: Union[Unset, RazorPayReadOnly]
        if isinstance(_readonly, Unset):
            readonly = UNSET
        else:
            readonly = RazorPayReadOnly.from_dict(_readonly)

        _config = d.pop("config", UNSET)
        config: Union[Unset, RazorPayConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = RazorPayConfig.from_dict(_config)

        razor_pay_checkout_options = cls(
            provider=provider,
            key=key,
            name=name,
            description=description,
            remember_customer=remember_customer,
            notes=notes,
            callback_url=callback_url,
            modal=modal,
            retry=retry,
            order_id=order_id,
            customer_id=customer_id,
            provider_order_id=provider_order_id,
            readonly=readonly,
            config=config,
        )

        razor_pay_checkout_options.additional_properties = d
        return razor_pay_checkout_options

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
