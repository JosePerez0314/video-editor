# 🎬 Video Editor — Shorts

<div align="center">

[English](./README.en.md) · **Español**

### Sistema de producción de shorts verticales con agentes de IA

Un equipo de agentes de Claude Code convierte un tema en un video vertical 1080×1920 listo para publicar: idea → guion → escenas → render → revisión → calendario de redes. La persona creadora solo decide en los puntos de control y pone la voz.

![Claude Code](https://img.shields.io/badge/Claude_Code-agentes-D97757?logo=anthropic)
![Remotion](https://img.shields.io/badge/Remotion-4-0B84F3?logo=remotion)
![React](https://img.shields.io/badge/React-19-61DAFB?logo=react)
![Node.js](https://img.shields.io/badge/Node.js-24-339933?logo=nodedotjs)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python)
![FFmpeg](https://img.shields.io/badge/FFmpeg-6.1-007808?logo=ffmpeg)

</div>

---

## 📚 Documentación

| | |
| --- | --- |
| 📖 **Este README** ([English](./README.en.md)) | Explicación completa del sistema y cómo replicarlo |
| 📏 [`CLAUDE.md`](./CLAUDE.md) | Reglas exactas que siguen los agentes (fuente de verdad) |
| 🤖 [`.claude/agents/`](./.claude/agents/) | Los 6 agentes, uno por archivo |
| 🧠 [`nichos/shorts/skills/`](./nichos/shorts/skills/) | Los 42 manuales de trabajo |
| 📈 [`nichos/shorts/ideas-virales/ANALISIS.md`](./nichos/shorts/ideas-virales/ANALISIS.md) | Análisis de reels virales del que sale la rúbrica de ideas |
| 📍 [`RESUME.example.md`](./RESUME.example.md) | Plantilla del estado de sesión |
| 🔐 [`.claude/settings.example.json`](./.claude/settings.example.json) | Plantilla de permisos |

---

## 📖 Visión general

El proyecto **no es una aplicación**: es una organización de carpetas, agentes, skills y un motor de render que Claude Code sigue para fabricar videos.

| Pieza | Qué es | Dónde |
| --- | --- | --- |
| **Agentes** | Un Claude con un único oficio y un contrato de trabajo | `.claude/agents/` |
| **Skills** | Manuales en Markdown con el «cómo se hace» de cada tarea | `nichos/shorts/skills/` |
| **Reglas** | Lo que todos cumplen: formato, estilos, flujo, permisos | `CLAUDE.md` |
| **Motor de render** | Remotion: el video se describe en JSON y se dibuja con código | `tools/architect/` |
| **Persona creadora** | Elige la idea, aprueba guion y prueba, genera la voz y publica | ✋ |

**Principio central:** todos los tiempos salen de la voz. Whisper transcribe palabra por palabra y cada escena, subtítulo y efecto se ancla a una palabra («cuando dice *piano*, suena una tecla»). Si cambia la voz, se re-ejecuta el generador y todo se recoloca solo.

> **Nota:** el repositorio contiene solo el sistema del nicho `shorts`. No incluye videos, audios, imágenes, guiones ni datos de publicación. Agentes, skills y reglas están en español; hay una [versión en inglés](./README.en.md) de este README.

---

## 📘 Glosario

| Término | Significado |
| --- | --- |
| **Slug** | Nombre corto de un video, sin espacios ni tildes. Todas sus carpetas lo usan |
| **Director** | El agente `shorts-executive-producer`. Coordina; no produce |
| **Skill** | Manual con el procedimiento de una tarea (p. ej. cómo escribir un gancho) |
| **EDL** | *Edit decision list*: JSON (`edicion-vN.json`) con qué se ve, se oye y se lee en cada momento |
| **Crudo sintético** | Fondo liso + voz. Los explainers no tienen cámara: el crudo es solo la voz |
| **SFX** | Efectos de sonido |
| **LUFS** | Volumen percibido. Las redes normalizan a −14 LUFS |
| **Bucle** | El final empalma con el principio para que la repetición no se note |
| **Ronda (Rn)** | Cada versión de un video: `final_r2.mp4` es la versión 2 |
| **Señal** | Frase con la que un agente declara su trabajo terminado (`VIDEO LISTO`…) |
| **✋** | Punto de control: decide la persona creadora |
| **[M] / [H]** | Dato medido / hipótesis. Todo dato de redes se marca así |

---

## 🛠 Stack

| Tecnología | Uso |
| --- | --- |
| **Claude Code** | Ejecuta los agentes; permisos en `.claude/settings.json` |
| **Remotion 4 + React 19 + TypeScript** | Render del video a partir de la EDL |
| [**video-editor-architect**](https://github.com/Hainrixz/video-editor-architect) | Editor de reels sobre Remotion, ampliado con capas propias |
| **Node.js 24** (nvm) | Herramientas del editor (`npx tsx …`) |
| **FFmpeg / FFprobe 6.1** | Crudo sintético, mezcla y medición (duración, LUFS, picos) |
| **whisper.cpp large-v3 + VAD Silero** | Transcripción local con tiempos por palabra |
| **Python 3.12** | Generadores de escenas y SFX por video, mediciones |
| **ElevenLabs** | Voz (desde la web) y efectos de sonido (API) |
| **yt-dlp** | Descarga de reels de referencia para analizarlos |
| **Claude in Chrome** (opcional) | Lectura de estadísticas de redes, solo lectura |
| **Vitest** | Pruebas del código del editor |

---

## 📂 Estructura del proyecto

Lo marcado con 🔒 existe en local pero **no se sube** (`.gitignore`).

```bash
.
├── README.md / README.en.md
├── CLAUDE.md                     # Reglas de todo el proyecto (único CLAUDE.md)
├── RESUME.example.md             # Plantilla → copiar a RESUME.md 🔒
├── .env                          # 🔒 Claves de API
├── .nvmrc                        # Node 24
├── .claude/
│   ├── settings.example.json     # Plantilla → copiar a settings.json 🔒
│   └── agents/                   # 6 agentes shorts-*.md
├── ideas/shorts/                 # 🔒 Lluvias de ideas: YYYY-MM-DD-<slug>.md
├── tools/                        # 🔒 Clones externos
│   └── architect/                # Motor de render (Remotion) + biblioteca
└── nichos/shorts/
    ├── skills/                   # 42 manuales de trabajo
    ├── herramientas/             # comprobar_guion.py (4 pilares) · consumo_sesion.py (consumo estimado)
    ├── ideas-virales/
    │   ├── ANALISIS.md           # Análisis destilado de reels virales → rúbrica
    │   ├── ANALISIS-series-es.md # 10 virales en español → umbrales de los 4 pilares
    │   ├── raw/                  # 🔒 Los reels analizados
    │   └── frames/               # 🔒 Tiras de cuadros por reel
    ├── references/current/       # 🔒 Videos que marcan la vara estética
    ├── scripts/<tema>/           # 🔒 Concepto, guion de voz y plan de escenas de cada video
    ├── assets/audios/<slug>/     # 🔒 voz.mp3 de cada video
    ├── exports/<slug>/           # 🔒 Todo lo producido de cada video
    ├── publicacion/              # 🔒 Calendario, fichas de subida, marca, análisis de redes
    └── aprobaciones-pendientes.md  # 🔒 Cola de permisos del protocolo nocturno
```

### Temas (`scripts/<tema>/`)

| Tema | Señales |
| --- | --- |
| `historia` | Fechas, personajes, imperios, paradojas del pasado |
| `economia` | Empresas, precios, mercados, modelos de negocio |
| `tecnologia` | Gadgets, software, internet, IA |
| `ciencia` | Física, química, biología, astronomía |
| `finanzas` | Inversión, bancos, tarjetas, impuestos |
| `psicologia` | Sesgos, comportamiento, emociones |
| `salud` | Cuerpo humano, hábitos, nutrición |
| `sociedad` | Política, cultura, tendencias |
| `curiosidades` | Datos raros, récords, todo lo demás |

Si una idea cruza dos temas, gana el más específico.

### Archivos por video (`<slug>`)

Por video **solo existen** estos documentos, y cada uno tiene un dueño:

| Archivo | Ruta | Dueño |
| --- | --- | --- |
| `<slug>.concept.md` | `scripts/<tema>/` | viral-strategist |
| `<slug>.guion-voz.md` | `scripts/<tema>/` | creative-producer |
| `<slug>.escenas.md` | `scripts/<tema>/` | creative-producer |
| `voz.mp3` (`voz-v2.mp3`…) | `assets/audios/<slug>/` | persona creadora |
| `escenas_<slug>.py` · `sfx_<slug>.py` | `exports/<slug>/` | video-editor |
| `prueba_10s.mp4` · `final.mp4` · `final_rN.mp4` | `exports/<slug>/` | video-editor |
| `crudo_rN.mp4` · `qa/rN_frames/` · `architect_rN` (enlace al proyecto Remotion) | `exports/<slug>/` | video-editor |
| `render-log.md` (comandos y medidas) | `exports/<slug>/` | video-editor |
| `review.md` (hallazgos con evidencia) | `exports/<slug>/` | quality-reviewer |
| `project-log.md` (decisiones, palabras literales del creador, tokens) | `exports/<slug>/` | executive-producer |

Nada se sobrescribe: cada versión se guarda como `_rN` antes de reemplazarla.

---

## 🤖 Agentes

| Agente | Responsabilidad | Entrega | Señal | Modelo |
| --- | --- | --- | --- | --- |
| `shorts-executive-producer` | Coordina, respeta los ✋, verifica en disco, lleva el log. No produce | `project-log.md` | `🎬 PROYECTO ENTREGADO` / `🛑 BUCLE AGOTADO` | Opus medium |
| `shorts-viral-strategist` | 3 ideas puntuadas con rúbrica; separa hechos de hipótesis | `<slug>.concept.md` | `CONCEPTO LISTO` | Opus medium |
| `shorts-creative-producer` | Texto para la voz y plan de escenas | `guion-voz.md` + `escenas.md` | `GUION Y ESCENAS LISTOS` | Opus medium |
| `shorts-video-editor` | Pipeline de Remotion, generadores de escenas y SFX | `final.mp4` + `render-log.md` | `VIDEO LISTO (shorts · Remotion)` | Opus high (nunca Sonnet) |
| `shorts-quality-reviewer` | 30 comprobaciones medidas con comandos | `review.md` | `REVIEW APPROVED` / `REVIEW NEEDS_REVISION` | Opus high |
| `shorts-social-strategist` | Textos por red, portada, horarios, calendario y lectura de estadísticas | `publicacion/calendario.md`, `subidas/<slug>.md`, `analisis-redes-*.md` | `CALENDARIO LISTO` / `ANALISIS LISTO` | Sonnet medium (Opus si no da la talla) |

El director corre como **sesión principal** (`claude --agent shorts-executive-producer`) porque un subagente en segundo plano no puede lanzar otros agentes.

### Esquema de un agente

Cada agente es un Markdown en `.claude/agents/shorts-<rol>.md` con cabecera YAML y cuerpo:

```markdown
---
name: shorts-<rol>
description: Qué hace, qué entrega y «NO usar para montaje ni storytelling»
model: opus | sonnet
effort: medium | high
tools: Read, Write, Edit, Bash, …   # permisos mínimos para su oficio
---

# shorts-<rol>
## Entradas            # qué archivos lee (si falta uno, se detiene)
## Salida              # qué archivo escribe, dónde y con qué señal termina
## Lecciones (…)       # reglas aprendidas en producción, con fecha y origen
## Escala si           # cuándo para y devuelve el problema al director
## Reglas globales     # las 5 reglas comunes
```

El contrato cubre **6 secciones**: responsabilidad exclusiva, información de entrada, formato de salida, criterios de aceptación, herramientas permitidas y condiciones para escalar.

| Agente | Herramientas |
| --- | --- |
| executive-producer | `Read, Write, Edit, Bash, Agent, Task*, Skill, WebSearch, Chrome` — el único que lanza agentes |
| viral-strategist · creative-producer | `Read, Write, Edit, Bash, WebFetch, WebSearch` |
| video-editor | `Read, Write, Edit, Bash, Skill, WebSearch` |
| quality-reviewer | `Read, Write, Edit, Bash, WebSearch` |
| social-strategist | `Read, Write, Edit, Bash, WebSearch, WebFetch, Chrome` (solo lectura) |

### Cómo se comunican

```text
                     ┌──────────────────────────────┐
  persona creadora ◀▶│ executive-producer (sesión)  │──▶ project-log.md
        (✋)         └──────────────┬───────────────┘
                                   │ encargo corto: rutas, estilo, qué cambiar y qué no
        ┌──────────────┬───────────┼──────────────┬───────────────┐
        ▼              ▼           ▼              ▼               ▼
   strategist   creative-prod.   editor        reviewer      social-strat.
        │              │           │              │               │
        └──────────────┴─────┬─────┴──────────────┴───────────────┘
                             ▼
              archivos en disco + señal de cierre
```

- **Los agentes no hablan entre sí**: se pasan el trabajo por archivos. Cada uno lee lo que dejó el anterior.
- **El director verifica en disco** (`test -f`, `ffprobe`, `sha256sum`) antes de dar un paso por hecho; si un agente termina sin informe, comprueba los archivos y sigue.
- **Encargos cortos**: rutas exactas, estilo del proyecto, qué cambiar y qué no tocar. No se meten reglas que no vengan del perfil del estilo, del creador o de las referencias.
- **Un agente en marcha no recibe mensajes**: las preferencias nuevas se escriben en el agente o la skill *antes* de lanzarlo.
- **Dudas de narrativa**: el director consulta a strategist y creative-producer en paralelo, sin que escriban archivos, y recomienda una opción.
- **Paralelismo**: máximo 3 agentes Opus a la vez (1 en modo nocturno).
- **Vigilancia**: si un agente pasa 20 min sin escribir en disco, probablemente espera un permiso en la terminal; no se relanza (duplicaría el gasto).
- **Memoria**: las lecciones viven en los propios agentes (secciones fechadas), en los `aprendizajes.md` de cada estilo y en las skills.

---

## 🧠 Skills

En `nichos/shorts/skills/`. Los agentes las leen antes de trabajar.

| Grupo | Skills | Quién |
| --- | --- | --- |
| Ideas y viralidad | `viral-idea-generation`, `viral-rubric`, `viral-reference-analysis`, `viral-pattern-execution`, `fact-vs-hypothesis`, `concepto-shorts`, `fases-viralidad-tiktok`, `adaptacion-ingles` (adaptar reels en inglés) | strategist, social-strategist |
| Guion | 🔒 `guion-4-pilares` (gancho · retención · profundización · CTA; se comprueba con `herramientas/comprobar_guion.py`), `hook-opening` (primeros 3 s), `narrative-structure`, `scriptwriting` (mapa tema → carpeta) | strategist, creative-producer |
| Escenas y estilo | `plan-escenas`, `visual-reference-analysis`, `composition-vertical` (zonas seguras), `pacing-tight` (ritmo), `subtitles-keyword-highlight` | creative-producer, editor |
| Edición | `edicion-escenas`, `reutilizacion-materiales`, `revision-por-bloques` (paradas de revisión antes del render) | editor |
| Animación por estilo | `animacion-monigotes`, `animacion-monigotes-3d`, `animacion-serie-pov` | editor |
| Calidad | `revision-calidad` (las 30 comprobaciones), `render-inspection`, `errores-edicion` y `errores-serie-pov` (errores ya cometidos) | reviewer, editor |
| Redes | `publicacion-multired`, `red-instagram-reels`, `red-tiktok`, `red-youtube-shorts`, `red-facebook-reels`, `titulos-descripciones`, `portadas-shorts`, `checklist-subida`, `lanzamiento-cuenta`, `seguimiento-resultados`, `metricas-viralidad`, `analisis-cuentas`, `investigacion-redes-chrome` | social-strategist |
| Dirección | `presupuesto-tokens`, `protocolo-nocturno` | director |

---

## 🔄 Flujo de producción

```text
 1. IDEA ─────────── viral-strategist ──▶ 3 ideas puntuadas ──✋ elige una ──▶ concept.md
 2. GUION+ESCENAS ── creative-producer ─▶ guion-voz.md + escenas.md ──✋ aprueba
 3. VOZ ──────────── la persona creadora la genera en ElevenLabs ──▶ assets/audios/<slug>/voz.mp3
 4. PRUEBA ───────── video-editor ──────▶ prueba_10s.mp4 ──✋ ok
 5. RENDER ───────── video-editor ──────▶ final.mp4 (+ SFX)
 6. REVISIÓN ─────── quality-reviewer ──▶ review.md: APPROVED o NEEDS_REVISION
 7. CORRECCIONES ─── editor ⇄ reviewer (máx. 2 rondas automáticas)
 8. ENTREGA ──────── director: 🎬 PROYECTO ENTREGADO
 9. PUBLICACIÓN ──── social-strategist ─▶ calendario.md + subidas/<slug>.md ──✋ la persona sube
10. MEDICIÓN ─────── social-strategist ─▶ analisis-redes-*.md (24 h y 7 días)
```

- **Paso 1:** las ideas se puntúan con una rúbrica derivada de `ANALISIS.md`; cada dato se marca como hecho o hipótesis.
- **Paso 3:** el plan gratuito de ElevenLabs no permite voces de biblioteca por API, así que la voz se genera en la web pegando `guion-voz.md`.
- **Paso 4:** la prueba de 10 s aprueba el aspecto antes de gastar en el render completo, que es lo más caro.
- **Paso 7:** antes de cada ronda el reviewer valida qué quedó arreglado. Tras 2 rondas automáticas, `🛑 BUCLE AGOTADO` con 3 opciones. Las correcciones de la persona creadora no tienen tope y se apuntan literales en el log.
- **Cierre por decisión:** si la persona creadora da el video por bueno, se entrega aunque el reviewer no haya aprobado; los hallazgos quedan como aceptados en el log.
- **Al entregar:** el director anota slug, versión, ruta, duración, LUFS, rondas y tokens, y un análisis posterior (fallos, ahorros y reglas nuevas).

---

## 🎞️ Cadena del editor (modo «solo audio»)

Desde `tools/architect/`, con Node 24:

| # | Paso | Qué hace |
| --- | --- | --- |
| 0 | `ffmpeg` | Crudo sintético: fondo liso + `voz.mp3` → `crudo_rN.mp4` |
| 1 | `npx tsx herramientas/ingesta.ts` | Crea el proyecto en `proyectos/<fecha>-<slug>-rN/` |
| 2 | `npx tsx herramientas/transcribir.ts` | Whisper → palabras con tiempos (se compara con el guion) |
| 3 | `npx tsx herramientas/cortes.ts` | Cortes sin quitar nada de la voz |
| 4 | `npx tsx herramientas/base.ts` | Video base |
| 5 | `npx tsx herramientas/subtitulos.ts` | Bloques de subtítulo |
| 6 | `director.ts` → `armar-edl.ts` → `ajustar.ts` | EDL versionada (`edicion-vN.json`) |
| 7 | `python3 escenas_<slug>.py --edl …` | Escenas, cámara y carteles anclados a palabras |
| 8 | `python3 sfx_<slug>.py --edl …` | Efectos de sonido |
| 9 | `npx tsx herramientas/validar.ts` | Valida la EDL contra su esquema |
| 10 | `npx remotion render src/index.ts Reel …` | Imagen y audio |
| 11 | `ffmpeg` (loudnorm) | Mezcla y normaliza a −14 LUFS → `final.mp4` |

### Capas propias añadidas al architect

| Capa | Archivos |
| --- | --- |
| Escenas ilustradas | `src/estilo/escenas.ts`, `src/reel/escenas/` |
| Etiquetas de ilustración | `src/estilo/ilustracion.ts` |
| Subtítulos «selección» (arriba, palabra por palabra, recuadro en la clave) | `src/estilo/subtitulos-seleccion.ts` |
| Subtítulos centrados (1–2 palabras) | `src/estilo/subtitulos-centro.ts` |
| Monigotes y escenarios | `src/reel/escenas/Monigote.tsx`, `Escenario.tsx` |
| Cámara `golpe` con desenfoque | `src/estilo/motion.ts`, `src/estilo/escenas.ts` |
| SFX extra en la EDL | `src/esquema/edicion.ts` (`sfx_extra`), `biblioteca/sfx/` |
| Perfiles de estilo | `estilo/estilos/<estilo>/perfil.md` + `aprendizajes.md` |
| Catálogo de reutilizables | `biblioteca/reutilizables/CATALOGO.md` + `comprobar_catalogo.py` |
| Pruebas | `pruebas/unit/*.test.ts` |

---

## 📦 Biblioteca de materiales

Vive en `tools/architect/biblioteca/`. Es el material reutilizable entre videos, para no dibujar ni generar dos veces lo mismo.

```bash
tools/architect/biblioteca/
├── reutilizables/
│   ├── CATALOGO.md           # Índice único de todo lo reutilizable (escenas y SFX)
│   └── comprobar_catalogo.py # Verifica que el catálogo está al día
├── sfx/
│   ├── catalogo.json         # Metadatos de cada sonido (normalización, reglas)
│   ├── aprobaciones.json     # Qué sonidos aprobó o rechazó la persona creadora
│   ├── comun/                # Sonidos usados en ≥ 2 videos
│   └── _originales/<origen>/ # Sonidos por procedencia (API, síntesis…)
├── fuentes/                  # Fuentes OFL (Figtree, Archivo Black, Anton, Inter…) + preparar.sh
├── stickers/                 # logos/ (Simple Icons CC0, svgl MIT) · propios/
├── memes/catalogo.json
├── vocabulario.json          # Nombres que whisper debe reconocer + correcciones
└── LICENCIAS.md              # Una fila por archivo con su licencia
```

Las piezas visuales reutilizables son componentes React en `src/reel/escenas/` y `src/reel/escenas/comun/`.

### Reglas de reutilización (skill `reutilizacion-materiales`)

1. **Catálogo primero**: antes de crear una pieza o un sonido, el editor busca en `CATALOGO.md`.
2. **Columna «Usos»**: cuenta en cuántos videos se ha usado cada pieza.
3. **Promoción a `comun/`**: con ≥ 2 usos se copia a `comun/`; el original se queda donde estaba para no alterar renders antiguos, y los videos nuevos importan desde `comun/`. Una prueba (`pruebas/unit/comun.test.ts`) comprueba que la copia dibuja igual.
4. **Al cerrar un video**: `python3 tools/architect/biblioteca/reutilizables/comprobar_catalogo.py` debe decir «CATALOGO al día».

### De dónde salen los SFX (en este orden)

1. Catálogo propio (`biblioteca/sfx/`)
2. Fuentes gratuitas con licencia clara (p. ej. Kenney, CC0)
3. Síntesis local (`herramientas/sfx/sintesis.ts`)
4. API de ElevenLabs Sound Effects — gasta créditos: antes se comprueba el saldo (`GET /v1/user/subscription`) y que la clave tenga permiso `sound_generation`

Cada sonido nuevo se registra en `catalogo.json`, `CATALOGO.md` y `LICENCIAS.md`.

---

## 🎨 Estilos

Cada proyecto declara su estilo en el `project-log.md` y en cada encargo. El `perfil.md` del estilo gana sobre cualquier agente; las correcciones duraderas de la persona creadora se añaden a su `aprendizajes.md`.

| | `estilo-gabriel` | `estilo-monigotes` |
| --- | --- | --- |
| Imagen | Escenas 2D ilustradas de noche, esquemas en neón, gráficos del tema, UI de móvil, capítulos | Monigotes de cabeza redonda en escenarios saturados de atrezo |
| Ritmo | Cambio visible cada ≤ 3 s; se corta solo si cambia lo mostrado; fundidos de 0.4 s | Un cambio cada 1–1.5 s, golpes o barridos con desenfoque, sin fundidos |
| Subtítulos | «Selección»: Figtree arriba al centro, palabra a palabra, recuadro en la clave; bajan en tomas con gráficos | Centrados, 1–2 palabras, Archivo Black con contorno; abajo (y≈1380) o arriba (y≈950) según el plano |
| Sonido | Voz (+ ambiente suave) | Voz + SFX diegéticos de lo que aparece, sin música, ≥ 10 dB bajo la voz |
| Final | Bucle con 1.2 s de cola | Bucle |

| | `estilo-monigotes-3d` | `estilo-serie-pov` |
| --- | --- | --- |
| Imagen | Los mismos monigotes 2D dentro de escenarios 3D de CSS; la cámara viaja en profundidad y nunca para | 2D plano en segunda persona («tú»): personajes de cabeza negra con filo de luz, sudadera de color por personaje, HUD «DÍA · hora · lugar · cuenta atrás», UI de móvil en POV |
| Ritmo | Como monigotes, con barridos con desenfoque | Cortes secos (flash blanco, flashback sepia, barrido); algo nuevo cada ≈ 1.7 s |
| Subtítulos | Como monigotes | Poppins ExtraBold en mayúsculas, 2–3 palabras, la dicha en amarillo, fijos en y ≈ 1460 |
| Sonido | Como monigotes | Sin música; sirena, ambiente grave y SFX al nivel y timbre medidos del original; varias voces |
| Final | Bucle | Elección A/B en pantalla + «Sígueme para la parte N»; serie por episodios, puede pasar de 90 s |

Los estilos no se mezclan: ninguna regla de un perfil se aplica a otro.

**Prohibido:** un emoji o icono por palabra, formas geométricas apiladas, texto plano como visual principal, pantalla vacía, imágenes generadas con Flux, cortes sin cambio y finales en seco.

---

## ✅ Control de calidad

El reviewer **mide con comandos**; no opina a ojo.

| Qué | Cómo |
| --- | --- |
| Formato y duración | `ffprobe`: 1080×1920, 30 fps, H.264 + AAC |
| Audio | `ffmpeg -af ebur128`: LUFS, LRA, pico y nivel de cada SFX frente a la voz |
| Bucle | Último cuadro ≈ primero (SSIM ≈ 0.98) |
| Composición | Hojas de cuadros (`qa/rN_frames/`): carteles en zona segura (x 135–945), subtítulos que no tapan lo clave, sin pantallas vacías |
| Contenido | Texto igual al guion; datos correctos |
| Errores conocidos | Lista de `revision-calidad.md` y `aprendizajes.md` |

Cada hallazgo lleva gravedad (**CRITICAL / MAJOR / MINOR**) y se atribuye a quien lo causó. La primera revisión es completa; en las rondas solo se revisa lo que cambió. Solo el reviewer declara `APPROVED`.

| Medida de entrega | Valor |
| --- | --- |
| Formato | 1080×1920, 30 fps, H.264 + AAC |
| Duración | 20–90 s (ideal 60–90 s) |
| Volumen | −14 LUFS integrado (±0.5), LRA ≤ 2.5 LU, pico ≤ −0.7 dBFS |

---

## 📣 Publicación y medición

Lo lleva el `shorts-social-strategist` en `nichos/shorts/publicacion/`:

| Archivo | Qué es |
| --- | --- |
| `calendario.md` | Fechas, horas, orden por red, textos de cada video y tabla de resultados |
| `subidas/<slug>.md` | Ficha lista para copiar: por red, título, descripción, hashtags, **comentario fijado**, portada (segundo del cuadro), hora y ajustes |
| `analisis-redes-*.md` | Informes de estadísticas y de cuentas de referencia |
| `marca/` | Nombre del canal, descripciones, prompts de logo y banner |
| `cuentas/<red>/` | Datos guardados de cuentas de referencia (se reutilizan si tienen < 4 días) |

- **Redes:** Instagram Reels, TikTok, YouTube Shorts y Facebook Reels, cada una con su skill.
- **Medición** a las 24 h y a los 7 días: vistas, % visto, compartidos, guardados, comentarios y seguidores, marcados [M]/[H].
- **Chrome solo en lectura**: el agente no publica, no comenta y no inicia sesión. Las subidas las hace siempre la persona creadora.

---

## 🪙 Presupuesto de tokens

Skill `presupuesto-tokens`: se aplica antes de cada tarea cara y cada entrega apunta sus tokens en el `project-log.md`.

| Tarea | Coste aprox. |
| --- | --- |
| Concepto | ~87K |
| Guion + escenas | ~104K |
| Prueba de 10 s | ~300–380K |
| Render | 180–430K |
| Revisión completa / acotada | ~150–205K / ~70–83K |
| Análisis de redes con Chrome (Sonnet) | 50–100K |
| **Video completo** | **~0.9–1.6M** |

**Ahorro:** juntar cambios en una pasada del editor, revisiones acotadas en las rondas, encargos cortos, lo mecánico a Sonnet o a un comando, máximo 3 Opus a la vez y reutilizar catálogo y datos recientes. Si una partida supera la tabla en más de un 50 %, se apunta la causa.

---

## 🌙 Protocolos del director

- **Informe de avance cada 45 min** mientras haya agentes en marcha (estado comprobado en disco).
- **Protocolo nocturno** (skill `protocolo-nocturno`, se activa con «me voy a dormir»): se termina lo empezado sin interrumpir, un solo agente a la vez, lo que pida permiso va a `aprobaciones-pendientes.md` y al volver hay un resumen (completado / fallido / bloqueado / aprobaciones / siguientes pasos).
- **Antes de un render**: comprobar fuentes de sonido, claves y saldo de ElevenLabs, y que los comandos del agente están en la allowlist.

---

## ⚙️ Configuración

### `.env` (raíz)

```env
ELEVENLABS_API_KEY=...
```

### `.claude/settings.json`

Copia `.claude/settings.example.json` y sustituye los marcadores:

| Marcador | Valor |
| --- | --- |
| `<RUTA_PROYECTO>` | Ruta absoluta del proyecto |
| `<HOME>` | Tu carpeta personal |
| `<PROYECTO_CODIFICADO>` | Nombre de la carpeta de memoria de Claude Code (la ruta del proyecto con `/` cambiadas por `-`) |

Incluye:
- **Allowlist** (lectura/escritura en el proyecto, ffmpeg, npx, python3, node, yt-dlp, utilidades de archivo, WebSearch, dominios de WebFetch) y `defaultMode: acceptEdits`.
- **Siempre preguntan:** `rm`, `sudo`, `git push` y cualquier comando con `--si-gasto` (gasto de créditos).
- **`env`:** rutas de `whisper-cli` y `whisper-vad-speech-segments`.

> ⚠️ **Nunca uses modo plan** con agentes en segundo plano: bloquea sus escrituras sin avisar. «Permiso denegado» en un agente = falta una regla en `settings.json`.

---

## 🚀 Replicar el proyecto

```bash
# 1. Proyecto
git clone <repository-url> video-editor
cd video-editor

# 2. Node 24
source ~/.nvm/nvm.sh && nvm install 24 && nvm use 24

# 3. Motor de render
git clone https://github.com/Hainrixz/video-editor-architect.git tools/architect
cd tools/architect
npm install
npm run instalar -- --si   # ffmpeg, whisper.cpp + modelos, Python (uv), yt-dlp, fuentes
npm run doctor             # comprueba que todo está
cd ../..

# 4. Configuración local
cp RESUME.example.md RESUME.md
cp .claude/settings.example.json .claude/settings.json   # y sustituye los marcadores
touch .env                                               # y añade las claves

# 5. Carpetas de trabajo
mkdir -p nichos/shorts/{scripts/{historia,economia,tecnologia,ciencia,finanzas,psicologia,salud,sociedad,curiosidades},assets/audios,exports,references/current,ideas-virales/{raw,frames},publicacion/{subidas,cuentas,marca}} ideas/shorts

# 6. Producir
claude --agent shorts-executive-producer           # director
claude --agent shorts-executive-producer --chrome  # si hay que leer redes
```

Los modelos de whisper (`ggml-large-v3.bin`, `ggml-silero-v5.1.2.bin`) quedan en `~/.cache/video-editor/modelos/`.

| Quiero… | Le digo al director |
| --- | --- |
| Un video nuevo | «Quiero hacer un short sobre <tema>. Referencias: <links>.» |
| Seguir uno a medias | «Lee RESUME.md y sigue con <slug>.» |
| Rehacer con otra voz | Dejar `voz-v2.mp3` en `assets/audios/<slug>/` y pedir que se re-sincronice |
| Textos para subir | «Dame la ficha de subida de <slug>.» |
| Medir un video | «Analiza <slug> en redes.» (sesión iniciada en Chrome) |
| Dejarlo trabajando | «Me voy a dormir.» |

---

## 🩺 Problemas frecuentes

| Síntoma | Causa probable | Qué hacer |
| --- | --- | --- |
| «Permiso denegado» en un agente | Falta una regla en `settings.json` | Añadirla y relanzar |
| Un agente sin avances en 20 min | Espera un permiso en la terminal | Mirar la terminal; no relanzarlo |
| `npx` falla con errores raros | Node 20 en vez de 24 | `nvm use 24` |
| La transcripción no cuadra con el guion | ElevenLabs leyó distinto | Comparar el número de palabras; regenerar la voz o ajustar el texto |
| ElevenLabs da 401/403 en SFX | Clave sin `sound_generation` o sin saldo | Comprobar con `GET /v1/user/subscription` y revisar los permisos de la clave |
| Los agentes no escriben nada | Sesión en modo plan | Salir del modo plan |
| El render se corta | Límite de uso o demasiados agentes a la vez | Máx. 3 Opus en paralelo; relanzar solo esa parte |

---

## 🤝 Contribuir

### Commits

[Conventional Commits](https://www.conventionalcommits.org/):

```bash
<type>(<scope>): <subject>
```

Tipos: `feat`, `fix`, `refactor`, `docs`, `chore`.

```bash
feat(editor): capa de subtítulos centrados
docs(skills): regla de densidad de SFX
chore(agents): ajustar modelo del social-strategist
```

### Reglas globales (todos los agentes)

1. Inspecciona el entorno antes de decidir arquitectura.
2. Usa solo los permisos declarados.
3. No sobrescribas ni elimines originales: versiona con `_rN`.
4. No afirmes nada sin verificarlo (`test -f`, `ffprobe`, `ebur128`).
5. No prometas viralidad: criterios medibles y métricas reales.

### Convenciones

- Un solo `CLAUDE.md` en la raíz.
- Agentes con prefijo de nicho (`shorts-*`); nunca se cruzan skills, agentes ni convenciones entre nichos.
- Las preferencias nuevas de la persona creadora se escriben en el agente o la skill antes del siguiente encargo; las de estilo, en `aprendizajes.md`.

Las reglas completas están en [`CLAUDE.md`](./CLAUDE.md).

---
