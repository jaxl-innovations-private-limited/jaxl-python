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

from ..models.call_type_enum import CallTypeEnum
from ..models.direction_enum import DirectionEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.call_cost import CallCost
    from ..models.call_location_epoch import CallLocationEpoch
    from ..models.call_metadata import CallMetadata
    from ..models.call_tag_response import CallTagResponse
    from ..models.campaign_metadata import CampaignMetadata
    from ..models.device import Device
    from ..models.location import Location


T = TypeVar("T", bound="Call")


@attr.s(auto_attribs=True)
class Call:
    """
    Attributes:
        id (int):
        direction (DirectionEnum):
        from_number (str):
        to_number (str):
        created_on (datetime.datetime): Datetime when this object was created
        modified_on (datetime.datetime): Datetime when this object was last modified
        recording_playback_url (str):
        type (str):
        call_type (CallTypeEnum):
        costs (List['CallCost']):
        tags (List['CallTagResponse']):
        parent (Union[Unset, None, int]): Represents the parent call. Happens if a call being served through multiple
            providers
        sid (Union[Unset, None, str]): Provider call sid. Can be null if server issued an outgoing call token but
            provider never called back.
        missed (Union[Unset, bool]): Whether the call was a missed call i.e. none of the user devices received the call.
        has_voicemail (Union[Unset, bool]): Whether this call routed to user voicemail
        via_number (Optional[str]):
        completed_on (Union[Unset, None, datetime.datetime]): Datetime when this call ended.
        duration (Union[Unset, None, int]): Duration of the call
        recording_start_time (Union[Unset, None, datetime.datetime]): Datetime when recording was started
        recording_duration (Optional[int]):
        device (Optional[Device]): Adds a 'jaxlid' field which contains signed ID information.
        device_id (Union[Unset, None, int]):
        device_user_id (Optional[int]):
        device_app_user_id (Optional[int]):
        ivr (Union[Unset, None, int]): IVR menu that this call was greeted with
        metadata (Optional[CallMetadata]):
        org_id (Optional[int]):
        actor (Optional[str]):
        locations (Optional[List['Location']]):
        has_transcription (Optional[bool]):
        location_keys (Optional[List['CallLocationEpoch']]):
        recording_upload_id (Optional[int]):
        is_finalized (Optional[bool]):
        cid (Optional[int]):
        is_bot (Optional[bool]):
        camp (Optional[CampaignMetadata]):
    """

    id: int
    direction: DirectionEnum
    from_number: str
    to_number: str
    created_on: datetime.datetime
    modified_on: datetime.datetime
    recording_playback_url: str
    type: str
    call_type: CallTypeEnum
    costs: List["CallCost"]
    tags: List["CallTagResponse"]
    via_number: Optional[str]
    recording_duration: Optional[int]
    device: Optional["Device"]
    device_user_id: Optional[int]
    device_app_user_id: Optional[int]
    metadata: Optional["CallMetadata"]
    org_id: Optional[int]
    actor: Optional[str]
    locations: Optional[List["Location"]]
    has_transcription: Optional[bool]
    location_keys: Optional[List["CallLocationEpoch"]]
    recording_upload_id: Optional[int]
    is_finalized: Optional[bool]
    cid: Optional[int]
    is_bot: Optional[bool]
    camp: Optional["CampaignMetadata"]
    parent: Union[Unset, None, int] = UNSET
    sid: Union[Unset, None, str] = UNSET
    missed: Union[Unset, bool] = UNSET
    has_voicemail: Union[Unset, bool] = UNSET
    completed_on: Union[Unset, None, datetime.datetime] = UNSET
    duration: Union[Unset, None, int] = UNSET
    recording_start_time: Union[Unset, None, datetime.datetime] = UNSET
    device_id: Union[Unset, None, int] = UNSET
    ivr: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        direction = self.direction.value

        from_number = self.from_number
        to_number = self.to_number
        created_on = self.created_on.isoformat()

        modified_on = self.modified_on.isoformat()

        recording_playback_url = self.recording_playback_url
        type = self.type
        call_type = self.call_type.value

        costs = []
        for costs_item_data in self.costs:
            costs_item = costs_item_data.to_dict()

            costs.append(costs_item)

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()

            tags.append(tags_item)

        parent = self.parent
        sid = self.sid
        missed = self.missed
        has_voicemail = self.has_voicemail
        via_number = self.via_number
        completed_on: Union[Unset, None, str] = UNSET
        if not isinstance(self.completed_on, Unset):
            completed_on = self.completed_on.isoformat() if self.completed_on else None

        duration = self.duration
        recording_start_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.recording_start_time, Unset):
            recording_start_time = (
                self.recording_start_time.isoformat()
                if self.recording_start_time
                else None
            )

        recording_duration = self.recording_duration
        device = self.device.to_dict() if self.device else None

        device_id = self.device_id
        device_user_id = self.device_user_id
        device_app_user_id = self.device_app_user_id
        ivr = self.ivr
        metadata = self.metadata.to_dict() if self.metadata else None

        org_id = self.org_id
        actor = self.actor
        if self.locations is None:
            locations = None
        else:
            locations = []
            for locations_item_data in self.locations:
                locations_item = locations_item_data.to_dict()

                locations.append(locations_item)

        has_transcription = self.has_transcription
        if self.location_keys is None:
            location_keys = None
        else:
            location_keys = []
            for location_keys_item_data in self.location_keys:
                location_keys_item = location_keys_item_data.to_dict()

                location_keys.append(location_keys_item)

        recording_upload_id = self.recording_upload_id
        is_finalized = self.is_finalized
        cid = self.cid
        is_bot = self.is_bot
        camp = self.camp.to_dict() if self.camp else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "direction": direction,
                "from_number": from_number,
                "to_number": to_number,
                "created_on": created_on,
                "modified_on": modified_on,
                "recording_playback_url": recording_playback_url,
                "type": type,
                "call_type": call_type,
                "costs": costs,
                "tags": tags,
                "via_number": via_number,
                "recording_duration": recording_duration,
                "device": device,
                "device_user_id": device_user_id,
                "device_app_user_id": device_app_user_id,
                "metadata": metadata,
                "org_id": org_id,
                "actor": actor,
                "locations": locations,
                "has_transcription": has_transcription,
                "location_keys": location_keys,
                "recording_upload_id": recording_upload_id,
                "is_finalized": is_finalized,
                "cid": cid,
                "is_bot": is_bot,
                "camp": camp,
            }
        )
        if parent is not UNSET:
            field_dict["parent"] = parent
        if sid is not UNSET:
            field_dict["sid"] = sid
        if missed is not UNSET:
            field_dict["missed"] = missed
        if has_voicemail is not UNSET:
            field_dict["has_voicemail"] = has_voicemail
        if completed_on is not UNSET:
            field_dict["completed_on"] = completed_on
        if duration is not UNSET:
            field_dict["duration"] = duration
        if recording_start_time is not UNSET:
            field_dict["recording_start_time"] = recording_start_time
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if ivr is not UNSET:
            field_dict["ivr"] = ivr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.call_cost import CallCost
        from ..models.call_location_epoch import CallLocationEpoch
        from ..models.call_metadata import CallMetadata
        from ..models.call_tag_response import CallTagResponse
        from ..models.campaign_metadata import CampaignMetadata
        from ..models.device import Device
        from ..models.location import Location

        d = src_dict.copy()
        id = d.pop("id")

        direction = DirectionEnum(d.pop("direction"))

        from_number = d.pop("from_number")

        to_number = d.pop("to_number")

        created_on = isoparse(d.pop("created_on"))

        modified_on = isoparse(d.pop("modified_on"))

        recording_playback_url = d.pop("recording_playback_url")

        type = d.pop("type")

        call_type = CallTypeEnum(d.pop("call_type"))

        costs = []
        _costs = d.pop("costs")
        for costs_item_data in _costs:
            costs_item = CallCost.from_dict(costs_item_data)

            costs.append(costs_item)

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = CallTagResponse.from_dict(tags_item_data)

            tags.append(tags_item)

        parent = d.pop("parent", UNSET)

        sid = d.pop("sid", UNSET)

        missed = d.pop("missed", UNSET)

        has_voicemail = d.pop("has_voicemail", UNSET)

        via_number = d.pop("via_number")

        _completed_on = d.pop("completed_on", UNSET)
        completed_on: Union[Unset, None, datetime.datetime]
        if _completed_on is None:
            completed_on = None
        elif isinstance(_completed_on, Unset):
            completed_on = UNSET
        else:
            completed_on = isoparse(_completed_on)

        duration = d.pop("duration", UNSET)

        _recording_start_time = d.pop("recording_start_time", UNSET)
        recording_start_time: Union[Unset, None, datetime.datetime]
        if _recording_start_time is None:
            recording_start_time = None
        elif isinstance(_recording_start_time, Unset):
            recording_start_time = UNSET
        else:
            recording_start_time = isoparse(_recording_start_time)

        recording_duration = d.pop("recording_duration")

        _device = d.pop("device")
        device: Optional[Device]
        if _device is None:
            device = None
        else:
            device = Device.from_dict(_device)

        device_id = d.pop("device_id", UNSET)

        device_user_id = d.pop("device_user_id")

        device_app_user_id = d.pop("device_app_user_id")

        ivr = d.pop("ivr", UNSET)

        _metadata = d.pop("metadata")
        metadata: Optional[CallMetadata]
        if _metadata is None:
            metadata = None
        else:
            metadata = CallMetadata.from_dict(_metadata)

        org_id = d.pop("org_id")

        actor = d.pop("actor")

        locations = []
        _locations = d.pop("locations")
        for locations_item_data in _locations or []:
            locations_item = Location.from_dict(locations_item_data)

            locations.append(locations_item)

        has_transcription = d.pop("has_transcription")

        location_keys = []
        _location_keys = d.pop("location_keys")
        for location_keys_item_data in _location_keys or []:
            location_keys_item = CallLocationEpoch.from_dict(location_keys_item_data)

            location_keys.append(location_keys_item)

        recording_upload_id = d.pop("recording_upload_id")

        is_finalized = d.pop("is_finalized")

        cid = d.pop("cid")

        is_bot = d.pop("is_bot")

        _camp = d.pop("camp")
        camp: Optional[CampaignMetadata]
        if _camp is None:
            camp = None
        else:
            camp = CampaignMetadata.from_dict(_camp)

        call = cls(
            id=id,
            direction=direction,
            from_number=from_number,
            to_number=to_number,
            created_on=created_on,
            modified_on=modified_on,
            recording_playback_url=recording_playback_url,
            type=type,
            call_type=call_type,
            costs=costs,
            tags=tags,
            parent=parent,
            sid=sid,
            missed=missed,
            has_voicemail=has_voicemail,
            via_number=via_number,
            completed_on=completed_on,
            duration=duration,
            recording_start_time=recording_start_time,
            recording_duration=recording_duration,
            device=device,
            device_id=device_id,
            device_user_id=device_user_id,
            device_app_user_id=device_app_user_id,
            ivr=ivr,
            metadata=metadata,
            org_id=org_id,
            actor=actor,
            locations=locations,
            has_transcription=has_transcription,
            location_keys=location_keys,
            recording_upload_id=recording_upload_id,
            is_finalized=is_finalized,
            cid=cid,
            is_bot=is_bot,
            camp=camp,
        )

        call.additional_properties = d
        return call

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
