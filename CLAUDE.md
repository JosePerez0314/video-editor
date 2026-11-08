# Video Editor — Proyecto multi-nicho

Editor de videos para 3 nichos distintos. Cada nicho tiene su propia estructura, skills, scripts y referencias. **Este es el único `CLAUDE.md` del proyecto** — toda la configuración y contexto por nicho vive aquí.

## Sistema operativo

Linux (Ubuntu, kernel 7.0.0-38-generic). Node 24 vía `.nvmrc`.

## Estructura general

```
video-editor/
├── CLAUDE.md                 (este archivo, único)
├── .env .gitignore .nvmrc    (compartidos)
├── .claude/
│   └── agents/               (agentes del proyecto — solo shorts por ahora)
├── tools/                    (herramientas compartidas: video-use, etc.)
├── ideas/                    (brainstorms y propuestas por nicho, antes de producir)
│   ├── shorts/
│   ├── storytelling/
│   └── montaje/
└── nichos/
    ├── shorts/               (TikTok/Reels/Shorts educativos — 20–90s, 9:16)
    ├── storytelling/         (YouTube narrativo — parábolas 5–6 min, 16:9)
    └── montaje/              (Shorts deportivos — compilaciones 35–60s, 9:16)
```

**Carpeta `ideas/`:** sesiones de ideación con 1 o varias propuestas puntuadas. Un archivo por sesión (nombre `YYYY-MM-DD-<slug>.md`). Es el paso anterior a `nichos/<nicho>/scripts/<topic>/<slug>.concept.md`: aquí vive la lluvia de ideas con rúbrica; solo las aprobadas pasan a `scripts/` como concepto formal.

## Herramientas compartidas (todas instaladas)

| Herramienta | Versión | Ruta / notas |
|---|---|---|
| FFmpeg / FFprobe | 6.1.1 | sistema |
| Python | 3.12.3 | sistema |
| Node.js | v24.11.1 | `.nvmrc`. **El Node por defecto del sistema es 20**: antes de cualquier `npx` del architect, `source ~/.nvm/nvm.sh && nvm use 24` |
| video-editor-architect | clon local | `tools/architect/` — editor Remotion del nicho shorts (ver Nicho 1) |
| Whisper large-v3 + VAD | — | `~/.cache/video-editor/`; rutas en `.claude/settings.json` → `env` |
| yt-dlp | 2026.10.21 | descargar reels de referencia |
| video-use | 0.1.0 | `tools/video-use/` (nicho montaje) |
| ElevenLabs | `ELEVENLABS_API_KEY` | `.env`. SFX por API; las voces las genera el creador en la web (el plan free no permite voces de biblioteca por API) |

## Permisos y modo de sesión

- `.claude/settings.json` tiene la allowlist del proyecto (lectura/escritura en el proyecto, ffmpeg, npx, python3, node, yt-dlp, utilidades de archivo, WebSearch) y `defaultMode: acceptEdits`. **No hace falta `--permission-mode bypassPermissions`.** `rm`, `sudo` y gastos (`--si-gasto`) piden confirmación.
- **Nunca trabajar en modo plan** con agentes en segundo plano: bloquea toda escritura de los subagentes sin avisar.
- Un subagente en segundo plano **no puede lanzar otros agentes**. El director (`shorts-executive-producer`) debe correr como sesión principal o el hilo principal lanza a cada especialista.
- Si un subagente dice «permiso denegado», falta una regla en `.claude/settings.json`: añadirla ahí, no reintentar a ciegas.

## Al empezar una conversación

1. Lee `RESUME.md` (estado actual y cómo seguir).
2. El usuario dice qué nicho va a tocar (o se infiere: "short", "parábola", "montaje"); lee su sección **en este archivo**.
3. Si el nicho tiene agentes y skills, úsalas. **Nunca cruces skills, agentes ni convenciones entre nichos.**
4. Para un short completo: `claude --agent shorts-executive-producer` desde la raíz del proyecto, o pedir al hilo principal que lance a los especialistas en orden.

---

# Nicho 1 — shorts · edutainment vertical

Videos cortos educativos / de curiosidad para TikTok, Reels de Instagram y YouTube Shorts.

**Estado:** operativo end-to-end. 6 agentes, 33 skills, editor Remotion (`tools/architect/`). **Dos estilos:** `estilo-gabriel` (aprobado; referencia **voz-grabada** R9) y `estilo-monigotes` (aprobado; referencia **hedy-lamarr-wifi**, refs de @resultaaquee). Cada proyecto dice cuál usa.

## Specs técnicas

- **Formato:** 1080×1920 vertical, 30 fps, H.264 + AAC
- **Duración:** 20–90 s (sweet spot 60–90 s)
- **Audio:** −14 LUFS integrado (±0.5), LRA ≤ 2.5 LU, Peak ≤ −0.7 dBFS

## Estilo del canal (aprobado por el creador)

Fuente de verdad: `tools/architect/estilo/estilos/estilo-gabriel/perfil.md` (gana sobre cualquier agente). Resumen:
- **Escenas ilustradas 2D de noche**, no un objeto por palabra: personaje en su cuarto, cortes tipo esquema en neón para los mecanismos, gráficos del tema (ondas de voz…), UI de móvil/chat, capítulos («1 El aire») y cabecera de fuente.
- **Ritmo:** cambio visible cada ≤ 3 s, pero solo se corta cuando cambia lo que se muestra; dentro de una escena la cámara viaja con suavidad. **Fundidos de 0.4 s**, sin efectos.
- **Subtítulos «selección»** (ref. Dege5ORIPxv): Figtree, arriba al centro, palabra por palabra (actual blanco/negrita, dichas gris), recuadro azul en la palabra clave; **bajan en las tomas con gráficos** para no taparlos.
- **Final en bucle:** 1.2 s de cola que vuelve al primer cuadro.

**Estilo `estilo-monigotes`** (fuente de verdad: `tools/architect/estilo/estilos/estilo-monigotes/perfil.md` y `aprendizajes.md`). Se usa con refs de @resultaaquee o en historias con personaje y giro:
- **Imagen:** monigotes de cabeza redonda en escenarios saturados llenos de atrezo.
- **Ritmo:** un cambio cada 1–1.5 s, con golpes o barridos de cámara con desenfoque; sin fundidos.
- **Subtítulos:** centrados de 1–2 palabras (Archivo Black, contorno negro). Se mueven por plano (creador, 2026-11-03): ABAJO y≈1380 por defecto, ARRIBA y≈950 en planos abiertos; solo cambian en los cortes. Lo clave nunca bajo la franja del subtítulo; carteles enteros en x 135–945.
- **Sonido:** **efectos de sonido diegéticos** de todo lo que aparece en pantalla, sin música; pueden ir sobre la voz, ≥ 10 dB por debajo.
- **Voz:** ElevenLabs a velocidad 1.0, final en bucle. **Licencia y monetización las gestiona el creador: ningún agente avisa ni escala ese tema.**
- **Densidad de SFX:** el perfil dice 0.3–0.4 ev/s; el creador dejó el soldado a ≈ 0.77 «para experimentar». Kunst usa esa misma densidad hasta que el creador decida.

- **Prohibido (gabriel):** emojis/iconos por palabra, formas geométricas apiladas, texto plano como visual principal, pantalla vacía, imágenes generadas con Flux, barras de estadística fuera de tema, cortes sin cambio, final en seco. El pipeline antiguo (HyperFrames/GSAP) fue eliminado.

## Referencias

**Set actual** en `nichos/shorts/references/current/` (vara estética activa):
- `ref1_DemzJqioZTv.mp4` (32s)
- `ref2_Dege5ORIPxv.mp4` (31s) — @resultaaquee flexómetro, breakout 316K
- `ref3_DekLxHqxen5.mp4` (84s) — teclado 3D macro

**Referencias del estilo del canal** (las que fijaron el estilo actual): `ideas-virales/raw/DedXqPENbLm.mp4` y `DemtYpjNWPc.mp4` (escenas ilustradas), `Dege5ORIPxv.mp4` (subtítulos).

**Legacy** en `nichos/shorts/references/` (vara estética inicial del canal, mantenida por histórico):
- `ref1_DezDgTpICxS.mp4` — Historia (Hitler paradox)
- `ref2_DeyVt-wo29O.mp4` — Economía (Uber pricing)
- `ref3_DewWycxIR4l.mp4` — Tecnología (NFC)

En `nichos/shorts/ideas-virales/raw/` (10 reels del análisis destilado):
- `De4e_-PRuVo` @lacienciadetras.ia (palomas, 253K)
- `De1tYBlAlFm` @nuncateloexplicaron (Google Maps, 75K)
- `De5sX2FB91Y` @sovera.ia (brazo marco puerta, 757K) **breakout**
- `De4OyYeAGCS` @thebioloco (calamar colosal, 80K)
- `DedXqPENbLm` @chispalogica2026 (cargador vampiro, 366K)
- `DemtYpjNWPc` @historiasparanormales (noche 1, 204K)
- `DexioYQtICU` @loconstruiste.mx (puente, 1.09M) **breakout**
- `Dd-eg3sDg7_` @1bit1pixel (60 min, 294K)
- `DehA1hgonRL` @resultaaquee (electrocución móvil, 757K) **breakout**
- `Dege5ORIPxv` @resultaaquee (flexómetro, 316K)

Tiras de 4 frames por reel en `nichos/shorts/ideas-virales/frames/<id>_strip.jpg`.

## Flujo de producción

```
1 Idea (strategist) ──✋ elige──▶ 2 Guion de voz + plan de escenas (creative-producer) ──✋ aprueba──▶
3 Voz: el creador la genera en ElevenLabs y la pega en nichos/shorts/assets/audios/<slug>/voz.mp3 ──▶
4 Video de prueba de 10 s (editor, `prueba_10s.mp4`) ──✋ ok──▶ 5 Render (editor) ──▶ 6 Revisión (reviewer) ──▶
7 Correcciones (validar antes de cada ronda; 2 automáticas máx.) ──▶ 8 Entrega ──▶ 9 Publicación (social-strategist)
```

## Agentes del nicho (en `.claude/agents/`)

Contrato de 6 secciones + 5 reglas globales cada uno.

| Agente | Entrega | Señal |
|---|---|---|
| **shorts-executive-producer** | `project-log.md`, coordinación (corre como sesión principal) | `🎬 PROYECTO ENTREGADO` / `🛑 BUCLE AGOTADO` |
| **shorts-viral-strategist** | `scripts/<topic>/<slug>.concept.md` | `CONCEPTO LISTO` |
| **shorts-creative-producer** | `<slug>.guion-voz.md` (texto para ElevenLabs) + `<slug>.escenas.md` (plan de escenas) | `GUION Y ESCENAS LISTOS` |
| **shorts-video-editor** | `exports/<slug>/final.mp4` + `escenas_<slug>.py` + sección en `render-log.md` | `VIDEO LISTO (shorts · Remotion)` |
| **shorts-social-strategist** | `publicacion/calendario.md` (lanzamiento, horarios, título/descripción/hashtags/CTA/portada por red), informes `publicacion/analisis-redes-*.md`; tiene Chrome (solo lectura) | `CALENDARIO LISTO` / `ANALISIS LISTO` |
| **shorts-quality-reviewer** | `exports/<slug>/review.md` (30 comprobaciones con evidencia) | `REVIEW APPROVED` / `REVIEW NEEDS_REVISION` |

### Editor (`shorts-video-editor`) en breve
- Pipeline **Remotion + video-editor-architect** en `tools/architect/`. Explainer sin crudo = **modo solo-audio**: crudo sintético (fondo `#272523` + voz) → ingesta → transcribir → cortes sin quitar nada → base → subtítulos → armar-edl → **generador de escenas** (`escenas_<slug>.py --edl …`, ejemplo `exports/voz-grabada/escena_r7.py`) → render → entrega a 1080×1920.
- **Todos los tiempos salen de las palabras de la transcripción.** Con una voz nueva solo se rehace el proyecto del architect y se re-ejecuta el generador.
- Capas propias añadidas al architect: `escenas` (`src/estilo/escenas.ts`, `src/reel/escenas/`), `ilustracion` (etiquetas), `subtitulos_seleccion`; para monigotes, `subtitulos_centro`, cámara `golpe` con desenfoque, `Monigote.tsx`, `Escenario.tsx`/`EscenariosHedy.tsx` y SFX en `sfx_extra` (biblioteca `tools/architect/biblioteca/sfx/`, ejemplo `exports/hedy-lamarr-wifi/sfx_r3.py`). Pruebas en `tools/architect/pruebas/unit/` (`npx vitest run`).
- Versiones: `final_rN.mp4` respaldado antes de sobrescribir; ediciones `edicion-vN.json` vía `ajustar.ts`.

### Reglas globales que todos cumplen

1. Inspecciona el entorno antes de decidir arquitectura.
2. Usa solo los permisos declarados.
3. No sobrescribas ni elimines originales (versiona `_rN`).
4. No afirmes nada sin verificarlo (`test -f`, `ffprobe`, `ebur128`).
5. No prometas viralidad.

### Correcciones

- Antes de cada ronda nueva, el reviewer valida qué quedó arreglado.
- 2 rondas automáticas como máximo; después `🛑 BUCLE AGOTADO` y 3 opciones al creador.
- Las correcciones del creador se anotan literales en el `project-log.md` y, si son preferencias duraderas, en el perfil del estilo.

## Skills del nicho (en `nichos/shorts/skills/`)

- Narrativa y viralidad: `hook-opening`, `narrative-structure`, `scriptwriting`, `viral-reference-analysis`, `viral-pattern-execution`, `viral-idea-generation`, `viral-rubric`, `fact-vs-hypothesis`.
- Producción: `plan-escenas` (cómo planear las escenas), `visual-reference-analysis`, `subtitles-keyword-highlight` (apunta a «selección»), `composition-vertical`, `pacing-tight`.
- Por agente: `concepto-shorts` (strategist), `plan-escenas` (creative-producer), `edicion-escenas` (editor), `revision-calidad` (reviewer).
- Redes (social-strategist): `lanzamiento-cuenta` (secuencia de @resultaaquee), `publicacion-multired`, `analisis-cuentas`; una por red: `red-instagram-reels`, `red-tiktok`, `red-youtube-shorts`, `red-facebook-reels`; transversales: `titulos-descripciones`, `portadas-shorts` (no se diseñan miniaturas), `checklist-subida`, `seguimiento-resultados`, `metricas-viralidad`, `investigacion-redes-chrome`.
- Calidad: `render-inspection`.
- Editor: `reutilizacion-materiales` (catálogo único `tools/architect/biblioteca/reutilizables/CATALOGO.md`; lo usado en ≥ 2 videos pasa a `comun/`).
- Director: `protocolo-nocturno` (se activa con «me voy a dormir»: termina lo empezado sin interrumpir; lo que pida permiso va a `nichos/shorts/aprobaciones-pendientes.md` para el final; resumen al volver).
- Director: `presupuesto-tokens` (antes de cada tarea cara; registro de tokens por proyecto; tabla de modelo/esfuerzo por agente).

**Modelos (2026-11-03):** editor y reviewer Opus high · creative-producer, viral-strategist y director Opus medium · social-strategist **Sonnet** medium (Opus solo para análisis de fondo; si Sonnet no da la talla, vuelve a Opus y se avisa al creador). El editor nunca usa Sonnet.

## Mapa de nicho de contenido → carpeta

Al generar un script, el `shorts-viral-strategist` lo clasifica según el mapa de `scriptwriting.md`:

| Nicho de contenido | Carpeta | Señales |
|---|---|---|
| Historia | `scripts/historia/` | Fechas, personajes históricos, imperios, paradojas del pasado |
| Economía | `scripts/economia/` | Empresas, precios, mercados, modelos de negocio |
| Tecnología | `scripts/tecnologia/` | Gadgets, software, internet, IA, plataformas |
| Ciencia | `scripts/ciencia/` | Física, química, biología, astronomía, experimentos |
| Finanzas | `scripts/finanzas/` | Inversión, bancos, tarjetas, impuestos |
| Psicología | `scripts/psicologia/` | Sesgos cognitivos, comportamiento, emociones |
| Salud | `scripts/salud/` | Cuerpo humano, hábitos, enfermedades, nutrición |
| Sociedad | `scripts/sociedad/` | Política, cultura, tendencias sociales |
| Curiosidades | `scripts/curiosidades/` | Datos raros, récords, todo lo demás |

Si el contenido cruza dos, elegir el más específico. Si no hay encaje, usar `curiosidades/`.

## Estructura del nicho

```
nichos/shorts/
├── references/current/           (set estético actual)
├── ideas-virales/{ANALISIS.md, raw/, frames/}
├── skills/                       (33 skills)
├── publicacion/                  (calendario.md + cuentas/<cuenta>/ datos de referencia)
├── scripts/<topic>/
│   ├── <slug>.concept.md         (strategist)
│   ├── <slug>.guion-voz.md       (creative-producer — texto para ElevenLabs)
│   └── <slug>.escenas.md         (creative-producer — plan de escenas)
├── assets/audios/<slug>/voz.mp3  (voz del creador; voz-v2.mp3… para nuevas tomas)
└── exports/<slug>/
    ├── final.mp4 · final_rN.mp4  (entregable y versiones)
    ├── escenas_<slug>.py         (generador de escenas)
    ├── crudo_rN.mp4              (crudo sintético)
    ├── architect_rN -> tools/architect/proyectos/<fecha>-<slug>-rN/
    ├── qa/rN_frames/             (hojas de cuadros)
    ├── render-log.md · review.md · project-log.md
```


---

# Nicho 2 — montaje · compilaciones deportivas

Shorts verticales de 35–60s armados con **clips reales que el usuario provee** + voz TTS/grabada + subtítulos karaoke + logo del canal. Estilo FutNation.

**Estado:** operativo con **8 skills** (sin agentes todavía). Cuando se construyan, seguirán la convención `montaje-*` en `.claude/agents/` con sus propios análisis y rúbricas específicos del nicho.

## Specs técnicas

- **Formato:** 1080×1920 vertical
- **FPS:** 30
- **Duración:** 35–60s
- **Audio:** -22 a -24 LUFS integrado, LRA 3–6 LU, Peak ≤-3 dBFS
- **Ritmo:** 1 corte cada 4–8s (medio ritmo)

## Diferencia clave con los otros nichos

**El material visual lo trae el usuario, no se genera.** Clips en `assets/clips/`, logo en `assets/logo/`. El flujo lo decide la voz (guion propio con TTS vs audio grabado transcrito con Scribe).

## Estilo visual observado

- Logo del canal overlay fijo top-left
- Clips reales recortados 3–8s, concatenados con hard cuts
- Subs ALL CAPS blanco con outline negro grueso, 2–3 palabras max, centro-centro
- Flechas rojas señalando jugadores
- Marcadores grandes tipo "7-0" sobre clips
- Watermark de autor bottom (opcional)

## Referencias

En `nichos/montaje/references/`:
- `ref1_J_NK655Pyx8.webm` (52s — FutNation)
- `ref2_jStPCjGZmcs.webm` (55s — Mourinho)
- `ref3_1E4lnI_Ufak.webm` (39s — Dembélé)

## Skills del nicho (en `nichos/montaje/skills/`)

Leer en este orden:

1. `scriptwriting-montaje.md` — guion punchy con nombres propios, data, frases cortas
2. `clip-pipeline.md` — inventariar clips → `inventory.md` + thumbs
3. `storyboard-montaje.md` — **obligatorio**: mapear frase → clip con aprobación del usuario
4. `clip-standardization.md` — normalizar cada clip a 1080×1920
5. `voice-driven-timing.md` — recortar clips al largo de su frase, concatenar
6. `logo-overlay.md` — logo top-left permanente (45, 80), 160×160
7. `karaoke-subtitles.md` — subs ALL CAPS centro con pop-in word-by-word
8. `audio-mixing-montaje.md` — voz + música bed con ducking, -23 LUFS

## Estructura del nicho

```
nichos/montaje/
├── skills/                   (8 skills operativas)
├── scripts/                  (guiones por tema: jugadores/, partidos/)
├── assets/
│   ├── logo/                 (logos reutilizables)
│   ├── clips/                (globales opcionales — videos o imágenes)
│   └── music/                (beds reutilizables)
├── references/               (3 videos FutNation descargados)
└── exports/<slug>/
    ├── assets/{logo,clips,music}/   (específicos del proyecto)
    ├── voiceover.mp3                (en el root del proyecto)
    ├── alignment.json
    ├── inventory/{inventory.md,thumbs/}
    ├── segments/
    ├── storyboard.md
    ├── sequence.json
    └── final.mp4
```

**Reglas de estructura:**
1. `assets/clips/` acepta videos E imágenes. Imágenes como clips estáticos (`static`) o Ken Burns (`ken-burns`). Formatos: `.jpg`, `.jpeg`, `.png`, `.webp`.
2. La voz vive en el root del proyecto, no dentro de `assets/`. Path siempre `exports/<slug>/voiceover.mp3`.

## Flujo end-to-end

```
1. Usuario crea exports/<slug>/ con assets/{logo,clips,music}/ y voiceover.mp3
   (o pide generar TTS; en ambos casos termina en exports/<slug>/voiceover.mp3)
2. Scriptwriting → scripts/<tema>/<slug>.md
3. Transcribir voz → alignment.json (Scribe)
4. clip-pipeline → inventory/
5. storyboard-montaje → tabla frase → recurso → ESPERAR "ok"
6. Guardar storyboard.md + sequence.json
7. clip-standardization → normaliza
8. voice-driven-timing → corta + concat
9. logo-overlay
10. karaoke-subtitles
11. audio-mixing-montaje → loudnorm -23 LUFS
12. exports/<slug>/final.mp4
```

Herramientas requeridas: FFmpeg, Python+PIL, ElevenLabs API, `tools/video-use/helpers/transcribe.py`. Todas instaladas.

---

# Nicho 3 — storytelling · narrativa larga ilustrada

Videos narrativos de 5–6 minutos con personajes ilustrados animados, voz narrada y música ambient. Estilo "Estoy con Jesús" / parábolas.

**Estado:** en configuración. Estructura creada; **skills, herramientas y flujo todavía no están definidos**. Decidir herramientas antes de empezar a producir. Cuando se construyan agentes, seguirán la convención `storytelling-*`.

## Specs técnicas

- **Formato:** 1920×1080 horizontal
- **FPS:** 24 (cinematográfico)
- **Duración:** 5–6 minutos
- **Audio:** -20 a -23 LUFS integrado (estándar YouTube), LRA 2–3 LU
- **Ritmo:** 1 corte cada 12–60s (contemplativo)

## Estilo visual observado

- Ilustración 2D estilo anime/cartoon con personajes recurrentes (ej. Jesús + Templario)
- Fondos ilustrados por escena (hoguera, aldea, montaña, barca)
- Paleta cálida (fuego naranja) + fría (cielo nocturno púrpura)
- Composición cinematográfica: over-the-shoulder, two-shots, medium shots
- Watermark top-right permanente

## Estilo de subtítulos

Sentence case, bottom-center, blanco con outline negro grueso, estilo clásico de YouTube.

## Referencias

En `nichos/storytelling/references/`:
- `ref1_7dvhXs135n8.webm` (6.3 min)
- `ref2_Q6Lw0VSViKU.webm` (5.3 min)
- `ref3_YCNZQNtpKkg.webm` (5.6 min)

## Pendiente de decidir antes de construir skills y agentes

1. **Generación de personajes consistentes** — Flux + IP-Adapter / Midjourney / Stable Diffusion local
2. **Generación de fondos** — misma herramienta
3. **Animación de imágenes** — Ken Burns + Hedra lipsync / Runway / Kling
4. **Voces narrativas** — ElevenLabs voces de narrador en español
5. **Música bed** — Suno / Udio / stock
6. **SFX** — Freesound / Pixabay

## Estructura del nicho

```
nichos/storytelling/
├── skills/                   (vacío — construir tras decidir herramientas)
├── scripts/                  (vacío)
├── assets/
│   ├── characters/           (JPGs de referencia por personaje)
│   ├── scenes/               (fondos generados)
│   └── music/                (beds ambient)
├── references/               (3 videos descargados)
└── exports/                  (proyectos renderizados)
```

---

# Convenciones comunes a los 3 nichos

1. **Un `CLAUDE.md` solo.** Este archivo. No crear sub-CLAUDE.md por nicho.
2. **Prefijo del agente = nicho.** Los agentes viven en `.claude/agents/` y se nombran `<nicho>-<rol>.md` (ej. `shorts-viral-strategist.md`). Cada agente opera **solo** sobre su nicho y rechaza explícitamente los demás.
3. **Skills viven en el nicho.** `nichos/<nicho>/skills/`. Nunca se cruzan entre nichos sin motivo documentado.
4. **Referencias por nicho.** Cada nicho tiene su `references/` con la vara estética y, si aplica, un `ideas-virales/` con análisis destilado.
5. **Exports siempre por slug.** `nichos/<nicho>/exports/<slug>/` con el bundle completo del proyecto.
6. **Cada agente tiene contrato operativo de 6 secciones:**
   - Responsabilidad exclusiva
   - Información de entrada
   - Formato de salida
   - Criterios de aceptación
   - Herramientas permitidas
   - Condiciones para escalar al director (o al usuario si es el director)
7. **5 reglas globales** aplican a todos los agentes de todos los nichos:
   - Inspecciona el entorno antes de decidir arquitectura
   - Permisos mínimos necesarios
   - No sobrescribas ni elimines recursos originales
   - No afirmes etapa completada sin verificar
   - No prometas viralidad: criterios medibles y métricas reales
