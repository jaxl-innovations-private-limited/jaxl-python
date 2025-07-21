"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Optional,
    Type,
    TypeVar,
    Union,
)

import attr

from ..models.location_enum import LocationEnum
from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.sim_metadata import SimMetadata


T = TypeVar("T", bound="Sim")


@attr.s(auto_attribs=True)
class Sim:
    """Adds a 'jaxlid' field which contains signed ID information.

    Attributes:
        id (int):
        location (LocationEnum):
        uid (str): Phone number assigned to the SIM Card
        imsi (str): IMSI number assigned to the SIM Card. First 3 digits represents MCC (Mobile Country Code) e.g. 405
            == India. Next 2-3 digits represents MNC (Mobile Network Code). In India, its typically 2-digit long. e.g. MNC
            == 54. Remaining digits represents MSIN (Mobile Subscriber Identification Number).
        imei (str): IMEI number assigned to the SIM Module
        endpoint (str): Public URL for SIM host controller
        hostname (str): Controller hostname
        local_ip (str): Local network IP Address of SIM host controller
        serial_port (str): Serial port over which host controller is communicating with SIM Module
        input_device_index (int): Corresponds to 'index' returned by lsusb and represents the USB index on which SIM
            audio input is expected
        output_device_index (int): Corresponds to 'index' returned by lsusb and represents the USB index on which
            streaming audio output will be dispatched
        metadata (Union[Unset, SimMetadata]): Metadata about SIM module and microcontroller
        jaxlid (Optional[str]):
    """

    id: int
    location: LocationEnum
    uid: str
    imsi: str
    imei: str
    endpoint: str
    hostname: str
    local_ip: str
    serial_port: str
    input_device_index: int
    output_device_index: int
    jaxlid: Optional[str]
    metadata: Union[Unset, "SimMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        location = self.location.value

        uid = self.uid
        imsi = self.imsi
        imei = self.imei
        endpoint = self.endpoint
        hostname = self.hostname
        local_ip = self.local_ip
        serial_port = self.serial_port
        input_device_index = self.input_device_index
        output_device_index = self.output_device_index
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        jaxlid = self.jaxlid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "location": location,
                "uid": uid,
                "imsi": imsi,
                "imei": imei,
                "endpoint": endpoint,
                "hostname": hostname,
                "local_ip": local_ip,
                "serial_port": serial_port,
                "input_device_index": input_device_index,
                "output_device_index": output_device_index,
                "jaxlid": jaxlid,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sim_metadata import SimMetadata

        d = src_dict.copy()
        id = d.pop("id")

        location = LocationEnum(d.pop("location"))

        uid = d.pop("uid")

        imsi = d.pop("imsi")

        imei = d.pop("imei")

        endpoint = d.pop("endpoint")

        hostname = d.pop("hostname")

        local_ip = d.pop("local_ip")

        serial_port = d.pop("serial_port")

        input_device_index = d.pop("input_device_index")

        output_device_index = d.pop("output_device_index")

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, SimMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = SimMetadata.from_dict(_metadata)

        jaxlid = d.pop("jaxlid")

        sim = cls(
            id=id,
            location=location,
            uid=uid,
            imsi=imsi,
            imei=imei,
            endpoint=endpoint,
            hostname=hostname,
            local_ip=local_ip,
            serial_port=serial_port,
            input_device_index=input_device_index,
            output_device_index=output_device_index,
            metadata=metadata,
            jaxlid=jaxlid,
        )

        sim.additional_properties = d
        return sim

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
