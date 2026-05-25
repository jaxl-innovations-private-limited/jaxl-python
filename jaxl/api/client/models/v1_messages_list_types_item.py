"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import Enum


class V1MessagesListTypesItem(str, Enum):
    AUDIO = "AUDIO"
    CALL_EVENT = "CALL_EVENT"
    CHAT = "CHAT"
    CONTACT = "CONTACT"
    LINK = "LINK"
    LIVE_LOCATION = "LIVE_LOCATION"
    LOCATION = "LOCATION"
    MEDIA = "MEDIA"
    NOTE = "NOTE"
    PHOTO = "PHOTO"
    PROVIDER_EVENT = "PROVIDER_EVENT"
    SUGGESTION = "SUGGESTION"
    SUMMARY = "SUMMARY"
    VIDEO = "VIDEO"

    def __str__(self) -> str:
        return str(self.value)
