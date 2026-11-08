# 🎬 Video Editor — Shorts

<div align="center">

**English** · [Español](./README.md)

### AI-agent production system for vertical shorts

A team of Claude Code agents turns a topic into a publish-ready 1080×1920 vertical video: idea → script → scenes → render → review → social media calendar. The creator only decides at the checkpoints and provides the voice.

![Claude Code](https://img.shields.io/badge/Claude_Code-agents-D97757?logo=anthropic)
![Remotion](https://img.shields.io/badge/Remotion-4-0B84F3?logo=remotion)
![React](https://img.shields.io/badge/React-19-61DAFB?logo=react)
![Node.js](https://img.shields.io/badge/Node.js-24-339933?logo=nodedotjs)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python)
![FFmpeg](https://img.shields.io/badge/FFmpeg-6.1-007808?logo=ffmpeg)

</div>

---

## 📚 Documentation

| | |
| --- | --- |
| 📖 **This README** | Full explanation of the system and how to replicate it |
| 📏 [`CLAUDE.md`](./CLAUDE.md) | Exact rules the agents follow (source of truth) |
| 🤖 [`.claude/agents/`](./.claude/agents/) | The 6 agents, one file each |
| 🧠 [`nichos/shorts/skills/`](./nichos/shorts/skills/) | The 33 working manuals |
| 📈 [`nichos/shorts/ideas-virales/ANALISIS.md`](./nichos/shorts/ideas-virales/ANALISIS.md) | Viral reels analysis the idea rubric is built on |
| 📍 [`RESUME.example.md`](./RESUME.example.md) | Session state template |
| 🔐 [`.claude/settings.example.json`](./.claude/settings.example.json) | Permissions template |

> **Language note:** the agents, skills, rules and folder/file names are in **Spanish** — the system reads them literally, so they are not translated here. Names such as `escenas`, `guion-voz` or `VIDEO LISTO` appear as-is, with their meaning explained.

---

## 📖 Overview

The project **is not an application**: it is an arrangement of folders, agents, skills and a render engine that Claude Code follows to produce videos.

| Piece | What it is | Where |
| --- | --- | --- |
| **Agents** | A Claude with a single job and a work contract | `.claude/agents/` |
| **Skills** | Markdown manuals with the "how-to" of each task | `nichos/shorts/skills/` |
| **Rules** | What everyone complies with: format, styles, flow, permissions | `CLAUDE.md` |
| **Render engine** | Remotion: the video is described in JSON and drawn with code | `tools/architect/` |
| **Creator** | Picks the idea, approves script and test, generates the voice, publishes | ✋ |

**Core principle:** all timing comes from the voice. Whisper transcribes word by word, and every scene, subtitle and sound effect is anchored to a word ("when it says *piano*, a key sounds"). If the voice changes, the generator is re-run and everything repositions itself.

> **Note:** this repository only contains the system for the `shorts` niche. It includes no videos, audio, images, scripts or publishing data.

---

## 📘 Glossary

| Term | Meaning |
| --- | --- |
| **Slug** | Short video name, no spaces or accents. All its folders use it |
| **Director** | The `shorts-executive-producer` agent. Coordinates; does not produce |
| **Skill** | Manual with the procedure for one task (e.g. how to write a hook) |
| **EDL** | *Edit decision list*: JSON (`edicion-vN.json`) describing what is seen, heard and read at each moment |
| **Synthetic raw** (`crudo`) | Plain background + voice. Explainers have no camera footage: the raw is just the voice |
| **SFX** | Sound effects |
| **LUFS** | Perceived loudness. Platforms normalize to −14 LUFS |
| **Loop** (`bucle`) | The ending joins the beginning so the replay is seamless |
| **Round (Rn)** | Each version of a video: `final_r2.mp4` is version 2 |
| **Signal** | Phrase an agent uses to declare its work done (`VIDEO LISTO`…) |
| **✋** | Checkpoint: the creator decides |
| **[M] / [H]** | Measured fact / hypothesis. Every social media figure is tagged this way |

---

## 🛠 Tech Stack

| Technology | Purpose |
| --- | --- |
| **Claude Code** | Runs the agents; permissions in `.claude/settings.json` |
| **Remotion 4 + React 19 + TypeScript** | Renders the video from the EDL |
| [**video-editor-architect**](https://github.com/Hainrixz/video-editor-architect) | Reel editor built on Remotion, extended with our own layers |
| **Node.js 24** (nvm) | Editor tooling (`npx tsx …`) |
| **FFmpeg / FFprobe 6.1** | Synthetic raw, mixing and measurement (duration, LUFS, peaks) |
| **whisper.cpp large-v3 + Silero VAD** | Local transcription with per-word timestamps |
| **Python 3.12** | Per-video scene and SFX generators, measurements |
| **ElevenLabs** | Voice (via the web app) and sound effects (API) |
| **yt-dlp** | Downloads reference reels for analysis |
| **Claude in Chrome** (optional) | Reads social media analytics, read-only |
| **Vitest** | Tests for the editor code |

---

## 📂 Project Structure

Items marked 🔒 exist locally but are **not committed** (`.gitignore`).

```bash
.
├── README.md / README.en.md
├── CLAUDE.md                     # Project-wide rules (the only CLAUDE.md)
├── RESUME.example.md             # Template → copy to RESUME.md 🔒
├── .env                          # 🔒 API keys
├── .nvmrc                        # Node 24
├── .claude/
│   ├── settings.example.json     # Template → copy to settings.json 🔒
│   └── agents/                   # 6 shorts-*.md agents
├── ideas/shorts/                 # 🔒 Brainstorms: YYYY-MM-DD-<slug>.md
├── tools/                        # 🔒 External clones
│   └── architect/                # Render engine (Remotion) + asset library
└── nichos/shorts/                # "niches/shorts"
    ├── skills/                   # 33 working manuals
    ├── ideas-virales/            # "viral ideas"
    │   ├── ANALISIS.md           # Distilled analysis of viral reels → rubric
    │   ├── raw/                  # 🔒 The analyzed reels
    │   └── frames/               # 🔒 Frame strips per reel
    ├── references/current/       # 🔒 Videos that set the aesthetic bar
    ├── scripts/<tema>/           # 🔒 Concept, voice script and scene plan per video
    ├── assets/audios/<slug>/     # 🔒 voz.mp3 (voice) per video
    ├── exports/<slug>/           # 🔒 Everything produced for each video
    ├── publicacion/              # 🔒 Calendar, upload sheets, brand, analytics
    └── aprobaciones-pendientes.md  # 🔒 Night-mode permission queue
```

### Topics (`scripts/<tema>/`)

| Folder | Topic | Signals |
| --- | --- | --- |
| `historia` | History | Dates, historical figures, empires, paradoxes |
| `economia` | Economy | Companies, prices, markets, business models |
| `tecnologia` | Technology | Gadgets, software, internet, AI |
| `ciencia` | Science | Physics, chemistry, biology, astronomy |
| `finanzas` | Finance | Investing, banks, cards, taxes |
| `psicologia` | Psychology | Biases, behavior, emotions |
| `salud` | Health | Human body, habits, nutrition |
| `sociedad` | Society | Politics, culture, trends |
| `curiosidades` | Curiosities | Odd facts, records, everything else |

If an idea spans two topics, the more specific one wins.

### Files per video (`<slug>`)

Each video has **only** these documents, and each one has an owner:

| File | Path | Owner |
| --- | --- | --- |
| `<slug>.concept.md` | `scripts/<tema>/` | viral-strategist |
| `<slug>.guion-voz.md` (voice script) | `scripts/<tema>/` | creative-producer |
| `<slug>.escenas.md` (scene plan) | `scripts/<tema>/` | creative-producer |
| `voz.mp3` (`voz-v2.mp3`…) | `assets/audios/<slug>/` | creator |
| `escenas_<slug>.py` · `sfx_<slug>.py` | `exports/<slug>/` | video-editor |
| `prueba_10s.mp4` (10 s test) · `final.mp4` · `final_rN.mp4` | `exports/<slug>/` | video-editor |
| `crudo_rN.mp4` · `qa/rN_frames/` · `architect_rN` (link to the Remotion project) | `exports/<slug>/` | video-editor |
| `render-log.md` (commands and measurements) | `exports/<slug>/` | video-editor |
| `review.md` (findings with evidence) | `exports/<slug>/` | quality-reviewer |
| `project-log.md` (decisions, the creator's literal words, tokens) | `exports/<slug>/` | executive-producer |

Nothing is overwritten: every version is saved as `_rN` before being replaced.

---

## 🤖 Agents

| Agent | Responsibility | Output | Signal | Model |
| --- | --- | --- | --- | --- |
| `shorts-executive-producer` | Coordinates, respects ✋, verifies on disk, keeps the log. Does not produce | `project-log.md` | `🎬 PROYECTO ENTREGADO` (delivered) / `🛑 BUCLE AGOTADO` (loop exhausted) | Opus medium |
| `shorts-viral-strategist` | 3 ideas scored with a rubric; separates facts from hypotheses | `<slug>.concept.md` | `CONCEPTO LISTO` | Opus medium |
| `shorts-creative-producer` | Voice script and scene plan | `guion-voz.md` + `escenas.md` | `GUION Y ESCENAS LISTOS` | Opus medium |
| `shorts-video-editor` | Remotion pipeline, scene and SFX generators | `final.mp4` + `render-log.md` | `VIDEO LISTO (shorts · Remotion)` | Opus high (never Sonnet) |
| `shorts-quality-reviewer` | 30 checks measured with commands | `review.md` | `REVIEW APPROVED` / `REVIEW NEEDS_REVISION` | Opus high |
| `shorts-social-strategist` | Per-platform copy, cover, schedule, calendar and analytics | `publicacion/calendario.md`, `subidas/<slug>.md`, `analisis-redes-*.md` | `CALENDARIO LISTO` / `ANALISIS LISTO` | Sonnet medium (Opus if not good enough) |

The director runs as the **main session** (`claude --agent shorts-executive-producer`) because a background subagent cannot launch other agents.

### Agent schema

Each agent is a Markdown file at `.claude/agents/shorts-<role>.md` with a YAML header and a body:

```markdown
---
name: shorts-<role>
description: What it does, what it delivers, and "NOT for montaje or storytelling"
model: opus | sonnet
effort: medium | high
tools: Read, Write, Edit, Bash, …   # minimum permissions for its job
---

# shorts-<role>
## Entradas            # inputs: files it reads (stops if one is missing)
## Salida              # output: file it writes, where, and its completion signal
## Lecciones (…)       # lessons learned in production, dated and sourced
## Escala si           # escalate if: when it stops and hands back to the director
## Reglas globales     # the 5 shared rules
```

The contract covers **6 sections**: exclusive responsibility, input, output format, acceptance criteria, allowed tools and escalation conditions.

| Agent | Tools |
| --- | --- |
| executive-producer | `Read, Write, Edit, Bash, Agent, Task*, Skill, WebSearch, Chrome` — the only one that launches agents |
| viral-strategist · creative-producer | `Read, Write, Edit, Bash, WebFetch, WebSearch` |
| video-editor | `Read, Write, Edit, Bash, Skill, WebSearch` |
| quality-reviewer | `Read, Write, Edit, Bash, WebSearch` |
| social-strategist | `Read, Write, Edit, Bash, WebSearch, WebFetch, Chrome` (read-only) |

### How they communicate

```text
                     ┌──────────────────────────────┐
         creator    ◀▶│ executive-producer (session) │──▶ project-log.md
          (✋)        └──────────────┬───────────────┘
                                    │ short brief: paths, style, what to change and what not
        ┌──────────────┬────────────┼──────────────┬───────────────┐
        ▼              ▼            ▼              ▼               ▼
   strategist   creative-prod.   editor         reviewer      social-strat.
        │              │            │              │               │
        └──────────────┴──────┬─────┴──────────────┴───────────────┘
                              ▼
                files on disk + completion signal
```

- **Agents don't talk to each other**: they hand work over through files. Each one reads what the previous one left.
- **The director verifies on disk** (`test -f`, `ffprobe`, `sha256sum`) before marking a step done; if an agent ends without a report, it checks the files and moves on.
- **Short briefs**: exact paths, project style, what to change and what not to touch. No rules that don't come from the style profile, the creator or the references.
- **A running agent receives no messages**: new preferences are written into the agent or skill *before* launching it.
- **Narrative doubts**: the director consults strategist and creative-producer in parallel, without them writing files, and recommends one option.
- **Parallelism**: at most 3 Opus agents at once (1 in night mode).
- **Monitoring**: if an agent writes nothing to disk for 20 min, it is probably waiting for a permission prompt; it is not relaunched (that would double the cost).
- **Memory**: lessons live in the agents themselves (dated sections), in each style's `aprendizajes.md` (learnings) and in the skills.

---

## 🧠 Skills

In `nichos/shorts/skills/`. Agents read them before working.

| Group | Skills | Used by |
| --- | --- | --- |
| Ideas and virality | `viral-idea-generation`, `viral-rubric`, `viral-reference-analysis`, `viral-pattern-execution`, `fact-vs-hypothesis`, `concepto-shorts` | strategist |
| Script | `hook-opening` (first 3 s), `narrative-structure`, `scriptwriting` (topic → folder map) | strategist, creative-producer |
| Scenes and style | `plan-escenas`, `visual-reference-analysis`, `composition-vertical` (safe zones), `pacing-tight` (rhythm), `subtitles-keyword-highlight` | creative-producer, editor |
| Editing | `edicion-escenas`, `reutilizacion-materiales` (asset reuse) | editor |
| Quality | `revision-calidad` (the 30 checks), `render-inspection` | reviewer |
| Social media | `publicacion-multired`, `red-instagram-reels`, `red-tiktok`, `red-youtube-shorts`, `red-facebook-reels`, `titulos-descripciones`, `portadas-shorts`, `checklist-subida`, `lanzamiento-cuenta`, `seguimiento-resultados`, `metricas-viralidad`, `analisis-cuentas`, `investigacion-redes-chrome` | social-strategist |
| Direction | `presupuesto-tokens` (token budget), `protocolo-nocturno` (night protocol) | director |

---

## 🔄 Production Flow

```text
 1. IDEA ─────────── viral-strategist ──▶ 3 scored ideas ──✋ pick one ──▶ concept.md
 2. SCRIPT+SCENES ── creative-producer ─▶ guion-voz.md + escenas.md ──✋ approve
 3. VOICE ────────── the creator generates it in ElevenLabs ──▶ assets/audios/<slug>/voz.mp3
 4. TEST ─────────── video-editor ──────▶ prueba_10s.mp4 ──✋ ok
 5. RENDER ───────── video-editor ──────▶ final.mp4 (+ SFX)
 6. REVIEW ───────── quality-reviewer ──▶ review.md: APPROVED or NEEDS_REVISION
 7. FIXES ────────── editor ⇄ reviewer (max. 2 automatic rounds)
 8. DELIVERY ─────── director: 🎬 PROYECTO ENTREGADO
 9. PUBLISHING ───── social-strategist ─▶ calendario.md + subidas/<slug>.md ──✋ the creator uploads
10. MEASUREMENT ──── social-strategist ─▶ analisis-redes-*.md (24 h and 7 days)
```

- **Step 1:** ideas are scored with a rubric derived from `ANALISIS.md`; every claim is tagged as fact or hypothesis.
- **Step 3:** the ElevenLabs free plan doesn't allow library voices via API, so the voice is generated in the web app by pasting `guion-voz.md`.
- **Step 4:** the 10 s test approves the look before spending on the full render, which is the most expensive step.
- **Step 7:** before each round the reviewer validates what was fixed. After 2 automatic rounds, `🛑 BUCLE AGOTADO` with 3 options. The creator's corrections have no limit and are logged verbatim.
- **Closing by decision:** if the creator signs off on the video, it is delivered even without reviewer approval; open findings are logged as accepted.
- **On delivery:** the director records slug, version, path, duration, LUFS, rounds and tokens, plus a post-mortem (failures, savings and new rules).

---

## 🎞️ Editor Pipeline ("audio-only" mode)

From `tools/architect/`, with Node 24:

| # | Step | What it does |
| --- | --- | --- |
| 0 | `ffmpeg` | Synthetic raw: plain background + `voz.mp3` → `crudo_rN.mp4` |
| 1 | `npx tsx herramientas/ingesta.ts` | Creates the project in `proyectos/<date>-<slug>-rN/` |
| 2 | `npx tsx herramientas/transcribir.ts` | Whisper → timed words (checked against the script) |
| 3 | `npx tsx herramientas/cortes.ts` | Cuts without removing any of the voice |
| 4 | `npx tsx herramientas/base.ts` | Base video |
| 5 | `npx tsx herramientas/subtitulos.ts` | Subtitle blocks |
| 6 | `director.ts` → `armar-edl.ts` → `ajustar.ts` | Versioned EDL (`edicion-vN.json`) |
| 7 | `python3 escenas_<slug>.py --edl …` | Scenes, camera and signs anchored to words |
| 8 | `python3 sfx_<slug>.py --edl …` | Sound effects |
| 9 | `npx tsx herramientas/validar.ts` | Validates the EDL against its schema |
| 10 | `npx remotion render src/index.ts Reel …` | Picture and audio |
| 11 | `ffmpeg` (loudnorm) | Mixes and normalizes to −14 LUFS → `final.mp4` |

### Custom layers added to the architect

| Layer | Files |
| --- | --- |
| Illustrated scenes | `src/estilo/escenas.ts`, `src/reel/escenas/` |
| Illustration labels | `src/estilo/ilustracion.ts` |
| "Selection" subtitles (top, word by word, box on the keyword) | `src/estilo/subtitulos-seleccion.ts` |
| Centered subtitles (1–2 words) | `src/estilo/subtitulos-centro.ts` |
| Stick figures and sets | `src/reel/escenas/Monigote.tsx`, `Escenario.tsx` |
| `golpe` camera punch with blur | `src/estilo/motion.ts`, `src/estilo/escenas.ts` |
| Extra SFX in the EDL | `src/esquema/edicion.ts` (`sfx_extra`), `biblioteca/sfx/` |
| Style profiles | `estilo/estilos/<style>/perfil.md` + `aprendizajes.md` |
| Reusable assets catalog | `biblioteca/reutilizables/CATALOGO.md` + `comprobar_catalogo.py` |
| Tests | `pruebas/unit/*.test.ts` |

---

## 📦 Asset Library

Lives in `tools/architect/biblioteca/`. Material reused across videos, so nothing is drawn or generated twice.

```bash
tools/architect/biblioteca/
├── reutilizables/
│   ├── CATALOGO.md           # Single index of everything reusable (scenes and SFX)
│   └── comprobar_catalogo.py # Checks the catalog is up to date
├── sfx/
│   ├── catalogo.json         # Metadata for each sound (normalization, rules)
│   ├── aprobaciones.json     # Sounds approved or rejected by the creator
│   ├── comun/                # Sounds used in ≥ 2 videos
│   └── _originales/<source>/ # Sounds by origin (API, synthesis…)
├── fuentes/                  # OFL fonts (Figtree, Archivo Black, Anton, Inter…) + preparar.sh
├── stickers/                 # logos/ (Simple Icons CC0, svgl MIT) · propios/ (own)
├── memes/catalogo.json
├── vocabulario.json          # Names whisper must recognize + corrections
└── LICENCIAS.md              # One row per file with its license
```

Reusable visual pieces are React components in `src/reel/escenas/` and `src/reel/escenas/comun/`.

### Reuse rules (skill `reutilizacion-materiales`)

1. **Catalog first**: before creating a piece or a sound, the editor searches `CATALOGO.md`.
2. **"Usos" column**: counts how many videos each piece has been used in.
3. **Promotion to `comun/`**: at ≥ 2 uses it is copied to `comun/`; the original stays put so old renders don't change, and new videos import from `comun/`. A test (`pruebas/unit/comun.test.ts`) checks the copy draws identically.
4. **When closing a video**: `python3 tools/architect/biblioteca/reutilizables/comprobar_catalogo.py` must report "CATALOGO al día" (catalog up to date).

### Where SFX come from (in this order)

1. Own catalog (`biblioteca/sfx/`)
2. Free sources with a clear license (e.g. Kenney, CC0)
3. Local synthesis (`herramientas/sfx/sintesis.ts`)
4. ElevenLabs Sound Effects API — spends credits: first check the balance (`GET /v1/user/subscription`) and that the key has the `sound_generation` permission

Every new sound is registered in `catalogo.json`, `CATALOGO.md` and `LICENCIAS.md`.

---

## 🎨 Styles

Each project declares its style in `project-log.md` and in every brief. The style's `perfil.md` (profile) overrides any agent; the creator's lasting corrections are added to its `aprendizajes.md`.

| | `estilo-gabriel` | `estilo-monigotes` (stick figures) |
| --- | --- | --- |
| Visuals | Illustrated 2D night scenes, neon diagrams, topic graphics, phone UI, chapters | Round-headed stick figures in prop-packed, saturated sets |
| Pacing | Visible change every ≤ 3 s; cut only when what's shown changes; 0.4 s crossfades | A change every 1–1.5 s, camera punches or blurred whip pans, no crossfades |
| Subtitles | "Selection": Figtree, top center, word by word, box on the keyword; moves down over graphics | Centered, 1–2 words, Archivo Black with outline; bottom (y≈1380) or top (y≈950) depending on the shot |
| Sound | Voice (+ soft ambience) | Voice + diegetic SFX for what's on screen, no music, ≥ 10 dB under the voice |
| Ending | Loop with a 1.2 s tail | Loop |

**Forbidden:** one emoji or icon per word, stacked geometric shapes, plain text as the main visual, empty screens, Flux-generated images, cuts with no change, and abrupt endings.

---

## ✅ Quality Control

The reviewer **measures with commands**; it doesn't judge by eye.

| What | How |
| --- | --- |
| Format and duration | `ffprobe`: 1080×1920, 30 fps, H.264 + AAC |
| Audio | `ffmpeg -af ebur128`: LUFS, LRA, peak and each SFX level against the voice |
| Loop | Last frame ≈ first (SSIM ≈ 0.98) |
| Composition | Contact sheets (`qa/rN_frames/`): signs in the safe zone (x 135–945), subtitles not covering key content, no empty screens |
| Content | Text matches the script; facts are correct |
| Known errors | List in `revision-calidad.md` and `aprendizajes.md` |

Each finding has a severity (**CRITICAL / MAJOR / MINOR**) and is attributed to whoever caused it. The first review is full; later rounds only check what changed. Only the reviewer declares `APPROVED`.

| Delivery spec | Value |
| --- | --- |
| Format | 1080×1920, 30 fps, H.264 + AAC |
| Duration | 20–90 s (ideal 60–90 s) |
| Loudness | −14 LUFS integrated (±0.5), LRA ≤ 2.5 LU, peak ≤ −0.7 dBFS |

---

## 📣 Publishing and Measurement

Handled by `shorts-social-strategist` in `nichos/shorts/publicacion/`:

| File | What it is |
| --- | --- |
| `calendario.md` | Dates, times, platform order, copy per video and a results table |
| `subidas/<slug>.md` | Ready-to-copy upload sheet: per platform, title, description, hashtags, **pinned comment**, cover (frame timestamp), time and settings |
| `analisis-redes-*.md` | Analytics reports and reference account studies |
| `marca/` | Channel name, descriptions, logo and banner prompts |
| `cuentas/<platform>/` | Saved data from reference accounts (reused if < 4 days old) |

- **Platforms:** Instagram Reels, TikTok, YouTube Shorts and Facebook Reels, each with its own skill.
- **Measured** at 24 h and 7 days: views, % watched, shares, saves, comments and followers, tagged [M]/[H].
- **Chrome is read-only**: the agent doesn't post, comment or log in. Uploads are always done by the creator.

---

## 🪙 Token Budget

Skill `presupuesto-tokens`: applied before every expensive task; each delivery logs its tokens in `project-log.md`.

| Task | Approx. cost |
| --- | --- |
| Concept | ~87K |
| Script + scenes | ~104K |
| 10 s test | ~300–380K |
| Render | 180–430K |
| Full / scoped review | ~150–205K / ~70–83K |
| Social analytics with Chrome (Sonnet) | 50–100K |
| **Full video** | **~0.9–1.6M** |

**Savings:** batch changes into one editor pass, scoped reviews in fix rounds, short briefs, mechanical work to Sonnet or a single command, at most 3 Opus agents at once, and reuse the catalog and recent data. If a line item exceeds the table by more than 50 %, the cause is logged.

---

## 🌙 Director Protocols

- **Progress report every 45 min** while agents are running (status checked on disk).
- **Night protocol** (skill `protocolo-nocturno`, triggered by "me voy a dormir" — "I'm going to sleep"): finish what's started without interruptions, one agent at a time, anything needing permission goes to `aprobaciones-pendientes.md`, and a summary on return (completed / failed / blocked / approvals / next steps).
- **Before a render**: check sound sources, ElevenLabs key and balance, and that the agent's commands are in the allowlist.

---

## ⚙️ Configuration

### `.env` (root)

```env
ELEVENLABS_API_KEY=...
```

### `.claude/settings.json`

Copy `.claude/settings.example.json` and replace the placeholders:

| Placeholder | Value |
| --- | --- |
| `<RUTA_PROYECTO>` | Absolute project path |
| `<HOME>` | Your home folder |
| `<PROYECTO_CODIFICADO>` | Claude Code's memory folder name (the project path with `/` replaced by `-`) |

It contains:
- **Allowlist** (read/write in the project, ffmpeg, npx, python3, node, yt-dlp, file utilities, WebSearch, WebFetch domains) and `defaultMode: acceptEdits`.
- **Always ask:** `rm`, `sudo`, `git push` and any command with `--si-gasto` ("yes, spend": uses credits).
- **`env`:** paths to `whisper-cli` and `whisper-vad-speech-segments`.

> ⚠️ **Never use plan mode** with background agents: it silently blocks their writes. "Permission denied" in an agent = a rule is missing from `settings.json`.

---

## 🚀 Replicating the Project

```bash
# 1. Project
git clone <repository-url> video-editor
cd video-editor

# 2. Node 24
source ~/.nvm/nvm.sh && nvm install 24 && nvm use 24

# 3. Render engine
git clone https://github.com/Hainrixz/video-editor-architect.git tools/architect
cd tools/architect
npm install
npm run instalar -- --si   # ffmpeg, whisper.cpp + models, Python (uv), yt-dlp, fonts
npm run doctor             # checks everything is in place
cd ../..

# 4. Local configuration
cp RESUME.example.md RESUME.md
cp .claude/settings.example.json .claude/settings.json   # then replace the placeholders
touch .env                                               # then add the key

# 5. Working folders
mkdir -p nichos/shorts/{scripts/{historia,economia,tecnologia,ciencia,finanzas,psicologia,salud,sociedad,curiosidades},assets/audios,exports,references/current,ideas-virales/{raw,frames},publicacion/{subidas,cuentas,marca}} ideas/shorts

# 6. Produce
claude --agent shorts-executive-producer           # director
claude --agent shorts-executive-producer --chrome  # if social analytics are needed
```

Whisper models (`ggml-large-v3.bin`, `ggml-silero-v5.1.2.bin`) end up in `~/.cache/video-editor/modelos/`.

The agents work in Spanish. Typical requests to the director:

| I want… | Tell the director |
| --- | --- |
| A new video | «Quiero hacer un short sobre <tema>. Referencias: <links>.» |
| Resume one in progress | «Lee RESUME.md y sigue con <slug>.» |
| Redo with another voice | Drop `voz-v2.mp3` into `assets/audios/<slug>/` and ask for a re-sync |
| Upload copy | «Dame la ficha de subida de <slug>.» |
| Measure a video | «Analiza <slug> en redes.» (logged-in Chrome session) |
| Leave it working | «Me voy a dormir.» |

---

## 🩺 Troubleshooting

| Symptom | Likely cause | What to do |
| --- | --- | --- |
| "Permission denied" in an agent | Missing rule in `settings.json` | Add it and relaunch |
| An agent shows no progress for 20 min | Waiting for a permission prompt | Check the terminal; don't relaunch |
| `npx` fails with odd errors | Node 20 instead of 24 | `nvm use 24` |
| Transcript doesn't match the script | ElevenLabs read it differently | Compare word counts; regenerate the voice or adjust the text |
| ElevenLabs returns 401/403 on SFX | Key lacks `sound_generation` or has no balance | Check with `GET /v1/user/subscription` and review the key's permissions |
| Agents write nothing | Session in plan mode | Exit plan mode |
| Render gets cut off | Usage limit or too many agents at once | Max. 3 Opus in parallel; relaunch only that part |

---

## 🤝 Contributing

### Commits

[Conventional Commits](https://www.conventionalcommits.org/), written in English:

```bash
<type>(<scope>): <subject>
```

Types: `feat`, `fix`, `refactor`, `docs`, `chore`.

```bash
feat(editor): centered subtitles layer
docs(skills): SFX density rule
chore(agents): adjust social-strategist model
```

### Global rules (all agents)

1. Inspect the environment before deciding on architecture.
2. Use only the declared permissions.
3. Never overwrite or delete originals: version with `_rN`.
4. Never claim anything without verifying it (`test -f`, `ffprobe`, `ebur128`).
5. Never promise virality: measurable criteria and real metrics.

### Conventions

- A single `CLAUDE.md` at the root.
- Agents prefixed by niche (`shorts-*`); skills, agents and conventions are never mixed across niches.
- New creator preferences are written into the agent or skill before the next brief; style ones go into `aprendizajes.md`.

Full rules are in [`CLAUDE.md`](./CLAUDE.md).

---
