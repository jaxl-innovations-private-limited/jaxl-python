# Jaxl Python SDK Examples

Jaxl SDK Apps implements [`BaseJaxlApp`](https://github.com/jaxl-innovations-private-limited/jaxl-python/blob/main/jaxl/api/base.py#L79) class. See `BaseJaxlApp` documentation for all possible lifecycle methods. Implement the lifecycle method you expect your custom call flows to hit.

1. [Setup](#setup)
   - [Development Setup](#development-setup)
2. [Run](#run)
   - [Grout for Development](#grout-for-development)
   - [Webhook IVR](#webhook-ivr)
3. [Examples](#examples)
   - [Send To Phone](#send-to-phone)
   - [Request Code and Send To Phone](#request-code-and-send-to-phone)
   - [Request Code, Ask for Confirmation and Send To Phone](#request-code-ask-for-confirmation-and-send-to-phone)
   - [Realtime Streaming Audio](#realtime-streaming-audio)
   - [Realtime Streaming Speech Segments](#realtime-streaming-speech-segments)
   - [Realtime Streaming Transcriptions per Speech Segment](#realtime-streaming-transcriptions-per-speech-segment)
   - [AI Agent: Realtime Transcriptions STT ➡️ LLM/MCP ➡️ TTS](#ai-agent-realtime-transcriptions-stt-️-llmmcp-️-tts)
4. [Conversational AI Agents](#conversational-ai-agents)
5. [Production](#production)

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

View available flags:

```bash
jaxl apps run -h
usage: jaxl apps run [-h] [--app APP] [--host HOST] [--port PORT] [--transcribe] [--transcribe-model-size TRANSCRIBE_MODEL_SIZE] [--transcribe-language TRANSCRIBE_LANGUAGE]
                     [--transcribe-device TRANSCRIBE_DEVICE]

options:
  -h, --help            show this help message and exit
  --app APP             Dotted path to Jaxl SDK App module to run e.g. examples.app:JaxlApp
  --host HOST           Defaults to 127.0.0.1
  --port PORT           Defaults to 9919
  --transcribe          This flag is required to enable realtime transcription pipeline
  --transcribe-model-size TRANSCRIBE_MODEL_SIZE
                        Options are: tiny, base, small, medium, large
  --transcribe-language TRANSCRIBE_LANGUAGE
                        Options are: auto, ar, bg, bn, cs, da, de, el, en, es, et, fi, fil, fr, gu, he, hi, hr, hu, id, it, ja, kn, ko, lt, lv, ml, mr, nl, no, pa, pl, pt, ro, ru, sk, sl, sr, sv, ta, te, th, tr, uk, ur, vi, zh
  --transcribe-device TRANSCRIBE_DEVICE
                        Options are: auto, cpu, cuda, cuda:N, mps
```

Run your Jaxl SDK app:

```bash
jaxl apps run --app <Module:ClassName>
```

### Grout for Development

You will need to expose your IVR app publicly so that Jaxl servers can reach your app.

In a separate terminal, start [`grout`](https://github.com/abhinavsingh/proxy.py?tab=readme-ov-file#grout-ngrok-alternative) to get a public URL:

```bash
pip install -U jaxl-python[grout]
grout http://127.0.0.1:9919
```

### Webhook IVR

Next go ahead and:

1. [Create a webhook IVR](https://github.com/jaxl-innovations-private-limited/jaxl-python?tab=readme-ov-file#receive-call-events-via-webhook-ivrs). Use your public url as `--message`.
2. [Assign a number to webhook IVR](https://github.com/jaxl-innovations-private-limited/jaxl-python?tab=readme-ov-file#assign-a-phone-number-to-ivr-by-id) app.
3. For enable streaming apps, you must add `?stream` to your registered webhook IVR url.

## Examples

`examples` python module contains variety of use cases for you to quickly get started. Copy and paste the provided examples in your own code base and modify as needed.

- In example apps, `JAXL_SDK_PLACEHOLDER_CTA_PHONE` is only used for demonstration purposes.
- In your Jaxl SDK production apps, you will likely fetch target phone number from your databases.

```bash
export JAXL_SDK_PLACEHOLDER_CTA_PHONE=+USE-A-REAL-NUMBER-HERE
```

### Send To Phone

```bash
PYTHONPATH=. jaxl apps run --app examples:JaxlAppSendToCellular
```

### Request Code and Send To Phone

```bash
PYTHONPATH=. jaxl apps run --app examples:JaxlAppRequestCodeAndSendToCellular
```

### Request Code, Ask for Confirmation and Send To Phone

```bash
PYTHONPATH=. jaxl apps run --app examples:JaxlAppConfirmRequestedCodeAndSendToCellular
```

### Realtime Streaming Audio

```bash
PYTHONPATH=. jaxl apps run --app examples:JaxlAppStreamingAudioChunk
```

### Realtime Streaming Speech Segments

```bash
pip install -U jaxl-python[silence]
PYTHONPATH=. jaxl apps run --app examples:JaxlAppStreamingSpeechSegment
```

### Realtime Streaming Transcriptions per Speech Segment

```bash
# Requires ffmpeg installed on your system
pip install -U jaxl-python[silence,transcribe]
PYTHONPATH=. jaxl apps run --app examples:JaxlAppStreamingTranscription --transcribe
```

### AI Agent: Realtime Transcriptions STT ➡️ LLM/MCP ➡️ TTS

```bash
# Requires ffmpeg installed on your system
pip install -U jaxl-python[silence,transcribe]
# Defaults to gemma3:1b model, ensure you have the model installed
export JAXL_OLLAMA_URL=https://<llm.domain>/api/chat
PYTHONPATH=. jaxl apps run --app examples:JaxlAppStreamingAIAgent --transcribe
```

## Conversational AI Agents

When building conversational AI agents i.e. your app is expecting no IVR style DTMF inputs,
also add `&conv` to your app URL.

This will signal Jaxl Calling Infrastructure to not enforce certain rules only eligible for a classic IVR flow e.g. prompting the user when no input is received within timeout seconds.

NOTE: By default, Jaxl Calling Infrastructure assumes your app will return a prompt (text) to speak out in response from `handle_setup` method. For conversational AI agents, your AI agent likely won't be immediately ready with a response. For such scenarios, continue returning sample response below:

```python
async def handle_setup(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
   # Asynchronously initialize your AI Agent here
   # ...
   return JaxlWebhookResponse(prompt=["."], num_characters=-1)
```

- Returning `.` doesn't result in a speech
- `num_characters=-1` is currently mandatory for conversational bots because your app is expecting zero DTMF inputs

## Production

- In production, if not using grout, configure your load balancer to point to your Jaxl App instance IP:PORT service endpoint.

- You can also continue using `grout` in production environments but we highly recommended to reserve a dedicated grout url for your Jaxl App. This will make sure your `grout` public URL remains consistent across restarts.

  To reserve a `grout` url simply provide a custom URL to use e.g.

  ```bash
  grout http://127.0.0.1:9919 https://my-company-delivery-driver-app.jaxl.io
  ```

  For more instructions and dedicated domain setup refer to `Grout` documentation
