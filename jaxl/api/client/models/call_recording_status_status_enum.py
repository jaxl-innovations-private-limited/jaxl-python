"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import Enum


class CallRecordingStatusStatusEnum(str, Enum):
    PAUSE = "pause"
    RESUME = "resume"
    STOP = "stop"

    def __str__(self) -> str:
        return str(self.value)
