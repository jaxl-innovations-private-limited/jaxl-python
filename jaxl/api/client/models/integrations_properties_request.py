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
    from ..models.exotel_auth_request_request import ExotelAuthRequestRequest
    from ..models.kwik_engage_auth_request_request import KwikEngageAuthRequestRequest
    from ..models.nimbus_post_auth_request_request import NimbusPostAuthRequestRequest
    from ..models.sales_max_auth_request_request import SalesMaxAuthRequestRequest
    from ..models.shiprocket_delivery_auth_request_request import (
        ShiprocketDeliveryAuthRequestRequest,
    )
    from ..models.shopify_auth_request_request import ShopifyAuthRequestRequest
    from ..models.stripe_auth_request_request import StripeAuthRequestRequest
    from ..models.twilio_call_auth_request_request import TwilioCallAuthRequestRequest


T = TypeVar("T", bound="IntegrationsPropertiesRequest")


@attr.s(auto_attribs=True)
class IntegrationsPropertiesRequest:
    """
    Attributes:
        shopify (Union[Unset, None, ShopifyAuthRequestRequest]):
        exotel (Union[Unset, None, ExotelAuthRequestRequest]):
        stripe (Union[Unset, None, StripeAuthRequestRequest]):
        shiprocket (Union[Unset, None, ShopifyAuthRequestRequest]):
        nimbuspost (Union[Unset, None, NimbusPostAuthRequestRequest]):
        salesmax (Union[Unset, None, SalesMaxAuthRequestRequest]):
        kwik_engage (Union[Unset, None, KwikEngageAuthRequestRequest]):
        twilio (Union[Unset, None, TwilioCallAuthRequestRequest]): F-171 BYO call provider: the org's OWN Twilio
            account.
        shiprocket_delivery (Union[Unset, None, ShiprocketDeliveryAuthRequestRequest]): Push-only from Shiprocket's side
            -- no credentials are needed to
            receive the webhook, just a URL pasted into their dashboard.
            webhook_secret is reserved for future signature verification.
    """

    shopify: Union[Unset, None, "ShopifyAuthRequestRequest"] = UNSET
    exotel: Union[Unset, None, "ExotelAuthRequestRequest"] = UNSET
    stripe: Union[Unset, None, "StripeAuthRequestRequest"] = UNSET
    shiprocket: Union[Unset, None, "ShopifyAuthRequestRequest"] = UNSET
    nimbuspost: Union[Unset, None, "NimbusPostAuthRequestRequest"] = UNSET
    salesmax: Union[Unset, None, "SalesMaxAuthRequestRequest"] = UNSET
    kwik_engage: Union[Unset, None, "KwikEngageAuthRequestRequest"] = UNSET
    twilio: Union[Unset, None, "TwilioCallAuthRequestRequest"] = UNSET
    shiprocket_delivery: Union[Unset, None, "ShiprocketDeliveryAuthRequestRequest"] = (
        UNSET
    )
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shopify: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.shopify, Unset):
            shopify = self.shopify.to_dict() if self.shopify else None

        exotel: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.exotel, Unset):
            exotel = self.exotel.to_dict() if self.exotel else None

        stripe: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.stripe, Unset):
            stripe = self.stripe.to_dict() if self.stripe else None

        shiprocket: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.shiprocket, Unset):
            shiprocket = self.shiprocket.to_dict() if self.shiprocket else None

        nimbuspost: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.nimbuspost, Unset):
            nimbuspost = self.nimbuspost.to_dict() if self.nimbuspost else None

        salesmax: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.salesmax, Unset):
            salesmax = self.salesmax.to_dict() if self.salesmax else None

        kwik_engage: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.kwik_engage, Unset):
            kwik_engage = self.kwik_engage.to_dict() if self.kwik_engage else None

        twilio: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.twilio, Unset):
            twilio = self.twilio.to_dict() if self.twilio else None

        shiprocket_delivery: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.shiprocket_delivery, Unset):
            shiprocket_delivery = (
                self.shiprocket_delivery.to_dict() if self.shiprocket_delivery else None
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shopify is not UNSET:
            field_dict["shopify"] = shopify
        if exotel is not UNSET:
            field_dict["exotel"] = exotel
        if stripe is not UNSET:
            field_dict["stripe"] = stripe
        if shiprocket is not UNSET:
            field_dict["shiprocket"] = shiprocket
        if nimbuspost is not UNSET:
            field_dict["nimbuspost"] = nimbuspost
        if salesmax is not UNSET:
            field_dict["salesmax"] = salesmax
        if kwik_engage is not UNSET:
            field_dict["kwik_engage"] = kwik_engage
        if twilio is not UNSET:
            field_dict["twilio"] = twilio
        if shiprocket_delivery is not UNSET:
            field_dict["shiprocket_delivery"] = shiprocket_delivery

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.exotel_auth_request_request import ExotelAuthRequestRequest
        from ..models.kwik_engage_auth_request_request import (
            KwikEngageAuthRequestRequest,
        )
        from ..models.nimbus_post_auth_request_request import (
            NimbusPostAuthRequestRequest,
        )
        from ..models.sales_max_auth_request_request import SalesMaxAuthRequestRequest
        from ..models.shiprocket_delivery_auth_request_request import (
            ShiprocketDeliveryAuthRequestRequest,
        )
        from ..models.shopify_auth_request_request import ShopifyAuthRequestRequest
        from ..models.stripe_auth_request_request import StripeAuthRequestRequest
        from ..models.twilio_call_auth_request_request import (
            TwilioCallAuthRequestRequest,
        )

        d = src_dict.copy()
        _shopify = d.pop("shopify", UNSET)
        shopify: Union[Unset, None, ShopifyAuthRequestRequest]
        if _shopify is None:
            shopify = None
        elif isinstance(_shopify, Unset):
            shopify = UNSET
        else:
            shopify = ShopifyAuthRequestRequest.from_dict(_shopify)

        _exotel = d.pop("exotel", UNSET)
        exotel: Union[Unset, None, ExotelAuthRequestRequest]
        if _exotel is None:
            exotel = None
        elif isinstance(_exotel, Unset):
            exotel = UNSET
        else:
            exotel = ExotelAuthRequestRequest.from_dict(_exotel)

        _stripe = d.pop("stripe", UNSET)
        stripe: Union[Unset, None, StripeAuthRequestRequest]
        if _stripe is None:
            stripe = None
        elif isinstance(_stripe, Unset):
            stripe = UNSET
        else:
            stripe = StripeAuthRequestRequest.from_dict(_stripe)

        _shiprocket = d.pop("shiprocket", UNSET)
        shiprocket: Union[Unset, None, ShopifyAuthRequestRequest]
        if _shiprocket is None:
            shiprocket = None
        elif isinstance(_shiprocket, Unset):
            shiprocket = UNSET
        else:
            shiprocket = ShopifyAuthRequestRequest.from_dict(_shiprocket)

        _nimbuspost = d.pop("nimbuspost", UNSET)
        nimbuspost: Union[Unset, None, NimbusPostAuthRequestRequest]
        if _nimbuspost is None:
            nimbuspost = None
        elif isinstance(_nimbuspost, Unset):
            nimbuspost = UNSET
        else:
            nimbuspost = NimbusPostAuthRequestRequest.from_dict(_nimbuspost)

        _salesmax = d.pop("salesmax", UNSET)
        salesmax: Union[Unset, None, SalesMaxAuthRequestRequest]
        if _salesmax is None:
            salesmax = None
        elif isinstance(_salesmax, Unset):
            salesmax = UNSET
        else:
            salesmax = SalesMaxAuthRequestRequest.from_dict(_salesmax)

        _kwik_engage = d.pop("kwik_engage", UNSET)
        kwik_engage: Union[Unset, None, KwikEngageAuthRequestRequest]
        if _kwik_engage is None:
            kwik_engage = None
        elif isinstance(_kwik_engage, Unset):
            kwik_engage = UNSET
        else:
            kwik_engage = KwikEngageAuthRequestRequest.from_dict(_kwik_engage)

        _twilio = d.pop("twilio", UNSET)
        twilio: Union[Unset, None, TwilioCallAuthRequestRequest]
        if _twilio is None:
            twilio = None
        elif isinstance(_twilio, Unset):
            twilio = UNSET
        else:
            twilio = TwilioCallAuthRequestRequest.from_dict(_twilio)

        _shiprocket_delivery = d.pop("shiprocket_delivery", UNSET)
        shiprocket_delivery: Union[Unset, None, ShiprocketDeliveryAuthRequestRequest]
        if _shiprocket_delivery is None:
            shiprocket_delivery = None
        elif isinstance(_shiprocket_delivery, Unset):
            shiprocket_delivery = UNSET
        else:
            shiprocket_delivery = ShiprocketDeliveryAuthRequestRequest.from_dict(
                _shiprocket_delivery
            )

        integrations_properties_request = cls(
            shopify=shopify,
            exotel=exotel,
            stripe=stripe,
            shiprocket=shiprocket,
            nimbuspost=nimbuspost,
            salesmax=salesmax,
            kwik_engage=kwik_engage,
            twilio=twilio,
            shiprocket_delivery=shiprocket_delivery,
        )

        integrations_properties_request.additional_properties = d
        return integrations_properties_request

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
