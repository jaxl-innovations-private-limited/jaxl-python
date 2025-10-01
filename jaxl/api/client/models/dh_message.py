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

from ..models.dh_message_type_enum import DHMessageTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dh_message_attachment import DHMessageAttachment
    from ..models.dh_message_reaction import DHMessageReaction


T = TypeVar("T", bound="DHMessage")


@attr.s(auto_attribs=True)
class DHMessage:
    """Adds a 'jaxlid' field which contains signed ID information.

    Attributes:
        id (int):
        ver (int):
        fpk (int):
        fau (int):
        tau (int):
        fkey (str):
        tkey (str):
        pkey (str):
        fwded (bool):
        con (datetime.datetime):
        read (bool):
        signature (str):
        encrypted (str):
        att (List['DHMessageAttachment']):
        deleted (bool):
        type (Union[Unset, DHMessageTypeEnum]):
        irt (Optional[int]):
        fname (Optional[str]):
        reactions (Optional[DHMessageReaction]):
        jaxlid (Optional[str]):
    """

    id: int
    ver: int
    fpk: int
    fau: int
    tau: int
    fkey: str
    tkey: str
    pkey: str
    fwded: bool
    con: datetime.datetime
    read: bool
    signature: str
    encrypted: str
    att: List["DHMessageAttachment"]
    deleted: bool
    irt: Optional[int]
    fname: Optional[str]
    reactions: Optional["DHMessageReaction"]
    jaxlid: Optional[str]
    type: Union[Unset, DHMessageTypeEnum] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        ver = self.ver
        fpk = self.fpk
        fau = self.fau
        tau = self.tau
        fkey = self.fkey
        tkey = self.tkey
        pkey = self.pkey
        fwded = self.fwded
        con = self.con.isoformat()

        read = self.read
        signature = self.signature
        encrypted = self.encrypted
        att = []
        for att_item_data in self.att:
            att_item = att_item_data.to_dict()

            att.append(att_item)

        deleted = self.deleted
        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        irt = self.irt
        fname = self.fname
        reactions = self.reactions.to_dict() if self.reactions else None

        jaxlid = self.jaxlid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "ver": ver,
                "fpk": fpk,
                "fau": fau,
                "tau": tau,
                "fkey": fkey,
                "tkey": tkey,
                "pkey": pkey,
                "fwded": fwded,
                "con": con,
                "read": read,
                "signature": signature,
                "encrypted": encrypted,
                "att": att,
                "deleted": deleted,
                "irt": irt,
                "fname": fname,
                "reactions": reactions,
                "jaxlid": jaxlid,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dh_message_attachment import DHMessageAttachment
        from ..models.dh_message_reaction import DHMessageReaction

        d = src_dict.copy()
        id = d.pop("id")

        ver = d.pop("ver")

        fpk = d.pop("fpk")

        fau = d.pop("fau")

        tau = d.pop("tau")

        fkey = d.pop("fkey")

        tkey = d.pop("tkey")

        pkey = d.pop("pkey")

        fwded = d.pop("fwded")

        con = isoparse(d.pop("con"))

        read = d.pop("read")

        signature = d.pop("signature")

        encrypted = d.pop("encrypted")

        att = []
        _att = d.pop("att")
        for att_item_data in _att:
            att_item = DHMessageAttachment.from_dict(att_item_data)

            att.append(att_item)

        deleted = d.pop("deleted")

        _type = d.pop("type", UNSET)
        type: Union[Unset, DHMessageTypeEnum]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DHMessageTypeEnum(_type)

        irt = d.pop("irt")

        fname = d.pop("fname")

        _reactions = d.pop("reactions")
        reactions: Optional[DHMessageReaction]
        if _reactions is None:
            reactions = None
        else:
            reactions = DHMessageReaction.from_dict(_reactions)

        jaxlid = d.pop("jaxlid")

        dh_message = cls(
            id=id,
            ver=ver,
            fpk=fpk,
            fau=fau,
            tau=tau,
            fkey=fkey,
            tkey=tkey,
            pkey=pkey,
            fwded=fwded,
            con=con,
            read=read,
            signature=signature,
            encrypted=encrypted,
            att=att,
            deleted=deleted,
            type=type,
            irt=irt,
            fname=fname,
            reactions=reactions,
            jaxlid=jaxlid,
        )

        dh_message.additional_properties = d
        return dh_message

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
