"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import Enum


class CampaignUploadTypeEnum(str, Enum):
    GREETING_CONFIGURATION = "GREETING_CONFIGURATION"
    IVR_MENU = "IVR_MENU"
    MARKETPLACE = "MARKETPLACE"
    ORGANIZATION_EMPLOYEE = "ORGANIZATION_EMPLOYEE"
    ORGANIZATION_GROUP = "ORGANIZATION_GROUP"
    UNDEFINED = "UNDEFINED"

    def __str__(self) -> str:
        return str(self.value)
