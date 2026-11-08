---
name: composition-vertical
description: Reglas de composición visual para 9:16 vertical: zonas de texto, sujeto, overlays y safe areas para TikTok/Reels/Shorts.
---

# Skill: Composición vertical 9:16

## Mapa de zonas (1080 × 1920 px)

```
┌──────────────────────────────┐  y=0
│                              │
│   ZONA DE TEXTO PRINCIPAL    │  y=120–320 (6–17%)
│   (subtítulos, labels)       │
│                              │
├──────────────────────────────┤  y=320
│                              │
│                              │
│   ZONA DE CONTENIDO          │  y=320–1400 (17–73%)
│   (sujeto, animación,        │
│   producto, personaje)       │
│                              │
│                              │
├──────────────────────────────┤  y=1400
│                              │
│   ZONA BAJA (UI de apps)     │  y=1400–1600 (73–83%)
│   TikTok: botones acción     │
│   Instagram: username/desc   │
│                              │
├──────────────────────────────┤  y=1600
│                              │
│   SAFE AREA INFERIOR         │  y=1600–1920 (83–100%)
│   NUNCA poner texto aquí     │
│                              │
└──────────────────────────────┘  y=1920
```

## Lo observado en las referencias

| Elemento | REF1 | REF2 | REF3 |
|---|---|---|---|
| Subtítulos | Top ~180px | Top ~100px | Top ~120px |
| Sujeto principal | Centro-bajo (40–80%) | Centro (30–75%) | Centro (25–75%) |
| UI overlay | No aplica | No aplica | No aplica |
| Safe bottom | Libre en las 3 | Libre en las 3 | Libre en las 3 |

El sujeto (personaje, mano con producto, etc.) siempre ocupa la mitad inferior del canvas. El texto siempre va arriba.

## Reglas de composición

### Texto
- **Subtítulos**: MarginV desde top = 120–200px. NUNCA en el tercio inferior.
- **Labels flotantes** (nombre, dato, fecha): dentro de la zona de contenido, acompañando al elemento que describen.
- **Texto grande de impacto** (año, número, frase corta): centrado vertical en la zona de contenido (y=700–900), tamaño 80–120px.

### Sujeto
- Cara o elemento de atención: entre y=400–900 (zona de alta atención del viewer).
- Para talking head: encuadre de hombros hacia arriba, centrado horizontalmente, cara en tercio superior del frame de contenido.
- Nunca cortar la cabeza del sujeto por el borde superior.

### Safe areas para plataformas

```
TikTok:
  - Top UI bar:     0–80px (ignorar)
  - Botones acción: x=940–1080, y=900–1600 (derecha)
  - Descripción:    y=1550–1750 (fondo izquierda)
  → Mantener zona derecha y=900–1600 sin texto/elementos clave

Instagram Reels:
  - Username/desc:  y=1550–1800
  - Botones:        x=940–1080, y=1200–1600
  → Similar a TikTok

YouTube Shorts:
  - UI overlay:     y=1650–1920
  → Más permisivo en los lados
```

### Regla práctica

Diseñar para la zona segura universal: **x=60–1020, y=120–1550**. Todo elemento de información importante dentro de estos límites funciona en las 3 plataformas.

## Para talking head con overlays

El talking head ocupa la zona de contenido completa (y=320–1600). Los overlays de animación van o bien:
1. **Encima del hablante** (translúcidos o en zona libre del frame) — para datos/números.
2. **En corte**: reemplazando el talking head completamente durante el overlay — para explicaciones visuales complejas.

Las referencias usan la opción 2: el talking head desaparece completamente durante la animación, luego vuelve. No intentan superponerlos.

## Crop y reencuadre para vertical

Si el material original es 16:9, aplicar:

```bash
# Crop centrado con enfoque en la cara (ajustar x offset según posición de la cara)
ffmpeg -i input_16x9.mp4 -vf "crop=1080:1920:420:0,scale=1080:1920" output_9x16.mp4

# Si la cara está a la izquierda del frame:
# crop=1080:1920:0:0

# Si está a la derecha:
# crop=1080:1920:840:0
```

Para talking head centrado en 16:9, el crop x=420 (centro de 1920px → toma 1080px centrales) es el default correcto.
