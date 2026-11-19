"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import hashlib


def sha256_hexdigest(data: str) -> str:
    """Returns sha256 hex digest of `data`.

    Jaxl APIs filter on hashed identifiers instead of the raw value
    e.g. `email_hash` when listing organization employees and `okey`
    when listing messages. SDK resources therefore accept real email
    IDs from the user and hash them here, right before the API call.
    """
    key = hashlib.sha256()
    key.update(data.encode())
    return key.hexdigest()
