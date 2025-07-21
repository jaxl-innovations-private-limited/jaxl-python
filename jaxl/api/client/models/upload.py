"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset


T = TypeVar("T", bound="Upload")


@attr.s(auto_attribs=True)
class Upload:
    """
    Attributes:
        id (int):
        name (str): object_name provided at time of the upload
        sha256 (str): SHA256 of uploaded file content.  NOTE, this value is totally client sent and is not verified by
            the server in any way currently.  Simple reason being, because, server NEVER gets to see the content of the
            uploaded file.  BUT, sha256 helps us to track duplicate uploads in the system.  As a downside, sha256
            calculation on mobile devices can take upto 10-15 seconds for 1Gb file.
        mimetype (str): Mimetype of the file being uploaded
        size (int): Size in bytes declared at time out upload
        tag (Union[Unset, None, str]): A free form tag associated with this uploaded file.  You can use this field to
            later query uploads for a specific tag.  This tag is also used during object finalization signals.  Example,
            when source is DEVICE, system uses device fingerprint as tag value.
    """

    id: int
    name: str
    sha256: str
    mimetype: str
    size: int
    tag: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        sha256 = self.sha256
        mimetype = self.mimetype
        size = self.size
        tag = self.tag

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "sha256": sha256,
                "mimetype": mimetype,
                "size": size,
            }
        )
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        sha256 = d.pop("sha256")

        mimetype = d.pop("mimetype")

        size = d.pop("size")

        tag = d.pop("tag", UNSET)

        upload = cls(
            id=id,
            name=name,
            sha256=sha256,
            mimetype=mimetype,
            size=size,
            tag=tag,
        )

        upload.additional_properties = d
        return upload

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
