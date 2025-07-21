"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import Enum


class AddressProviderStatusEnum(str, Enum):
    PSEUDO_VALIDATION = "pseudo_validation"
    QUEUED = "queued"
    VALIDATION_APPROVED = "validation_approved"
    VALIDATION_REJECTED = "validation_rejected"

    def __str__(self) -> str:
        return str(self.value)
