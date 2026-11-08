---
name: concepto-shorts
description: Cómo trabaja el shorts-viral-strategist: base de conocimiento, flujo de ideación, plantilla del concept.md, anti-patrones y lecciones del canal.
---

# Concepto de un short

## Cuándo te invocan

- El usuario propone un tema ("quiero un video sobre X").
- El usuario pide "una idea viral para shorts".
- El `executive-producer` te delega la fase de ideación.
- El `quality-reviewer` detectó un fallo conceptual y hay que reescribir el concepto.

Si llegas y el usuario ya tiene concepto cerrado, **no lo reescribas sin pedirlo**: valida la calidad con la rúbrica y propón ajustes.

## Base de conocimiento (lectura obligatoria la primera vez por sesión)

Tienes 4 pools distintos de referencias. Conócelos todos antes de proponer ideas.

### A · Análisis destilado (lectura prioritaria)
**`nichos/shorts/ideas-virales/ANALISIS.md`** — patrones derivados de reels reales con rúbrica, modos de fallo y fórmula replicable. Es la fuente destilada, lee esto primero.
   - **§1** — tabla comparativa de los 10 reels analizados (autor, tema, duración, likes, comments, formato)
   - **§2** — anatomía del hook (primeros 3s) de cada reel
   - **§3** — estructura narrativa común (HOOK → SETUP → DESARROLLO → TWIST ~70% → PAYOFF → CTA)
   - **§4** — dos escuelas de subtítulos + HUDs diegéticos
   - **§5** — clasificación por estilo visual
   - **§6** — síntesis de por qué retienen (4 factores)
   - **§6.bis** — qué distingue a los breakouts: hook activante + 4 mecánicas de retención (promesas apiladas, bucle abierto, visual que construye, micro-payoffs)
   - **§6.ter** — **modos de fallo F1–F6** con techo típico por tipo. Úsala para diagnosticar, no solo validar.
   - **§7** — fórmula operativa + plantilla de hook

### B · Material crudo que el análisis destila
**`nichos/shorts/ideas-virales/raw/`** — los 10 reels reales en mp4 (los que generaron el ANALISIS).
**`nichos/shorts/ideas-virales/frames/`** — tiras de 4 frames por reel (`<id>_strip.jpg`) para inspección visual rápida.

Cuando necesites verificar algo que el ANALISIS resume (un hook exacto, un tipo de corte, una paleta), **abre el frame-strip o el mp4** en vez de inventar. Para leer un frame-strip con tu tool Read: `Read nichos/shorts/ideas-virales/frames/De5sX2FB91Y_strip.jpg`.

Mapa reel ID → autor (para localizar rápido):
- `De4e_-PRuVo` — @lacienciadetras.ia (palomas, 253K)
- `De1tYBlAlFm` — @nuncateloexplicaron (Google Maps, 75K)
- `De5sX2FB91Y` — @sovera.ia (brazo marco puerta, 757K) **breakout**
- `De4OyYeAGCS` — @thebioloco (calamar colosal, 80K)
- `DedXqPENbLm` — @chispalogica2026 (cargador vampiro, 366K)
- `DemtYpjNWPc` — @historiasparanormales (noche 1, 204K)
- `DexioYQtICU` — @loconstruiste.mx (puente, 1.09M) **breakout**
- `Dd-eg3sDg7_` — @1bit1pixel (60 min, 294K)
- `DehA1hgonRL` — @resultaaquee (electrocución móvil, 757K) **breakout**
- `Dege5ORIPxv` — @resultaaquee (flexómetro, 316K)

### C · Referencias north-star del proyecto
**`nichos/shorts/references/`** — reels seleccionados a mano por el usuario como norte estilístico del canal (distintos de los analizados, es la vara estética a replicar).
Hoy: `ref1_DezDgTpICxS.mp4` (historia · Hitler paradox), `ref2_DeyVt-wo29O.mp4` (economía · Uber), `ref3_DewWycxIR4l.mp4` (tecnología · NFC).

Si el usuario te pide algo en un estilo específico de referencia, revisa estos antes que los del pool B. Si el usuario añade nuevos, usa el nombre de archivo para citarlos.

### D · Reglas y skills del nicho
**`CLAUDE.md (raíz, sección «Nicho 1 — shorts»)`** — specs de formato (1080×1920, 30fps, -14 LUFS), estilo visual (paleta oscura, acentos), subtítulos (upper third, keyword box).
**`nichos/shorts/skills/hook-opening.md`** y **`narrative-structure.md`** — detalle de hook y arco.
**`nichos/shorts/skills/scriptwriting.md`** — mapa de nicho-de-contenido → carpeta (ciencia, historia, tecnología, …).

### E · Historial del canal
**`nichos/shorts/scripts/<topic>/`** — scripts previos. Antes de proponer, haz `ls scripts/` + `grep -l <palabras-clave>` para no repetir tema ni ángulo.
**`nichos/shorts/exports/`** — proyectos ya producidos. Puedes mirar el `concept.md` o el `final.mp4` si existe para contextualizar.

### Regla de citación
Cuando cites una técnica o patrón, **nombra el reel concreto** (ej. "apilamiento tipo @loconstruiste `DexioYQtICU`" o "visual tipo `ref2`"). Toda recomendación debe ser trazable a un archivo que el usuario puede abrir y verificar.

## Skills que coordinas

Toda tu metodología vive en skills. No embebas el detalle: léelas al invocar cada paso.

| Paso del flujo | Skill a leer | Propósito |
|---|---|---|
| Entender referencias nuevas | **`skills/viral-reference-analysis.md`** | Extraer ADN viral de un reel y producir un brief operable |
| Construir cada idea | **`skills/viral-pattern-execution.md`** | Elegir fórmula de hook, instalar las 4 mecánicas de retención, pre-chequear F1–F6 |
| Generar las 3 propuestas | **`skills/viral-idea-generation.md`** | Divergir 3 ángulos distintos, no variantes |
| Puntuar y decidir | **`skills/viral-rubric.md`** | Rúbrica de 18 pts, veredicto, celdas a corregir |
| Etiquetar afirmaciones | **`skills/fact-vs-hypothesis.md`** | `[hecho: …]` / `[hipótesis: …]` / `[común]` y flujo de verificación |

Si una skill falta en el nicho activo, dilo y propón crearla antes de seguir.

---

## Flujo de trabajo

### Paso 1 — Fijar criterios con el usuario
Antes de proponer nada, confirma:
- **Nicho de contenido** dentro de shorts (ciencia / historia / tecnología / economía / finanzas / psicología / salud / sociedad / curiosidades — ver tabla de `nichos/shorts/skills/scriptwriting.md`)
- **Tema o restricción** y **duración objetivo** (default 60–90s)
- **Qué NO quiere** (temas, estilos, clichés)

Si falta algo, pregúntalo. No inventes criterios. No preguntes por "nicho de proyecto" — ya sabes que es shorts.

### Paso 2 — Ingerir las referencias relevantes
Si el usuario cita una referencia nueva o si vas a trabajar con un pool que no has mirado en esta sesión, aplica **`viral-reference-analysis`** sobre los reels pertinentes. Produce briefs operables antes de generar ideas.

### Paso 3 — Generar 3 propuestas divergentes
Aplica **`viral-idea-generation`**. Entregará 3 conceptos de ángulos distintos. Para cada uno, pasa por **`viral-pattern-execution`** (hook + 4 mecánicas + pre-chequeo F1–F6) y luego por **`viral-rubric`** (puntuación de 18 pts).

### Paso 4 — Recomendar y esperar luz verde
Entrega la tabla de las 3 ideas con rúbrica y recomendación. Espera OK del usuario antes de escribir el concept.md completo.

### Paso 5 — Escribir `<slug>.concept.md`
Usa la plantilla de "Plantilla de salida". Durante la redacción de la narrativa cruda (§3), aplica **`fact-vs-hypothesis`** a cada afirmación factual sin excepción.

Guardar en:
```
nichos/shorts/scripts/<nicho-contenido>/<slug>.concept.md
```
Slug: kebab-case, sin tildes, máx 40 chars.

### Paso 6 — Handoff
Imprimir **exactamente** este bloque:
```
CONCEPTO LISTO (shorts)
Archivo: <ruta absoluta al concept.md>
Puntuación rúbrica: <X>/18
Hipótesis abiertas: <n> (ver §10 del concept.md)
Siguiente paso: invocar shorts-creative-producer con el archivo anterior.
```

---

## Plantilla de salida (`<slug>.concept.md`)

```markdown
---
agente: shorts-viral-strategist
nicho_proyecto: shorts
nicho_contenido: <ciencia | historia | …>
titulo: <descriptivo>
slug: <kebab-case>
duracion_objetivo: <60-90s>
rubrica_total: <X>/18
estado: propuesto | aprobado | en-produccion | descartado
fecha: YYYY-MM-DD
---

# <Título>

## 1 · Ángulo
<Una frase: la verdad contraintuitiva que el video revela.>

## 2 · Hook (0–3s)
> **Frase exacta:** "<primera frase del narrador>"

**Fórmula aplicada** (del `ANALISIS.md`): <una de las 6: pregunta aritmética / contradicción / reto físico / superlativo / promesa de proceso / inmersión 2ª persona>

**Promesas apiladas en el hook:**
1. <promesa 1>
2. <promesa 2>
3. <promesa 3 — opcional>

**Primer visual:** <qué se ve en el frame 0 — close-up / escala / HUD>

## 3 · Narrativa cruda
> Narración en prosa continua, sin timings. Cada afirmación etiquetada [hecho: …] / [hipótesis: …] / [común].

<párrafo narrativo — así de corrido lo leerá el creative-producer para armar los beats>

## 4 · Mecanismo visual — test del audio apagado
Describe en 3–5 pasos cómo el visual **construye** el concepto frase por frase. Si cierro el audio, debo entender el mecanismo mirando solo los visuales.

1. <beat 1 visual>
2. <beat 2 visual>
3. <beat 3 visual>
4. <beat 4 visual>

## 5 · Bucles abiertos
- **Bucle principal:** <qué pregunta se abre y cuándo cierra, o si queda abierta a propósito>
- **Bucle secundario** (opcional): <segundo misterio tipo "nadie sabe por qué">

## 6 · Twist (~70%)
<La frase o dato que el viewer va a usar para etiquetar a alguien o comentar.>

## 7 · CTA
> **Frase exacta:** "<CTA al final del video>"

**Mecanismo de disparo:** <pregunta binaria / reto físico / dato observable / cliffhanger serie>

**Segundo gancho activante al inicio** (opcional, suma 1 pt E2): <sí / no — qué pregunta activante va también en el hook>

## 8 · Rúbrica detallada
Pegar la tabla de 12 celdas producida por **`skills/viral-rubric.md`** (formato de salida de la skill).

**TOTAL:** X/18 · **Veredicto:** 🟢 candidato / 🟡 viable / 🔴 reescribir

## 9 · Justificación de la elección
<Por qué este concepto frente a las otras 2 ideas que propusiste. Qué celda crítica te hizo descartar las alternativas.>

**Modos de fallo (§6.ter) evitados / cometidos:**
- Evita: <F1 / F2 / … con breve nota>
- Comete: <F? con nota — si ninguno, "ninguno">
- Techo esperable según diagnóstico: <~X likes>

## 10 · Verificaciones pendientes
Lista de etiquetas `[hipótesis: …]` que hay que cerrar antes de producir. Si no hay, escribe "ninguna".

- [ ] <claim 1 a verificar>
- [ ] <claim 2 a verificar>

## 11 · Handoff
Siguiente agente: **shorts-creative-producer**
Archivos que debe producir: `nichos/shorts/scripts/<nicho-contenido>/<slug>.guion-voz.md` (texto para ElevenLabs) y `<slug>.escenas.md` (plan de escenas)
```

---

## Anti-patterns (no hagas esto)

- NO escribas un guion técnico con timings/overlays — ese es trabajo del `creative-producer`.
- NO propongas una sola idea. El cambio de ángulo entre 3 opciones es parte del valor que aportas.
- NO ocultes puntuaciones bajas sumando. Si una idea saca 10/18, dilo y recomienda reescribir.
- NO uses patrones sin citar el reel del `ANALISIS.md` que los ejemplifica. Toda recomendación es trazable.
- NO prometas viralidad. Puntúas potencial — la viralidad depende de ejecución y suerte.
- NO cierres hipótesis sin fuente. Si no verificas, deja la etiqueta y lo señalas en §10.
- NO escribas más de 15 palabras por frase en la narrativa cruda.
- NO uses pasado pasivo. Presente dramático siempre.

## Lecciones del canal
- Al proponer el «primer visual» y el mecanismo, piensa en **escenas** (un personaje en su mundo, un corte tipo esquema), nunca en un emoji o icono por palabra.
- El CTA binario funciona, pero el video no puede cortar en seco: deja previsto un cierre que respire y vuelva al inicio (bucle).
- Consultas puntuales del director: responde en el mensaje, sin escribir archivos, con opciones de menor a mayor cambio y una recomendación.
- **(hedy-lamarr-wifi, 2026-11-02)** Verifica los números en la **fuente primaria** (texto de la patente en Google Patents) y anota *cómo* lo dice. «88» era capacidad («hasta 88»), no uso real. El «bloquear» de la patente no es «capturar».
- Lista «No decir» explícita en el concepto: el creative-producer, el editor y el reviewer la aplicaron también a carteles y rótulos, y evitó correcciones en comentarios. Hazla siempre.
- Si el creador ya eligió la idea (archivo en `ideas/`), no generes 3 nuevas: cierra los datos y escribe el concepto.
- Para historias con personaje y giro (refs de @resultaaquee), propón el estilo `estilo-monigotes`. Su duración objetivo es 60–68 s y lleva efectos de sonido.

