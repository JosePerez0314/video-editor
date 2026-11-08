---
name: hook-opening
description: Estructura del hook de apertura de los primeros 2-3 segundos: pregunta, paradoja o dato imposible que fuerza el scroll-stop.
---

# Skill: Hook de apertura (primeros 2-3 segundos)

## El patrón observado en las referencias

Todos los videos arrancan con un elemento de tensión cognitiva en los primeros 2-3 segundos:

- **REF1**: Visual de un niño ahogándose + subtítulo "Este niño" → pregunta implícita: ¿lo salvas? Reveal progresivo que el niño ES el padre de Hitler.
- **REF2**: Personaje en la calle + "¿Por qué Uber te cobra más cuando estás con alguien?" → pregunta directa sobre algo que todos han vivido.
- **REF3**: Tarjeta acercándose al datáfono + "Tu tarjeta" → promesa de revelar algo que el viewer no sabe sobre un objeto cotidiano.

## Estructura del hook

```
Segundo 0.0–0.5:  Visual de impacto (ya en escena, sin intro)
Segundo 0.0–1.5:  Frase gancho (pregunta / paradoja / dato imposible)
Segundo 1.5–3.0:  Setup que amplifica la tensión — NO el reveal
```

El reveal nunca va en los primeros 3 segundos. El hook es la pregunta, no la respuesta.

## Tipos de hook efectivos (extraídos de las refs)

### 1. Paradoja moral / dilema
"Si pudieras volver al pasado y salvar a un niño de 4 años que se ahoga..."
→ El viewer asume que debe salvarlo → giro: ese niño es el padre de Hitler.

### 2. Pregunta sobre algo cotidiano incomprendido
"¿Por qué Uber te cobra más cuando estás con alguien?"
→ El viewer lo ha vivido pero no sabe la respuesta → necesita saberla.

### 3. Revelación sobre objeto cotidiano
"Tu tarjeta tiene algo que los bancos no te explican..."
→ El viewer usa tarjetas todos los días → le falta información → quiere saber.

## Implementación en el EDL

El hook define el primer segmento. Criterios de selección del take de hook:

```
- Energía vocal alta desde la primera sílaba (sin warming up)
- Sin filler al inicio (nada de "bueno", "entonces", "o sea")
- Duración: 1.5–3.0 segundos máximo
- Si el speaker tiene múltiples takes del hook, elegir el más directo y con mayor confianza vocal
```

En el brief del editor sub-agent, siempre incluir:

```json
{"beat": "HOOK", "target_duration_s": "1.5-3.0", 
 "criteria": "máxima energía, sin fillers, entra directo al conflicto"}
```

## Visual del hook

El frame 0 debe contener el elemento de mayor tensión visual. No black, no fade-in, no texto de presentación. La escena ya está ocurriendo.

Para talking head: el speaker ya está mirando a cámara con expresión que anticipa el gancho. Cortar cualquier ajuste de posición previo.

## Anti-patterns

- NO empezar con "Hola", "Bienvenidos", nombre del creator, intro musical.
- NO revelar el giro en el hook — guardar el payoff.
- NO usar más de 1 frase en los primeros 3 segundos.
- NO empezar con plano abierto o de establecimiento — entrar directo al close-up o al detalle.
