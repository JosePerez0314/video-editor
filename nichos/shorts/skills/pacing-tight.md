---
name: pacing-tight
description: Ritmo de corte y timing exacto de las referencias: silencios 200-280ms, cortes duros, sin transiciones, LRA ≤2 LU.
---

# Skill: Pacing tight (ritmo de formato corto)

## Lo que define este ritmo

Los 3 videos de referencia comparten el mismo patrón de pacing:

| Métrica | REF1 | REF2 | REF3 |
|---|---|---|---|
| Duración | 55.9s | 62.1s | 86.7s |
| FPS | 30 | 60 | 60 |
| LRA | 1.9 LU | 1.9 LU | 2.5 LU |
| LUFS integrado | -14.1 | -14.1 | -14.1 |
| Silencios detectados | ~230ms promedio | ~210ms promedio | ~260ms promedio |
| Tipo de corte | Duro | Duro | Duro |

## Parámetros de corte

```
Silencios usables como punto de corte:  ≥ 200ms
Padding antes del primer word kept:     40–60ms (fast pace)
Padding después del último word kept:   60–80ms
Silencio entre frases:                  cortar a 200-250ms (no dejar el gap completo)
Transiciones:                           NINGUNA — solo hard cut
```

El oído no percibe el corte si el padding de audio es correcto. Nunca añadir crossfade de video: el jump cut brusco es intencional y parte del estilo.

## Target de longitud

```
Ideal:    55–75 segundos
Máximo:   90 segundos
Mínimo:   45 segundos
```

Si el material supera 90s después de cortar, eliminar un beat completo, no recortar milisegundos de cada uno.

## Audio mastering

Aplicar en el render final (no por segmento):

```bash
# Paso 1: normalizar a -14.1 LUFS, true peak ≤ -0.7 dBTP
ffmpeg -i input.mp4 \
  -af "loudnorm=I=-14.1:TP=-0.7:LRA=2:measured_I=-X:measured_TP=-X:measured_LRA=X:measured_thresh=-X:offset=X:linear=true" \
  -c:v copy output.mp4

# Usar dos pasadas para precisión:
# Pasada 1: medir
ffmpeg -i input.mp4 -af loudnorm=I=-14.1:TP=-0.7:LRA=2:print_format=json -f null - 2>&1 | tail -12
# Pasada 2: aplicar con valores medidos
```

### Compresión de dinámica

LRA objetivo: ≤ 2 LU (audio muy comprimido, consistente). Si el material tiene LRA alto (>4 LU), aplicar compresión antes de loudnorm:

```bash
-af "acompressor=threshold=-18dB:ratio=4:attack=5:release=100:makeup=2,loudnorm=I=-14.1:TP=-0.7:LRA=2"
```

## FPS

- Contenido con movimiento de cámara real o animación fluida: **60fps**
- Contenido estático con pocos cambios de escena: **30fps**
- Para talking head con overlays animados: **60fps** — da la sensación de mayor calidad percibida en scroll

## Verificación de ritmo

Después de renderizar, medir:

```bash
ffmpeg -i output.mp4 -af ebur128=peak=true -f null - 2>&1 | grep -E "I:|LRA:|Peak:"
```

Objetivos:
- `I: -14.1 LUFS ± 0.5`
- `LRA: ≤ 2.5 LU`
- `Peak: ≤ -0.7 dBFS`

Si LRA > 2.5, aumentar la compresión. Si I > -13.6, reducir makeup gain.

## Anti-patterns

- NO dejar silencios > 300ms en el audio del output — el viewer hace scroll.
- NO usar fade-in/fade-out de video entre segmentos.
- NO usar música de fondo que compita con la voz (si hay música, ducking a -15dB bajo la voz).
- NO estirarte más de 90s aunque tengas material — perderás al viewer.
