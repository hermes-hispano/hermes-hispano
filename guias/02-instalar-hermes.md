---
titulo: Instalar Hermes y tener tu primera conversación
etiqueta: probado
version_hermes: v0.23.4
modelo: claude-sonnet-5-5
sistema: Linux (contenedor Docker, kernel 6.8, 4 núcleos, 7 GB de RAM)
fecha: 2026-11-25
autor: hermes-hispano
---

# Instalar Hermes y tener tu primera conversación

Lo que hay en esta guía lo hemos hecho en Linux con la versión v0.23.4. Windows y macOS **no los hemos probado**: esas partes salen de la documentación oficial y lo indicamos en cada caso. Si los pruebas, cuéntanos cómo te fue (al final te decimos cómo).

Si aún no sabes si Hermes te encaja, empieza por [01-que-es-hermes.md](01-que-es-hermes.md).

## Antes de empezar

- Descarga siempre de `hermes-agent.nousresearch.com` o del GitHub de `NousResearch` ([Official Domains](https://hermes-agent.nousresearch.com/docs/getting-started/official-domains)).
- En Linux, macOS y WSL2 el instalador necesita Git, curl, tar y una herramienta de SHA-256. El propio instalador se baja su Python (3.14), Node.js y el resto de herramientas, así que no hace falta que los tengas ([Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation), apartado Prerequisites).
- Deja sitio en disco. En nuestro laboratorio la instalación ocupó 1,9 GB sin el navegador ni la herramienta de control del escritorio (probado).
- Vas a necesitar un proveedor de modelos (una suscripción o una clave). Lo eliges al final de la instalación. La guía [03-elegir-modelo.md](03-elegir-modelo.md) te ayuda a decidir.

## Opción 1: Linux, macOS o WSL2 (terminal)

Este es el camino que hemos probado. En una terminal:

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

Si prefieres leer el script antes de ejecutarlo, bájalo primero y luego lánzalo:

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh -o install.sh
less install.sh
bash install.sh
```

Qué hace, según la documentación: clona el código, prepara Python y las herramientas que necesita, instala por defecto un Chromium para navegar y el controlador del escritorio, crea el comando `hermes` en `~/.local/bin` y, si la terminal es interactiva, abre el asistente de configuración ([Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation)).

Opciones útiles del instalador ([Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation)):

| Opción | Para qué |
|---|---|
| `--skip-browser` | No instala el Chromium para navegar |
| `--skip-computer-use` | No instala el controlador del escritorio |
| `--non-interactive` | No pregunta nada; la configuración la haces después |

Al acabar, recarga la terminal para que encuentre el comando:

```bash
source ~/.bashrc   # o source ~/.zshrc si usas zsh
```

### Lo que pasó en nuestro laboratorio (probado)

Instalamos el 25-11-2026 en un Linux limpio con:

```bash
bash install.sh --non-interactive --skip-browser --skip-computer-use
```

- Terminó bien (código de salida 0) en 397 segundos, unos 6 minutos y medio.
- Ocupó 1,9 GB.
- `hermes --version` devolvió:

```text
Hermes Agent v0.23.4 (2026.9.24) · stable · local 8fc037444731
Install directory: /srv/hh-lab/home/.hermes/hermes-agent
Install method: git
Python: 3.14.9
```

En tu equipo la ruta será `~/.hermes/hermes-agent`. La nuestra es distinta porque el laboratorio usa una carpeta aislada.

## Opción 2: Windows nativo (no probado)

La documentación indica abrir PowerShell y ejecutar ([Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation)):

```powershell
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```

En Windows el código va a `%LOCALAPPDATA%\hermes\hermes-agent\` y el comando a `%LOCALAPPDATA%\hermes\bin\`. Las opciones equivalentes a las de Linux son `-SkipBrowser`, `-SkipComputerUse` y `-NonInteractive`. Si no tienes Git, el instalador puede bajarse uno ([Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation)).

También puedes usar WSL2 y seguir la opción 1 dentro de Linux.

## Opción 3: app de escritorio para Windows o macOS (no probado)

Se descarga desde la web oficial, [hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com/) ([Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation)):

- **Windows:** abre el archivo `.appinstaller` con el Instalador de aplicaciones de Windows.
- **macOS:** abre el DMG y arrastra `Hermes.app` a Aplicaciones. Solo funciona en Mac con Apple Silicon (M1 o posterior); los Mac con Intel no están soportados.

El paquete ya trae el agente, Python y las dependencias. Si instalaste por terminal y luego quieres la app, la documentación indica ejecutar `hermes desktop`.

En móviles Android con procesador aarch64 se usa el paquete de Termux, que tiene su propia guía oficial ([Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation)).

## Elegir proveedor y modelo

Con la instalación interactiva el asistente se abre solo. Si no, lánzalo tú:

```bash
hermes setup
```

En una instalación nueva te hace una sola pregunta, cómo quieres hacer funcionar Hermes, con estas opciones ([Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)):

- **Gratis, empezar ya:** un modelo gratuito (`nous/welcome`) sin cuenta ni clave. Solo aparece si está disponible, y solo cuando respondes tú en una terminal (no en contenedores ni scripts).
- **Entrar en Nous Portal:** inicias sesión en el navegador y tienes modelos y herramientas con tu suscripción. El atajo es `hermes setup --portal`.
- **Usar mi clave o una suscripción:** abre el selector de `hermes model` con Anthropic, OpenAI, OpenRouter, modelos locales y el resto.
- **Configuración completa** y **Pizarra en blanco** (lo mínimo, todo lo demás apagado), para quien quiere decidir cada cosa.

Para cambiar de proveedor más tarde no hace falta repetir todo:

```bash
hermes model
```

Hermes guarda las claves en `~/.hermes/.env` y el resto de ajustes en `~/.hermes/config.yaml`. Con `hermes config set` cada valor va a su archivo sin que tengas que pensar en ello ([Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)).

### Lo que hicimos en el laboratorio (probado)

Como instalamos sin preguntas, configuramos el proveedor a mano. Usamos Anthropic con una cuenta de Claude ya conectada en el equipo (Hermes lee las credenciales de Claude Code si las encuentra, según [Providers](https://hermes-agent.nousresearch.com/docs/integrations/providers)):

```bash
hermes config set model.provider anthropic
hermes config set model.default claude-sonnet-5-5
hermes config get model
```

Salida:

```text
default: claude-sonnet-5-5
provider: anthropic
base_url: ''
```

## Tu primera conversación

Para conversar ([Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)):

```bash
hermes          # interfaz clásica
hermes --tui    # interfaz nueva, la que recomienda la documentación
```

Para una sola pregunta sin abrir la interfaz, está el modo de una pasada:

```bash
hermes -z 'Hola. Preséntate en dos frases en español y dime qué puedes hacer en este ordenador.'
```

Resultados en el laboratorio (probado, 25-11-2026):

| Prueba | Tiempo | Coste estimado |
|---|---|---|
| Primera pregunta, con Hermes recién arrancado y uso de la terminal para mirar la fecha | 55,6 s | 0,038 $ |
| La misma pregunta repetida a los pocos minutos | 8,4 s | 0,009 $ |
| Ordenar 6 archivos en 3 carpetas | 9,3 s | 0,014 $ |
| «Responde solo con la palabra: funciona» | 6,2 s | 0,006 $ |

La primera vez es más lenta y más cara porque Hermes prepara cosas al arrancar y porque el modelo aún no tiene en caché las instrucciones del agente. El coste es la estimación que da Hermes con `--usage-file`. Lo comprobamos a mano con los precios públicos de Claude Sonnet 5.5 y coincide.

Para retomar la última conversación ([Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)):

```bash
hermes -c
hermes sessions list
```

Dentro de una conversación, escribe `/` para ver los comandos. `/help` los lista todos y `/model` cambia de modelo.

## `hermes doctor`: qué significan sus avisos

`hermes doctor` revisa la instalación y te dice qué falta ([Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation), apartado Troubleshooting). Esta es la parte relevante de lo que nos dio a nosotros, con el modelo ya configurado y funcionando (probado):

```text
◆ Configuration Files
  ✓ ~/.hermes/.env file exists
  ✓ API key or custom endpoint configured
  ✓ ~/.hermes/config.yaml exists
◆ Auth Providers
  ⚠ Nous Portal auth (not logged in)
  ⚠ OpenAI Codex auth (not logged in)
  ⚠ MiniMax OAuth (not logged in)
  ⚠ xAI OAuth (not logged in)
◆ API Connectivity
  ⚠ OpenRouter API (not configured)
◆ Tool Availability
  ⚠ discord (missing DISCORD_BOT_TOKEN)
  ⚠ feishu_doc (system dependency not met)
  ⚠ image_gen (image generation unavailable — check the provider selection and its key or SDK with 'hermes tools')
  ⚠ x_search (missing XAI_API_KEY)
◆ Skills Hub
  ⚠ Skills Hub directory not initialized (run: hermes skills list)
  ⚠ No GITHUB_TOKEN (60 req/hr rate limit — set in ~/.hermes/.env for better rates)
────────────────────────────────────────────────────────────
  Found 1 issue(s) to address:
  1. Run 'hermes setup' to configure missing API keys for full tool access
```

Cómo leerlo:

| Aviso | Qué quiere decir | Qué hacer |
|---|---|---|
| `API key or custom endpoint configured` con ✓ | Hay un proveedor configurado | Nada |
| `... auth (not logged in)` | No has entrado en ese proveedor | Nada, si no lo usas |
| `OpenRouter API (not configured)` | No tienes clave de OpenRouter | Nada, si usas otro proveedor |
| `system dependency not met` o `missing ..._KEY` en una herramienta | Esa herramienta opcional (Discord, imágenes, búsqueda en X...) no está lista | Solo si la quieres usar: `hermes tools` |
| `Skills Hub directory not initialized` | El catálogo de habilidades aún no se ha descargado | `hermes skills list` lo prepara |
| `No GITHUB_TOKEN` | Sin token, el catálogo de habilidades permite 60 consultas por hora | Opcional: pon un token de GitHub en `~/.hermes/.env` |
| `Found 1 issue: Run 'hermes setup' to configure missing API keys for full tool access` | Faltan claves de herramientas opcionales | Ver la nota de abajo |

Una cosa que nos sorprendió: ese «1 problema» salió igual antes de configurar el modelo y después, cuando Hermes ya contestaba bien. Además `hermes doctor` termina con código de salida 1. O sea, que ese aviso no te dice si el modelo funciona. Para saberlo, haz una pregunta corta como la de «Comprueba que funciona».

Si algo falla, la documentación recomienda este orden: `hermes doctor`, `hermes model`, `hermes setup`, `hermes sessions list` ([Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart), apartado Recovery Toolkit). Y `hermes doctor --fix` intenta arreglar solo lo que pueda.

## Poner Hermes en español

El ajuste es `display.language`:

```bash
hermes config set display.language es
```

Según la documentación, traduce un grupo pequeño de mensajes fijos: la pregunta de aprobación de comandos y algunas respuestas de los comandos con `/` en las apps de mensajería. No traduce las respuestas del agente, los registros, la salida de las herramientas ni los errores. Para que el agente te hable en español basta con escribirle en español o pedírselo. También puedes usar la variable `HERMES_LANGUAGE` para una sola sesión ([Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration), apartado UI language for static messages).

Lo que vimos en el laboratorio (probado):

- `hermes config set display.language es` se acepta. Si pones un idioma que no existe, lo rechaza y te da la lista:

```text
✗ Unknown language 'xx' for display.language. Available: en, af, ar, de, es, fr, ga, hu, it, ja, ko, pt, ru, tr, uk, zh, zh-hant.
```

- El paquete de español de la v0.23.4 (`locales/es.yaml`) tiene unas 4.000 líneas, con apartados para aprobaciones, mensajería, comandos `/`, la terminal y consejos. Por ejemplo, la pregunta de aprobación sale como `Opción [o/s/a/D]` con «una vez», «sesión», «siempre» y «denegar».
- Aun con `es` puesto, `hermes doctor` y `hermes status` siguen saliendo en inglés.
- Escribiendo en español, el agente contestó en español en todas las pruebas.

## Problemas frecuentes

Según la tabla de la documentación ([Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation)):

| Problema | Qué hacer |
|---|---|
| `hermes: command not found` | `source ~/.bashrc` o revisa que `~/.local/bin` está en el PATH |
| `API key not set` | `hermes model` para configurar el proveedor |
| Falta configuración tras actualizar | `hermes config check` y después `hermes config migrate` |

## Ayúdanos con Windows y macOS

No hemos probado ni Windows (nativo o app) ni macOS. Si lo instalas en uno de ellos, abre un issue «Problema en una guía» en el repositorio con: sistema y versión, método (script o app), salida de `hermes --version`, salida de `hermes doctor` (revisa que no tenga claves) y dónde te atascaste. Con eso marcaremos esa parte como probada.

## Comprueba que funciona

```bash
hermes --version | head -1
hermes -z 'Responde solo con la palabra: funciona'
```

Salida esperada (la nuestra, 25-11-2026):

```text
Hermes Agent v0.23.4 (2026.9.24) · stable · local 8fc037444731
funciona
```

El número de versión y el código final pueden cambiar en tu equipo. Si la segunda línea es un error de clave o de proveedor, vuelve a `hermes model`.

## Fuentes

Consultadas el 25-11-2026.

- Installation: https://hermes-agent.nousresearch.com/docs/getting-started/installation
- Quickstart: https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
- Configuration (UI language for static messages): https://hermes-agent.nousresearch.com/docs/user-guide/configuration
- AI Providers (Anthropic y credenciales de Claude Code): https://hermes-agent.nousresearch.com/docs/integrations/providers
- Official Domains: https://hermes-agent.nousresearch.com/docs/getting-started/official-domains
- Precios de Claude Sonnet 5.5 (para comprobar el coste): https://docs.claude.com/en/docs/about-claude/pricing
- Prueba propia: laboratorio Hermes Hispano, 25-11-2026. Comandos y salidas en bruto en [laboratorio/2026-11-25-guias-inicio.md](../laboratorio/2026-11-25-guias-inicio.md).
