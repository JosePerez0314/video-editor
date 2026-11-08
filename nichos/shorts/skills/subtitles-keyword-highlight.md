---
name: subtitles-keyword-highlight
description: Estilo de subtítulos exacto de las referencias: tercio superior, 1-3 palabras por cue, palabra clave en negrita con caja de selección tipo cursor.
---

# Skill: Subtítulos keyword-highlight

> **Implementación vigente (desde voz-grabada R8):** capa `subtitulos_seleccion` del architect (`tools/architect/src/estilo/subtitulos-seleccion.ts`). Figtree, y = 360, palabra por palabra al ritmo de la voz (actual blanco 700 con entrada desenfocada, dichas gris 400), recuadro azul #3B7BF6 con dos puntos en la palabra clave, frases ≤5 palabras sin terminar en palabra de enlace, y **bajan en las tomas donde arriba hay un gráfico** (`posiciones`). Las cifras de abajo son las medidas originales de referencia.

## Lo que hace este estilo

Cada cue muestra 1-3 palabras en blanco, sentence case, posicionado en el **tercio superior** de la pantalla (no en el fondo). La **última palabra o la palabra más importante** del cue recibe: negrita + un rectángulo de borde fino a su alrededor (efecto "cursor de selección de texto").

Observado en las 3 referencias:
- REF1: "Este **niño**" / "de mayor **matará**" / "era el **padre** de Hitler."
- REF2: "¿Por qué **Uber**" / "**once** minutos"
- REF3: "Tu **tarjeta**" / "con el **datáfono**" / "lo que **consume**,"

## Parámetros exactos

```
Resolución canvas:   1080 × 1920 px
Posición Y del cue:  180–240 px desde el top (9–12.5% del alto)
Alineación:          centrado horizontalmente
Fuente normal:       Sans-serif, peso 400–500, blanco puro #FFFFFF
Fuente keyword:      mismo tamaño, peso 700–800 (Bold), blanco #FFFFFF
Tamaño de fuente:    52–58 px (ajustar según largo del cue)
Palabras por cue:    1–3 (máximo 3, preferir 1-2)
Case:                Sentence case (no ALL CAPS)
Duración mínima cue: 0.35s (nunca flash corto)
```

### Caja de selección (keyword box)

```
Border:           2px sólido, blanco o azul muy oscuro (#1a2a4a)
Border-radius:    4–6 px
Padding:          4px horizontal, 2px vertical
Background:       transparente o negro 10% de opacidad
Posición:         sobre la keyword, alineada exactamente a sus límites de texto
```

## Implementación con render.py + ASS

En `master.srt` / `render.py`, este estilo requiere ASS (Advanced SubStation Alpha) en lugar de SRT simple. Genera el archivo `.ass` directamente.

### Plantilla de estilo ASS base

```ass
[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Normal,Arial,54,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,8,30,30,180,1
Style: Bold,Arial,54,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,1,0,0,0,100,100,0,0,1,0,0,8,30,30,180,1
```

`Alignment=8` = centro-top (tercio superior). `MarginV=180` = 180px desde el top.

### Generación de cues con keyword box

Para cada cue, dividir el texto en `(palabras normales) + (keyword)`. Renderizar:

```ass
Dialogue: 0,0:00:02.52,0:00:05.36,Normal,,0,0,0,,Este {\b1}niño{\b0}
```

La caja se implementa como overlay PNG generado con PIL sobre cada frame donde aparece la keyword, o como rectángulo dibujado con `drawbox` de ffmpeg sincronizado al cue. El método PIL es más preciso:

```python
# Calcular bbox de la keyword en el frame
from PIL import ImageDraw, ImageFont
font_bold = ImageFont.truetype("Arial Bold.ttf", 54)
bbox = font_bold.getbbox(keyword_text)  # (left, top, right, bottom)

# Dibujar caja
draw.rounded_rectangle(
    [bbox[0]-4, bbox[1]-2, bbox[2]+4, bbox[3]+2],
    radius=5,
    outline=(255, 255, 255),  # o (26, 42, 74) para azul oscuro
    width=2
)
```

## Reglas de chunking

1. Romper en límites de puntuación (`,` `.` `?` `¡` `¿`).
2. Si no hay puntuación, romper en silencios ≥ 0.3s del transcript de Scribe.
3. La keyword es la última palabra del cue O la palabra con mayor énfasis fonético (Scribe marca intensidad).
4. Si el cue tiene solo 1 palabra, esa palabra ES la keyword.
5. Nunca dejar una keyword de menos de 3 caracteres (artículos, preposiciones no son keywords).

## Anti-patterns observados

- NO usar placement en fondo (MarginV desde bottom) — en estas referencias el texto siempre va arriba.
- NO usar ALL CAPS.
- NO usar más de 3 palabras por cue.
- NO usar fondo sólido detrás de todo el texto (solo la caja sobre la keyword).
- NO usar sombra agresiva (Outline=0 o 1 máximo).
