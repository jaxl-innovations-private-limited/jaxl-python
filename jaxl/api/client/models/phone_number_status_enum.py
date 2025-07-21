"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import Enum


class PhoneNumberStatusEnum(str, Enum):
    CHECKOUT = "CHECKOUT"
    FAILURE = "FAILURE"
    IN_PROGRESS = "IN_PROGRESS"
    QUEUED = "QUEUED"
    RELEASED_BY_PROVIDER = "RELEASED_BY_PROVIDER"
    RELEASED_TO_PROVIDER = "RELEASED_TO_PROVIDER"
    SCHEDULED_FOR_RELEASE = "SCHEDULED_FOR_RELEASE"
    SUCCESS = "SUCCESS"
    UNDEFINED = "UNDEFINED"

    def __str__(self) -> str:
        return str(self.value)
