"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import Enum


class OrderStatusEnum(str, Enum):
    CREATED = "CREATED"
    INVOICE_CREATED = "INVOICE_CREATED"
    INVOICE_PAID = "INVOICE_PAID"
    INVOICE_PAYMENT_FAILED = "INVOICE_PAYMENT_FAILED"
    PAID = "PAID"
    UNPAID = "UNPAID"

    def __str__(self) -> str:
        return str(self.value)
