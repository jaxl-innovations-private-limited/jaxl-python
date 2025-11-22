"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import Enum


class V1CallsReportRetrieveFieldsItem(str, Enum):
    ACTOR = "actor"
    DIRECTION = "direction"
    DURATION = "duration"
    FROM_NUMBER = "from_number"
    ID = "id"
    RECORDING_URL = "recording_url"
    TAGS = "tags"
    TO_NUMBER = "to_number"

    def __str__(self) -> str:
        return str(self.value)
