"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import Enum


class V1CallsReportRetrieveFieldsItem(str, Enum):
    ACTOR = "actor"
    CUSTOMER_PHONE_NUMBER = "customer_phone_number"
    DIRECTION = "direction"
    DURATION = "duration"
    ID = "id"
    OUR_PHONE_NUMBER = "our_phone_number"
    RECORDING_URL = "recording_url"
    TAGS = "tags"
    TRANSCRIPT = "transcript"

    def __str__(self) -> str:
        return str(self.value)
