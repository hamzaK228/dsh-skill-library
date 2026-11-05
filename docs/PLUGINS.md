# Плагины Codex

Снимок доступного локального кэша на 2026-11-05. Наличие в кэше не доказывает, что плагин подключён или доступен другому аккаунту. Код проприетарных плагинов не включён.

Откройте **Plugins** в Codex, найдите плагин по имени, установите и выполните вход в нужный сервис. Встроенные компоненты поставляются самим приложением. Если плагин отсутствует в вашем каталоге, его нельзя восстановить копированием этого репозитория. Версии ниже фиксируют исходный сетап, но каталог может предлагать другую версию.

| Плагин | Версия снимка | Источник | Лицензия метаданных |
|---|---|---|---|
| Browser | 26.1013.40934 | openai-bundled | Proprietary |
| Code Review | 26.1013.40934 | openai-bundled | Proprietary |
| codex-app-tools | 0.1.6 | openai-bundled | Proprietary |
| unified-computer-use | 26.1013.40934 | openai-bundled | not declared |
| Visualize | 1.0.50 | openai-bundled | Proprietary |
| Documents | 26.1030.10813 | openai-primary-runtime | MIT |
| PDF | 26.1030.10813 | openai-primary-runtime | MIT |
| Presentations | 26.1030.10813 | openai-primary-runtime | MIT |
| Spreadsheets | 26.1030.10813 | openai-primary-runtime | MIT |
| Template Creator | 26.1030.10813 | openai-primary-runtime | Proprietary |
| Context7 | 1.0.0 | openai-curated-remote | not declared |
| Railway | 1.0.0 | openai-curated-remote | not declared |
| Strix | 1.0.0 | openai-curated-remote | not declared |
| Cecil-IA Labs FFmpeg | 2.0.0 | openai-curated-remote | MIT |
| Cloud Environment | 0.1.2 | openai-curated-remote | not declared |
| Codex Security | 0.1.32 | openai-curated-remote | Proprietary |
| Codex Security Cloud | 0.1.1 | openai-curated-remote | Proprietary |
| Figma | 17.0.0 | openai-curated-remote | not declared |
| GitHub | 0.1.13-77c10e110b37 | openai-curated-remote | MIT |
| Gmail | 0.1.10 | openai-curated-remote | MIT |
| Google Calendar | 1.2.7 | openai-curated-remote | MIT |
| Google Contacts | 1.0.0 | openai-curated-remote | not declared |
| Google Drive | 0.1.22 | openai-curated-remote | MIT |
| HyperFrames by HeyGen | 0.1.2 | openai-curated-remote | Apache-2.0 |
| Impeccable | 4.3.1 | openai-curated-remote | Apache-2.0 |
| Default templates | 0.1.1 | openai-curated-remote | Proprietary |
| Pages | 0.1.26 | openai-curated-remote | Proprietary |
| Plugin Management | 0.1.0 | openai-curated-remote | Proprietary |
| Product Design | 0.1.56 | openai-curated-remote | Proprietary |
| Remotion | 4.0.534 | openai-curated-remote | MIT |
| Sites | 1.1.3 | openai-curated-remote | Proprietary |
| Supabase | 1.0.0 | openai-curated-remote | MIT |
| Vercel | 0.54.1 | openai-curated-remote | Apache-2.0 |
| Pets | 0.1.6 | openai-curated-remote | Proprietary |
| Writing Style | 0.1.1 | openai-curated-remote | Proprietary |

Машиночитаемый список: [setup/plugins.json](../setup/plugins.json). Не копируйте `auth.json`, cookies, ключи API, настройки MCP с секретами или кэш авторизации с чужого компьютера.

Скилл сам по себе не предоставляет сервер MCP, подключение Figma/GitHub/Supabase/Vercel или права к данным. Для FFmpeg нужен установленный FFmpeg; для видео — зависимости выбранного проекта; для FreeLLMAPI — отдельный локальный роутер и свои настройки. Репозиторий не устанавливает эти сервисы автоматически.
