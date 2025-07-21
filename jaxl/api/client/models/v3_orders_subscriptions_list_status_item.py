"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import Enum


class V3OrdersSubscriptionsListStatusItem(str, Enum):
    ACTIVE = "ACTIVE"
    CANCELED = "CANCELED"
    COMPLETED = "COMPLETED"
    INCOMPLETE = "INCOMPLETE"
    INCOMPLETE_EXPIRED = "INCOMPLETE_EXPIRED"
    PAST_DUE = "PAST_DUE"
    TRIALING = "TRIALING"
    UNPAID = "UNPAID"

    def __str__(self) -> str:
        return str(self.value)
