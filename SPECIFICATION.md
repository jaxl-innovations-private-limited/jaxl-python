# Jaxl HTTP Webhook Specification

Jaxl Apps are simply an implementation of Jaxl HTTP Webhook Specification. If you cannot use
`jaxl-python` based apps, feel free to implement the below protocol in your existing HTTP
services to build custom call flows.

1. [Jaxl Webhook Requests](#requests)
   - [Setup Event (1)](#setup-event-1)
   - [Setup User Data Event (1)](#setup-user-data-event-1)
   - [IVR Option Event (2)](#ivr-option-event-2)
   - [IVR Option Data Event (2)](#ivr-option-data-event-2)
   - [Teardown Event (3)](#teardown-event-3)
2. [Jaxl Webhook Responses](#jaxl-webhook-responses)
   - [Prompts](#prompts)
     - [Prompt user to enter a numeric input followed by a star sign](#prompt-user-to-enter-a-numeric-input-followed-by-a-star-sign)
     - [Prompt user to choose one of the option](#prompt-user-to-choose-one-of-the-option)
     - [Speak and hangup](#speak-and-hangup)
   - [CTAs](#ctas)
     - [Send to phone](#send-to-phone)

## Jaxl Webhook Requests

### Setup Event (1)

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

### Setup User Data Event (1)

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

### IVR Option Event (2)

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

### IVR Option Data Event (2)

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

### Teardown Event (3)

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

## Jaxl Webhook Responses

You can return one of the following JSON objects as responses:

### Prompts

Prompts is a way to speak back to the user e.g.

#### Prompt user to enter a numeric input followed by a star sign

```json
{
  "prompt": ["Please enter your code followed by star sign"],
  "num_characters": "*"
}
```

#### Prompt user to choose one of the option

```json
{
  "prompt": [
    "You entered 657.",
    "Press 1 to confirm.",
    "Press 2 to re-enter your code."
  ],
  "num_characters": 1
}
```

#### Speak and hangup

```json
{
  "prompt": [
    "Thank you for calling Jaxl Innovations Private Limited.",
    "We are currently closed.",
    "Our team will get back to you as soon as possible"
  ],
  "num_characters": 0
}
```

### CTAs

CTA objects are a way to tell the Jaxl system that no more user input is expected and sends user to provided CTA.

#### Send to phone

```json
{
  "next": null,
  "phone": { "to_number": "+91XXXXXXXXXX", "from_number": null },
  "devices": null,
  "appusers": null,
  "teams": null
}
```
