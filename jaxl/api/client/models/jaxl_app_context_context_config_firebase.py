"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar

import attr


T = TypeVar("T", bound="JaxlAppContextContextConfigFirebase")


@attr.s(auto_attribs=True)
class JaxlAppContextContextConfigFirebase:
    """
    Attributes:
        api_key (str):
        app_id (str):
        auth_domain (str):
        measurement_id (str):
        messaging_sender_id (str):
        project_id (str):
        storage_bucket (str):
    """

    api_key: str
    app_id: str
    auth_domain: str
    measurement_id: str
    messaging_sender_id: str
    project_id: str
    storage_bucket: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api_key = self.api_key
        app_id = self.app_id
        auth_domain = self.auth_domain
        measurement_id = self.measurement_id
        messaging_sender_id = self.messaging_sender_id
        project_id = self.project_id
        storage_bucket = self.storage_bucket

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "appId": app_id,
                "authDomain": auth_domain,
                "measurementId": measurement_id,
                "messagingSenderId": messaging_sender_id,
                "projectId": project_id,
                "storageBucket": storage_bucket,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        api_key = d.pop("apiKey")

        app_id = d.pop("appId")

        auth_domain = d.pop("authDomain")

        measurement_id = d.pop("measurementId")

        messaging_sender_id = d.pop("messagingSenderId")

        project_id = d.pop("projectId")

        storage_bucket = d.pop("storageBucket")

        jaxl_app_context_context_config_firebase = cls(
            api_key=api_key,
            app_id=app_id,
            auth_domain=auth_domain,
            measurement_id=measurement_id,
            messaging_sender_id=messaging_sender_id,
            project_id=project_id,
            storage_bucket=storage_bucket,
        )

        jaxl_app_context_context_config_firebase.additional_properties = d
        return jaxl_app_context_context_config_firebase

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
