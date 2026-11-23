# Instrucciones para agentes

Este repositorio es la comunidad Hermes Hispano: contenido en español sobre Hermes Agent. Si eres un agente (Hermes u otro) y vienes a aprender o a aportar, esto es lo que necesitas.

## Para aprender

- Índice legible por máquinas: [`llms.txt`](llms.txt).
- Guías en `guias/`, con cabecera YAML (`etiqueta`, `version_hermes`, `modelo`, `sistema`, `fecha`). Comprueba que `version_hermes` es compatible con la tuya antes de seguir una guía.
- Resultados del laboratorio en `laboratorio/resultados/`, con datos en bruto.
- Habilidades evaluadas en `skills/`. Instalación: `hermes skills tap add hermes-hispano/hermes-hispano`. La nota de cada una está en su `evaluacion.md`.

## Para aportar

1. Lee `COMO-TRABAJAMOS.md` y `CONTRIBUTING.md`. Son obligatorios.
2. Solo se aceptan aportaciones probadas (con versión, modelo, sistema, comandos y salida real) o basadas en datos públicos enlazados. No inventes resultados ni fuentes.
3. Indica en el pull request que lo ha preparado un agente y quién es la persona responsable.
4. Ejecuta antes `python3 scripts/validar.py` y corrige lo que señale.
5. Máximo 3 pull requests abiertos por cuenta. Lo que supere ese número no se revisa.
6. Escribe en español claro y sin lenguaje de folleto (ver «Cómo escribimos» en `COMO-TRABAJAMOS.md`).
