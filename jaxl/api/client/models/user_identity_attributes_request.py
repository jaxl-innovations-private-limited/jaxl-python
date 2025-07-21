"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.business_attributes_request import BusinessAttributesRequest


T = TypeVar("T", bound="UserIdentityAttributesRequest")


@attr.s(auto_attribs=True)
class UserIdentityAttributesRequest:
    """
    Attributes:
        first_name (str):
        last_name (str):
        friendly_name (str):
        birth_date (datetime.datetime):
        phone_number (str):
        nationality (str):
        email (str):
        business (Union[Unset, None, BusinessAttributesRequest]):
    """

    first_name: str
    last_name: str
    friendly_name: str
    birth_date: datetime.datetime
    phone_number: str
    nationality: str
    email: str
    business: Union[Unset, None, "BusinessAttributesRequest"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        first_name = self.first_name
        last_name = self.last_name
        friendly_name = self.friendly_name
        birth_date = self.birth_date.isoformat()

        phone_number = self.phone_number
        nationality = self.nationality
        email = self.email
        business: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.business, Unset):
            business = self.business.to_dict() if self.business else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "first_name": first_name,
                "last_name": last_name,
                "friendly_name": friendly_name,
                "birth_date": birth_date,
                "phone_number": phone_number,
                "nationality": nationality,
                "email": email,
            }
        )
        if business is not UNSET:
            field_dict["business"] = business

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.business_attributes_request import (
            BusinessAttributesRequest,
        )

        d = src_dict.copy()
        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        friendly_name = d.pop("friendly_name")

        birth_date = isoparse(d.pop("birth_date"))

        phone_number = d.pop("phone_number")

        nationality = d.pop("nationality")

        email = d.pop("email")

        _business = d.pop("business", UNSET)
        business: Union[Unset, None, BusinessAttributesRequest]
        if _business is None:
            business = None
        elif isinstance(_business, Unset):
            business = UNSET
        else:
            business = BusinessAttributesRequest.from_dict(_business)

        user_identity_attributes_request = cls(
            first_name=first_name,
            last_name=last_name,
            friendly_name=friendly_name,
            birth_date=birth_date,
            phone_number=phone_number,
            nationality=nationality,
            email=email,
            business=business,
        )

        user_identity_attributes_request.additional_properties = d
        return user_identity_attributes_request

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
