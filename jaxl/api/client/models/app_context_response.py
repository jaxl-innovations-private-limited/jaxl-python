"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Optional,
    Type,
    TypeVar,
    Union,
)

import attr

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.jaxl_app_context_context import JaxlAppContextContext
    from ..models.jaxl_app_detail_context import JaxlAppDetailContext
    from ..models.jaxl_app_messaging_context import JaxlAppMessagingContext
    from ..models.jaxl_app_organization_context import (
        JaxlAppOrganizationContext,
    )
    from ..models.jaxl_app_pay_context import JaxlAppPayContext
    from ..models.jaxl_app_transport_context import JaxlAppTransportContext


T = TypeVar("T", bound="AppContextResponse")


@attr.s(auto_attribs=True)
class AppContextResponse:
    """
    Attributes:
        jaxl_app_detail (JaxlAppDetailContext):
        jaxl_app_context (JaxlAppContextContext):
        jaxl_transport_context (JaxlAppTransportContext):
        messaging_context (JaxlAppMessagingContext):
        pay_context (JaxlAppPayContext):
        static_url (Optional[str]):
        organization_context (Union[Unset, None, JaxlAppOrganizationContext]):
    """

    jaxl_app_detail: "JaxlAppDetailContext"
    jaxl_app_context: "JaxlAppContextContext"
    jaxl_transport_context: "JaxlAppTransportContext"
    messaging_context: "JaxlAppMessagingContext"
    pay_context: "JaxlAppPayContext"
    static_url: Optional[str]
    organization_context: Union[Unset, None, "JaxlAppOrganizationContext"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        jaxl_app_detail = self.jaxl_app_detail.to_dict()

        jaxl_app_context = self.jaxl_app_context.to_dict()

        jaxl_transport_context = self.jaxl_transport_context.to_dict()

        messaging_context = self.messaging_context.to_dict()

        pay_context = self.pay_context.to_dict()

        static_url = self.static_url
        organization_context: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.organization_context, Unset):
            organization_context = (
                self.organization_context.to_dict()
                if self.organization_context
                else None
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jaxl_app_detail": jaxl_app_detail,
                "jaxl_app_context": jaxl_app_context,
                "jaxl_transport_context": jaxl_transport_context,
                "messaging_context": messaging_context,
                "pay_context": pay_context,
                "static_url": static_url,
            }
        )
        if organization_context is not UNSET:
            field_dict["organization_context"] = organization_context

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.jaxl_app_context_context import JaxlAppContextContext
        from ..models.jaxl_app_detail_context import JaxlAppDetailContext
        from ..models.jaxl_app_messaging_context import JaxlAppMessagingContext
        from ..models.jaxl_app_organization_context import (
            JaxlAppOrganizationContext,
        )
        from ..models.jaxl_app_pay_context import JaxlAppPayContext
        from ..models.jaxl_app_transport_context import JaxlAppTransportContext

        d = src_dict.copy()
        jaxl_app_detail = JaxlAppDetailContext.from_dict(d.pop("jaxl_app_detail"))

        jaxl_app_context = JaxlAppContextContext.from_dict(d.pop("jaxl_app_context"))

        jaxl_transport_context = JaxlAppTransportContext.from_dict(
            d.pop("jaxl_transport_context")
        )

        messaging_context = JaxlAppMessagingContext.from_dict(
            d.pop("messaging_context")
        )

        pay_context = JaxlAppPayContext.from_dict(d.pop("pay_context"))

        static_url = d.pop("static_url")

        _organization_context = d.pop("organization_context", UNSET)
        organization_context: Union[Unset, None, JaxlAppOrganizationContext]
        if _organization_context is None:
            organization_context = None
        elif isinstance(_organization_context, Unset):
            organization_context = UNSET
        else:
            organization_context = JaxlAppOrganizationContext.from_dict(
                _organization_context
            )

        app_context_response = cls(
            jaxl_app_detail=jaxl_app_detail,
            jaxl_app_context=jaxl_app_context,
            jaxl_transport_context=jaxl_transport_context,
            messaging_context=messaging_context,
            pay_context=pay_context,
            static_url=static_url,
            organization_context=organization_context,
        )

        app_context_response.additional_properties = d
        return app_context_response

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
