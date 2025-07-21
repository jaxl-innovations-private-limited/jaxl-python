"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import Enum


class ActionEnum(str, Enum):
    ACCEPT = "accept"
    CANCEL = "cancel"
    REJECT = "reject"
    REMOVE = "remove"

    def __str__(self) -> str:
        return str(self.value)
