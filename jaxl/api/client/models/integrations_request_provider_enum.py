"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import IntEnum


class IntegrationsRequestProviderEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_7 = 7
    VALUE_2 = 2
    VALUE_4 = 4
    VALUE_6 = 6
    VALUE_8 = 8
    VALUE_3 = 3
    VALUE_5 = 5
    VALUE_10 = 10
    VALUE_12 = 12
    VALUE_18 = 18
    VALUE_20 = 20
    VALUE_11 = 11
    VALUE_19 = 19
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_23 = 23
    VALUE_24 = 24
    VALUE_25 = 25
    VALUE_26 = 26

    def __str__(self) -> str:
        return str(self.value)
