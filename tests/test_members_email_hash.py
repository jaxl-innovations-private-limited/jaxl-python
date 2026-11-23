"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import hashlib
from typing import Any, Dict, List

import unittest
from unittest import mock

from jaxl.api.resources.members import _email_hashes, members_list


def _sha256(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()


class TestEmailHashes(unittest.TestCase):
    """Jaxl filters members on `email_hash`, never on the raw email ID.

    These are pure unit tests, no network and no credentials.
    """

    def test_no_emails_sends_no_filter(self) -> None:
        self.assertEqual(_email_hashes(None), [])
        self.assertEqual(_email_hashes([]), [])

    def test_lowercase_email_sends_single_digest(self) -> None:
        email = "member@example.com"
        self.assertEqual(_email_hashes([email]), [_sha256(email)])

    def test_email_is_hashed_exactly_as_given(self) -> None:
        """Jaxl only accepts lowercase email IDs, so no case folding here."""
        self.assertEqual(
            _email_hashes(["Member@Example.com"]),
            [_sha256("Member@Example.com")],
        )

    def test_multiple_emails_are_all_hashed_in_order(self) -> None:
        self.assertEqual(
            _email_hashes(["a@example.com", "b@example.com"]),
            [_sha256("a@example.com"), _sha256("b@example.com")],
        )

    def test_surrounding_whitespace_is_stripped(self) -> None:
        self.assertEqual(
            _email_hashes(["  member@example.com\n"]),
            [_sha256("member@example.com")],
        )

    def test_duplicate_digests_are_collapsed(self) -> None:
        email = "member@example.com"
        self.assertEqual(_email_hashes([email, email]), [_sha256(email)])

    def test_raw_email_is_never_sent(self) -> None:
        """Regression guard: the API returns zero results for a raw email ID."""
        email = "member@example.com"
        self.assertNotIn(email, _email_hashes([email]))


class TestMembersListForwardsEmailHash(unittest.TestCase):
    """`members_list` must forward the digests as the `email_hash` param."""

    # pylint: disable=no-self-use
    def _captured_kwargs(self, args: Dict[str, Any]) -> Dict[str, Any]:
        with mock.patch(
            "jaxl.api.resources.members.first_org_id", return_value=1
        ), mock.patch(
            "jaxl.api.resources.members.jaxl_api_client", return_value=mock.Mock()
        ), mock.patch(
            "jaxl.api.resources.members.v2_app_organizations_employees_list"
        ) as endpoint:
            members_list(args)
        return dict(endpoint.sync_detailed.call_args.kwargs)

    def test_emails_are_forwarded_as_digests(self) -> None:
        kwargs = self._captured_kwargs({"member_email": ["member@example.com"]})
        self.assertEqual(kwargs["email_hash"], [_sha256("member@example.com")])

    def test_without_emails_the_filter_is_empty(self) -> None:
        kwargs = self._captured_kwargs({})
        self.assertEqual(kwargs["email_hash"], [])

    def test_statuses_default_to_accepted(self) -> None:
        kwargs = self._captured_kwargs({})
        statuses: List[Any] = kwargs["status"]
        self.assertEqual([status.value for status in statuses], ["accepted"])


if __name__ == "__main__":
    unittest.main()
