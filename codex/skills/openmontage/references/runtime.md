# Runtime and pipeline entry

Upstream: https://github.com/OpenMontageInc/OpenMontage at `fecb9a1e3cc23ef84de30b272059457a427f16f8`, reviewed 2026-11-09.

Separate runtime requirements include Python 3.10+, FFmpeg and a supported Node release. Use the checkout's current `.node-version`, dependency manifests and lockfiles instead of assuming all Node 22 builds work. Upstream `make setup` installs Python/Node dependencies and Piper; it is not an adapter installation command or a safe no-op probe. Inspect its definitions before a requested runtime setup.

The registry exposes `registry.discover()`, `registry.support_envelope()` and `registry.provider_menu()` from `tools.tool_registry`. Run discovery only in an inspected, trusted checkout/environment; importing and discovering application modules executes application code. Do not dump environment values or provider secrets. A provider entry without working credentials/required dependencies is not a usable service.

Pipeline examples:

- `animated-explainer`: generated educational/topic video; manifest `pipeline_defs/animated-explainer.yaml` points to `skills/pipelines/explainer/*` (the director directory is not always identical to pipeline name).
- `documentary-montage`: retrieval-led actual footage and archival material.
- `clip-factory`, `podcast-repurpose`, `talking-head`: source-led repurposing and edits.
- `screen-demo`, `cinematic`, `animation`: inspect current manifests and available tools before selection.

Use manifest-declared `skill` and `required_skills` paths rather than constructing directory names. Resume using `checkpoint.get_next_stage()` as documented in `lib/checkpoint.py` and `skills/meta/checkpoint-protocol.md`. The optional Backlot UI (`python -m backlot open <project-id>`) observes project files; opening it does not run the production.

Both Remotion and HyperFrames can be used. Present their relevant tradeoff when selecting a new runtime, honor an existing user choice, then record `render_runtime`. Some workflows use local tools and open archives; others require provider keys and paid remote generation. No default dollar figure is authorization. Resource/model downloads can be substantial, and local setup is not equivalent to an offline-only pipeline.

Final convention: `projects/<project-id>/renders/final.mp4`, with stage JSON under `artifacts/` and media under `assets/`. Validate actual output and media rights for the requested delivery; do not equate open-archive discovery with clearance of every asset.
