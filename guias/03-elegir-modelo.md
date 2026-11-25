---
titulo: Elegir proveedor y modelo sin sustos en la factura
etiqueta: probado
version_hermes: v0.23.4
modelo: claude-sonnet-5-5
sistema: Linux (contenedor Docker, kernel 6.8, 4 núcleos, 7 GB de RAM)
fecha: 2026-11-25
autor: hermes-hispano
---

# Elegir proveedor y modelo sin sustos en la factura

Hermes es gratis, pero el modelo de IA que lo mueve casi nunca lo es. Esta guía compara las opciones más habituales, explica dónde guarda Hermes cada clave y cómo vigilar y limitar lo que gastas.

Qué hemos probado y qué no:

- **Probado:** Anthropic con Claude Sonnet 5.5, la medición de tokens y coste, `hermes insights`, `hermes usage` y el límite de iteraciones.
- **No probado:** Nous Portal, OpenRouter, OpenAI y Ollama. Lo que contamos de ellos sale de sus páginas oficiales.

Todos los precios son los publicados el 25-11-2026, en dólares, sin impuestos. Cambian a menudo: mira siempre el enlace antes de decidir.

## Antes de elegir: dos requisitos

- El modelo tiene que admitir al menos 64.000 tokens de contexto. Con menos, Hermes lo rechaza al arrancar ([Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)).
- Tiene que saber usar herramientas (llamadas a funciones). Un modelo que solo charla no puede tocar archivos ni ejecutar comandos ([Ollama local](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup)).

Por esa razón la documentación desaconseja usar dentro del agente los modelos Hermes 4 de Nous: están pensados para conversar, no para encadenar herramientas ([Nous Portal](https://hermes-agent.nousresearch.com/docs/integrations/nous-portal)).

## Las opciones

### Nous Portal: una suscripción para todo

Es la opción que recomienda la documentación oficial. Con un inicio de sesión tienes más de 300 modelos y además las herramientas del Tool Gateway: búsqueda web, generación de imágenes, voz y navegador en la nube, sin claves aparte ([Nous Portal](https://hermes-agent.nousresearch.com/docs/integrations/nous-portal)).

```bash
hermes setup --portal    # instalación nueva
hermes model             # instalación existente: elige «Nous Portal»
hermes portal info       # ver si has entrado y qué pasa por el Portal
```

Cómo cobra, según la página de comparación de Nous ([Nous Portal vs OpenRouter](https://portal.nousresearch.com/compare/openrouter)):

- Hay un plan gratuito con modelos gratuitos y límites estándar. La búsqueda web dentro de Hermes es gratis en todos los planes.
- Los planes de pago (Plus, Super y Ultra) incluyen uso de modelos y herramientas con límites que se renuevan cada día, semana y mes. Los modelos caros consumen ese uso antes. Si se acaba, puedes pasar a un modelo gratuito o esperar a que se renueve.
- Las claves de API del Portal cobran por token de tu saldo de créditos, aparte del uso incluido en el plan.

Precio de cada plan: no lo hemos podido consultar. La página de suscripciones bloqueó nuestro acceso automático el 25-11-2026. Míralo en [portal.nousresearch.com/manage-subscription](https://portal.nousresearch.com/manage-subscription).

Dónde guarda la credencial: un token en `~/.hermes/auth.json`. No hace falta poner claves en `.env` ([Nous Portal](https://hermes-agent.nousresearch.com/docs/integrations/nous-portal)).

### OpenRouter: muchos modelos, pago por uso

Una sola clave te da acceso a modelos de muchos proveedores ([Providers](https://hermes-agent.nousresearch.com/docs/integrations/providers)). Se configura con `hermes model` o guardando `OPENROUTER_API_KEY` en `~/.hermes/.env`. También se puede entrar con el navegador: `hermes auth add openrouter --type oauth`.

Cómo cobra ([OpenRouter Pricing](https://openrouter.ai/pricing)):

- El modelo se paga al precio del proveedor original, sin recargo por petición.
- OpenRouter cobra una comisión al comprar créditos: 5,5 % en el plan Standard y 8 % en Business.
- El plan gratuito tiene más de 25 modelos gratuitos con un límite de 50 peticiones al día. Con Hermes se queda corto, porque una sola pregunta puede hacer varias llamadas al modelo (en nuestra prueba de ordenar archivos hubo 3).
- Los presupuestos y límites de gasto («Budgets & Spend Controls») están en Standard y Business, no en el gratuito.

### Anthropic (Claude) directo

Dos formas de pagar ([Providers](https://hermes-agent.nousresearch.com/docs/integrations/providers), apartado Anthropic):

- **Clave de API** (`ANTHROPIC_API_KEY`): pagas por token, aparte de cualquier suscripción de Claude.
- **Iniciar sesión con tu cuenta de Claude** (`hermes model`, opción OAuth): solo funciona con el plan Max **y** créditos de uso extra comprados. Hermes no gasta lo incluido en Max: todo lo que haga se cobra de los créditos extra. Con el plan Pro este camino no funciona. Es la fuente de sorpresas más habitual que señala la documentación.

Precios por millón de tokens ([precios de Claude](https://docs.claude.com/en/docs/about-claude/pricing)):

| Modelo | Entrada | Salida | Lectura de caché |
|---|---|---|---|
| Claude Opus 5.5 | 4 $ | 20 $ | 0,20 $ |
| Claude Sonnet 5.5 | 2 $ | 10 $ | 0,10 $ |
| Claude Haiku 5.5 (peticiones de hasta 100.000 tokens) | 0,10 $ | 0,50 $ | 0,01 $ |

Un detalle que vimos en el laboratorio (probado): entrando con la cuenta de Claude, a la pregunta «preséntate» el agente contestó «soy Claude Code». La documentación explica que por ese camino Hermes se conecta como Claude Code ([Providers](https://hermes-agent.nousresearch.com/docs/integrations/providers)). No es un fallo de la instalación.

### OpenAI

Con clave de API, el proveedor es `openai-api` y la clave va en `OPENAI_API_KEY`. También puedes entrar con una suscripción de ChatGPT o Codex desde `hermes model`, pero la documentación dice que aún no explica cómo cuenta ese uso contra los límites de tu plan ([Providers](https://hermes-agent.nousresearch.com/docs/integrations/providers)).

Precios por millón de tokens, tarifa estándar ([precios de la API de OpenAI](https://developers.openai.com/api/docs/pricing)):

| Modelo | Entrada | Salida | Entrada en caché |
|---|---|---|---|
| gpt-6.2-astra | 8 $ | 40 $ | 0,40 $ |
| gpt-6.2-sol | 2 $ | 10 $ | 0,10 $ |
| gpt-6.1-sol | 2 $ | 10 $ | 0,10 $ |

### Un modelo en tu ordenador con Ollama

No pagas por uso y tus conversaciones no salen de tu equipo, pero necesitas máquina ([Ollama local](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup)):

- Para usar herramientas, la guía oficial recomienda `gemma4:31b`: unos 20 GB en disco y 24 GB de RAM o más. Los modelos más pequeños de su tabla (`gemma2:9b`, `llama3.2:3b`) no usan herramientas.
- Sin tarjeta gráfica funciona, pero lento: un modelo de 31B en procesador da de 2 a 5 tokens por segundo y cada respuesta tarda de 30 a 120 segundos.
- Ollama trae por defecto un contexto de 2.048 tokens. Hay que subirlo a 64.000 con un Modelfile (`PARAMETER num_ctx 64000`).

Los pasos, resumidos de la guía oficial:

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull gemma4:31b
```

Después, en `hermes setup` o `hermes model`, elige «Custom Endpoint» con la dirección `http://localhost:11434/v1`, sin clave y con el nombre del modelo. O en `~/.hermes/config.yaml`:

```yaml
model:
  default: "gemma4:31b"
  provider: "custom"
  base_url: "http://localhost:11434/v1"
```

Si las respuestas tardan tanto que se cortan, la guía indica subir el tiempo de espera con `HERMES_API_TIMEOUT=1800` en `~/.hermes/.env`.

No lo hemos probado: nuestro laboratorio tiene 7 GB de RAM y no llega para `gemma4:31b`.

## Dónde va cada clave

Hermes separa las claves del resto de ajustes ([Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)):

| Qué | Dónde |
|---|---|
| Claves de API y tokens (`OPENROUTER_API_KEY`, `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`...) | `~/.hermes/.env` |
| Inicios de sesión por navegador (Nous Portal, ChatGPT/Codex y otros) | `~/.hermes/auth.json` |
| Proveedor, modelo y demás ajustes | `~/.hermes/config.yaml` |

La forma más segura de guardar una clave es `hermes model`, que te la pide, o `hermes config set NOMBRE_DE_LA_CLAVE valor`, que la manda al archivo correcto. Nunca pegues una clave en un issue, en un chat ni en una captura. Si se te escapa, revócala en la web del proveedor.

## Cómo vigilar y limitar el gasto

### 1. Pon un tope en el proveedor

En el propio Hermes no hemos encontrado un ajuste que corte por dinero. El tope en dinero se pone en la cuenta del proveedor:

- **Anthropic:** en la consola de Claude, apartado Spend limits ([platform.claude.com/settings/spend-limits](https://platform.claude.com/settings/spend-limits)), fijas un gasto máximo al mes por debajo del de tu nivel. Al llegar, las peticiones dan error hasta el mes siguiente ([Rate limits de Anthropic](https://docs.claude.com/en/api/rate-limits)).
- **OpenRouter:** presupuestos y límites de gasto en los planes de pago ([OpenRouter Pricing](https://openrouter.ai/pricing)). Con créditos de prepago, cada petición descuenta su coste de tu saldo ([OpenRouter FAQ](https://openrouter.ai/pricing)).
- **Nous Portal:** el plan tiene límites de uso que se renuevan cada día, semana y mes ([Nous Portal vs OpenRouter](https://portal.nousresearch.com/compare/openrouter)).

### 2. Mide lo que gasta cada tarea

En modo de una pasada, Hermes puede escribir un informe con tokens y coste estimado:

```bash
hermes -z 'Tu tarea aquí' --usage-file uso.json
```

Y para ver el acumulado de los últimos 30 días:

```bash
hermes insights
```

Con una cuenta de Claude conectada, `hermes usage` enseña cuánto queda del límite de la cuenta. En el laboratorio dio `Current week: 98% remaining (2% used)` (probado).

### 3. Pon límites dentro de Hermes

- **Iteraciones por pregunta:** `agent.max_turns` limita cuántas veces seguidas puede usar herramientas el agente. La documentación dice que por defecto no hay límite ([Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)). En nuestra instalación nueva el archivo `config.yaml` ya traía `max_turns: 500`. Para tareas cortas, el propio archivo sugiere de 20 a 30:

```bash
hermes config set agent.max_turns 30
```

- **Tiempo por conversación:** `hermes chat --run-budget SEGUNDOS` fija un máximo de tiempo. Al 80 % el agente recibe aviso para cerrar (ayuda de `hermes chat --help` en la v0.23.4).
- **Tamaño de cada llamada:** `compression.threshold_tokens` hace que Hermes resuma la conversación antes de llegar a esa cantidad de tokens. La documentación lo propone para fijar un techo de coste por llamada en modelos con contexto muy grande ([Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)).
- **Tareas secundarias más baratas:** resumir el historial, ver imágenes y otras tareas auxiliares usan por defecto tu modelo principal. Puedes mandarlas a uno más barato desde `hermes model`, opción «Configure auxiliary models» ([Providers](https://hermes-agent.nousresearch.com/docs/integrations/providers) y [Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)).

### 4. Aprovecha la caché

Las instrucciones del agente y la lista de herramientas se mandan en cada llamada. Cuando el proveedor las tiene en caché, se cobran mucho más baratas: en Claude Sonnet 5.5, 0,10 $ por millón en vez de 2 $ ([precios de Claude](https://docs.claude.com/en/docs/about-claude/pricing)). Por eso la primera pregunta de una sesión cuesta más que las siguientes.

## Coste real de nuestras pruebas (probado)

Laboratorio, 25-11-2026, Hermes v0.23.4, Anthropic, `claude-sonnet-5-5`. El coste es la estimación de `--usage-file`, que comprobamos a mano con los precios públicos de Claude Sonnet 5.5: coincide.

| Tarea | Llamadas | Tokens de entrada (de ellos, en caché) | Tokens de salida | Coste estimado | Tiempo |
|---|---|---|---|---|---|
| Primera pregunta en frío (mirar la fecha con la terminal) | 2 | 27.891 (13.893) | 129 | 0,0377 $ | 55,6 s |
| La misma pregunta, unos minutos después | 2 | 27.891 (25.898) | 132 | 0,0089 $ | 8,4 s |
| Ordenar 6 archivos en 3 carpetas | 3 | 42.898 (40.301) | 313 | 0,0136 $ | 9,3 s |
| «Responde solo con la palabra: funciona» | 1 | 13.850 (12.005) | 5 | 0,0059 $ | 6,2 s |

Lo que se ve: casi todo el coste está en la entrada (instrucciones del agente y herramientas, unos 14.000 tokens por llamada), no en la respuesta. La caché lo baja a menos de una cuarta parte.

En el laboratorio usamos una cuenta de Claude ya conectada, pero no sabemos de qué plan es, así que no podemos decir cómo se cobró. Si entras con OAuth, mira antes qué plan tienes: la regla de Max y los créditos extra de la sección de Anthropic es la que manda ([Providers](https://hermes-agent.nousresearch.com/docs/integrations/providers)).

## Comprueba que funciona

Mira qué proveedor y modelo tienes y cuánto cuesta una pregunta mínima:

```bash
hermes config get model
hermes -z 'Responde solo con la palabra: funciona' --usage-file uso.json
python3 -c "import json; d=json.load(open('uso.json')); print(d['model'], d['estimated_cost_usd'], d['api_calls'])"
```

Salida esperada (la nuestra):

```text
default: claude-sonnet-5-5
provider: anthropic
base_url: ''
funciona
claude-sonnet-5-5 0.005861 1
```

Con otro proveedor o modelo verás sus nombres y otro coste. Si el coste sale `0` con un proveedor de pago, puede que Hermes no conozca el precio de ese modelo: compáralo con el panel de tu proveedor.

## Fuentes

Consultadas el 25-11-2026.

- AI Providers: https://hermes-agent.nousresearch.com/docs/integrations/providers
- Nous Portal: https://hermes-agent.nousresearch.com/docs/integrations/nous-portal
- Run Hermes Locally with Ollama: https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup
- Quickstart: https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
- Configuration: https://hermes-agent.nousresearch.com/docs/user-guide/configuration
- Nous Portal vs OpenRouter (página de Nous): https://portal.nousresearch.com/compare/openrouter
- Suscripciones de Nous Portal (no accesible de forma automática ese día): https://portal.nousresearch.com/manage-subscription
- OpenRouter Pricing: https://openrouter.ai/pricing
- Precios de Claude: https://docs.claude.com/en/docs/about-claude/pricing
- Límites de gasto de Anthropic: https://docs.claude.com/en/api/rate-limits
- Precios de la API de OpenAI: https://developers.openai.com/api/docs/pricing
- Prueba propia: laboratorio Hermes Hispano, 25-11-2026. Comandos y salidas en bruto en [laboratorio/2026-11-25-guias-inicio.md](../laboratorio/2026-11-25-guias-inicio.md).
