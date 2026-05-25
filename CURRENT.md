# jaxl-python — Findings, bugs, edge cases, gaps

A **living ledger** of open work on `jaxl-python`. Every contributor (and AI assistant) reads from and writes to it so issues don't get re-discovered.

**Conventions:**
- When you fix an item, mark it `**FIXED** (YYYY-MM-DD, commit/PR)` in place — don't delete the entry. Keep the description so the next reader sees what was wrong.
- When you discover a new issue, add it under the right section with a stable ID (`B1`, `B2`, …) so it can be referenced in commits/PRs.
- When something turns out to be wrong/stale, mark it `~~strikethrough~~ **OBSOLETE** — <reason>`.

**Bootstrap audit**: 2026-05-11. Items below were surfaced from a structural read of `setup.cfg`, the hand-written `jaxl/api/` files (`_client.py`, `_sdk.py`, `base.py`, `cli.py`), and the `jaxl/api/resources/` module list. Deeper per-file audits will land as work touches those files.

## Bugs / suspicious patterns

### B1. `jaxl/api/cli.py::_init_subparsers` swallows every load-time error
[jaxl/api/cli.py:39-40](jaxl/api/cli.py:39) — the `except Exception as e: logging.info(f"Skipping {full_module_name} due to error: {e}")` block hides any failure during dynamic subparser loading. If a resource module imports incorrectly (typo, missing dep, syntax error after a refactor), the CLI silently *drops* that subcommand. The `logging.info` is below the default log level, so the user sees a CLI with fewer verbs than expected and no clue why. Suggested fix: log at `WARNING` or higher with a stack trace, OR re-raise unless an explicit env var (e.g. `JAXL_TOLERATE_CLI_LOAD_ERRORS=1`) is set.

### B2. `JaxlSDK` exposes 13 of 14 resource modules — `silence` is CLI-only
[jaxl/api/_sdk.py](jaxl/api/_sdk.py) — the SDK facade wires up `accounts`, `apps`, `calls`, `campaigns`, `devices`, `ivrs`, `kycs`, `members`, `messages`, `notifications`, `payments`, `phones`, `teams`. The `silence` resource (under [jaxl/api/resources/silence.py](jaxl/api/resources/silence.py)) exists as a CLI verb but has no `JaxlSilenceSDK` wrapper on `JaxlSDK`. Confirm whether this is deliberate (CLI-only audio-silence tooling) or an oversight to address.

### B3. `base.py::chat_with_ollama` has commented-out `max_tokens` left in body
[jaxl/api/base.py:266-267](jaxl/api/base.py:266) — `# "max_tokens": max_tokens,` is a dead line inside the `payload` dict, and the matching argument is commented out at the signature (lines 248-250). Minor cleanup — either wire it back in or remove the dead comments.

### B4. `BaseJaxlApp.send_audio` / `clear_audio` / `hangup` / `add_tag` return `False` / `None` by default
[jaxl/api/base.py:295-314](jaxl/api/base.py:295) — these primitives are wired up at runtime by the consuming application (via a `set_caller_funcs(...)`-style hook or by overriding the methods). The base-class default is to silently no-op. If a consumer forgets to wire the caller funcs and calls `await self.send_audio(...)`, they get `False` and *no* exception — an easy footgun to miss in tests. Suggested: log a `WARNING` from the base-class default ("send_audio invoked but no caller fn registered"), OR raise `NotImplementedError`. Low priority but documented.

### B5. Asymmetric defensive coding between CLI loader and SDK constructor
The CLI's `_init_subparsers` swallows resource-module import errors (B1). `JaxlSDK.__init__` has no equivalent guard — if a resource module fails to import, the SDK constructor hard-crashes. Pick one stance (fail-fast or tolerate-and-warn) and apply it everywhere.

## Gaps / things missing

### G1. No `JaxlSilenceSDK` on `JaxlSDK`
See B2. Decide intent and wire it up (or document the CLI-only carve-out in `_sdk.py`'s class docstring).

### G2. No tests visible for `BaseJaxlApp` handlers at the base-class level
The `tests/` dir exists but hasn't been inventoried in this audit. Downstream consumers test their own subclasses, but `BaseJaxlApp` itself — a public-contract surface — should have base-level tests that pin the handler signatures and the Pydantic model shapes, so a breaking change here gets caught in this repo's CI rather than in consumers. Followup: audit `tests/` and add base-class tests if missing.

### G3. mypy / pylint / isort configs are split across multiple files
`setup.cfg` has `[mypy]`, root has `.pylintrc` and `.isort.cfg`. Consider consolidating in `pyproject.toml` `[tool.*]` blocks. Low priority — current setup works.

### G4. `examples/` scripts are not exercised by CI
The example scripts under `examples/` are runnable demos but there's no smoke-test that imports each. Running them requires real credentials, but an import smoke (`python -c "import examples.streaming_aiagent"`) would catch breakage from generated-client changes. Low priority.

### G5. `python_requires` floor not verified in CI matrix
`setup.cfg` advertises `>= 3.9`. Confirm the GitHub Actions matrix covers 3.9 (the lowest claimed) — if it only tests 3.12, the floor is aspirational. Either align the matrix or raise the floor.

## Open questions

### Q1. Older `jaxl-python` versions may be pinned in downstream consumers
Some applications consuming this SDK may pin exact older versions (e.g. via `jaxl-python[app]==0.0.X`). When cutting a new release, coordinate with known consumers before bumping; provide a deprecation note in the changelog when removing or renaming public surface.

---

## Severity legend

- **HIGH** — actively biting users / breaking deploys. None currently in this list.
- **MEDIUM** — incorrect behaviour in narrow conditions OR observable footgun (`B4`).
- **LOW** — cosmetic / dead code / minor cleanup (`B3`, gaps).

Suggested triage: B1 (silent CLI load errors) → B4 (silent no-op `send_audio`) → G2 (`BaseJaxlApp` base-level tests) are the highest-leverage hardening items for the public contract.
