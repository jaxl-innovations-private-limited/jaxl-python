"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import Enum


class KeyInfoTypeEnum(str, Enum):
    BOOL = "bool"
    FLOAT = "float"
    INT = "int"
    STR = "str"

    def __str__(self) -> str:
        return str(self.value)
