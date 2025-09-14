# Jaxl CLI & Jaxl Python API Client

Use Jaxl from Python code or directly via the `jaxl` command-line tool.

1. [Install](#install)
2. [JAXL CLI](#jaxl-cli)
   - [CLI Example Usage](#cli-example-usage)
3. [Jaxl Python SDK](#jaxl-python-sdk)
   - [SDK Example Usage](#sdk-example-usage)
4. [Documentation](#documentation)
5. [Status](#status)

## Install

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

### CLI Example Usage

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

### SDK Example Usage:

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

### Dial-out 2-Party Conference

```bash
jaxl calls create \
  --to "+91<Doctors Number>" \
  --from "+91<Purchased Number from Jaxl>" \
  --message "Hello Doctor, this is a call from MyCompany regarding your appointment with Mr. Patient Name. When ready please, " \
  --option "1=Press 1 to proceed with your appointment:phone=+91<Patient Number>"
```

## Documentation

```
# Clone this repository
git clone git@github.com:jaxl-innovations-private-limited/jaxl-python.git

# Enter cloned repo directory
cd jaxl-python

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install
pip install -e ".[dev]"

# Generate documentation
./docs.sh

# View documentation in browser
open docs/jaxl/index.html
```

## Status

[![Python 3.x](https://img.shields.io/static/v1?label=Python&message=3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12&color=blue&style=flat-square)](https://www.python.org/)

[![Checked with mypy](https://img.shields.io/static/v1?label=MyPy&message=checked&color=blue&style=flat-square)](http://mypy-lang.org/)
