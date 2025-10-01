"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import IntEnum


class DirectionEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

    def __str__(self) -> str:
        return str(self.value)
