# jaxl-python

`jaxl-python` is the **open-source Python SDK + `jaxl` CLI** for the Jaxl API. It is the supported entry point for Python code (CLI or library) that talks to the Jaxl platform — managing calls, IVRs, devices, teams, payments, campaigns, streaming transcriptions, and AI agents.

This file orients new contributors (and AI assistants helping them) on the codebase. For end-user docs, see [README.md](README.md) and the rendered docs site (`docs.sh`).

## What this repo ships

Three deliverables in one package:

1. **`jaxl` CLI** — `jaxl <resource> <action>` for everyday Jaxl operations. Entry point: [`jaxl/api/cli.py`](jaxl/api/cli.py) → `entry_point()` (registered as a `console_scripts` in [`setup.cfg`](setup.cfg)). Subcommand dispatch is dynamic — every module under [`jaxl/api/resources/`](jaxl/api/resources/) that exports a `_subparser(parser)` function becomes a CLI verb. Adding a new verb = drop a file in that dir, no central registration needed.

2. **`JaxlSDK` Python facade** — [`jaxl/api/_sdk.py`](jaxl/api/_sdk.py). A Pythonic wrapper around the generated client, exposing `.accounts`, `.calls`, `.campaigns`, `.devices`, `.ivrs`, `.kycs`, `.members`, `.messages`, `.notifications`, `.payments`, `.phones`, `.teams`, `.apps`. The supported way to script against Jaxl from Python.

3. **`BaseJaxlApp` webhook + streaming base class** — [`jaxl/api/base.py`](jaxl/api/base.py). The contract any HTTP/WS-mode Jaxl application subclasses to receive webhook lifecycle events and bidirectional streaming audio. Defines:
   - **Lifecycle handlers**: `handle_configure`, `handle_setup`, `handle_user_data`, `handle_option`, `handle_mark`, `handle_teardown`.
   - **Streaming hooks**: `on_stream_connect`, `on_stream_disconnect`, `handle_speech_detection`, `handle_audio_chunk`, `handle_speech_chunks`, `handle_speech_segment`, `handle_transcription`.
   - **Outbound primitives**: `tts`, `send_audio`, `clear_audio`, `hangup`, `add_tag`.
   - **API/WS routing**: `api_routes()`, `websocket_routes()` for app-mode HTTP endpoints (requires the `[app]` extra: `uvicorn`, `fastapi`, `wsproto`).
   - Pydantic models the handlers receive: `JaxlWebhookRequest`, `JaxlWebhookState`, `JaxlStreamRequest`, `JaxlWebhookResponse`, `JaxlCtaResponse`.

The HTTP wire protocol that drives those handlers is documented in [SPECIFICATION.md](SPECIFICATION.md).

## Top-level layout

```
jaxl/                          (namespace package — `jaxl.*`)
└── api/
    ├── _client.py             # attestation / JWT / device-cred bootstrap
    ├── _sdk.py                # JaxlSDK facade
    ├── base.py                # BaseJaxlApp + webhook/stream Pydantic models
    ├── cli.py                 # `jaxl` CLI entry point + dynamic subparser load
    ├── client/                # generated OpenAPI client (DO NOT hand-edit)
    │   ├── api/v1/...         #   generated endpoint functions
    │   ├── models/...         #   generated response/request shapes
    │   ├── client.py          #   AuthenticatedClient
    │   ├── errors.py
    │   ├── types.py           #   Response[T] etc.
    │   └── _scm_version.py
    └── resources/             # per-resource CLI subcommand + SDK wrapper
        ├── accounts.py        #   each module: _subparser() + JaxlXxxSDK class
        ├── apps.py
        ├── calls.py
        ├── campaigns.py
        ├── devices.py
        ├── ivrs.py
        ├── kycs.py
        ├── members.py
        ├── messages.py
        ├── notifications.py
        ├── payments.py
        ├── phones.py
        ├── silence.py
        └── teams.py
examples/                      # example scripts (streaming SDK usage demos)
tests/                         # unit tests
docs/                          # mkdocs site sources (mkdocs.yml at root)
SPECIFICATION.md               # JAXL HTTP Webhook Protocol spec
README.md                      # public-facing intro + CLI cookbook
```

## Generated client (`jaxl/api/client/`)

The `jaxl/api/client/` tree is **machine-generated** from Jaxl's OpenAPI schema. Do not hand-edit files in there — your changes will be wiped on the next regeneration. The convention is: regenerate, then the hand-written code at `jaxl/api/_client.py`, `jaxl/api/_sdk.py`, `jaxl/api/base.py`, `jaxl/api/cli.py`, and `jaxl/api/resources/` is what you own.

If a generated endpoint is missing a behaviour you need, the fix is upstream in the OpenAPI schema, not in this repo.

## Build / test / lint

```bash
# Install in editable mode with the extras you need:
pip install -e .[dev,types,app]

# Type-check (strict):
.venv/bin/mypy -p jaxl

# Lint:
.venv/bin/pylint jaxl

# Format:
.venv/bin/isort jaxl

# Test:
.venv/bin/pytest tests/

# Docs:
./docs.sh                      # builds mkdocs site under site/
```

`mypy --strict` is the baseline (see `[mypy]` in [`setup.cfg`](setup.cfg)). New code should pass without `# type: ignore`.

## Extras (`setup.cfg` `[options.extras_require]`)

The package ships with named extras so consumers pull only what they need:

| Extra | Adds |
|---|---|
| `dev` | `isort`, `mypy`, `autoflake`, `pylint==3.3.3` |
| `docs` | `pdoc3`, `mkdocs`, `mkdocstrings`, `mkdocstrings-python` |
| `types` | type stubs (`types-python-dateutil`, `types-PyYAML`, `types-Pygments`, `types-ujson`, `types-requests`) |
| `app` | `uvicorn[standard]==0.35.0`, `fastapi==0.116.1`, `wsproto==1.3.2` — required when subclassing `BaseJaxlApp` and running as an HTTP/WS server |
| `grout` | `proxy.py==2.4.10` — for secure-tunnel scenarios |
| `silence` | `webrtcvad==2.0.10`, `setuptools==80.9.0` — for VAD-on-streams scenarios |
| `transcribe` | `openai-whisper==20250625`, `numpy==1.26.4` — for local STT scenarios |
| `openai` | `openai==2.1.0` |
| `release` | `build`, `twine` — release pipeline |

When you add a new dependency, decide whether it belongs as a new extra here or in a downstream app's own `install_requires`. Anything that is part of `BaseJaxlApp`'s contract goes here as an extra.

## Credentials + auth (`_client.py`)

API credentials live in a JSON file named like `jaxl-api-credentials.json` (or `jaxl-api-credentials-<env>.json`). Shape is `ApiCredentials` (see [`jaxl/api/_client.py`](jaxl/api/_client.py)): `watermark` + `app` + `client` keys. The `client.genesis_key` + `client.key` + `client.secret` triple powers RSA-based device attestation through the `v1_devices_attest_create` endpoint.

`attest()` is called at the top of every CLI invocation (`cli.py::main()`); it boots a JWT-signed `AuthenticatedClient` by either reusing a cached attestation under `~/.jaxl/cli/` or freshly attesting against the API.

Credentials files at the repo root (`jaxl-api-credentials*.json`) are personal — they are git-ignored and must never be committed.

## Conventions

- **Copyright header** on every `.py` (excluding `_scm_version.py`, `__pycache__/`, generated `client/`). Existing files have a 7-line proprietary-license header; match it.
- **`py.typed`** marker shipped so downstream consumers get full type-checking. Don't break it.
- **mypy strict + pylint + isort + autoflake** — enforce via `[options.extras_require].dev`.
- **`python_requires = >= 3.9`** — match this; it's the supported floor for consumers.
- **No hand edits inside `jaxl/api/client/`** (regenerated from upstream OpenAPI schema).

## Public API surface — versioning policy

Anything exported from `jaxl.api` (the SDK facade, `BaseJaxlApp`, the Pydantic models, the CLI verbs) is **public API**. Breaking changes — renaming a method, removing a handler, changing a Pydantic field type or required-ness, changing the shape of an `outcome_payload` — require a major version bump and a deprecation cycle. Adding a new method / handler / model field with a default is **additive** and ships in a minor version.

## Bugs / gaps

See [CURRENT.md](CURRENT.md). Stable IDs `B1`, `B2`, ….

## Note for AI assistants

This file is the public-facing orientation. If you're an AI assistant helping with this repo, **do not introduce references to private/internal sibling repos, coordination docs, or session-management infrastructure into any file checked into this repo** — `jaxl-python` is published as open source and its checked-in content must remain self-contained.
