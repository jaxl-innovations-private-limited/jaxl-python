# Jaxl CLI & Jaxl Python API Client

Use Jaxl from Python code or directly via the `jaxl` command-line tool.

1. [Install](#install)
2. [JAXL CLI](#jaxl-cli)
   - [Setup](#setup)
   - [Verify API Credentials & Auth Token](#verify-api-credentials--auth-token)
   - [Check Account Balance](#check-account-balance)
   - [Create an IVR](#create-an-ivr)
   - [Create a hangup IVR](#create-a-hangup-ivr)
   - [Configure IVR Options](#configure-ivr-options)
   - [List IVRs](#list-ivrs)
   - [List Purchased Jaxl Numbers](#list-purchased-jaxl-numbers)
   - [Assign a Phone Number to IVR by ID](#assign-a-phone-number-to-ivr-by-id)
   - [Place Outgoing Cellular Call with Existing IVR](#place-outgoing-cellular-call-with-existing-ivr)
   - [Place Outgoing Cellular Call with Ad-hoc IVR](#place-outgoing-cellular-call-with-ad-hoc-ivr)
   - [Dial-out 2-Party Conference with Ad-hoc IVR](#dial-out-2-party-conference-with-ad-hoc-ivr)
   - [Add External Phone Number to an Active Call](#add-external-phone-number-to-an-active-call)
   - [Add External Phone Number via Another Phone Number to an Active Call](#add-external-phone-number-via-another-phone-number-to-an-active-call)
   - [Add Agent to an Active Call](#add-agent-to-an-active-call)
   - [Remove External Phone Number from an Active Call](#remove-external-phone-number-from-an-active-call)
   - [Remove Agent from an Active Call](#remove-agent-from-an-active-call)
   - [Send Text Prompts (TTS) in an Active Call](#send-text-prompts-tts-in-an-active-call)
   - [Play Audio File in an Active Call](#play-audio-file-in-an-active-call)
   - [Mute a Participant in an Active Call](#mute-a-participant-in-an-active-call)
   - [Unmute a Participant in an Active Call](#unmute-a-participant-in-an-active-call)
   - [Hold a Participant in an Active Call](#hold-a-participant-in-an-active-call)
   - [Unhold a Participant in an Active Call](#unhold-a-participant-in-an-active-call)
   - [Get call details](#get-call-details)
   - [Receive Call Events via Webhook IVRs](#receive-call-events-via-webhook-ivrs)
   - [Realtime Streaming Audio](#realtime-streaming-audio)
   - [Realtime Streaming Speech Segments](#realtime-streaming-speech-segments)
   - [Realtime Streaming Transcriptions per Speech Segment](#realtime-streaming-transcriptions-per-speech-segment)
   - [AI Agent: Realtime Transcriptions STT ➡️ LLM/MCP ➡️ TTS](#ai-agent-realtime-transcriptions-stt-️-llmmcp-️-tts)
   - [List Subscriptions Payments](#list-subscriptions-payments)
   - [List Consumable Payments](#list-consumable-payments)
3. [Jaxl Python SDK](#jaxl-python-sdk)
   - [SDK Example Usage](#sdk-example-usage)
4. [JAXL HTTP Webhook Protocol](./SPECIFICATION.md)
5. [SDK Documentation](#sdk-documentation)
6. [Status](#status)

## Install

`pip install -U jaxl-python`

## JAXL CLI

```bash
jaxl -h
usage: jaxl [-h] {accounts,apps,calls,campaigns,devices,ivrs,kycs,members,messages,notifications,orgs,payments,phones,teams} ...

Jaxl CLI

positional arguments:
  {accounts,apps,calls,campaigns,devices,ivrs,kycs,members,messages,notifications,orgs,payments,phones,teams}
    accounts            Manage Accounts
    apps                Manage Apps for Webhooks and Streaming audio/speech/transcriptions.
    calls               Manage Calls (Domestic & International Cellular, App-to-App)
    campaigns           Manage Campaigns
    devices             Manage Devices
    ivrs                Manage IVRs (Interactive Voice Response)
    kycs                Manage KYCs
    members             Manage Members
    messages            Manage Messages (SMS, WA, RCS, Email, App-to-App)
    notifications       Manage Notifications (Android, iOS, Web)
    orgs                Manage Organizations
    payments            Manage Payments
    phones              Manage Phones (Landline, Mobile, TollFree)
    teams               Manage Teams (Managers, Phones)

options:
  -h, --help            show this help message and exit
```

### Setup

You will require the following to successfully run `jaxl` command line tool:

- `JAXL_API_CREDENTIALS`: Required to connect with Jaxl API Infrastructure
- `JAXL_API_AUTH_TOKEN`: Ensure necessary permissions are added to generated auth token.

Please visit [Jaxl Business Website](https://business.jaxl.com) or download the [Jaxl Business Android](https://play.google.com/store/apps/details?id=com.jaxl.business) or [Jaxl Business iOS](https://apps.apple.com/app/id6451118240) mobile application to access your credentials and auth tokens.

[![Setup](https://raw.githubusercontent.com/jaxl-innovations-private-limited/jaxl-python/main/setup.gif)](https://github.com/jaxl-innovations-private-limited/jaxl-python#setup)

Finally, setup following environment variables when trying `jaxl` command line.

```bash
export JAXL_API_CREDENTIALS=/path/to/jaxl-api-credentials.json
export JAXL_API_AUTH_TOKEN="....authentication token...."
```

### Verify API Credentials & Auth Token

```bash
jaxl accounts me
```

### Check Account Balance

```bash
jaxl accounts balance
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
  --message "Hello, we are calling via Jaxl IVR demo created from CLI.  Will hang up after speaking this message." \
  --hangup
```

### Configure IVR Options

This IVR option uses `--next` to send user to another IVR or to the same IVR for a "repeat this menu" experience.

```bash
jaxl ivrs options configure \
  --ivr <IVR ID TO CONFIGURE> \
  --input 0 \
  --message "Press 0 to repeat this menu" \
  --next <NEXT IVR ID>
```

> Use same value for &lt;IVR ID TO CONFIGURE&gt; and &lt;NEXT IVR ID&gt; to complete the "repeat this menu" experience.

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

### List Purchased Jaxl Numbers

```bash
jaxl phones list
```

You can also search for a specific purchased number:

```bash
jaxl phones list --e164 "+CC<Purchased Jaxl Number>"
```

### Assign a Phone Number to IVR by ID

All incoming calls to this number will send user to the assigned IVR.

```bash
jaxl phones ivrs \
  --e164 "+CC<Purchased Jaxl Number>" \
  --ivr <IVR ID>
```

### Place Outgoing Cellular Call with Existing IVR

Below command will execute the following flow:

- Places a call to &lt;Callee Number&gt;
- When answered sends them to an existing IVR ID
- Once IVR finishes, call continues to CTA returned by IVR

```bash
jaxl calls create \
  --to "+CC<Callee Number>" \
  --from "+CC<Purchased Jaxl Number>" \
  --ivr <IVR ID>
```

### Place Outgoing Cellular Call with Ad-hoc IVR

Below command will execute the following flow:

- Creates an Ad-hoc IVR using `--message` and `--option` flags
- Places a call to <Callee Number>
- When answered sends callee to the ad-hoc IVR
- Once IVR finishes, call continues to CTA returned by IVR

```bash
jaxl calls create \
  --to "+CC<Callee Number>" \
  --from "+CC<Purchased Jaxl Number>" \
  --message "Hello, we are calling you from MyCompany" \
  --option "1=Press 1 for sales:team=<Sales Team ID>" \
  --option "2=Press 2 for HR department:team=<HR Team ID>
```

### Dial-out 2-Party Conference with Ad-hoc IVR

Below command will execute the following flow:

- Dials out to Doctor first
- When doctor answers the call, they are asked to press 1 when ready
- If doctor presses 1, a second call is placed to the patient
- Ends the call when one but all others have hanged up the call

```bash
jaxl calls create \
  --to "+CC<Doctors Number>" \
  --from "+CC<Purchased Jaxl Number>" \
  --message "Hello Doctor, this is a call from MyCompany regarding your appointment with Mr. Patient Name. When ready please, " \
  --option "1=Press 1 to connect with the patient:phone=+CC<Patient Number>"
```

### Add External Phone Number to an Active Call

```bash
jaxl calls add --call-id 1234 --e164 +CC<Mobile Number>
```

### Add External Phone Number via Another Phone Number to an Active Call

```bash
jaxl calls add --call-id 1234 --e164 +CC<Mobile Number> --from-e164 +CC<Purchased Jaxl Number>
```

### Add Agent to an Active Call

```bash
jaxl calls add --call-id 1234 --email <someone@mycompany.com>
```

### Remove External Phone Number from an Active Call

```bash
jaxl calls remove --call-id 1234 --e164 +CC<Mobile Number>
```

### Remove Agent from an Active Call

```bash
jaxl calls remove --call-id 1234 --email <someone@mycompany.com>
```

### Send Text Prompts (TTS) in an Active Call

```bash
jaxl calls tts --call-id 1234 \
  --prompt "Hello, this text was injected in the middle of an active call"
```

### Play Audio File in an Active Call

```bash
jaxl calls play --call-id 1234 --audio /path/to/a/file/on/local/disk/or/public/url
```

> NOTE: Audio file must be in SLIN16 format i.e. 8KHz Mono 16-bit.

### Mute a Participant in an Active Call

Mute a specific cellular user in a call.

```bash
jaxl calls mute --call-id 1234 --e164 +CC<Mobile Number>
```

Mute an agent (Jaxl App User) in a call.

```bash
jaxl calls mute --call-id 1235 --email <someone@mycompany.com>
```

### Unmute a Participant in an Active Call

Unmute a specific cellular user in a call.

```bash
jaxl calls unmute --call-id 1234 --e164 +CC<Mobile Number>
```

Unmute a specific agent (Jaxl App User) in a call.

```bash
jaxl calls unmute --call-id 1235 --email <someone@mycompany.com>
```

### Hold a Participant in an Active Call

Put a cellular user on-hold in a call

```bash
jaxl calls hold --call-id 1234 --e164 +CC<Mobile Number>
```

Put an agent on-hold in a call

```bash
jaxl calls hold --call-id 1235 --email <someone@mycompany.com>
```

### Unhold a Participant in an Active Call

Unhold a cellular user in a call

```bash
jaxl calls unhold --call-id 1234 --e164 +CC<Mobile Number>
```

Unhold an agent in a call

```bash
jaxl calls unhold --call-id 1235 --email <someone@mycompany.com>
```

### Get call details

```bash
jaxl calls get --call-id 1234
```

### Receive Call Events via Webhook IVRs

Webhook IVRs can be used to programatically control the lifecycle of incoming and outgoing calls.
Jaxl will invoke configured webhook URL for subscribed call events. Handle the webhook request and
use Jaxl SDK to continue and customise the call flows.

To create a webhook IVR, use a `https://` URL as `--message` flag e.g.

```bash
jaxl ivrs create --message "https://example.com/jaxl-webhook-ivr"
```

Next, assign a number to webhook IVR as shown previously under [Assign a Phone Number to IVR by ID](#assign-a-phone-number-to-ivr-by-id). Now, all incoming calls on the number will start with
webhook before proceeding further.

To control flow of outgoing calls, use webhook IVR ID when placing an outbound call. See [Place Outgoing Cellular Call with Existing IVR](#place-outgoing-cellular-call-with-existing-ivr)

See [examples](https://github.com/jaxl-innovations-private-limited/jaxl-python/tree/main/examples) directory for working webhook examples.

### Realtime Streaming Audio

Refer to [examples](https://github.com/jaxl-innovations-private-limited/jaxl-python/tree/main/examples) directory for working streaming audio examples.

### Realtime Streaming Speech Segments

Refer to [examples](https://github.com/jaxl-innovations-private-limited/jaxl-python/tree/main/examples) directory for working streaming speech segments examples.

### Realtime Streaming Transcriptions per Speech Segment

Refer to [examples](https://github.com/jaxl-innovations-private-limited/jaxl-python/tree/main/examples) directory for working streaming transcription per speech segment examples.

### AI Agent: Realtime Transcriptions STT ➡️ LLM/MCP ➡️ TTS

Refer to [examples](https://github.com/jaxl-innovations-private-limited/jaxl-python/tree/main/examples) directory for working AI Agent examples.

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

### SDK Example Usage:

```python
from jaxl.api import JaxlSDK

os.environ.setdefault("JAXL_API_CREDENTIALS", "/path/to/jaxl-api-credentials.json")

os.environ.setdefault("JAXL_API_AUTH_TOKEN", "....authentication token...")

sdk = JaxlSDK()

response = sdk.calls.create(to="+CC<Callee Number>", from_="+CC<Purchased Jaxl Number>", ivr=1234)
response = sdk.calls.list(currency=2) # 1=USD, 2=INR
response = sdk.accounts.me()
```

## SDK Documentation

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
pip install -e ".[dev,docs]"

# Generate documentation
./docs.sh

# View documentation in browser
open docs/jaxl/index.html
```

## Status

[![pypi version](https://img.shields.io/pypi/v/jaxl-python)](https://pypi.org/project/jaxl-python/)

[![PyPi Monthly](https://img.shields.io/pypi/dm/jaxl-python)](https://pypi.org/project/jaxl-python/)

[![Python 3.x](https://img.shields.io/static/v1?label=Python&message=3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12&color=blue)](https://www.python.org/)

[![Checked with mypy](https://img.shields.io/static/v1?label=MyPy&message=checked&color=blue)](http://mypy-lang.org/)
