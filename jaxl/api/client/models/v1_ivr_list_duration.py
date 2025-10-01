"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import Enum


class V1IvrListDuration(str, Enum):
    ONE_DAY = "ONE_DAY"
    ONE_HOUR = "ONE_HOUR"
    ONE_MINUTE = "ONE_MINUTE"
    ONE_MONTH = "ONE_MONTH"
    ONE_WEEK = "ONE_WEEK"
    ONE_YEAR = "ONE_YEAR"
    SIX_MONTH = "SIX_MONTH"

    def __str__(self) -> str:
        return str(self.value)
