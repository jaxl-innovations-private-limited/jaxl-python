"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import Enum


class IVRMenuResponseStatusEnum(str, Enum):
    ARCHIVED = "ARCHIVED"
    DELETED = "DELETED"
    DRAFT = "DRAFT"
    READY_TO_ASSIGN = "READY_TO_ASSIGN"

    def __str__(self) -> str:
        return str(self.value)
