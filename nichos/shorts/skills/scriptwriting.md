---
name: scriptwriting
description: Crear guiones de video corto (55–75s) en formato production-ready, organizados por nicho en scripts/<nicho>/<slug>.md. Integra narrative-structure, hook-opening, subtitles-keyword-highlight, pacing-tight, composition-vertical y plan-escenas.
---

# Skill: Scriptwriting (guiones de formato corto)

## Qué hace esta skill

Genera guiones listos para producción en `scripts/<nicho>/<slug>.md`. Cada guion incluye narración, cues de subtítulos, notas de animación y timings — todo lo necesario para que el editor (esta misma sesión o una futura) pueda ejecutar sin preguntas.

## Nicho → carpeta

Detectar el nicho del contenido y guardar en la carpeta correspondiente:

| Nicho | Carpeta | Señales de contenido |
|---|---|---|
| Historia | `scripts/historia/` | Fechas, personajes históricos, guerras, imperios, paradojas del pasado |
| Economía | `scripts/economia/` | Empresas, precios, mercados, modelos de negocio, trabajo |
| Tecnología | `scripts/tecnologia/` | Gadgets, software, internet, IA, plataformas digitales |
| Ciencia | `scripts/ciencia/` | Física, química, biología, astronomía, experimentos |
| Finanzas | `scripts/finanzas/` | Inversión, bancos, tarjetas, impuestos, dinero personal |
| Psicología | `scripts/psicologia/` | Sesgos cognitivos, comportamiento, emociones, relaciones |
| Salud | `scripts/salud/` | Cuerpo humano, hábitos, enfermedades, nutrición |
| Sociedad | `scripts/sociedad/` | Política, cultura, tendencias sociales, fenómenos urbanos |
| Curiosidades | `scripts/curiosidades/` | Datos raros, récords, fenómenos inexplicables, todo lo demás |

Si el contenido cruza dos nichos, elegir el más específico. Si no hay carpeta adecuada, usar `curiosidades/`.

## Nombre de archivo

```
scripts/<nicho>/<slug>.md
```

Slug: kebab-case del tema, sin tildes ni caracteres especiales, máximo 40 caracteres.

Ejemplos:
- `scripts/historia/padre-de-hitler.md`
- `scripts/economia/uber-precio-dinamico.md`
- `scripts/tecnologia/nfc-como-funciona.md`

## Proceso de creación del guion

### Paso 1 — Definir el gancho

Antes de escribir una línea, confirmar el hook (ver `hook-opening.md`):
- ¿Cuál es el dato sorprendente / paradoja / pregunta que nadie se hace?
- ¿El viewer puede hacer scroll sin conocer la respuesta?

Si el usuario te da un tema genérico ("quiero un video sobre el NFC"), derivar el hook tú:
- Busca el ángulo más contraintuitivo del tema.
- Propón el hook al usuario y espera confirmación antes de escribir el guion completo.

### Paso 2 — Mapear los beats

Usando `narrative-structure.md`:

```
HOOK:        1.5 – 3.0s   → 1 frase
SETUP:       8  – 15s     → 2–4 frases
DESARROLLO:  30 – 45s     → 4–8 sub-beats de 5–10s c/u
PAYOFF:      3  – 8s      → 1–2 frases cortas
CTA:         2  – 5s      → 1 frase o implícito
```

### Paso 3 — Escribir la narración

Criterios de escritura para este formato:
- **Frases cortas**: máximo 12–15 palabras por frase hablada.
- **Ritmo oral**: leer en voz alta. Si no fluye natural, reescribir.
- **Sin muletillas de escritura**: "en primer lugar", "cabe destacar", "es importante mencionar" — nunca.
- **Presente dramático**: contar en presente aunque sean hechos del pasado ("En 1894, un niño SE AHOGA en el río Inn").
- **Números concretos**: siempre cifras exactas, nunca "muchos", "varios", "algunos".
- **Una idea por frase**: nunca subordinar dos conceptos nuevos en una sola oración.

### Paso 4 — Definir cues de subtítulos

Para cada frase de narración, dividir en cues de 1–3 palabras (ver `subtitles-keyword-highlight.md`):
- Marcar la keyword de cada cue con `**negrita**`.
- La keyword es la palabra de mayor impacto semántico del cue.
- Verificar que ningún cue tenga artículos o preposiciones como keyword.

### Paso 5 — Planear los overlays

Para cada beat del DESARROLLO, definir qué se ve en pantalla (ver `plan-escenas.md`: una escena por idea, nunca un objeto por palabra):
- Tipo de overlay: A (personaje 3D), B (infografía/dato), C (footage real + motion graphics).
- Duración del overlay.
- Palabra de sincronización (qué palabra del narrador dispara el reveal del overlay).
- Paleta (heredar de la paleta del proyecto si ya fue definida; si no, proponer una y esperar confirmación).

---

## Formato del archivo MD de guion

Cada guion sigue exactamente esta plantilla:

```markdown
---
nicho: <nicho>
titulo: <título descriptivo del video>
hook: <la pregunta/paradoja de apertura en una línea>
duracion_estimada: <Xs>
estado: borrador | revisado | grabado | editado
fecha: YYYY-MM-DD
paleta: <nombre de paleta o "pendiente">
---

# <Título>

## META
- **Nicho:** <nicho>
- **Duración objetivo:** <X>s
- **Target:** TikTok / Reels / Shorts
- **Paleta visual:** <paleta o "pendiente — confirmar antes de producción">

---

## BEAT 1 — HOOK (`0s – Xs`)

### Narración
> <texto exacto que dice el speaker>

### Subtítulos
| Cue | Texto | Keyword |
|-----|-------|---------|
| 1 | <palabras> | **<keyword>** |
| 2 | <palabras> | **<keyword>** |

### Visual
- **Tipo:** talking head / overlay tipo <A|B|C>
- **Descripción:** <qué se ve exactamente>
- **Timing overlay:** inicia en `Xs`, sincroniza con palabra "<palabra>"

---

## BEAT 2 — SETUP (`Xs – Xs`)

### Narración
> <texto>

### Subtítulos
| Cue | Texto | Keyword |
|-----|-------|---------|
| 1 | <palabras> | **<keyword>** |

### Visual
- **Tipo:** <tipo>
- **Descripción:** <descripción>

---

## BEAT 3 — DESARROLLO

### Sub-beat 3.1 — <nombre> (`Xs – Xs`)

#### Narración
> <texto>

#### Subtítulos
| Cue | Texto | Keyword |
|-----|-------|---------|
| 1 | <palabras> | **<keyword>** |

#### Visual
- **Tipo:** <tipo>
- **Descripción:** <descripción>
- **Dato en pantalla:** <número/label exacto que aparece como overlay>

### Sub-beat 3.2 — <nombre> (`Xs – Xs`)
[repetir estructura]

---

## BEAT 4 — PAYOFF (`Xs – Xs`)

### Narración
> <texto — frase corta y contundente>

### Subtítulos
| Cue | Texto | Keyword |
|-----|-------|---------|
| 1 | <palabras> | **<keyword>** |

### Visual
- **Tipo:** <tipo>
- **Descripción:** el frame de mayor impacto del video

### Nota de pausa
> ⚠️ Dejar el silencio natural antes de esta frase — NO cortar. Mínimo 300ms de pausa anterior.

---

## BEAT 5 — CTA (`Xs – Xs`)

### Narración
> <texto o "implícito — cortar en el frame de impacto del payoff">

### Visual
- **Tipo:** talking head / freeze frame / fade
- **Descripción:** <descripción>

---

## CHECKLIST DE PRODUCCIÓN

- [ ] Paleta confirmada con el usuario
- [ ] Hook validado (¿fuerza el scroll-stop?)
- [ ] Narración leída en voz alta — ¿fluye natural?
- [ ] Todos los cues de subtítulos ≤ 3 palabras
- [ ] Cada keyword es sustantivo/verbo/adjetivo (no artículo ni preposición)
- [ ] Duración estimada entre 55–75s
- [ ] Overlays tipados (A, B o C) con palabra de sincronización definida
- [ ] Silencio del payoff marcado como NO CORTAR
- [ ] Guardado en `scripts/<nicho>/<slug>.md`
```

---

## Reglas de calidad del guion

1. **El hook decide si el video existe.** Si el hook no genera urgencia de ver el siguiente segundo, reescribir antes de continuar.
2. **Cada sub-beat del DESARROLLO abre una micro-pregunta antes de cerrarla.** El viewer debe estar siempre un paso detrás del relato.
3. **Los números son el alma del edutainment.** Cada claim abstracto debe tener un número concreto: no "muy lejos" sino "a 11 km". No "muchos años" sino "101 años después".
4. **El payoff debe poder funcionar como screenshot.** Si alguien hace pausa ahí, debe haber algo que valga la pena compartir.
5. **La narración se escribe para el oído, no para el ojo.** Leer siempre en voz alta antes de finalizar.

## Anti-patterns de guion

- NO escribir más de 15 palabras en una frase oral.
- NO usar pasado para hechos dramáticos — usar presente narrativo.
- NO poner dos datos nuevos en la misma frase.
- NO escribir el CTA como párrafo — 1 frase máximo o nada.
- NO dejar un beat sin su correspondiente overlay definido (aunque sea "talking head").
- NO guardar el guion si el hook no fue validado.

## Flujo al recibir un tema del usuario

1. Identificar el nicho → carpeta de destino.
2. Derivar el ángulo más contraintuitivo del tema.
3. Proponer el hook en una línea → esperar OK.
4. Mapear beats con duraciones → esperar OK si hay duda.
5. Escribir el guion completo en la plantilla.
6. Guardar en `scripts/<nicho>/<slug>.md`.
7. Confirmar al usuario: ruta del archivo + duración estimada + paleta pendiente si aplica.
