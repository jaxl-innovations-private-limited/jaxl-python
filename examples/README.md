# Jaxl Python SDK Examples

Jaxl SDK Apps implements [`BaseJaxlApp`](https://github.com/jaxl-innovations-private-limited/jaxl-python/blob/main/jaxl/api/base.py#L79) class. See `BaseJaxlApp` documentation for all possible lifecycle methods. Implement the lifecycle method you expect your custom calling flows to hit.

`examples` python module contains variety of use cases for you to quickly get started.

1. [Setup](#setup)
   - [Development Setup](#development-setup)
2. [Run](#run)
   - [Grout for Development](#grout-for-development)
   - [Webhook IVR](#webhook-ivr)
3. [Examples](#examples)
   - [Send To Phone](#send-to-phone)
   - [Request Code and Send To Phone](#request-code-and-send-to-phone)
   - [Request Code, Ask for Confirmation and Send To Phone](#request-code-ask-for-confirmation-and-send-to-phone)

## Setup

You must install `app` extras to build custom Jaxl SDK Apps.

```bash
pip install -U jaxl-python[app]
```

### Development Setup

When developing locally on your laptops and desktops, you will also need to install `grout` extras. `Grout` is a drop-in replacement of `Ngrok` and likes, built by the team at Jaxl.

```bash
pip install -U jaxl-python[grout]
```

## Run

```bash
jaxl apps run --app <Module:ClassName>
```

> `JAXL_SDK_PLACEHOLDER_CTA_PHONE` is only used by example code. You will not need this variable for your own production Jaxl SDK Apps

### Grout for Development

You will need to expose your IVR app publicly so that Jaxl servers can reach your app.

In a separate terminal, start `grout` to get a public URL:

```bash
grout http://127.0.0.1:9919
```

### Webhook IVR

Next go ahead and:

1. [Create a webhook IVR](https://github.com/jaxl-innovations-private-limited/jaxl-python?tab=readme-ov-file#receive-call-events-via-webhook-ivrs). Use your public url as `--message`.
2. [Assign a number to webhook IVR](https://github.com/jaxl-innovations-private-limited/jaxl-python?tab=readme-ov-file#assign-a-phone-number-to-ivr-by-id) app.

## Examples

### Send To Phone

```bash
export JAXL_SDK_PLACEHOLDER_CTA_PHONE=+USE-A-REAL-NUMBER-HERE
PYTHONPATH=. jaxl apps run --app examples:JaxlAppSendToCellular
```

### Request Code and Send To Phone

```bash
export JAXL_SDK_PLACEHOLDER_CTA_PHONE=+USE-A-REAL-NUMBER-HERE
PYTHONPATH=. jaxl apps run --app examples:JaxlAppSendToCellular
```

### Request Code, Ask for Confirmation and Send To Phone

```bash
export JAXL_SDK_PLACEHOLDER_CTA_PHONE=+USE-A-REAL-NUMBER-HERE
PYTHONPATH=. jaxl apps run --app examples:JaxlAppSendToCellular
```
