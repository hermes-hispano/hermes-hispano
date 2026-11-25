# Laboratorio 25-11-2026: pruebas de las guías de inicio (01, 02 y 03)

Resultados en bruto de las pruebas citadas en las guías `guias/01-que-es-hermes.md`, `guias/02-instalar-hermes.md` y `guias/03-elegir-modelo.md`.

## Entorno

- Hermes Agent v0.23.4 (2026.9.24) · stable · local 8fc037444731, instalado con el instalador oficial (`install.sh --non-interactive --skip-browser --skip-computer-use`) en una carpeta aislada (`HOME` y `HERMES_HOME` propios). EXIT 0, 397 s, 1,9 GB, Python 3.14.9.
- Máquina: Linux 6.8 dentro de un contenedor Docker, 4 núcleos, 7 GB de RAM.
- Proveedor: `anthropic`, modelo `claude-sonnet-5-5`, autenticado con una cuenta de Claude ya conectada en el servidor (credenciales de Claude Code, que Hermes lee por su cuenta; no se copian claves al laboratorio).
- El contenedor trae una configuración gestionada en `/etc/hermes` que fija 51 ajustes. Para que el laboratorio sea limpio la anulamos con `HERMES_MANAGED_DIR` apuntando a una carpeta vacía. La prueba 1 se hizo antes de anularla; las demás, después.

Configuración aplicada:

```bash
hermes config set model.provider anthropic
hermes config set model.default claude-sonnet-5-5
hermes config set display.language es
hermes config get model
# default: claude-sonnet-5-5
# provider: anthropic
# base_url: ''
```

## Prueba 1: primera pregunta en frío

```bash
hermes -z 'Hola. Responde en español en una sola frase: ¿qué modelo eres y qué día es hoy según tu reloj del sistema? Usa la terminal para mirar la fecha.' --usage-file uso-1.json
```

Respuesta: `Soy claude-sonnet-5-5, de Anthropic, y según el reloj del sistema hoy es miércoles 25 de noviembre de 2026 (19:20 UTC, que son las 20:20 en Madrid).`

Tiempo: 55,6 s. EXIT 0.

```json
{
  "estimated_cost_usd": 0.0376713,
  "cost_status": "estimated",
  "cost_source": "provider_models_api",
  "input_tokens": 27891,
  "output_tokens": 129,
  "cache_read_tokens": 13893,
  "cache_write_tokens": 13992,
  "api_calls": 2,
  "model": "claude-sonnet-5-5",
  "provider": "anthropic",
  "completed": true
}
```

## Prueba 1b: la misma pregunta unos minutos después (laboratorio ya aislado)

Respuesta: `Soy claude-sonnet-5-5 (de Anthropic), y según el reloj del sistema hoy es miércoles 25 de noviembre de 2026 (19:26 UTC, es decir, las 20:26 en Madrid).`

Tiempo: 8,4 s. EXIT 0.

```json
{
  "estimated_cost_usd": 0.0088893,
  "cost_status": "estimated",
  "cost_source": "provider_models_api",
  "input_tokens": 27891,
  "output_tokens": 132,
  "cache_read_tokens": 25898,
  "cache_write_tokens": 1987,
  "api_calls": 2,
  "model": "claude-sonnet-5-5",
  "provider": "anthropic",
  "completed": true
}
```

## Prueba 2: presentación con `hermes chat --query-file --oneshot -Q`

```bash
hermes chat --query-file primera.txt --oneshot -Q
```

Tiempo: 15,0 s. EXIT 0. Respuesta:

```text
Hola, soy Claude Code, un asistente de programación y automatización que se ejecuta en tu terminal a través de Hermes. Puedo trabajar directamente en este equipo (directorio actual: /srv/hh-lab/pruebas) para ayudarte con tareas técnicas y de investigación.

Esto es lo que puedo hacer aquí:
- Ejecutar comandos de shell, y leer, buscar, crear y editar archivos.
- Escribir, probar y depurar código (Python con uv, entre otros) y revisar proyectos.
- Navegar por la web con un navegador real (páginas con JavaScript, formularios, clics) y buscar o extraer contenido online.
- Trabajar con documentos (PDF, Word, Excel, PowerPoint), correo, GitHub y otras herramientas mediante mis skills.
- Programar tareas recurrentes y delegar trabajo en subagentes en paralelo.

Dime qué necesitas y empezamos.
```

Nota: con la cuenta de Claude (OAuth), Hermes se conecta como Claude Code y el modelo se presenta así.

## Prueba 3: ordenar una carpeta (versión corta del caso 1)

Seis archivos de prueba: factura-enero.pdf, factura-febrero.pdf, foto-playa.jpg, foto-cumple.png, lista-compra.txt, contrato.docx.

```bash
hermes -z 'En la carpeta actual: mueve las facturas a facturas/, las fotos a fotos/ y el resto a otros/. No borres nada. Al acabar, dime en una línea cuántos archivos hay en cada carpeta.' --usage-file uso-tarea.json
```

Respuesta: `facturas/: 2 archivos, fotos/: 2 archivos, otros/: 2 archivos (contrato.docx y lista-compra.txt). No se ha borrado nada.`

Tiempo: 9,3 s. EXIT 0. Comprobación con `find . -type f | sort`:

```text
./facturas/factura-enero.pdf
./facturas/factura-febrero.pdf
./fotos/foto-cumple.png
./fotos/foto-playa.jpg
./otros/contrato.docx
./otros/lista-compra.txt
```

6/6 en su sitio, nada borrado. Pasa.

```json
{
  "estimated_cost_usd": 0.0136486,
  "cost_status": "estimated",
  "cost_source": "provider_models_api",
  "input_tokens": 42898,
  "output_tokens": 313,
  "cache_read_tokens": 40301,
  "cache_write_tokens": 2589,
  "api_calls": 3,
  "model": "claude-sonnet-5-5",
  "provider": "anthropic",
  "completed": true
}
```

Comprobación manual del coste con los precios de Claude Sonnet 5.5 (2 $/MTok entrada, 2,50 $/MTok escritura en caché de 5 min, 0,10 $/MTok lectura de caché, 10 $/MTok salida): 8 × 2 + 2.589 × 2,5 + 40.301 × 0,1 + 313 × 10 = 13.648,6 millonésimas de dólar = 0,01365 $. Coincide con la estimación de Hermes.

## Prueba 4: comprobación mínima

```bash
hermes --version | head -1
hermes -z 'Responde solo con la palabra: funciona' --usage-file uso-4.json
```

```text
Hermes Agent v0.23.4 (2026.9.24) · stable · local 8fc037444731
funciona
```

Tiempo: 6,2 s.

```json
{
  "estimated_cost_usd": 0.005861,
  "cost_status": "estimated",
  "cost_source": "provider_models_api",
  "input_tokens": 13850,
  "output_tokens": 5,
  "cache_read_tokens": 12005,
  "cache_write_tokens": 1841,
  "api_calls": 1,
  "model": "claude-sonnet-5-5",
  "provider": "anthropic",
  "completed": true
}
```

## Idioma (`display.language`)

```text
$ hermes config set display.language xx
✗ Unknown language 'xx' for display.language. Available: en, af, ar, de, es, fr, ga, hu, it, ja, ko, pt, ru, tr, uk, zh, zh-hant.
  Install a language pack plugin (hermes plugins install <pack>) or drop <HERMES_HOME>/locales/<id>.yaml to add one.
$ hermes config set display.language es
✓ Set display.language = es in .../config.yaml
```

- `locales/es.yaml`: 4.030 líneas (`en.yaml`: 4.146), con secciones approval, gateway, platform, slash, cli, display, explainer, tips, plan_usage y shared. Ejemplo: `prompt_long: "      Opción [o/s/a/D]: "`.
- Con `es`, `hermes doctor` y `hermes status` siguen en inglés.

## Gasto y límites

```text
$ hermes usage
📈 Account limits
Provider: anthropic
Current week: 98% remaining (2% used) • resets in 6d 17h (2026-12-02 12:59 UTC)
```

`hermes insights` (extracto): 3 sesiones, 12 mensajes, 3 llamadas a herramientas, 85.436 tokens, coste estimado ~0,06 $, modelo claude-sonnet-5-5, herramienta usada: terminal.

`agent.max_turns`: el `config.yaml` sembrado por el instalador trae `max_turns: 500` (la documentación dice que el valor por defecto es ilimitado). `hermes config set agent.max_turns 30` → `✓`, y `hermes config get agent.max_turns` → `30`.

## `hermes doctor` completo (modelo configurado, laboratorio aislado)

EXIT 1.

```text
┌─────────────────────────────────────────────────────────┐
│                 🩺 Hermes Doctor                        │
└─────────────────────────────────────────────────────────┘
◆ Security Advisories
  ✓ No active security advisories
◆ MCP Server Security
  ✓ No suspicious MCP stdio commands
◆ Python Environment
  ✓ Python 3.14.9
  ✓ SQLite 3.53.1
    → SQLite source id: 2026-05-05 10:34:17 c88b22011a54b4f6fbd149e9f8e4…
    → state.db: WAL journal mode (328.0 KB)
    → cron/executions.db: WAL journal mode (24.0 KB)
    → projects.db: WAL journal mode (44.0 KB)
    → kanban.db: WAL journal mode (116.0 KB)
  ✓ Runtime venv staged (/srv/hh-lab/home/.hermes/installs/0728d52c60afc16b/environments/955213ce542047c58370d4c30664240b/venv) (active in this process)
◆ SSL / CA Certificates
  ✓ TLS platform trust store configured; default SSL context available
◆ Required Packages
  ✓ OpenAI SDK
  ✓ Rich (terminal UI)
  ✓ python-dotenv
  ✓ ruamel.yaml
  ✓ HTTPX
  ✓ Croniter (cron expressions) (optional)
  ✓ python-telegram-bot (optional)
  ✓ discord.py (optional)
  ✓ Dashboard web surface (imports cleanly)
◆ Configuration Files
  ✓ Managed scope active: 0 config key(s), 0 env key(s) pinned by /srv/hh-lab/managed-vacio
    → managed dir set via HERMES_MANAGED_DIR=/srv/hh-lab/managed-vacio
  ✓ ~/.hermes/.env file exists
  ✓ API key or custom endpoint configured
  ✓ ~/.hermes/config.yaml exists
  ✓ Config version up to date (v54)
  ✓ No deprecated config keys or env vars
◆ xAI Model Retirement (May 15, 2026)
  ✓ No retired xAI models in config
◆ Session Reset (timers removed Sep 7, 2026)
  ✓ No idle/daily session_reset policy configured
◆ Auth Providers
  ⚠ Nous Portal auth (not logged in)
  ⚠ OpenAI Codex auth (not logged in)
    → No Codex credentials stored. Run `hermes auth add openai-codex --type oauth` to authenticate.
  ⚠ MiniMax OAuth (not logged in)
  ⚠ xAI OAuth (not logged in)
    → No xAI OAuth credentials stored. Select xAI Grok OAuth (SuperGrok / Premium+) in `hermes model`.
◆ Directory Structure
  ✓ ~/.hermes directory exists
  ✓ ~/.hermes/cron/ exists
  ✓ ~/.hermes/sessions/ exists
  ✓ ~/.hermes/logs/ exists
  ✓ ~/.hermes/skills/ exists
  ✓ ~/.hermes/memories/ exists
  ✓ ~/.hermes/cache/scratch/ is the scratch dir (TMPDIR; 5.9 KB, entries pruned after 24h idle)
  ✓ ~/.hermes/SOUL.md exists (persona configured)
  ✓ ~/.hermes/memories/ directory exists
    → MEMORY.md not created yet (will be created when the agent first writes a memory)
    → USER.md not created yet (will be created when the agent first writes a memory)
  ✓ ~/.hermes/state.db exists (1 sessions)
    → state.db logical size 476.0 KB, 119 pages, 0 free, WAL 1.0 MB
    → 4 messages, 1 sessions, journal_mode=wal, 1 process(es) holding the DB open (the host gateway (PID 24354) serving profiles default)
    → FTS tables: messages_fts, messages_fts_trigram
  ✓ ~/.hermes/cron/ store is writable
◆ Command Installation
  ✓ Hermes entry point exists (/srv/hh-lab/home/.hermes/hermes-agent/hermes)
  ✓ ~/.local/bin/hermes exists (non-symlink)
◆ External Tools
  ✓ git
  ✓ ripgrep (rg) (pm store) (faster file search)
    → Running inside a container — using local terminal backend (docker-in-docker is not configured by default)
  ✓ Docker (optional)
  ✓ Node.js
  ✓ Chromium (/opt/hermes/tools/chromium-1208/chrome-linux64/chrome)
  ✓ Root npm package deps (1 moderate vulnerability)
  ✓ web workspace deps (1 moderate vulnerability)
  ✓ ui-tui workspace deps (no known vulnerabilities)
◆ API Connectivity
  Running 44 connectivity checks in parallel…
  ✓ IPv6 route (no IPv6 route — IPv4 only)
  ⚠ OpenRouter API (not configured)
◆ Tool Availability
  ✓ browser
  ✓ browser-use
  ✓ catalog
  ✓ clarify
  ✓ code_execution
  ✓ computer_use
  ✓ connections
  ✓ cronjob
  ✓ delegation
  ✓ desktop_ui
  ✓ file
  ✓ memory
  ✓ onboarding
  ✓ project
  ✓ session_search
  ✓ skills
  ✓ terminal
  ✓ todo
  ✓ tts
  ✓ video
  ✓ vision
  ✓ kanban (runtime-gated; loaded only for dispatcher-spawned workers)
  ✓ web search (firecrawl)
  ✓ web extract (firecrawl)
  ⚠ a2a (system dependency not met)
  ⚠ browser-cdp (system dependency not met)
  ⚠ discord (missing DISCORD_BOT_TOKEN)
  ⚠ discord_admin (missing DISCORD_BOT_TOKEN)
  ⚠ feishu_doc (system dependency not met)
  ⚠ feishu_drive (system dependency not met)
  ⚠ image_gen (image generation unavailable — check the provider selection and its key or SDK with 'hermes tools')
  ⚠ video_gen (system dependency not met)
  ⚠ x_search (missing XAI_API_KEY)
◆ Skills Hub
  ⚠ Skills Hub directory not initialized (run: hermes skills list)
  ⚠ No GITHUB_TOKEN (60 req/hr rate limit — set in ~/.hermes/.env for better rates)
◆ Memory Provider
  ✓ Built-in memory active (no external provider configured — this is fine)
◆ NeMo Relay Plugins
  ✓ No Relay plugin files found
────────────────────────────────────────────────────────────
  Found 1 issue(s) to address:
  1. Run 'hermes setup' to configure missing API keys for full tool access
  Tip: run 'hermes doctor --fix' to auto-fix what's possible.
```

Antes de configurar el modelo (instalación del mismo día) el resultado final era el mismo: «Found 1 issue(s) to address: 1. Run 'hermes setup' to configure missing API keys for full tool access».
