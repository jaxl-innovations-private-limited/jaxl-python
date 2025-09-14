# Jaxl CLI & Jaxl Python API Client

Use Jaxl from Python code or directly via the `jaxl` command-line tool.

1. [Install](#install)
2. [JAXL CLI](#jaxl-cli)
   - [CLI Example Usage](#cli-example-usage)
   - [Verify API Credentials & Auth Token](#verify-api-credentials--auth-token)
   - [Check Account Balance](#check-account-balance)
   - [List Purchased Jaxl Numbers](#list-purchased-jaxl-numbers)
   - [Create an IVR](#create-an-ivr)
   - [Create a hangup IVR](#create-a-hangup-ivr)
   - [Configure IVR Options](#configure-ivr-options)
   - [List IVRs](#list-ivrs)
   - [Place Outgoing Call and Send to existing IVR](#place-outgoing-call-and-send-to-existing-ivr)
   - [Place Outgoing Call and Send to Ad-hoc IVR](#place-outgoing-call-and-send-to-ad-hoc-ivr)
   - [Dial-out 2-Party Conference with Ad-hoc IVR](#dial-out-2-party-conference-with-ad-hoc-ivr)
   - [List Subscriptions Payments](#list-subscriptions-payments)
   - [List Consumable Payments](#list-consumable-payments)
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

jaxl accounts me

Response(status_code=<HTTPStatus.OK: 200>, content=b'... [redacted] ...')
```

### Verify API Credentials & Auth Token

```bash
jaxl accounts me
```

### Check Account Balance

```bash
jaxl accounts balance
```

### List Purchased Jaxl Numbers

```bash
jaxl phones list
```

### Create an IVR

```bash
jaxl ivrs create \
  --message "Hello, we are calling via Jaxl IVR demo created from CLI"
```

### Create a hangup IVR

This IVR will speak the message and then hangup the call.

```bash
jaxl ivrs create \
  --message "Hello, we are calling via Jaxl IVR demo created from CLI" \
  --hangup
```

### Configure IVR Options

This IVR option uses `--next` to send user to another IVR.

```bash
jaxl ivrs options configure \
  --ivr <IVR ID TO CONFIGURE> \
  --input 0 \
  --message "Press 0 to repeat this menu" \
  --next <NEXT IVR ID>
```

> Use &lt;IVR ID TO CONFIGURE&gt; as the &lt;NEXT IVR ID&gt; to complete the "repeat this menu" experience.

One of the CTA key flag must be provided. Allowed CTA keys are:

- `--next`: Send to another IVR
- `--phone`: Send to an external phone number
- `--devices`: Send to devices by ID
- `--appusers`: Send to app users (org employees) by ID
- `--teams`: Send to teams by ID

### List IVRs

```bash
jaxl ivrs list
```

### Place Outgoing Call and Send to existing IVR

```bash
jaxl calls create \
  --to "+91<Callee Number>" \
  --from "+91<Purchased Jaxl Number>" \
  --ivr <IVR ID>
```

### Place Outgoing Call and Send to Ad-hoc IVR

```bash
jaxl calls create \
  --to "+91<Callee Number>" \
  --from "+91<Purchased Jaxl Number>" \
  --message "Hello, we are calling you from MyCompany" \
  --option "1=Press 1 for sales:team=<Sales Team ID>" \
  --option "2=Press 2 for HR department:team=<HR Team ID>
```

### Dial-out 2-Party Conference with Ad-hoc IVR

```bash
jaxl calls create \
  --to "+91<Doctors Number>" \
  --from "+91<Purchased Jaxl Number>" \
  --message "Hello Doctor, this is a call from MyCompany regarding your appointment with Mr. Patient Name. When ready please, " \
  --option "1=Press 1 to connect with the patient:phone=+91<Patient Number>"
```

### List Subscriptions Payments

```bash
jaxl payments subscriptions list
```

### List Consumable Payments

```bash
jaxl payments consumables total
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
