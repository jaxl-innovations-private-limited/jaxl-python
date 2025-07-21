"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import Enum


class UnitEnum(str, Enum):
    CALLS = "calls"
    CAMPAIGNS = "campaigns"
    CONNECTIONS = "connections"
    DEVICES = "devices"
    EMPLOYEES = "employees"
    INR = "inr"
    MESSAGES = "messages"
    ORDERS = "orders"
    SECONDS = "seconds"
    TEAMS = "teams"
    USD = "usd"

    def __str__(self) -> str:
        return str(self.value)
