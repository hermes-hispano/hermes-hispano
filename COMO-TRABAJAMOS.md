# Cómo trabajamos

## Qué publicamos

Solo dos tipos de contenido, marcados arriba de cada pieza:

- **Probado por nosotros.** Ejecutado en nuestro laboratorio. Indicamos versión de Hermes, modelo, sistema y fecha, y publicamos comandos y resultados en bruto.
- **Datos públicos.** Documentación oficial, notas de versión, benchmarks o estudios, con enlace a la fuente y fecha de consulta.

Lo que circula en redes (Reddit, X, Discord, vídeos) nos sirve de pista: lo comprobamos y lo publicamos como probado, o lo descartamos. No copiamos ni traducimos textos ajenos: si usamos una fuente, la contamos con nuestras palabras y la enlazamos.

## Cómo evaluamos una habilidad

Recomendamos una habilidad solo si mejora el resultado, y eso lo medimos con ella y sin ella.

1. 5 tareas reales del uso para el que existe, cada una con una comprobación automática del resultado.
2. Las mismas tareas con un modelo de referencia (hoy, Claude Sonnet 5.5), la misma configuración y un laboratorio limpio, con y sin la habilidad. 2 repeticiones por tarea; si no coinciden, una tercera.
3. Medimos éxito (porcentaje de tareas superadas), calidad (rúbrica de 0 a 5 publicada antes de la prueba), coste (tokens y euros) y tiempo, y revisamos la seguridad del código y del texto.
4. Nota de 0 a 10: éxito 50 %, calidad 25 %, coste 15 %, tiempo 10 %. Publicamos siempre la nota con y sin la habilidad.
5. Se recomienda si mejora al menos 15 puntos de éxito o 1 punto de nota, no empeora ninguna tarea de forma clara y no tiene hallazgos de seguridad.
6. Se repite con cada versión importante de Hermes o a los 3 meses.

## Cómo comparamos modelos

Solo cuando hay motivo (un modelo relevante nuevo o cada 3 meses), con un máximo de 4 modelos, los mismos casos comunes y 2 repeticiones. Publicamos la tabla completa, la configuración y los resultados en bruto, y citamos al lado los benchmarks públicos del mismo modelo. No declaramos ganadores generales: decimos qué conviene para cada tipo de tarea y a qué precio.

## Cómo aceptamos aportaciones

Una aportación entra si pasa las comprobaciones automáticas, indica versión de Hermes, modelo y sistema, la reproducimos en el laboratorio, cumple las normas de lenguaje y cita sus fuentes. Si falta algo, lo pedimos concretando qué. Respondemos en menos de 72 horas; si a los 30 días no hay respuesta, se cierra con una nota para reabrirla.

## Cómo escribimos

Como alguien que sabe del tema se lo explica a un compañero, en un español que se entienda en España y en Latinoamérica. Evitamos el lenguaje de folleto (descubre, potencia, revoluciona, solución), las coletillas («cabe destacar», «en resumen», «hoy más que nunca») y las estructuras de relleno. Datos concretos con su fuente, y «no lo sabemos» cuando no lo sabemos.

## Moderación

Código de conducta [Contributor Covenant 2.1](CODE_OF_CONDUCT.md) más una norma propia: nada de venta ni spam. Escalera: aviso privado, ocultar y aviso público, expulsión temporal, expulsión definitiva. El spam evidente y las estafas se retiran directamente.
