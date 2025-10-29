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
    from ..models.shopify_auth_request_request import ShopifyAuthRequestRequest


T = TypeVar("T", bound="IntegrationsPropertiesRequest")


@attr.s(auto_attribs=True)
class IntegrationsPropertiesRequest:
    """
    Attributes:
        shopify (Union[Unset, None, ShopifyAuthRequestRequest]):
        exotel (Union[Unset, None, ExotelAuthRequestRequest]):
    """

    shopify: Union[Unset, None, "ShopifyAuthRequestRequest"] = UNSET
    exotel: Union[Unset, None, "ExotelAuthRequestRequest"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shopify: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.shopify, Unset):
            shopify = self.shopify.to_dict() if self.shopify else None

        exotel: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.exotel, Unset):
            exotel = self.exotel.to_dict() if self.exotel else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shopify is not UNSET:
            field_dict["shopify"] = shopify
        if exotel is not UNSET:
            field_dict["exotel"] = exotel

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.exotel_auth_request_request import ExotelAuthRequestRequest
        from ..models.shopify_auth_request_request import ShopifyAuthRequestRequest

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

        integrations_properties_request = cls(
            shopify=shopify,
            exotel=exotel,
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
