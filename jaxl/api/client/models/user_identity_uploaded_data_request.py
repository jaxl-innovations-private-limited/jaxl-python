"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.iso_country_enum import IsoCountryEnum
from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.user_identity_attributes_request import (
        UserIdentityAttributesRequest,
    )
    from ..models.user_identity_uploaded_data_request_additional_attributes import (
        UserIdentityUploadedDataRequestAdditionalAttributes,
    )


T = TypeVar("T", bound="UserIdentityUploadedDataRequest")


@attr.s(auto_attribs=True)
class UserIdentityUploadedDataRequest:
    """
    Attributes:
        attributes (UserIdentityAttributesRequest):
        iso_country (IsoCountryEnum):
        additional_attributes (Union[Unset, None, UserIdentityUploadedDataRequestAdditionalAttributes]):
    """

    attributes: "UserIdentityAttributesRequest"
    iso_country: IsoCountryEnum
    additional_attributes: Union[
        Unset, None, "UserIdentityUploadedDataRequestAdditionalAttributes"
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attributes = self.attributes.to_dict()

        iso_country = self.iso_country.value

        additional_attributes: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_attributes, Unset):
            additional_attributes = (
                self.additional_attributes.to_dict()
                if self.additional_attributes
                else None
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributes": attributes,
                "iso_country": iso_country,
            }
        )
        if additional_attributes is not UNSET:
            field_dict["additional_attributes"] = additional_attributes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_identity_attributes_request import (
            UserIdentityAttributesRequest,
        )
        from ..models.user_identity_uploaded_data_request_additional_attributes import (
            UserIdentityUploadedDataRequestAdditionalAttributes,
        )

        d = src_dict.copy()
        attributes = UserIdentityAttributesRequest.from_dict(d.pop("attributes"))

        iso_country = IsoCountryEnum(d.pop("iso_country"))

        _additional_attributes = d.pop("additional_attributes", UNSET)
        additional_attributes: Union[
            Unset, None, UserIdentityUploadedDataRequestAdditionalAttributes
        ]
        if _additional_attributes is None:
            additional_attributes = None
        elif isinstance(_additional_attributes, Unset):
            additional_attributes = UNSET
        else:
            additional_attributes = (
                UserIdentityUploadedDataRequestAdditionalAttributes.from_dict(
                    _additional_attributes
                )
            )

        user_identity_uploaded_data_request = cls(
            attributes=attributes,
            iso_country=iso_country,
            additional_attributes=additional_attributes,
        )

        user_identity_uploaded_data_request.additional_properties = d
        return user_identity_uploaded_data_request

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
