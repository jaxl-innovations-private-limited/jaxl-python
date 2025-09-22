# Jaxl HTTP Webhook Specification

Jaxl Apps are simply an implementation of Jaxl HTTP Webhook Specification. If you cannot use
`jaxl-python` based apps, feel free to implement the below protocol in your existing HTTP
services to build custom call flows.

1. [Setup Event (1)](#setup-event-1)
2. [Setup User Data Event (1)](#setup-user-data-event-1)
3. [IVR Option Event (2)](#ivr-option-event-2)
4. [IVR Option Data Event (2)](#ivr-option-data-event-2)
5. [Teardown Event (3)](#teardown-event-3)

## Setup Event (1)

- Triggered when a call enters your Webhook/IVR Flow ID.
- Webhook endpoint will receive following POST request:

  ```json
  {
    "pk": "INTEGER-FLOW-ID",
    "event": 1,
    "state": {
      "call_id": "INTEGER-CALL-ID",
      "from_number": "+91XXXXXXXXXX",
      "to_number": "+91YYYYYYYYYY",
      "direction": 1,
      "org": { "name": "Your Org Name As Registered With Jaxl Business Phone" },
      "metadata": null,
      "greeting_message": null
    },
    "option": null,
    "data": null
  }
  ```

## Setup User Data Event (1)

- Triggered when setup prompts for user data via DTMF inputs

  ```json
  {
    "pk": "INTEGER-FLOW-ID",
    "event": 1,
    "state": {
      "call_id": "INTEGER-CALL-ID",
      "from_number": "+91XXXXXXXXXX",
      "to_number": "+91YYYYYYYYYY",
      "direction": 1,
      "org": { "name": "Your Org Name As Registered With Jaxl Business Phone" },
      "metadata": null,
      "greeting_message": null
    },
    "option": null,
    "data": "123*"
  }
  ```

## IVR Option Event (2)

- Triggered when a single digit is received via DTMF input from the caller

  ```json
  {
    "pk": "INTEGER-FLOW-ID",
    "event": 2,
    "state": {
      "call_id": "INTEGER-CALL-ID",
      "from_number": "+91XXXXXXXXXX",
      "to_number": "+91YYYYYYYYYY",
      "direction": 1,
      "org": { "name": "Your Org Name As Registered With Jaxl Business Phone" },
      "metadata": null,
      "greeting_message": null
    },
    "option": "1",
    "data": null
  }
  ```

## IVR Option Data Event (2)

- Triggered when data via DTMF inputs is received while within an IVR option

  ```json
  {
    "pk": "INTEGER-FLOW-ID",
    "event": 2,
    "state": {
      "call_id": "INTEGER-CALL-ID",
      "from_number": "+91XXXXXXXXXX",
      "to_number": "+91YYYYYYYYYY",
      "direction": 1,
      "org": { "name": "Your Org Name As Registered With Jaxl Business Phone" },
      "metadata": null,
      "greeting_message": null
    },
    "option": "1",
    "data": "123*"
  }
  ```

## Teardown Event (3)

- Triggered when an incoming call ends.
- Webhook endpoint will receive following POST request:

  ```json
  {
    "pk": "INTEGER-FLOW-ID",
    "event": 3,
    "state": {
      "call_id": "INTEGER-CALL-ID",
      "from_number": "+91XXXXXXXXXX",
      "to_number": "+91YYYYYYYYYY",
      "direction": 1,
      "org": { "name": "Your Org Name As Registered With Jaxl Business Phone" },
      "metadata": null,
      "greeting_message": null
    },
    "option": null,
    "data": null
  }
  ```
