"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.phone_number_provider_enum import PhoneNumberProviderEnum
from ..models.phone_number_status_enum import PhoneNumberStatusEnum
from ..models.resource_enum import ResourceEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.phone_number_attributes import PhoneNumberAttributes
    from ..models.phone_number_capabilities import PhoneNumberCapabilities


T = TypeVar("T", bound="PhoneNumber")


@attr.s(auto_attribs=True)
class PhoneNumber:
    """Adds a 'jaxlid' field which contains signed ID information.

    Attributes:
        id (int):
        uid (str):
        verified (bool): Whether this phone number has completed the verification process.  This is automatically set to
            True for system owned numbers
        provider (PhoneNumberProviderEnum):
        status (PhoneNumberStatusEnum):
        registered_on (datetime.datetime): Datetime when this device was registered by user or purchased from provider
            for an app user.
        registered_from_this_device (bool):
        capabilities (PhoneNumberCapabilities):
        resource (ResourceEnum):
        ivr (Union[Unset, None, int]): Optional IVR for all incoming calls to this number
        registered_from_device (Optional[int]):
        attributes (Optional[PhoneNumberAttributes]):
        jaxlid (Optional[str]):
    """

    id: int
    uid: str
    provider: PhoneNumberProviderEnum
    status: PhoneNumberStatusEnum
    registered_on: datetime.datetime
    registered_from_this_device: bool
    capabilities: "PhoneNumberCapabilities"
    resource: ResourceEnum
    registered_from_device: Optional[int]
    attributes: Optional["PhoneNumberAttributes"]
    jaxlid: Optional[str]
    verified: bool = False
    ivr: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        uid = self.uid
        verified = self.verified
        provider = self.provider.value

        status = self.status.value

        registered_on = self.registered_on.isoformat()

        registered_from_this_device = self.registered_from_this_device
        capabilities = self.capabilities.to_dict()

        resource = self.resource.value

        ivr = self.ivr
        registered_from_device = self.registered_from_device
        attributes = self.attributes.to_dict() if self.attributes else None

        jaxlid = self.jaxlid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uid": uid,
                "verified": verified,
                "provider": provider,
                "status": status,
                "registered_on": registered_on,
                "registered_from_this_device": registered_from_this_device,
                "capabilities": capabilities,
                "resource": resource,
                "registered_from_device": registered_from_device,
                "attributes": attributes,
                "jaxlid": jaxlid,
            }
        )
        if ivr is not UNSET:
            field_dict["ivr"] = ivr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.phone_number_attributes import PhoneNumberAttributes
        from ..models.phone_number_capabilities import PhoneNumberCapabilities

        d = src_dict.copy()
        id = d.pop("id")

        uid = d.pop("uid")

        verified = d.pop("verified")

        provider = PhoneNumberProviderEnum(d.pop("provider"))

        status = PhoneNumberStatusEnum(d.pop("status"))

        registered_on = isoparse(d.pop("registered_on"))

        registered_from_this_device = d.pop("registered_from_this_device")

        capabilities = PhoneNumberCapabilities.from_dict(d.pop("capabilities"))

        resource = ResourceEnum(d.pop("resource"))

        ivr = d.pop("ivr", UNSET)

        registered_from_device = d.pop("registered_from_device")

        _attributes = d.pop("attributes")
        attributes: Optional[PhoneNumberAttributes]
        if _attributes is None:
            attributes = None
        else:
            attributes = PhoneNumberAttributes.from_dict(_attributes)

        jaxlid = d.pop("jaxlid")

        phone_number = cls(
            id=id,
            uid=uid,
            verified=verified,
            provider=provider,
            status=status,
            registered_on=registered_on,
            registered_from_this_device=registered_from_this_device,
            capabilities=capabilities,
            resource=resource,
            ivr=ivr,
            registered_from_device=registered_from_device,
            attributes=attributes,
            jaxlid=jaxlid,
        )

        phone_number.additional_properties = d
        return phone_number

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
