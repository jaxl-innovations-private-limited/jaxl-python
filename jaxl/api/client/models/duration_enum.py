"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import Enum


class DurationEnum(str, Enum):
    ONE_MONTH = "ONE_MONTH"
    ONE_WEEK = "ONE_WEEK"
    ONE_YEAR = "ONE_YEAR"
    SIX_MONTH = "SIX_MONTH"
    THREE_MONTH = "THREE_MONTH"

    def __str__(self) -> str:
        return str(self.value)
