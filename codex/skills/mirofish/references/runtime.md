# Local runtime

Verified against upstream commit `7657031ac01184afe2cb220f5ee3545573b5e843`. Commands below are guidance to execute only within a requested setup or run. They do not grant authorization for uploads, API consumption, or deployment.

## Discover and inspect

```bash
mirofish_dir="${MIROFISH_HOME:-$HOME/.local/share/mirofish}"
test -f "$mirofish_dir/backend/pyproject.toml"
test -f "$mirofish_dir/backend/run.py"
test -f "$mirofish_dir/frontend/package.json"
git -C "$mirofish_dir" rev-parse HEAD
```

If absent, report runtime unavailable. If installation is requested and the target does not exist, clone upstream there and select the inspected commit; never overwrite an existing checkout or discard its changes:

```bash
git clone https://github.com/666ghj/MiroFish.git "$mirofish_dir"
git -C "$mirofish_dir" checkout --detach 7657031ac01184afe2cb220f5ee3545573b5e843
```

Use Python 3.11 or 3.12 and `uv`. Use Node 22.12+ (or Node 20.19+); the pinned frontend Vite 7 lockfile requires `^20.19.0 || >=22.12.0`, despite README's older Node 18 minimum. Inspect dependency manifests before installing; installation can execute package lifecycle scripts. Do not run remote installer shell scripts.

## Requested setup

From the checkout root, install its lockfile dependencies:

```bash
cd "$mirofish_dir"
npm ci
npm ci --prefix frontend
uv sync --frozen --project backend --python 3.11
```

There is no application CLI entry point. Do not use `pip install mirofish` as a substitute.

For configuration, preserve an existing `.env`. If none exists, copy `.env.example` locally and have the user configure actual secrets without printing them. Required settings:

```dotenv
LLM_API_KEY=<configure-locally>
LLM_BASE_URL=<authorized-openai-compatible-provider-url>
LLM_MODEL_NAME=<authorized-model>
ZEP_API_KEY=<configure-locally>
FLASK_HOST=127.0.0.1
FLASK_DEBUG=False
```

`backend/run.py` refuses normal startup without both API keys. This version supports Zep Cloud; `ZEP_API_URL` is explicitly rejected. A locally installed skill is not a configured provider account. Do not invent keys or send provider requests just to test setup. Provider usage can incur charges; agree on the scenario budget before running it.

## Requested local run

Use two terminals from the checkout root. Backend:

```bash
cd "$mirofish_dir/backend"
FLASK_HOST=127.0.0.1 FLASK_DEBUG=False uv run python run.py
```

Frontend:

```bash
cd "$mirofish_dir"
npm --prefix frontend run dev -- --host 127.0.0.1
```

Open `http://127.0.0.1:3000`. Backend is `http://127.0.0.1:5001`; frontend proxies `/api` there. Keep the services local; upstream's default development scripts bind all interfaces. Stop launched services when the requested session ends unless the user requests persistence. Do not change unrelated services or expose the app publicly.

## Verification boundaries

Before credentials are configured, validate the checkout/manifests, installed dependency state, and optionally run `npm --prefix frontend run build`. Do not claim the application or simulation works from those checks.

Once an authorized backend is running, `curl --fail --silent --show-error http://127.0.0.1:5001/health` should return `{"service":"MiroFish Backend","status":"ok"}` (object key order may differ). This is a local health check only; it does not prove LLM access, Zep access, simulation quality, or successful report generation. A full scenario requires separately authorized seed-data upload and provider usage.

Useful source: `backend/app/config.py` (configuration), `backend/app/__init__.py` (health and route prefixes), `backend/app/api/graph.py`, `simulation.py`, and `report.py` (actual API contracts). Read only the relevant endpoint before invoking it.
