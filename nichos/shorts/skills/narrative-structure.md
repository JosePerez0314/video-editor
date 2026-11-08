---
name: narrative-structure
description: Estructura narrativa de los videos de referencia — cómo organizar los beats para máximo engagement en formato corto educativo/entretenimiento.
---

# Skill: Estructura narrativa (formato corto educativo)

## El género

Las 3 referencias pertenecen al género **edutainment de dato sorprendente**: explican algo real (histórico, económico, tecnológico) de forma que parece magia o paradoja. El viewer aprende algo que no sabía y quiere compartirlo.

## Estructura observada en las 3 referencias

```
BEAT 1 — HOOK (0–3s)
  Pregunta/paradoja/dato imposible. Tensión cognitiva máxima.
  El viewer no puede hacer scroll sin saber la respuesta.

BEAT 2 — SETUP (3–15s)
  Contexto mínimo necesario para entender el conflicto.
  Solo los datos imprescindibles. Sin background innecesario.
  Visual: introduce el mundo / los personajes / el objeto.

BEAT 3 — DESARROLLO (15–50s)
  La explicación en capas. Cada capa añade un dato sorprendente.
  Cada dato nuevo abre una nueva pregunta pequeña antes de resolverla.
  Visual: animaciones que ilustran cada capa.

BEAT 4 — GIRO / PAYOFF (50–65s)
  El reveal principal o la conclusión inesperada.
  Lingüísticamente: frase corta, pausa, impacto.
  Visual: el frame de mayor impacto del video.

BEAT 5 — CTA implícito (últimos 3–5s)
  No siempre explícito. A veces es simplemente dejar el dato final resonando.
  En REF1: la imagen final del personaje adulto.
  En REF2/REF3: la solución revelada con número/dato concreto.
```

## Duraciones por beat (target)

```
HOOK:        1.5 – 3.0s
SETUP:       8  – 15s
DESARROLLO:  30 – 45s (múltiples sub-beats de 5-10s cada uno)
PAYOFF:      3  – 8s
CTA:         2  – 5s
Total:       55 – 75s ideal
```

## Cómo identificar los beats en el transcript

En el `takes_packed.md`, los beats se identifican por:

1. **HOOK**: Primera frase que contiene una pregunta, "¿sabías que", "imagina que", un número improbable, o una contradicción.
2. **SETUP**: Las frases que siguen con conjunciones causales: "porque", "resulta que", "lo que pasa es que".
3. **DESARROLLO**: Frases que empiezan con conector de secuencia: "entonces", "pero", "y resulta que", o que añaden un número/dato nuevo.
4. **PAYOFF**: La frase más corta del video, después de la pausa más larga. Frecuentemente una sola oración declarativa.
5. **CTA**: "Sígueme", "comparte si", "¿tú qué harías?", o el dato final sin más comentario.

## Brief para el editor sub-agent

Usar este arquetipo en el brief:

```
Estructura esperada: HOOK → SETUP → DESARROLLO (N sub-beats) → PAYOFF → CTA
Video objetivo: edutainment de dato sorprendente, 55-75s
Criterio de selección de takes: 
  - HOOK: mayor energía y velocidad de entrega
  - SETUP: claridad, sin titubeos
  - DESARROLLO: precisión en los datos, sin fillers
  - PAYOFF: pausa natural antes + frase corta y contundente después
  - CTA: directo, sin rodeos
```

## El momento del silencio antes del payoff

El silencio antes del PAYOFF es el momento más valioso del video. En las referencias, hay una pausa de 300-600ms justo antes de la revelación final. **Nunca cortar este silencio** — es parte del ritmo. En el EDL, incluirlo explícitamente:

```json
{"source": "C0103", "start": 48.2, "end": 50.6, 
 "beat": "PAYOFF_PAUSE", 
 "reason": "Incluir los 400ms de silencio antes del payoff — generan anticipación"}
```

## Anti-patterns narrativos

- NO revelar el payoff antes del segundo 45.
- NO tener más de 2 beats de SETUP — el viewer abandona.
- NO terminar con una pregunta retórica larga — el CTA debe ser brevísimo o implícito.
- NO empezar el DESARROLLO sin haber cerrado el SETUP con un mini-conflicto nuevo.
