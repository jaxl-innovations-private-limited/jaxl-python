"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import Enum


class V1CallsReportRetrieveDateRange(str, Enum):
    DAY_BEFORE_YESTERDAY = "Day before yesterday"
    LAST_12_HOURS = "Last 12 hours"
    LAST_15_MINUTES = "Last 15 minutes"
    LAST_1_HOUR = "Last 1 hour"
    LAST_1_YEAR = "Last 1 year"
    LAST_24_HOURS = "Last 24 hours"
    LAST_2_DAYS = "Last 2 days"
    LAST_2_YEARS = "Last 2 years"
    LAST_30_DAYS = "Last 30 days"
    LAST_30_MINUTES = "Last 30 minutes"
    LAST_3_HOURS = "Last 3 hours"
    LAST_5_MINUTES = "Last 5 minutes"
    LAST_5_YEARS = "Last 5 years"
    LAST_6_HOURS = "Last 6 hours"
    LAST_6_MONTHS = "Last 6 months"
    LAST_7_DAYS = "Last 7 days"
    LAST_90_DAYS = "Last 90 days"
    PREVIOUS_MONTH = "Previous month"
    PREVIOUS_WEEK = "Previous week"
    PREVIOUS_YEAR = "Previous year"
    THIS_DAY_LAST_WEEK = "This day last week"
    THIS_MONTH = "This month"
    THIS_MONTH_SO_FAR = "This month so far"
    THIS_WEEK = "This week"
    THIS_WEEK_SO_FAR = "This week so far"
    THIS_YEAR = "This year"
    THIS_YEAR_SO_FAR = "This year so far"
    TODAY = "Today"
    TODAY_SO_FAR = "Today so far"
    YESTERDAY = "Yesterday"

    def __str__(self) -> str:
        return str(self.value)
