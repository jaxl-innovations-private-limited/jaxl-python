"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import Enum


class ProofStatusEnum(str, Enum):
    APPROVED = "approved"
    DRAFT = "draft"
    EXPIRED = "expired"
    PENDING_REVIEW = "pending_review"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
