# Cómo aportar

Gracias por querer echar una mano. Antes de nada, lee [cómo trabajamos](COMO-TRABAJAMOS.md): explica qué publicamos y cómo lo comprobamos.

## Qué puedes aportar

- **Una guía** en `guias/`: algo que resolviste y que a otros les costará.
- **Una habilidad** en `skills/<nombre>/SKILL.md`.
- **Un experimento** en `laboratorio/`: una medición con método.
- **Probar una guía** en tu sistema y contarnos dónde te atascaste (abre un issue «Problema en una guía»).

## Requisitos

1. Probado, indicando versión de Hermes (`hermes --version`), modelo y sistema.
2. Con los comandos para comprobar que funciona.
3. Sin claves, tokens ni datos personales. Una comprobación automática lo busca en cada propuesta.
4. Si se basa en otra fuente, enlazada y contada con tus palabras.
5. En español claro, sin lenguaje de folleto.

## Formato de una guía

Cada guía empieza con esta cabecera:

```markdown
---
titulo: Instalar Hermes en Linux
etiqueta: probado        # probado | datos-publicos
version_hermes: v0.23.3
modelo: claude-sonnet-5-5
sistema: Ubuntu 24.04
fecha: 2026-11-23
autor: tu-usuario
---
```

## Formato de una habilidad

`skills/<nombre>/SKILL.md` con cabecera `name` (igual que la carpeta) y `description` (menos de 1024 caracteres). Incluye en la carpeta `pruebas.md` con las tareas con las que la probaste. Nosotros la evaluamos con y sin ella antes de aceptarla.

## Cómo enviarla

1. Haz un fork y una rama.
2. Añade tu aportación y abre un pull request rellenando la plantilla.
3. Las comprobaciones automáticas se ejecutan solas. Después la reproducimos en el laboratorio y te respondemos en menos de 72 horas.

## Agentes

Si eres un agente, lee [AGENTS.md](AGENTS.md). Las aportaciones hechas por agentes se aceptan si lo indican y pasan las mismas pruebas.
