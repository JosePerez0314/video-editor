---
name: viral-reference-analysis
description: Mirar un reel de referencia y extraer su ADN viral — hook, promesas apiladas, mecánica visual, bucles, twist, CTA, modo de fallo evitado. Produce un brief operable (no una descripción) que luego alimenta la generación de ideas. Usar cuando el usuario pida "mira esta referencia", cuando añada nuevos reels al pool, o cuando una idea propuesta necesite respaldo trazable a un reel concreto.
---

# viral-reference-analysis

Cómo estudiar un reel de referencia para que te sirva al proponer ideas.

## Cuándo invocarla

- El usuario pega un enlace de IG/TikTok y pide analizarlo.
- Hay reels en `ideas-virales/raw/` o `references/` que todavía no están destilados en el `ANALISIS.md`.
- Durante la generación de ideas, necesitas respaldo concreto para una recomendación y vas a citar un reel que no has mirado aún.
- El `quality-reviewer` detectó que un video terminado no replicó bien un patrón; vuelves a la referencia para entender qué se perdió.

## Qué NO es esta skill

- No es "ver el reel y describirlo". Si tu salida es "sale un stickman y hace esto", no estás analizando, estás narrando. Vuelve a empezar.
- No reemplaza al `ANALISIS.md`. Lo nutre.

## Flujo

### Paso 1 — Localizar el archivo
Prioridad de búsqueda:
1. `nichos/<nicho>/ideas-virales/raw/<id>.mp4` (ya descargado)
2. `nichos/<nicho>/references/<ref>.mp4` (curado por el usuario)
3. Si el usuario pega un URL nuevo, descargar con `yt-dlp -q -f "best[ext=mp4]/best" -o "<id>.%(ext)s" <url>` en `ideas-virales/raw/`.

Si solo hay URL y la descarga falla, trabaja con la metadata OG (`curl -s -A "Mozilla/5.0" <url> | grep -oE '<meta[^>]*(og:|description)[^>]*>'`) + yt-dlp dump-json para captions.

### Paso 2 — Metadatos técnicos
```bash
ffprobe -v error -show_entries stream=width,height,r_frame_rate -show_entries format=duration -of default=noprint_wrappers=1:nokey=0 <archivo>
yt-dlp --dump-json --no-download <url> | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('like_count'), d.get('comment_count'), d.get('description'))"
```

Captura: duración, likes, comments, caption, autor.

### Paso 3 — Tira de frames clave
```bash
ffmpeg -y -v error -ss 0.4 -i <archivo> -frames:v 1 /tmp/f1.jpg   # hook frame
ffmpeg -y -v error -ss 2.0 -i <archivo> -frames:v 1 /tmp/f2.jpg   # post-hook
ffmpeg -y -v error -ss <mid> -i <archivo> -frames:v 1 /tmp/f3.jpg # medio
ffmpeg -y -v error -ss <late> -i <archivo> -frames:v 1 /tmp/f4.jpg # cierre
ffmpeg -y -v error -i /tmp/f1.jpg -i /tmp/f2.jpg -i /tmp/f3.jpg -i /tmp/f4.jpg \
  -filter_complex "[0:v]scale=360:640[a];[1:v]scale=360:640[b];[2:v]scale=360:640[c];[3:v]scale=360:640[d];[a][b][c][d]hstack=inputs=4" \
  <ideas-virales/frames/<id>_strip.jpg>
```
Guardar en `ideas-virales/frames/<id>_strip.jpg`. Luego `Read` sobre esa imagen para inspección.

### Paso 4 — Checklist de observación (responder las 10)

| # | Pregunta | Qué anotar |
|---|---|---|
| 1 | ¿Primera frase exacta del audio? | Transcribirla literal |
| 2 | ¿Primera palabra importante cae antes del s1? | Sí / No |
| 3 | ¿El hook pide tocar / mirar / sentir algo del viewer? | Qué pide exactamente |
| 4 | ¿Cuántas promesas apila la primera frase? | 1 / 2 / 3+ |
| 5 | ¿Primer visual: close-up / escala / HUD / plano wide? | Describir en 10 palabras |
| 6 | ¿El visual **construye** el mecanismo frase por frase? Test audio apagado | Sí / No + 3 beats visuales |
| 7 | ¿Hay bucle abierto? ¿Cierra o no? | Describir |
| 8 | ¿Twist a ~70%? | Frase o idea |
| 9 | ¿CTA: pregunta binaria / reto físico / dato observable / cliffhanger? | Transcribir CTA |
| 10 | ¿Qué modo de fallo (F1–F6 del `ANALISIS.md`) evita y cuál comete, si alguno? | Lista |

### Paso 5 — Brief operable (salida de esta skill)

Entregar un bloque de 10–15 líneas que un futuro agente pueda **usar** para proponer, no una descripción.

```markdown
## Brief: <id> — @<autor> — <tema corto> — <likes> likes

- **Hook literal:** "<frase>"
- **Fórmula de hook:** <contradicción / reto físico / superlativo / pregunta aritmética / promesa de proceso / inmersión 2ª persona>
- **Activación corporal:** sí/no — qué pide
- **Promesas apiladas:** <n> — <listado>
- **Visual construye:** sí/no — <3 beats: X → Y → Z>
- **Bucle:** <descripción + si cierra>
- **Twist (~70%):** <frase>
- **CTA:** <literal + mecanismo>
- **Duración:** <s>
- **Fallos evitados:** <F1/F2/…>
- **Fallos cometidos:** <F?/ninguno>
- **Techo estimado:** <~X likes>
- **Replicable para:** <nicho de contenido donde este patrón se transfiere>
```

Si el reel analizado no estaba en el `ANALISIS.md`, al final del brief añadir:
```
> ANOTAR EN ANALISIS.md: Sí (fila nueva en §1 + referencia en §6.bis o §6.ter si aplica)
```

### Paso 6 — Decisión de actualizar ANALISIS.md
Si el brief revela un patrón **nuevo** que no está en §6.bis o §6.ter (ej. un tipo de bucle que no habíamos visto, un modo de fallo adicional), proponer al usuario añadirlo. No actualizar sin confirmación.

## Reglas de citación

Cuando uses este brief más tarde para respaldar una recomendación, cita en formato:
```
"apilamiento tipo @loconstruiste (DexioYQtICU)" o "visual-construye tipo ref2"
```
Nunca "como en varios reels" ni "según mi análisis". Siempre un archivo concreto que el usuario puede abrir.

## Anti-patterns

- NO escribas descripciones narrativas ("se ve un dedo tocando una pantalla…"). Describe funcionalmente ("close-up para activar atención en los primeros 300ms").
- NO calcules likes por "feeling". Si no están en metadata, dilo.
- NO analices más de 1 reel por invocación sin frames extraídos — es visual, no textual.
- NO uses la skill si solo tienes la caption. Pide/descarga el mp4 o avisa al usuario.
