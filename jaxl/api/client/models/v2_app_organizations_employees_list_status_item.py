"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import Enum


class V2AppOrganizationsEmployeesListStatusItem(str, Enum):
    ACCEPTED = "accepted"
    CANCELED = "canceled"
    INVITED = "invited"
    REJECTED = "rejected"
    REMOVED = "removed"

    def __str__(self) -> str:
        return str(self.value)
