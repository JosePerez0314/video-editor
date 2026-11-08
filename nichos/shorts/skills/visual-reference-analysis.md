---
name: visual-reference-analysis
description: Extraer el ADN de PRODUCCIÓN de un reel de referencia — estilo visual, cantidad de gráficos, paleta exacta, tratamiento de subtítulos, HUDs diegéticos, cortes por segundo, inventario de assets. Distinta de `viral-reference-analysis` (que extrae ADN narrativo). Entrega un brief técnico que `scriptwriting` y `plan-escenas` consumen para producir el video con la misma vara estética.
---

# visual-reference-analysis

Cómo mirar una referencia **como productor**, no como estratega. Mientras `viral-reference-analysis` responde "¿por qué este reel retiene?", esta skill responde "¿cómo exactamente está hecho visualmente para que yo pueda replicar la vara?".

## Cuándo invocarla

- Antes de escribir el guion técnico de un video nuevo, para heredar estilo/paleta/subs de una referencia.
- Cuando el usuario diga "quiero este video con el estilo de ref2" o "como @loconstruiste".
- Cuando el `quality-reviewer` detectó un gap de ejecución frente a una referencia.
- Al añadir una referencia nueva al canal, para catalogar su vocabulario visual.

## Qué NO es esta skill

- No es analizar por qué el video funcionó narrativamente — eso lo hace `viral-reference-analysis`.
- No es describir el video. Es **extraer parámetros** medibles que un plan de escenas pueda usar.
- No es imitar píxel a píxel. Es destilar vocabulario visual replicable.

## Flujo

### Paso 1 — Localizar el archivo
Mismos pools que viral-reference-analysis:
1. `nichos/shorts/ideas-virales/raw/<id>.mp4`
2. `nichos/shorts/references/<ref>.mp4`
3. URL nuevo → descargar con yt-dlp en `ideas-virales/raw/`.

### Paso 2 — Extracción de parámetros técnicos

**Resolución, duración, fps:**
```bash
ffprobe -v error -show_entries stream=width,height,r_frame_rate -show_entries format=duration -of default=noprint_wrappers=1:nokey=0 <archivo>
```

**Cortes / cambios de escena** (medida objetiva de densidad visual):
```bash
ffmpeg -i <archivo> -filter:v "select='gt(scene,0.3)',showinfo" -f null - 2>&1 | grep -c "pts_time"
```
Dividir entre duración para `cortes/s`. **Referencia**: los breakouts del ANALISIS tienen ≥1 corte cada 2.5s = ≥0.4 cortes/s. Si una referencia tiene <0.3 cortes/s, es muy quieta para shorts.

**Paleta dominante** (hasta 8 colores):
```bash
ffmpeg -y -i <archivo> -vf "fps=1,scale=200:-1,palettegen=max_colors=8" /tmp/palette_<id>.png
```
Luego `Read /tmp/palette_<id>.png` para ver los colores extraídos. Anotar hex aproximados del fondo + 2–3 acentos.

### Paso 3 — Extracción de frames densa (cada 2s)
Para análisis visual detallado:
```bash
mkdir -p /tmp/frames_<id>
ffmpeg -y -v error -i <archivo> -vf "fps=0.5,scale=360:-1" /tmp/frames_<id>/f%03d.jpg
```
Luego componer una cuadrícula para inspección completa:
```bash
ffmpeg -y -v error -i /tmp/frames_<id>/f%03d.jpg -vf "tile=5x6" /tmp/grid_<id>.jpg
```
`Read` sobre `grid_<id>.jpg` da panorama de todo el video de una vez.

### Paso 4 — Checklist de observación (12 categorías)

Responder las 12 con precisión medible. No "parece oscuro" — hex. No "subs centrados" — con padding, color, box, duración.

| # | Categoría | Qué anotar exactamente |
|---|---|---|
| 1 | **Estilo global** | 3D stylized gradient-rich / stickman 2D / isométrico low-poly / editorial 2D plano / motion-graphic UI minimalista |
| 2 | **Inventario de gráficos** | Nº de assets únicos (icons / personajes / props / fondos distintos). Ej: "9 iconos, 1 personaje, 3 fondos" |
| 3 | **Paleta** | Fondo dominante (hex), 2–3 acentos (hex). Ej: `bg #0e0e14, accent #ff8a3d, highlight #4ecbff` |
| 4 | **Tipografía narrativa** | Font family si identificable, peso, tamaño relativo al ancho (ej. "sans mono, bold, ~5% ancho") |
| 5 | **Subtítulos** | Posición (upper third / centro / lower), palabras por cue, keyword highlight (color/box/bold), duración de cue (ms), animación de entrada |
| 6 | **HUDs / UI diegético** | ¿Presentes? Qué info (hora, chip de fuente, timer, contador). Posición. Estilo. |
| 7 | **Densidad visual** | Cortes/s (del paso 2) + beats visuales distintos por cada 10s |
| 8 | **Transiciones** | Tipo (hard cut / fade / slide / morph / scale), duración (ms) |
| 9 | **Composición** | Dónde cae el sujeto (centro / tercio superior), zona reservada (margen top para subs, margen bottom para UI IG) |
| 10 | **Cámara / motion** | Estática / parallax leve / zoom in-out / rotación. Si hay 3D, ¿la cámara se mueve o solo los objetos? |
| 11 | **Branding** | Watermark (posición, opacidad), chapter titles, firma de autor |
| 12 | **Audio production** | Música presente, SFX puntuales, sidechain con voz, loudness aproximado |

### Paso 5 — Brief de producción (salida de esta skill)

Entregar un bloque reutilizable por `scriptwriting` y `plan-escenas`. Formato exacto:

```markdown
## Brief visual: <id | ref1> — <autor | nombre> — <tema corto>

### Especificaciones técnicas
- **Resolución · fps · duración:** 720×1280 · 30fps · 61s
- **Cortes/s:** 0.52 (densidad alta)
- **Beats visuales ≈** 32 en 61s

### Estilo
- **Clasificación:** <una de las 5>
- **Cómo se construiría aquí:** capa `escenas` del architect (Remotion) / pieza nueva a programar / no viable sin artista 3D
- **Replicable con stack actual:** sí/no — <nota>

### Paleta
- Fondo: `#RRGGBB` <nombre>
- Acentos: `#RRGGBB`, `#RRGGBB`, `#RRGGBB`
- Nota: <si usa gradientes, glow, etc.>

### Tipografía
- Font: <nombre o estilo>
- Peso: <regular / bold>
- Tamaño relativo: <% del ancho>

### Subtítulos
- Posición: <upper third / centro / lower>
- Palabras por cue: <n>
- Keyword highlight: <color / box / bold>
- Duración de cue: ~<ms>
- Animación entrada: <scale-pop / fade / slide>

### HUDs / UI diegético
- Presente: sí/no
- Qué: <descripción + posición>
- Útil para este concepto nuevo: sí/no — <nota>

### Inventario de gráficos
- Iconos únicos: <n>
- Personajes: <n>
- Props: <n>
- Fondos: <n>
- Total assets a producir si replico: <n>

### Transiciones
- Tipo dominante: <X>
- Duración: ~<ms>

### Composición
- Sujeto en: <centro / tercio superior / tercio inferior>
- Zonas reservadas: <top <n>px para subs, bottom <n>px para UI IG>

### Cámara / motion
- <descripción>

### Branding
- Watermark: <posición + opacidad + texto>
- Chapter titles: <sí/no + estilo>

### Audio
- Música: <sí/no + mood>
- SFX puntuales: <sí/no + cuántos>
- Sidechain con voz: <sí/no>
- Loudness aproximado: ~<LUFS>

### Veredicto de replicabilidad
- **Estilo transferible al stack actual:** sí/no
- **Costo relativo de producir en este estilo:** bajo / medio / alto
- **Recomendado para conceptos tipo:** <categorías de contenido donde este estilo encaja>
```

### Paso 6 — Decisión de catálogo (opcional)
Si la referencia es nueva y relevante, proponer al usuario añadirla al pool C (`references/`) con un nombre descriptivo. No la mueves sin confirmación.

---

## Mapas pre-calculados (de ANALISIS.md §5)

Para no reinventar: estos son los estilos ya clasificados del pool B.

| Estilo | Reels | Costo de producción | Stack recomendado |
|---|---|---|---|
| 3D stylized gradient-rich | De4e_-PRuVo, De1tYBlAlFm, DehA1hgonRL, Dege5ORIPxv | Medio | no viable sin artista 3D (el creador descartó Flux e iconos 3D) |
| Stickman 2D animado | De5sX2FB91Y, DemtYpjNWPc | Bajo | capa `escenas` (personaje + escenario) |
| Isométrico low-poly 3D | DexioYQtICU | Alto | no viable sin artista 3D |
| Ilustración 2D plana | De4OyYeAGCS, DedXqPENbLm | Medio | capa `escenas` — **estilo del canal** |
| Motion-graphic UI minimalista | Dd-eg3sDg7_ | Bajo-medio | capa `escenas` (`movil`, `chat`, gráficos) |

Si el concepto nuevo no exige un estilo específico, defaultear a **3D stylized gradient-rich** (coincide con `CLAUDE.md (raíz, sección «Nicho 1 — shorts»)`).

---

## Reglas duras

- **No describas con adjetivos vagos.** "Moderno", "limpio", "elegante" están prohibidos. Mide: hex, px, ms, cortes/s, contador.
- **Toda cifra tiene medición.** Si dices 32 beats, se puede verificar con ffmpeg scene detection.
- **No propongas un estilo que el stack no puede producir.** Si marcas "isométrico low-poly" para un video barato, estás regalando frustración al video-editor.
- **Un brief visual es consumible por otro agente.** Si tu brief solo tú lo entiendes, está mal escrito.

## Anti-patterns

- NO analices visualmente sin el mp4. La caption y la metadata no bastan.
- NO reutilices un brief viejo sin ver el video de nuevo. Las referencias evolucionan.
- NO salgas con "estilo moderno con animaciones chulas". Específica o no entregues.
- NO mezcles este brief con el de `viral-reference-analysis`. Son dos lentes distintas sobre el mismo archivo; se complementan, no se funden.
