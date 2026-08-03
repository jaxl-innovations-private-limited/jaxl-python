"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import Enum


class FailureReasonEnum(str, Enum):
    CAMPAIGN_STOPPED = "CAMPAIGN_STOPPED"
    DID_YOU_FORGET_THE_PLUS_SIGN = "DID_YOU_FORGET_THE_PLUS_SIGN"
    DND = "DND"
    EXTERNALLY_CONVERTED = "EXTERNALLY_CONVERTED"
    INVALID_FROM_NUMBER = "INVALID_FROM_NUMBER"
    INVALID_IVR_ID = "INVALID_IVR_ID"
    INVALID_TO_NUMBER = "INVALID_TO_NUMBER"
    LOCAL_REGULATION_ISSUE = "LOCAL_REGULATION_ISSUE"
    NOT_FOUND_IN_DB = "NOT_FOUND_IN_DB"
    OOB = "OOB"
    OOS = "OOS"
    PAYMENT_ISSUE = "PAYMENT_ISSUE"
    PROVIDER_SERVICE_ERROR = "PROVIDER_SERVICE_ERROR"
    PROVIDER_SERVICE_UNAVAILABLE = "PROVIDER_SERVICE_UNAVAILABLE"
    UNASSIGNED = "UNASSIGNED"
    UNFINISHED_CLEANUP = "UNFINISHED_CLEANUP"
    VVR = "VVR"

    def __str__(self) -> str:
        return str(self.value)
