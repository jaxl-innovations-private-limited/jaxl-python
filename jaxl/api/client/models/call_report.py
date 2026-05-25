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

from ..models.call_report_status_enum import CallReportStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.upload_metadata import UploadMetadata


T = TypeVar("T", bound="CallReport")


@attr.s(auto_attribs=True)
class CallReport:
    """
    Attributes:
        id (int):
        created_on (datetime.datetime): Datetime when this object was created
        modified_on (datetime.datetime): Datetime when this object was last modified
        start_time (datetime.datetime):
        end_time (datetime.datetime):
        status (Union[Unset, CallReportStatusEnum]):
        app_user_id (Optional[int]): Primary key of the AppUser related to this object
        upload_metadata (Optional[UploadMetadata]):
    """

    id: int
    created_on: datetime.datetime
    modified_on: datetime.datetime
    start_time: datetime.datetime
    end_time: datetime.datetime
    app_user_id: Optional[int]
    upload_metadata: Optional["UploadMetadata"]
    status: Union[Unset, CallReportStatusEnum] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        created_on = self.created_on.isoformat()

        modified_on = self.modified_on.isoformat()

        start_time = self.start_time.isoformat()

        end_time = self.end_time.isoformat()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        app_user_id = self.app_user_id
        upload_metadata = (
            self.upload_metadata.to_dict() if self.upload_metadata else None
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_on": created_on,
                "modified_on": modified_on,
                "start_time": start_time,
                "end_time": end_time,
                "app_user_id": app_user_id,
                "upload_metadata": upload_metadata,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.upload_metadata import UploadMetadata

        d = src_dict.copy()
        id = d.pop("id")

        created_on = isoparse(d.pop("created_on"))

        modified_on = isoparse(d.pop("modified_on"))

        start_time = isoparse(d.pop("start_time"))

        end_time = isoparse(d.pop("end_time"))

        _status = d.pop("status", UNSET)
        status: Union[Unset, CallReportStatusEnum]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CallReportStatusEnum(_status)

        app_user_id = d.pop("app_user_id")

        _upload_metadata = d.pop("upload_metadata")
        upload_metadata: Optional[UploadMetadata]
        if _upload_metadata is None:
            upload_metadata = None
        else:
            upload_metadata = UploadMetadata.from_dict(_upload_metadata)

        call_report = cls(
            id=id,
            created_on=created_on,
            modified_on=modified_on,
            start_time=start_time,
            end_time=end_time,
            status=status,
            app_user_id=app_user_id,
            upload_metadata=upload_metadata,
        )

        call_report.additional_properties = d
        return call_report

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
