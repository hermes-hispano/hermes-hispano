---
titulo: Qué es Hermes Agent y si te encaja
etiqueta: datos-publicos
version_hermes: v0.23.4
modelo: claude-sonnet-5-5 (solo en los ejemplos probados)
sistema: Linux (contenedor Docker, kernel 6.8)
fecha: 2026-11-25
autor: hermes-hispano
---

# Qué es Hermes Agent y si te encaja

Esta guía es para quien ha oído hablar de Hermes Agent y quiere saber, antes de instalar nada, qué hace, cuánto cuesta y de dónde bajarlo sin riesgo. Casi todo sale de la documentación oficial (enlazada en cada punto). Lo que hemos comprobado en nuestro laboratorio lo marcamos con «(probado)».

## Qué es

Hermes Agent es un agente de IA de código abierto de Nous Research. Tiene licencia MIT y puedes instalarlo en tu propio ordenador o servidor sin pagar por el programa ([Official Domains](https://hermes-agent.nousresearch.com/docs/getting-started/official-domains)).

Se usa desde la terminal, desde una app de escritorio o como bot en apps de mensajería como Telegram o Discord. También puede programar tareas que se ejecutan solas, guardar memoria entre sesiones y cargar habilidades (instrucciones para tareas concretas) ([Learning Path](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path)).

## Agente frente a chat

Un chat como los de las webs de IA te contesta con texto y tú copias, pegas y ejecutas. Un agente tiene herramientas: lee y escribe archivos, ejecuta comandos en la terminal, busca en la web y encadena varios pasos hasta acabar la tarea ([Learning Path](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path), tabla de funciones).

Un ejemplo de nuestro laboratorio (probado): le pedimos ordenar una carpeta con 6 archivos de prueba («facturas a facturas/, fotos a fotos/, el resto a otros/, no borres nada»). Hermes creó las carpetas, movió los 6 archivos a su sitio y respondió con el recuento. Tardó 9,3 segundos y usó 3 llamadas al modelo. Los comandos y las salidas están en [laboratorio/2026-11-25-guias-inicio.md](../laboratorio/2026-11-25-guias-inicio.md).

Como un agente actúa sobre tu equipo, conviene ir con cuidado. Antes de darle acceso a carpetas con datos importantes, lee la guía de instalación y prueba primero en una carpeta de pruebas.

## Qué cuesta

Hay dos cosas distintas:

- **El programa Hermes Agent es gratis.** Es código abierto con licencia MIT. La propia documentación avisa de que nadie legítimo te pedirá pagar por el agente ([Official Domains](https://hermes-agent.nousresearch.com/docs/getting-started/official-domains)).
- **El modelo de IA casi siempre se paga.** Hermes necesita al menos un proveedor de modelos para funcionar ([Providers](https://hermes-agent.nousresearch.com/docs/integrations/providers)). Puede ser una suscripción (Nous Portal), una clave de pago por uso (OpenRouter, Anthropic, OpenAI y muchos otros) o un modelo que corre en tu propio equipo con Ollama, que no cobra por uso pero pide un ordenador con bastante memoria ([Ollama local](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup)).

Lo que gastes depende del modelo y de cuánto lo uses. Como referencia (probado, 25-11-2026, Claude Sonnet 5.5 con los precios públicos de Anthropic), la tarea de ordenar la carpeta costó unos 0,014 dólares según la estimación que da Hermes. Una tarea larga de programación gasta mucho más. En la guía [03-elegir-modelo.md](03-elegir-modelo.md) explicamos cómo elegir proveedor y limitar el gasto.

## Si te encaja

Te encaja si:

- Quieres que la IA haga tareas en tu equipo (archivos, comandos, búsquedas) en vez de limitarse a contestarte.
- Te manejas con la terminal o estás dispuesto a aprender lo básico. Para Windows y macOS hay también app de escritorio ([Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation)).
- Quieres un asistente en Telegram, Discord u otra app de mensajería, o tareas programadas como un resumen diario.

Quizá no te encaje si:

- Solo quieres hacer preguntas y leer respuestas. Un chat web es más sencillo.
- No quieres pagar nada y tu ordenador tiene poca memoria. Los modelos locales que usan herramientas bien piden bastante: la guía oficial de Ollama recomienda `gemma4:31b`, que ocupa unos 20 GB y necesita 24 GB de RAM o más ([Ollama local](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup)).
- Tienes un Mac con procesador Intel: el instalador de escritorio para macOS es solo para Apple Silicon ([Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation)).

## De dónde descargarlo sin caer en webs falsas

Hermes es popular y ya hay webs falsas, cuentas de GitHub que suplantan al proyecto y correos que ofrecen «créditos». La documentación tiene una página con las fuentes oficiales ([Official Domains](https://hermes-agent.nousresearch.com/docs/getting-started/official-domains)). Lo que dice:

**Fuentes oficiales**

| Dirección | Para qué sirve |
|---|---|
| `hermes-agent.nousresearch.com` | Documentación, app de escritorio e instaladores `install.sh` e `install.ps1` |
| `hermes-assets.nousresearch.com` | Paquetes de escritorio, actualizaciones y repositorio de Termux |
| `portal.nousresearch.com` | Nous Portal: cuenta, suscripción y facturación |
| `inference-api.nousresearch.com` | La API de modelos de Nous (no tiene página web) |
| `github.com/NousResearch/hermes-agent` | Código fuente y versiones publicadas |
| `hub.docker.com/r/nousresearch/hermes-agent` | Imagen oficial de Docker (solo el espacio `nousresearch`) |

También son oficiales la cuenta [@NousResearch](https://x.com/NousResearch) en X y el Discord [discord.gg/NousResearch](https://discord.gg/NousResearch).

**La regla para no equivocarte**

Lee el nombre del dominio entero. Tiene que terminar en `nousresearch.com`. Una dirección como `hermes-agent.nousresearch.com.example.net` no es de Nous, aunque empiece igual. Tampoco lo son los dominios `.icu`, `.org` o `.ai` que llevan «hermes» en el nombre ([Official Domains](https://hermes-agent.nousresearch.com/docs/getting-started/official-domains)).

**Señales de estafa**

- Cualquier criptomoneda o «token» de Hermes o de Nous Research. No existe.
- Menciones masivas en GitHub con avisos «a la comunidad» y enlaces acortados (`bit.ly`, `goo.su`).
- Correos no pedidos que ofrecen créditos, versiones alojadas o acuerdos de colaboración.

Si recibes algo así, no abras el enlace, no metas contraseñas ni conectes carteras, y denuncia la cuenta en la plataforma donde la viste ([Official Domains](https://hermes-agent.nousresearch.com/docs/getting-started/official-domains)).

Hermes Hispano es una comunidad no oficial. No distribuimos instaladores: siempre te mandamos a las fuentes de la tabla.

## Comprueba que funciona

Antes de instalar, comprueba que el instalador sale del dominio oficial y que apunta al repositorio oficial de GitHub:

```bash
curl -sI https://hermes-agent.nousresearch.com/install.sh | head -1
curl -s https://hermes-agent.nousresearch.com/install.sh | grep -m1 REPO_URL
```

Salida esperada (la que obtuvimos el 25-11-2026):

```text
HTTP/2 200
REPO_URL="${HERMES_REPO_URL:-https://github.com/NousResearch/hermes-agent.git}"
```

Si el primer comando no da `200` o el segundo apunta a otro sitio que no sea `github.com/NousResearch/hermes-agent`, para y revisa que has escrito bien la dirección.

Siguiente paso: [02-instalar-hermes.md](02-instalar-hermes.md).

## Fuentes

Consultadas el 25-11-2026.

- Official Domains & Phishing Safety: https://hermes-agent.nousresearch.com/docs/getting-started/official-domains
- Learning Path: https://hermes-agent.nousresearch.com/docs/getting-started/learning-path
- Installation: https://hermes-agent.nousresearch.com/docs/getting-started/installation
- AI Providers: https://hermes-agent.nousresearch.com/docs/integrations/providers
- Run Hermes Locally with Ollama: https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup
- Precios de Claude (para el coste de la tarea de ejemplo): https://docs.claude.com/en/docs/about-claude/pricing
- Prueba propia: laboratorio Hermes Hispano, Hermes v0.23.4, claude-sonnet-5-5, 25-11-2026 (salidas en bruto en [laboratorio/2026-11-25-guias-inicio.md](../laboratorio/2026-11-25-guias-inicio.md)).
