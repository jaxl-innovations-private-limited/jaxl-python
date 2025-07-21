"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import Enum


class CustomerOrderStatusChangedNotificationTypeEnum(str, Enum):
    CANCELED = "canceled"
    EXPIRED = "expired"
    FAILED = "failed"
    FAILED_TO_RENEW = "failed_to_renew"
    PURCHASED = "purchased"
    RENEWED = "renewed"
    RESUBSCRIBED = "resubscribed"
    RESUMED = "resumed"
    WILL_RENEW = "will_renew"

    def __str__(self) -> str:
        return str(self.value)
