"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import Enum


class ScenarioEnum(str, Enum):
    CALL = "CALL"
    CONTACT = "CONTACT"
    DND = "DND"
    IVR = "IVR"
    OOO = "OOO"
    PHONE_NUMBER = "PHONE_NUMBER"
    VOICE_MAIL = "VOICE_MAIL"

    def __str__(self) -> str:
        return str(self.value)
