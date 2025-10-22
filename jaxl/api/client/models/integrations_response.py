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
    from ..models.organization_provider import OrganizationProvider


T = TypeVar("T", bound="IntegrationsResponse")


@attr.s(auto_attribs=True)
class IntegrationsResponse:
    """
    Attributes:
        redirect_url (Union[Unset, None, str]):
        provider (Union[Unset, None, OrganizationProvider]):
    """

    redirect_url: Union[Unset, None, str] = UNSET
    provider: Union[Unset, None, "OrganizationProvider"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        redirect_url = self.redirect_url
        provider: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.to_dict() if self.provider else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if redirect_url is not UNSET:
            field_dict["redirect_url"] = redirect_url
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.organization_provider import OrganizationProvider

        d = src_dict.copy()
        redirect_url = d.pop("redirect_url", UNSET)

        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, None, OrganizationProvider]
        if _provider is None:
            provider = None
        elif isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = OrganizationProvider.from_dict(_provider)

        integrations_response = cls(
            redirect_url=redirect_url,
            provider=provider,
        )

        integrations_response.additional_properties = d
        return integrations_response

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
