"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.

## Install

Use Jaxl from Python code or directly via the jaxl command-line tool.

`pip install jaxl-python`

## JAXL CLI

```bash
jaxl -h
usage: jaxl [-h] {calls} ...

Jaxl CLI

positional arguments:
  {phones,calls,members,teams,ivrs,devices,payments,accounts,kycs,messages,campaigns,notifications}
    phones              Manage Phones
    calls               Manage Calls (Domestic & International Cellular, VoIP audio/video)
    members             Manage Members
    teams               Manage Teams
    ivrs                Manage IVRs (Interactive Voice Response)
    devices             Manage Devices
    payments            Manage Payments
    accounts            Manage Accounts
    kycs                Manage KYCs
    messages            Manage Messages (SMS, WA, RCS, Email, App-to-App)
    campaigns           Manage Campaigns
    notifications       Manage Notifications (iOS, Android, Web)

options:
  -h, --help  show this help message and exit
```

### Example Usage

```bash
export JAXL_API_CREDENTIALS=/path/to/jaxl-api-credentials.json

export JAXL_API_AUTH_TOKEN="....authentication token..."

jaxl calls list

Response(status_code=<HTTPStatus.OK: 200>, content=b'... [redacted] ...')
```

## Jaxl Python SDK

- Jaxl APIs is built upon [OpenAPI specification](https://www.openapis.org/)
- `jaxl-python` contains following Python modules:
    - `jaxl.api.client`: Generated OpenAPI SDK
    - `jaxl.api.resources`: Wrapper methods written to support `jaxl` CLI
    - `jaxl_api_client`: Helper function to retrieve an instance of `JaxlApiClient`

### Example Usage:

```python
from jaxl.api import JaxlApiModule, jaxl_api_client
from jaxl.api.client.api.v1 import v1_calls_list

os.environ.setdefault("JAXL_API_CREDENTIALS", "/path/to/jaxl-api-credentials.json")

os.environ.setdefault("JAXL_API_AUTH_TOKEN", "....authentication token...")

response = v1_calls_list.sync_detailed(
    client=jaxl_api_client(JaxlApiModule.CALL),
    currency=2, # 1=USD, 2=INR
)
```
"""

from ._client import JaxlApiModule, jaxl_api_client


__all__ = [
    "JaxlApiModule",
    "jaxl_api_client",
]
