---
name: presupuesto-tokens
description: Control de gasto de tokens del director. Se ejecuta justo antes de cada tarea cara (render, revisión, Chrome, ronda de corrección, lote de ideas, consulta a varios agentes) para decidir si vale la pena, cómo abaratarla sin bajar la calidad del video y apuntar lo gastado.
---

# Skill: presupuesto de tokens (director)

Pedido del creador (2026-11-03): «reducir los tokens lo más que se pueda pero sin perder la calidad de videos que tenemos». La usa **solo el director** (`shorts-executive-producer`), sin lanzar ningún agente para ello: es una comprobación de 30 segundos antes de encargar trabajo caro.

## 1 · Cuándo se ejecuta (puertas)

Antes de **cualquiera** de estos encargos. Si la tarea no está en la lista, no hace falta.

| Puerta | Coste medido (2026-11-03) | Pregunta clave |
|---|---|---|
| Render o re-render del editor | 180–260K | ¿Puedo juntar más cambios en esta pasada? |
| Prueba de 10 s con piezas nuevas | 382K (soldado) | ¿El plan usa el catálogo? Más de 3 piezas nuevas encarece |
| Guion + escenas (creative) | ~104K | ¿Ya está el análisis del original? (evita la v2) |
| Concepto (strategist) | ~87K | — |
| Revisión del reviewer | ~150K completa · ~83K acotada | ¿Completa o solo de lo que cambió? |
| Investigación con Chrome (social) | ~235K Opus · ~62K Sonnet | ¿Hace falta ya o hay tema en cola? |
| Lote de ideas / reevaluación (strategist) | 90–115K | ¿Hay ya ideas guardadas sin usar? |
| Consulta a 2+ agentes | ~45K cada uno | ¿Basta con uno? |
| Ronda de corrección nueva | editor + reviewer ≈ 350K | ¿Es MAJOR/CRITICAL o se puede aceptar/agrupar? |

Coste de referencia por video completo (concepto → entrega): **~0.9–1.2M tokens**. Si un proyecto pasa de 1.5M, avisar al creador.

## 2 · Checklist (responder en la cabeza, no en archivo)

1. **¿Es necesario ahora?** Si el resultado no desbloquea el siguiente paso del creador, se pospone y se agrupa.
2. **¿Se puede agrupar?** Juntar todos los cambios pendientes del mismo video en **una** pasada del editor y **una** revisión. Nunca dos renders seguidos por cambios pequeños.
3. **¿Qué alcance mínimo?**
   - Revisión: completa solo en el primer render. En rondas de corrección, el reviewer valida **solo los hallazgos y lo que tocó el editor**, más especificaciones (LUFS, duración, bucle).
   - Editor: si solo cambia el audio, render solo de audio y vídeo copiado (como R10).
   - Chrome: solo las cuentas y fechas necesarias; reutilizar los datos de `publicacion/cuentas/` si tienen < 4 días.
4. **¿Qué modelo/esfuerzo?**
   - Guion, escenas, edición, revisión → modelo por defecto (la calidad se juega aquí).
   - Vigilancia de cuentas, búsquedas de datos, comprobaciones de disco, tareas mecánicas → `effort: "lower"` y, si es posible, `model: "sonnet"` o `"haiku"`.
5. **¿Uno o varios agentes?** Consultas: un solo agente, salvo dudas de narrativa (strategist + creative-producer, regla del director).
6. **¿Lo decido yo?** Lo técnico (niveles, márgenes, sincronía, a quién lanzar, orden) lo decide el director sin preguntar. Al creador solo: lo creativo, el estilo y lo que cuesta dinero.
7. **¿Lo hago yo con un comando?** Verificaciones de `ffprobe`, `sha256`, `ebur128`, existencia de archivos y pruebas de API las hace el director con Bash; no se lanza un agente para eso.

## 3 · Reglas fijas que ahorran sin bajar calidad

- **Una pasada por ronda:** correcciones del reviewer + preferencias del creador pendientes van juntas.
- **Encargos cortos y precisos:** rutas exactas, qué cambiar y qué no tocar; nada de «revisa todo».
- **Sin reglas inventadas** en los encargos (causan rondas extra; lección hedy-lamarr-wifi).
- **Decisiones del estilo al perfil:** cada preferencia del creador va al `perfil.md` para no volver a consultarla.
- **Vigilancia de cuentas con Chrome solo cuando la cola de temas tenga < 2 ideas** (aprox. cada 3–4 días), con modelo ligero.
- **No releer informes largos:** el director usa el resumen del agente y comprueba en disco lo imprescindible.

## 4 · Registro

Al recibir cada entrega, apuntar en el `project-log.md` del slug una línea:

```
- tokens · <agente> · <encargo> · <N>K
```

(`<N>` = `subagent_tokens` del aviso de fin de tarea). Al entregar el video, sumar y añadir a la señal `🎬 PROYECTO ENTREGADO`: `tokens ≈ X.XM (mayor gasto: <encargo>)`. Si una partida supera lo esperado de la tabla en más de un 50 %, anotar por qué y actualizar la tabla de la §1.

## 5 · Modelo y esfuerzo por agente (acordado con el creador, 2026-11-03)

Fijado en el frontmatter de cada agente (`model:` / `effort:`). El editor **nunca** usa Sonnet (creador).

| Agente | Modelo | Esfuerzo | Ajuste al lanzar |
|---|---|---|---|
| video-editor | opus | high | — |
| quality-reviewer | opus | high | rondas de corrección acotadas: `effort: "lower"` |
| creative-producer | opus | medium | — |
| viral-strategist | opus | medium | — |
| social-strategist | **sonnet** | medium | análisis estratégico de fondo: `model: "opus"` solo esa vez |
| executive-producer | opus | medium | — |

**Si Sonnet no da la talla** (datos sin fuente, cifras que el strategist no puede verificar, informe incompleto, o 2 entregas flojas seguidas): el director relanza ese encargo con `model: "opus"` y **avisa al creador** del cambio y del motivo («⚠️ social-strategist vuelve a Opus: …»), y lo anota en el `project-log.md`.

## 6 · Análisis posterior de cada video (creador, 2026-11-03)
Palabras del creador: «luego del proceso tu deber es analizar luego de que realices este video para analizar los fallos y las mejores formas de ahorrar tokens, para poder maximizar la eficiencia».

Al entregar cada video, el director (sin lanzar agentes) escribe en su `project-log.md` una sección `## Análisis posterior`:
1. **Tokens:** total y por agente/encargo (de las líneas `tokens ·`), frente a la tabla de la §1.
2. **Fallos:** cada ronda, reintento o encargo repetido, con su causa (encargo ambiguo, regla inventada, dato sin fuente, límite de uso, decisión tardía del creador…) y su coste.
3. **Ahorros:** qué se habría podido agrupar, acotar, pasar a Sonnet o resolver con un comando.
4. **Cambios:** 1–3 reglas concretas que se aplican desde el siguiente video; se escriben en esta skill (§1–§5) o en el agente afectado, y se comunican al creador en la entrega.

## 7 · Reglas aprendidas (análisis posteriores)
- **voz-grabada R10–R12 (2026-11-03):** (1) nivel de ambiente y densidad de SFX se fijan antes del primer render, no después; (2) dudas técnicas de mezcla/medida → 1 agente o un comando del director; (3) máximo 3 agentes Opus en paralelo (el límite de 5 h cortó un render); lo mecánico a Sonnet.
- **soldado (2026-11-04):** (1) una preferencia nueva del creador va al agente o skill **antes** de lanzar el encargo, porque un agente en marcha no recibe mensajes (23 SFX generados antes de la orden de reutilizar); (2) el plan de escenas marca `[catálogo]`/`[nueva]` y parte del catálogo (prueba de 10 s de 382K por piezas nuevas); (3) el análisis del original EN→ES va antes del guion (v2 de 104K); (4) SFX diseñados a 13 dB bajo la voz, porque el render los sube ~3 dB (un rehecho de audio); (5) los agentes usan solo comandos permitidos y, en modo desatendido, anotan y siguen (una revisión quedó ~9 h parada en un aviso de permiso); (6) Sonnet cumplió en el análisis social (62K frente a 154–235K en Opus).
