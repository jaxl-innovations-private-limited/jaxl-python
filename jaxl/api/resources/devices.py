"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import argparse
from typing import Any, Dict

from jaxl.api._client import JaxlApiModule, jaxl_api_client
from jaxl.api.client.api.v1 import v1_devices_list
from jaxl.api.client.models.paginated_device_list import PaginatedDeviceList
from jaxl.api.client.types import Response


# pylint: disable=unused-argument
def devices_list(args: Dict[str, Any]) -> Response[PaginatedDeviceList]:
    return v1_devices_list.sync_detailed(
        client=jaxl_api_client(
            JaxlApiModule.ACCOUNT,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        )
    )


def _subparser(parser: argparse.ArgumentParser) -> None:
    """Manage Devices"""
    subparsers = parser.add_subparsers(dest="action", required=True)

    # list
    devices_list_parser = subparsers.add_parser("list", help="List all devices")
    devices_list_parser.set_defaults(func=devices_list, _arg_keys=[])


class JaxlDevicesSDK:

    # pylint: disable=no-self-use
    def list(self, **kwargs: Any) -> Response[PaginatedDeviceList]:
        return devices_list(kwargs)
