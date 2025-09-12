"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import IntEnum


class V1PhonenumbersListProvider(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_10 = 10
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9

    def __str__(self) -> str:
        return str(self.value)
