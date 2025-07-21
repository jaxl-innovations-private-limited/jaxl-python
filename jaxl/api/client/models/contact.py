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
    from ..models.contact_address import ContactAddress
    from ..models.contact_email import ContactEmail
    from ..models.contact_phone import ContactPhone


T = TypeVar("T", bound="Contact")


@attr.s(auto_attribs=True)
class Contact:
    """
    Attributes:
        id (str):
        name (str):
        emails (List['ContactEmail']):
        phones (List['ContactPhone']):
        addresses (List['ContactAddress']):
        thumbnail (Union[Unset, str]):
    """

    id: str
    name: str
    emails: List["ContactEmail"]
    phones: List["ContactPhone"]
    addresses: List["ContactAddress"]
    thumbnail: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        emails = []
        for emails_item_data in self.emails:
            emails_item = emails_item_data.to_dict()

            emails.append(emails_item)

        phones = []
        for phones_item_data in self.phones:
            phones_item = phones_item_data.to_dict()

            phones.append(phones_item)

        addresses = []
        for addresses_item_data in self.addresses:
            addresses_item = addresses_item_data.to_dict()

            addresses.append(addresses_item)

        thumbnail = self.thumbnail

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "emails": emails,
                "phones": phones,
                "addresses": addresses,
            }
        )
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contact_address import ContactAddress
        from ..models.contact_email import ContactEmail
        from ..models.contact_phone import ContactPhone

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        emails = []
        _emails = d.pop("emails")
        for emails_item_data in _emails:
            emails_item = ContactEmail.from_dict(emails_item_data)

            emails.append(emails_item)

        phones = []
        _phones = d.pop("phones")
        for phones_item_data in _phones:
            phones_item = ContactPhone.from_dict(phones_item_data)

            phones.append(phones_item)

        addresses = []
        _addresses = d.pop("addresses")
        for addresses_item_data in _addresses:
            addresses_item = ContactAddress.from_dict(addresses_item_data)

            addresses.append(addresses_item)

        thumbnail = d.pop("thumbnail", UNSET)

        contact = cls(
            id=id,
            name=name,
            emails=emails,
            phones=phones,
            addresses=addresses,
            thumbnail=thumbnail,
        )

        contact.additional_properties = d
        return contact

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
