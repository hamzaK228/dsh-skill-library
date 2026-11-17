---
name: openmontage
description: Run or resume OpenMontage video production pipelines with stage artifacts, capability discovery, creative checkpoints and verified final media.
---

# OpenMontage

Use for work in OpenMontage or when the user chooses its pipeline system. This is an entrypoint to the separate application, not a replacement engine or an installation of its many internal skills.

1. Resolve a user-selected existing checkout, optionally from `OPENMONTAGE_HOME`. If absent, explain that runtime setup is needed; do not improvise a production while claiming OpenMontage ran. Read [runtime notes](references/runtime.md).
2. In that checkout, read `AGENT_GUIDE.md` and `PROJECT_CONTEXT.md`, then only the relevant pipeline manifest and stage instructions. Preserve the current project engine. The internal provider skills remain project-scoped; do not globally install hundreds of them or overwrite existing Remotion/HyperFrames skills.
3. Distinguish reference inspiration from footage to edit. Reference input routes through `skills/meta/video-reference-analyst.md`; source footage routes through source-media review and a footage-led pipeline. Do not describe a video as analyzed based on its title alone.
4. Inspect the registry capability envelope/provider menu in the authorized local runtime. Choose the pipeline from `pipeline_defs/`, then propose the concept, output format, composition runtime, providers and budget based on actual availability. Preserve user-approved choices and checkpoint gates; no implicit provider switching or paid sample batches.
5. Initialize or resume `projects/<project-id>/` using the documented checkpoint contract. Read each stage's director skill before using that stage's tools. Keep canonical artifacts, checkpoints, assets and renders in the project directory. For tool entries with `agent_skills`, read the referenced project-local skill before calling the tool.
6. Validate media with ffprobe, sample frames/audio and the pipeline's delivery checks. Report the actual final artifact, runtime, provider usage and incomplete gates. A manifest's advertised stability is not proof of a successful run here.

Do authorized ordinary steps without repeated approval. Installing this adapter does not authorize application installation, model downloads, paid calls, uploads or publishing stages. [Provenance](SOURCE-NOTICE.md).
