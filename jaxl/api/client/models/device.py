"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.platform_enum import PlatformEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connection import Connection


T = TypeVar("T", bound="Device")


@attr.s(auto_attribs=True)
class Device:
    """Adds a 'jaxlid' field which contains signed ID information.

    Attributes:
        id (int):
        uid (str): Unique device identifier which may or may not persist across app reinstalls. Currently, uid is same
            as one obtained on the device.
        created_on (datetime.datetime): Datetime when this object was created
        platform (Union[None, PlatformEnum, Unset]):
        parent (Union[Unset, None, int]): Parent of this device.
        parent_linked_on (Union[Unset, None, datetime.datetime]): Datetime when parent device was linked
        parent_unlinked_on (Union[Unset, None, datetime.datetime]): Datetime when parent was unlinked
        last_seen (Optional[Connection]): Adds a 'jaxlid' field which contains signed ID information.
        name (Union[Unset, None, str]): Devie name set by user.
        logged_out_on (Union[Unset, None, datetime.datetime]): Datetime when device was logged out
        restored_by (Optional[int]):
        jaxlid (Optional[str]):
    """

    id: int
    uid: str
    created_on: datetime.datetime
    last_seen: Optional["Connection"]
    restored_by: Optional[int]
    jaxlid: Optional[str]
    platform: Union[None, PlatformEnum, Unset] = UNSET
    parent: Union[Unset, None, int] = UNSET
    parent_linked_on: Union[Unset, None, datetime.datetime] = UNSET
    parent_unlinked_on: Union[Unset, None, datetime.datetime] = UNSET
    name: Union[Unset, None, str] = UNSET
    logged_out_on: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        uid = self.uid
        created_on = self.created_on.isoformat()

        platform: Union[None, Unset, int]
        if isinstance(self.platform, Unset):
            platform = UNSET
        elif self.platform is None:
            platform = None

        elif isinstance(self.platform, PlatformEnum):
            platform = UNSET
            if not isinstance(self.platform, Unset):
                platform = self.platform.value

        else:
            platform = self.platform

        parent = self.parent
        parent_linked_on: Union[Unset, None, str] = UNSET
        if not isinstance(self.parent_linked_on, Unset):
            parent_linked_on = (
                self.parent_linked_on.isoformat() if self.parent_linked_on else None
            )

        parent_unlinked_on: Union[Unset, None, str] = UNSET
        if not isinstance(self.parent_unlinked_on, Unset):
            parent_unlinked_on = (
                self.parent_unlinked_on.isoformat() if self.parent_unlinked_on else None
            )

        last_seen = self.last_seen.to_dict() if self.last_seen else None

        name = self.name
        logged_out_on: Union[Unset, None, str] = UNSET
        if not isinstance(self.logged_out_on, Unset):
            logged_out_on = (
                self.logged_out_on.isoformat() if self.logged_out_on else None
            )

        restored_by = self.restored_by
        jaxlid = self.jaxlid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uid": uid,
                "created_on": created_on,
                "last_seen": last_seen,
                "restored_by": restored_by,
                "jaxlid": jaxlid,
            }
        )
        if platform is not UNSET:
            field_dict["platform"] = platform
        if parent is not UNSET:
            field_dict["parent"] = parent
        if parent_linked_on is not UNSET:
            field_dict["parent_linked_on"] = parent_linked_on
        if parent_unlinked_on is not UNSET:
            field_dict["parent_unlinked_on"] = parent_unlinked_on
        if name is not UNSET:
            field_dict["name"] = name
        if logged_out_on is not UNSET:
            field_dict["logged_out_on"] = logged_out_on

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.connection import Connection

        d = src_dict.copy()
        id = d.pop("id")

        uid = d.pop("uid")

        created_on = isoparse(d.pop("created_on"))

        def _parse_platform(data: object) -> Union[None, PlatformEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                _platform_type_0 = data
                platform_type_0: Union[Unset, PlatformEnum]
                if isinstance(_platform_type_0, Unset):
                    platform_type_0 = UNSET
                else:
                    platform_type_0 = PlatformEnum(_platform_type_0)

                return platform_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, PlatformEnum, Unset], data)

        platform = _parse_platform(d.pop("platform", UNSET))

        parent = d.pop("parent", UNSET)

        _parent_linked_on = d.pop("parent_linked_on", UNSET)
        parent_linked_on: Union[Unset, None, datetime.datetime]
        if _parent_linked_on is None:
            parent_linked_on = None
        elif isinstance(_parent_linked_on, Unset):
            parent_linked_on = UNSET
        else:
            parent_linked_on = isoparse(_parent_linked_on)

        _parent_unlinked_on = d.pop("parent_unlinked_on", UNSET)
        parent_unlinked_on: Union[Unset, None, datetime.datetime]
        if _parent_unlinked_on is None:
            parent_unlinked_on = None
        elif isinstance(_parent_unlinked_on, Unset):
            parent_unlinked_on = UNSET
        else:
            parent_unlinked_on = isoparse(_parent_unlinked_on)

        _last_seen = d.pop("last_seen")
        last_seen: Optional[Connection]
        if _last_seen is None:
            last_seen = None
        else:
            last_seen = Connection.from_dict(_last_seen)

        name = d.pop("name", UNSET)

        _logged_out_on = d.pop("logged_out_on", UNSET)
        logged_out_on: Union[Unset, None, datetime.datetime]
        if _logged_out_on is None:
            logged_out_on = None
        elif isinstance(_logged_out_on, Unset):
            logged_out_on = UNSET
        else:
            logged_out_on = isoparse(_logged_out_on)

        restored_by = d.pop("restored_by")

        jaxlid = d.pop("jaxlid")

        device = cls(
            id=id,
            uid=uid,
            created_on=created_on,
            platform=platform,
            parent=parent,
            parent_linked_on=parent_linked_on,
            parent_unlinked_on=parent_unlinked_on,
            last_seen=last_seen,
            name=name,
            logged_out_on=logged_out_on,
            restored_by=restored_by,
            jaxlid=jaxlid,
        )

        device.additional_properties = d
        return device

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
