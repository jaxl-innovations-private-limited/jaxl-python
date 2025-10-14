"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from jaxl.api.resources.accounts import JaxlAccountsSDK
from jaxl.api.resources.apps import JaxlAppsSDK
from jaxl.api.resources.calls import JaxlCallsSDK
from jaxl.api.resources.campaigns import JaxlCampaignsSDK
from jaxl.api.resources.devices import JaxlDevicesSDK
from jaxl.api.resources.ivrs import JaxlIVRsSDK
from jaxl.api.resources.kycs import JaxlKYCsSDK
from jaxl.api.resources.members import JaxlMembersSDK
from jaxl.api.resources.messages import JaxlMessagesSDK
from jaxl.api.resources.notifications import JaxlNotificationsSDK
from jaxl.api.resources.payments import JaxlPaymentsSDK
from jaxl.api.resources.phones import JaxlPhonesSDK
from jaxl.api.resources.teams import JaxlTeamsSDK


# pylint: disable=too-many-instance-attributes
class JaxlSDK:
    def __init__(self) -> None:
        self.accounts = JaxlAccountsSDK()
        self.payments = JaxlPaymentsSDK()
        self.devices = JaxlDevicesSDK()
        self.kycs = JaxlKYCsSDK()
        self.members = JaxlMembersSDK()
        self.teams = JaxlTeamsSDK()
        self.phones = JaxlPhonesSDK()
        self.ivrs = JaxlIVRsSDK()
        self.calls = JaxlCallsSDK()
        self.campaigns = JaxlCampaignsSDK()
        self.messages = JaxlMessagesSDK()
        self.notifications = JaxlNotificationsSDK()
        self.apps = JaxlAppsSDK()
