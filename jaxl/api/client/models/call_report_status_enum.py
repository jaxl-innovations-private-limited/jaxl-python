"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import Enum


class CallReportStatusEnum(str, Enum):
    FINALIZED = "FINALIZED"
    GENERATED = "GENERATED"
    GENERATING = "GENERATING"
    REQUESTED = "REQUESTED"
    UPLOADED = "UPLOADED"
    UPLOADING = "UPLOADING"

    def __str__(self) -> str:
        return str(self.value)
