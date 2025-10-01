"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import Enum


class RentalCurrencyEnum(str, Enum):
    INR = "INR"
    USD = "USD"

    def __str__(self) -> str:
        return str(self.value)
