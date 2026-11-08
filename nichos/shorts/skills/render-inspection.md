---
name: render-inspection
description: Metodología para auditar un video renderizado (no un storyboard). Define las 7 categorías de inspección, los comandos de evidencia, la escala de severidad y el formato del review.md con veredicto APPROVED / NEEDS_REVISION. Reusada por shorts-quality-reviewer y, en modo diagnóstico, por shorts-executive-producer para auditorías puntuales.
---

# render-inspection

Cómo inspeccionar sistemáticamente un `final.mp4` de shorts y producir un `review.md` con hallazgos atribuidos y veredicto.

## Cuándo invocarla

- El `shorts-video-editor` emitió `VIDEO LISTO`.
- Un video ya publicado está siendo re-auditado tras feedback.
- El `shorts-executive-producer` necesita confirmar si un video cumple contrato antes de aprobar publicación.

## Entradas obligatorias

1. `nichos/shorts/exports/<slug>/final.mp4` — el entregable a auditar.
2. `nichos/shorts/exports/<slug>/render-log.md` — qué se ejecutó.
3. `nichos/shorts/scripts/<topic>/<slug>.concept.md` — intención viral + rúbrica original.
4. `nichos/shorts/scripts/<topic>/<slug>.md` — guion técnico con bloque `<!-- PRODUCCIÓN -->`.
5. `nichos/shorts/scripts/<topic>/<slug>.escenas.md` — plan de escenas aprobado (ver `plan-escenas.md`).

Si falta alguno, se detiene y pide al usuario localizarlo. No se audita a ciegas.

## Las 7 categorías de inspección

Cada categoría tiene (a) qué chequear, (b) comando de evidencia, (c) regla de severidad.

### 1 · Specs técnicas (contrato con `CLAUDE.md`)

Comando:
```bash
ffprobe -v error -show_entries stream=width,height,r_frame_rate,codec_name -show_entries format=duration,bit_rate -of default=noprint_wrappers=1:nokey=0 <final.mp4>
```

Checks:
- [ ] Resolución 1080×1920
- [ ] FPS 30 (o 60 si el contrato lo exige)
- [ ] Codec video H.264, audio AAC
- [ ] Duración dentro del contrato ±2s

Severidad por fallo: **CRITICAL** — cualquier spec fuera = contrato roto.

### 2 · Audio mastering (contrato con `pacing-tight.md`)

Comando:
```bash
ffmpeg -i <final.mp4> -af ebur128=peak=true -f null - 2>&1 | grep -E "I:|LRA:|Peak:"
```

Targets:
- `I: -14.1 LUFS ± 0.5`
- `LRA ≤ 2.5 LU`
- `Peak ≤ -0.7 dBFS`

Severidad:
- I fuera de ±1 LU → **CRITICAL**
- I fuera de ±0.5 pero dentro de ±1 LU → **MAJOR**
- LRA > 2.5 pero ≤ 3.5 → **MAJOR**
- LRA > 3.5 → **CRITICAL** (voz suena "pecho" vs "encima")
- Peak > −0.7 → **CRITICAL** (clipping percibido)

### 3 · Continuidad visual

Comando (cambios de escena):
```bash
ffmpeg -i <final.mp4> -filter:v "select='gt(scene,0.3)',showinfo" -f null - 2>&1 | grep "pts_time" > /tmp/cuts_<slug>.txt
```

Comando (frames estratégicos — cada 1.5s):
```bash
mkdir -p /tmp/qc_<slug>
ffmpeg -y -v error -i <final.mp4> -vf "fps=0.67,scale=360:-1" /tmp/qc_<slug>/f%03d.jpg
ffmpeg -y -v error -i /tmp/qc_<slug>/f%03d.jpg -vf "tile=5x8" /tmp/qc_<slug>/grid.jpg
```

Luego `Read /tmp/qc_<slug>/grid.jpg` para panorama completo.

Checks:
- [ ] Ningún frame negro inesperado (>0.3s)
- [ ] Ningún freeze inesperado (si `scene_detection` reporta <0.3 cortes/s cuando el contrato pedía ≥0.4 → MAJOR)
- [ ] Ninguna duplicación de shot
- [ ] Transiciones entre beats de 0.15–0.3s (no cross-fades)
- [ ] Primer frame no está vacío (regla de `plan-escenas.md`)

Severidad:
- Frame negro >0.5s en medio → **CRITICAL**
- Freeze inesperado >0.4s → **MAJOR**
- Densidad de cortes/s más de 20% por debajo del contrato → **MAJOR** (F3 ANALISIS)
- Transición no permitida (fade/dissolve) → **MINOR** si es un solo caso, **MAJOR** si es el patrón del video

### 4 · Legibilidad de subtítulos (contrato con `subtitles-keyword-highlight.md`)

Extraer frames donde hay subtítulos activos:
```bash
# Leer alignment.json → tiempos de cada cue
# Para cada cue, extraer el frame del medio:
ffmpeg -y -v error -ss <t_cue_mid> -i <final.mp4> -frames:v 1 /tmp/qc_<slug>/sub_<n>.jpg
```

Checks por frame de muestra (10 cues aleatorios):
- [ ] Posición respeta contrato (`subs_posicion` del bloque PRODUCCIÓN)
- [ ] Palabras por cue ≤ `subs_palabras_por_cue` + 1 (margen de ±1)
- [ ] Keyword box en el color correcto (`subs_keyword_box`)
- [ ] Contraste texto/fondo suficiente (texto blanco sobre bg oscuro, o color + outline)
- [ ] Texto no choca con zona reservada (ver `composition-vertical.md`)
- [ ] Ningún overflow de línea

Severidad:
- Subs ilegibles por contraste → **CRITICAL**
- Posición fuera del contrato → **MAJOR**
- Keyword no highlightada en >30% de cues → **MAJOR**
- Overflow o 1 cue con exceso de palabras → **MINOR**

### 5 · Hook ejecutado vs hook planeado (gap intención → entrega)

Comparar:
- Hook declarado en `concept.md §2` (frase exacta)
- Hook ejecutado en el `final.mp4` 0–3s

Comando (frame del hook):
```bash
ffmpeg -y -v error -ss 0.4 -i <final.mp4> -frames:v 1 /tmp/qc_<slug>/hook.jpg
ffmpeg -y -v error -ss 2.0 -i <final.mp4> -frames:v 1 /tmp/qc_<slug>/hook_post.jpg
```

Checks:
- [ ] Primera palabra importante del audio ANTES del segundo 1 (regla B2 de `viral-rubric`)
- [ ] Primer visual coincide con el descrito en `concept.md §2 Primer visual`
- [ ] Promesas apiladas se escuchan en la primera frase (contar en la narración de los 0–4s)
- [ ] Activación corporal — si el concept marcó A1=2, la ejecución debe tener la petición explícita

Severidad:
- Promesas apiladas prometidas y no entregadas en primera frase → **MAJOR** (destruye B1 del rubric en ejecución)
- Primer visual no coincide → **MAJOR**
- Primera palabra importante cae después del s1.5 → **MAJOR**

### 6 · Mecanismo visual: construye o ilustra (test del audio apagado)

Procedimiento:
```bash
# Extraer audio-less preview (opcional) o solo mirar la cuadrícula
# Comparar la secuencia de frames de /tmp/qc_<slug>/grid.jpg con el "Mecanismo visual" del concept.md §4
```

Checks:
- [ ] Cada beat visual añade una pieza nueva (no reutilización de plano)
- [ ] Secuencia visual del final.mp4 reproduce los 3–5 pasos del `concept.md §4`
- [ ] Si cierras el audio mentalmente, se entiende el mecanismo

Severidad:
- Visual ilustra en vez de construir cuando el concept.md marcó C1=2 → **MAJOR** (F3 del ANALISIS)
- Reutilización de plano >2 beats consecutivos → **MINOR**
- Mecanismo prometido en §4 no aparece en el video → **CRITICAL** (video no cumple intención)

### 7 · CTA y bucle

Comando:
```bash
# Último 10% del video
ffmpeg -y -v error -ss $(python3 -c "import subprocess; d=float(subprocess.getoutput('ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 <final.mp4>')); print(d*0.9)") -i <final.mp4> -frames:v 1 /tmp/qc_<slug>/cta.jpg
```

Checks:
- [ ] CTA declarado en `concept.md §7` suena literalmente en el final (o con mínima variación)
- [ ] CTA del tipo prometido (binario / reto / observable / cliffhanger)
- [ ] Si `concept.md §5` prometió bucle secundario abierto, verificar que NO cierra (no da respuesta al "nadie sabe por qué")
- [ ] Twist a ~70% del video presente

Severidad:
- CTA ausente o reemplazado por genérico → **MAJOR**
- Bucle que debía quedar abierto se cerró → **MAJOR** (destruye D1)
- Twist ausente → **MAJOR**

### 8 · Hipótesis sin cerrar (bonus: `fact-vs-hypothesis`)

Procedimiento:
```bash
grep -n "\[hipótesis:" <concept.md> <script.md>
```

Checks:
- [ ] Ninguna etiqueta `[hipótesis: …]` sobrevive en el guion que generó el audio final (todas deben estar `[hecho: fuente]` o eliminadas o `[hipótesis: usuario-aceptada]`).
- [ ] Narración final no afirma un claim que en concept.md estaba como hipótesis abierta.

Severidad:
- Hipótesis abierta llegó al video final sin autorización → **CRITICAL** (regla de `fact-vs-hypothesis.md`)

### 9 · Gap vs `visual-reference-analysis` del creative-producer

Si el creative-producer dejó un brief visual de referencia (en los comentarios del `<slug>.md` o en el `render-log.md`), re-aplicar la skill `visual-reference-analysis` al final.mp4 y comparar celda por celda:

| Categoría | Plan | Entrega | Gap |
|---|---|---|---|
| Paleta | `#0e0e14 + #ff8a3d` | `#0e0e14 + #e07020` | leve, MINOR |
| Subs posición | upper third | centro | MAJOR |
| Cortes/s | 0.45 | 0.28 | MAJOR (F3) |

Severidad:
- Cortes/s −20% o más vs plan → **MAJOR**
- Paleta divergente >15% en acentos → **MINOR**
- Estilo visual distinto al planeado → **CRITICAL** si es un cambio de clase (ej. prometió 3D stylized y entregó stickman)

---

## Escala de severidad (resumen)

| Severidad | Significa | Afecta el veredicto |
|---|---|---|
| 🟥 **CRITICAL** | Contrato roto, intención perdida, hipótesis abierta en video, specs fuera | Sí → NEEDS_REVISION automático |
| 🟧 **MAJOR** | Gap significativo con el concept/plan que baja techo esperable | Sí → NEEDS_REVISION |
| 🟨 **MINOR** | Detalle visible pero no bloqueante | No por sí solo. 3+ MINOR → NEEDS_REVISION |
| 🟩 **COSMETIC** | Opinión estética sin impacto en retención | No. Se documenta como "idea para próximo video" |

**Regla del veredicto:**
- 0 CRITICAL + 0 MAJOR + ≤2 MINOR + cualquier COSMETIC → **APPROVED**
- Lo demás → **NEEDS_REVISION**

---

## Atribución de causa

Cada hallazgo se atribuye a una fase, para que el `shorts-executive-producer` sepa a quién devolver:

| Causa | Signos | Devuelve a |
|---|---|---|
| **Concepto** | el plan no era viable desde el principio (hook pasivo pero marcó A1=2) | `shorts-viral-strategist` |
| **Plan** | el concepto estaba bien pero el plan de escenas o el guion de voz no lo tradujeron (prometió apilar 3, el guion tiene 1) | `shorts-creative-producer` |
| **Ejecución** | el plan estaba bien pero el video no lo ejecutó (el plan pedía 12 escenas, el final tiene 9) | `shorts-video-editor` |

Para atribuir correctamente, se compara en orden: `concept.md § → guion-voz.md → escenas.md → final.mp4`. El primer punto donde la cadena se rompe es la fase a devolver.

---

## Plantilla de salida (`review.md`)

```markdown
---
agente: shorts-quality-reviewer
slug: <slug>
veredicto: APPROVED | NEEDS_REVISION
fecha: YYYY-MM-DD HH:MM
duracion_final: Xs
lufs_i: -14.X
---

# Review — <título>

## Veredicto
**🟢 APPROVED** / **🔴 NEEDS_REVISION**

Resumen en 2 frases: <qué cumplió / qué falla crítica>.

## 1 · Verificación técnica
| Spec | Target | Medido | ✓ |
|---|---|---|---|
| Resolución | 1080×1920 | — | ✅/❌ |
| FPS | 30 | — | ✅/❌ |
| Codec | h264+aac | — | ✅/❌ |
| Duración | X±2s | — | ✅/❌ |
| LUFS I | −14.1 ±0.5 | — | ✅/❌ |
| LRA | ≤2.5 LU | — | ✅/❌ |
| Peak | ≤−0.7 dBFS | — | ✅/❌ |

## 2 · Rúbrica aplicada a ejecución
(usa `viral-rubric.md` sobre el video, no sobre el concepto)

| Celda | Pts concepto | Pts ejecución | Gap |
|---|---:|---:|---|
| A1 — Activación corporal | 2 | X | <nota> |
| … | … | … | … |
| **TOTAL** | **X/18** | **X/18** | **ΔX** |

## 3 · Hallazgos

| # | Timestamp | Categoría | Severidad | Hallazgo | Atribución | Corrección propuesta |
|---|---|---|---|---|---|---|
| 1 | 00:00.4 | Hook ejecutado | 🟥 CRITICAL | Primera palabra importante cae en s1.8 (planeado s0.5). El viewer scrollea | Ejecución (video-editor cortó mal el intro) | Recortar los primeros 1.3s del voiceover y re-compose |
| 2 | 00:18–00:25 | Mecanismo visual | 🟧 MAJOR | El beat "pilotes bajando" se repite 3 veces sin variación (plan: 1 vez + losa) | Ejecución | Re-render del tramo 18–25s con la pieza nueva |
| 3 | 00:52 | Subs | 🟨 MINOR | Cue "cada" con 4 palabras en vez de ≤3 | Plan (escenas) | Partir en 2 cues |

## 4 · Acciones recomendadas (si NEEDS_REVISION)
1. **Devolver a `shorts-video-editor`**: hallazgos #1, #2
2. **Devolver a `shorts-creative-producer`**: hallazgo #3

Tiempo estimado de corrección: X min.

## 5 · Evidencia
- Specs: `ffprobe <final.mp4>` → <output copiado>
- Audio: `ebur128` → <output copiado>
- Frames inspeccionados: `/tmp/qc_<slug>/grid.jpg`
- Comparación visual plan vs entrega: ver §9 de la skill

## 6 · Cosméticos (no bloquean)
- <opiniones estéticas o ideas para el siguiente video>
```

---

## Anti-patterns

- NO audites solo el render-log. El log cuenta lo que se intentó, no lo que salió. Inspeccionar el mp4 es obligatorio.
- NO emitas APPROVED con hallazgos CRITICAL o MAJOR.
- NO atribuyas "Ejecución" automáticamente a todo. La raíz suele estar en el plan o en el concepto.
- NO uses adjetivos vagos en hallazgos ("se ve raro"). Timestamp, qué, por qué, corrección.
- NO cuentes cosméticos como MAJOR. Son opiniones.
- NO termines un review sin veredicto. "Casi aprobado" no existe.
