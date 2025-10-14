"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import argparse
from typing import Any, Dict

from jaxl.api._client import JaxlApiModule, jaxl_api_client
from jaxl.api.client.api.v1 import (
    v1_phonenumbers_list,
    v1_phonenumbers_partial_update,
    v1_phonenumbers_search_retrieve,
)
from jaxl.api.client.models.paginated_phone_number_list import (
    PaginatedPhoneNumberList,
)
from jaxl.api.client.models.patched_phone_number_request import (
    PatchedPhoneNumberRequest,
)
from jaxl.api.client.models.phone_number import PhoneNumber
from jaxl.api.client.models.phone_number_search_response import (
    PhoneNumberSearchResponse,
)
from jaxl.api.client.models.v1_phonenumbers_list_additional_status_item import (
    V1PhonenumbersListAdditionalStatusItem,
)
from jaxl.api.client.models.v1_phonenumbers_list_status import (
    V1PhonenumbersListStatus,
)
from jaxl.api.client.models.v1_phonenumbers_search_retrieve_iso_country_code import (
    V1PhonenumbersSearchRetrieveIsoCountryCode,
)
from jaxl.api.client.models.v1_phonenumbers_search_retrieve_resource import (
    V1PhonenumbersSearchRetrieveResource,
)
from jaxl.api.client.types import Response


def _phone_type(ptype: str) -> V1PhonenumbersSearchRetrieveResource:
    if ptype == "landline":
        return V1PhonenumbersSearchRetrieveResource.LOCAL
    if ptype == "mobile":
        return V1PhonenumbersSearchRetrieveResource.MOBILE
    if ptype == "tollfree":
        return V1PhonenumbersSearchRetrieveResource.TOLL_FREE
    raise NotImplementedError()


def phones_ivrs(args: Dict[str, Any]) -> Response[PhoneNumber]:
    existing = phones_list({"e164": args["e164"]})
    if (
        existing.status_code != 200
        or existing.parsed is None
        or len(existing.parsed.results) != 1
    ):
        raise ValueError(f"Unable to fetch details for {args['e164']}")
    return v1_phonenumbers_partial_update.sync_detailed(
        client=jaxl_api_client(
            JaxlApiModule.CALL,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        ),
        id=existing.parsed.results[0].id,
        json_body=PatchedPhoneNumberRequest(ivr=args["ivr"]),
    )


def phones_search(args: Dict[str, Any]) -> Response[PhoneNumberSearchResponse]:
    return v1_phonenumbers_search_retrieve.sync_detailed(
        client=jaxl_api_client(
            JaxlApiModule.CALL,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        ),
        iso_country_code=V1PhonenumbersSearchRetrieveIsoCountryCode[args["country"]],
        resource=_phone_type(args["type"]),
        region=args.get("region", None),
        contains=args.get("contains", None),
        locality=args.get("locality", None),
        fax_enabled=None,
        mms_enabled=None,
        sms_enabled=None,
        voice_enabled=None,
    )


def phones_list(args: Dict[str, Any]) -> Response[PaginatedPhoneNumberList]:
    ctype = args.get("type", "active")
    client = jaxl_api_client(
        JaxlApiModule.CALL,
        credentials=args.get("credentials", None),
        auth_token=args.get("auth_token", None),
    )
    e164 = args.get("e164")
    if ctype == "all":
        return v1_phonenumbers_list.sync_detailed(
            client=client,
            uid=e164,
        )
    if ctype == "active":
        return v1_phonenumbers_list.sync_detailed(
            client=jaxl_api_client(
                JaxlApiModule.CALL,
                credentials=args.get("credentials", None),
                auth_token=args.get("auth_token", None),
            ),
            status=V1PhonenumbersListStatus.SUCCESS,
            additional_status=[
                V1PhonenumbersListAdditionalStatusItem.SCHEDULED_FOR_RELEASE
            ],
            uid=e164,
        )
    if ctype == "inactive":
        return v1_phonenumbers_list.sync_detailed(
            client=jaxl_api_client(
                JaxlApiModule.CALL,
                credentials=args.get("credentials", None),
                auth_token=args.get("auth_token", None),
            ),
            status=V1PhonenumbersListStatus.RELEASED_TO_PROVIDER,
            additional_status=[
                V1PhonenumbersListAdditionalStatusItem.RELEASED_BY_PROVIDER
            ],
            uid=e164,
        )
    raise NotImplementedError()


def _subparser(parser: argparse.ArgumentParser) -> None:
    """Manage Phones (Landline, Mobile, TollFree)"""
    subparsers = parser.add_subparsers(dest="action", required=True)

    # list
    phones_list_parser = subparsers.add_parser("list", help="List all phones")
    phones_list_parser.add_argument(
        "--type",
        choices=["all", "active", "inactive"],
        default="active",
        help="Filter phones by type (default: active)",
    )
    phones_list_parser.add_argument(
        "--e164",
        required=False,
        default=None,
        help="Fetch a specific phone by its e164 number",
    )
    phones_list_parser.set_defaults(func=phones_list, _arg_keys=["type", "e164"])

    # ivrs
    phones_ivrs_parser = subparsers.add_parser(
        "ivrs",
        help="Assign/Unassign IVR to a phone number",
    )
    phones_ivrs_parser.add_argument(
        "--e164",
        required=True,
        help="Phone number to configure",
    )
    phones_ivrs_parser.add_argument(
        "--ivr",
        type=int,
        required=False,
        default=None,
        help="IVR ID that this phone must be assigned to.  "
        + "When not passed, removes any existing IVR assignment on this phone number",
    )
    phones_ivrs_parser.set_defaults(func=phones_ivrs, _arg_keys=["e164", "ivr"])

    # search
    phones_search_parser = subparsers.add_parser(
        "search",
        help="Search for available phone numbers for purchase",
    )
    phones_search_parser.add_argument(
        "--country",
        type=str,
        choices=[c.value for c in V1PhonenumbersSearchRetrieveIsoCountryCode],
        required=True,
        help="Country for which to show search results",
    )
    phones_search_parser.add_argument(
        "--type",
        type=str,
        choices=["landline", "mobile", "tollfree"],
        default="landline",
        help="Type of number to search for.  Default: landline",
    )
    phones_search_parser.add_argument(
        "--region",
        type=str,
        default=None,
        required=False,
        help="Only search for numbers from provided region e.g. MP, KA, TX",
    )
    phones_search_parser.add_argument(
        "--locality",
        type=str,
        default=None,
        required=False,
        help="Only search for numbers from provided locality e.g. Tulia",
    )
    phones_search_parser.set_defaults(
        func=phones_search,
        _arg_keys=["country", "type", "region", "locality"],
    )


class JaxlPhonesSDK:
    # pylint: disable=no-self-use
    def list(self, **kwargs: Any) -> Response[PaginatedPhoneNumberList]:
        return phones_list(kwargs)

    # pylint: disable=no-self-use
    def search(self, **kwargs: Any) -> Response[PhoneNumberSearchResponse]:
        return phones_search(kwargs)

    # pylint: disable=no-self-use
    def ivrs(self, **kwargs: Any) -> Response[PhoneNumber]:
        return phones_ivrs(kwargs)
