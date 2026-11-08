---
name: viral-idea-generation
description: Convierte un tema o criterio del usuario en 3 conceptos virales de ángulos DIVERGENTES (no variantes). Fuerza una tabla de divergencia, aplica pre-rúbrica y recomienda uno. Nunca entrega una sola idea.
---

# viral-idea-generation

Cómo transformar un tema vago en 3 conceptos distintos listos para scoring.

## Cuándo invocarla

- El usuario pide una idea / varias ideas para shorts.
- El usuario propone un tema general ("algo sobre física", "quiero un video de curiosidades").
- El `executive-producer` necesita opciones para elegir.

Si el usuario trae un tema **ya cerrado y específico** (ej. "cómo funciona el NFC, hazlo en el estilo de ref3"), no uses esta skill — pasa directo a `viral-pattern-execution` con el ángulo propuesto. Las 3 ideas se usan cuando el espacio de concepto todavía está abierto.

## Entradas requeridas

Antes de generar, confirmar con el usuario:
- **Nicho de contenido** (de la tabla de `scriptwriting.md`: ciencia / historia / tecnología / economía / finanzas / psicología / salud / sociedad / curiosidades)
- **Tema o restricción** (si la hay)
- **Qué NO quiere** (temas, estilos, clichés)
- **Duración objetivo** (default 60–90s)

Si falta alguno, pregúntalo. No inventes.

---

## 1 · La regla de los 3 ángulos divergentes

Las 3 ideas NO pueden ser variantes del mismo ángulo. Deben venir de ejes narrativos distintos.

### Fuentes de ángulo (6 ejes)

| Eje | Qué pregunta | Fórmula de hook natural |
|---|---|---|
| **Mecanismo oculto** | ¿Cómo funciona realmente? | Promesa de proceso |
| **Motivo escondido** | ¿Por qué existe así y no de otra forma? | Pregunta aritmética / Contradicción |
| **Fenómeno corporal** | ¿Qué le pasa a tu cuerpo cuando…? | Reto físico 2ª persona |
| **Récord / superlativo** | ¿Cuál es el más X? | Superlativo con misterio |
| **Mito desmontable** | ¿Lo que crees es falso? | Contradicción directa |
| **Experiencia inmersiva** | ¿Qué sentirías si…? | Inmersión 2ª persona |

Al generar 3 ideas sobre el mismo tema, cada una debe pertenecer a un eje distinto. Ejemplo con el tema "palomas":
- Idea 1 — eje "mecanismo": por qué la cabeza queda quieta cuando caminan
- Idea 2 — eje "motivo": por qué las ciudades están llenas de palomas y no de otras aves
- Idea 3 — eje "fenómeno corporal": prueba a mover la cabeza como ellas y mira cómo cambia tu visión

### Divergencia check (bloqueante)
Antes de puntuar, verifica la tabla:

| Idea | Eje | Fórmula de hook | Primer visual | Mecánica dominante |
|---|---|---|---|---|
| 1 | <eje> | <fórmula> | <visual> | <mecánica> |
| 2 | <eje> | <fórmula> | <visual> | <mecánica> |
| 3 | <eje> | <fórmula> | <visual> | <mecánica> |

Si alguna columna se repite entre 2 ideas → no divergen → reescribe la que menos puntúa.

---

## 2 · Flujo de generación

### Paso 1 — Explorar ángulos (5 minutos de pensamiento, no de escritura)
Dado el tema, listar en bruto 6–10 ángulos aplicando cada eje. No filtres. No escribas hooks aún.

### Paso 2 — Filtrar por 3 divergentes
Seleccionar 3 ángulos de ejes distintos. Priorizar los ejes que llevaron a los 3 breakouts del `ANALISIS.md`:
1. **Fenómeno corporal** (reto físico) → techo más alto
2. **Mecanismo oculto** con detalle sensorial (promesa de proceso) → techo alto
3. **Mito desmontable** (contradicción) → techo alto si el mito está muy extendido

Si el tema no admite reto físico, saltar ese eje y escoger entre los otros 5.

### Paso 3 — Aplicar `viral-pattern-execution` a cada idea
Cada idea pasa por la skill de ejecución de patrones para quedar con hook definido + 4 beats + bucles + CTA + pre-chequeo F1–F6 limpio.

### Paso 4 — Pre-scoring con `viral-rubric`
Puntuar cada una. Mostrar las 3 puntuaciones en una tabla breve:

| Idea | Rúbrica | Fallos |
|---|---:|---|
| 1 — <título corto> | X/18 | <F? / ninguno> |
| 2 — <título corto> | X/18 | <F? / ninguno> |
| 3 — <título corto> | X/18 | <F? / ninguno> |

### Paso 5 — Recomendación
Elegir **una**. Criterio:
1. Puntuación más alta.
2. Si hay empate, la de mayor potencial de breakout (A1 activación corporal = 2 y D1 bucle = 2 pesan más que las demás).
3. Si siguen empatando, preguntar al usuario cuál prefiere.

Nunca recomendar sin justificar por qué las otras 2 quedaron fuera.

### Paso 6 — Esperar luz verde
Antes de escribir el concept.md completo, esperar OK del usuario. Si rechaza las 3, no insistas con variantes de las mismas — vuelve al Paso 1 con un cambio de ejes.

---

## 3 · Verificación de no-repetición

Antes del Paso 1, correr:
```bash
ls nichos/<nicho>/scripts/<nicho-contenido>/
grep -ril "<palabras-clave>" nichos/<nicho>/scripts/
```
Si ya hay un script sobre el mismo tema con ángulo similar, dilo. No propongas duplicados sin que el usuario confirme que es un remake intencional.

---

## 4 · Entregable de esta skill

Un mensaje al usuario con:

```
Tema: <X>
Nicho de contenido: <Y>
Scripts previos relacionados: <lista o "ninguno">

Idea 1 — [eje <X>] <título>
- Hook: "<frase>"
- Rúbrica: X/18
- Fallos: <lista o "ninguno">
- Reel análogo: <id del ANALISIS.md>

Idea 2 — [eje <Y>] <título>
- (igual)

Idea 3 — [eje <Z>] <título>
- (igual)

Recomiendo: Idea <N> — razón en una línea.
Esperando OK para escribir concept.md.
```

Si el usuario aprueba, pasar al Paso 5 del flujo del `viral-strategist` (escribir concept.md).

## Anti-patterns

- NO entregues 1 idea aunque creas que es brillante. El contraste de 3 es parte del valor.
- NO entregues 3 variantes del mismo ángulo con hooks distintos. Eso no es divergencia.
- NO inventes criterios del usuario. Si no te dijo "sin terror", no asumas que lo quiere o no.
- NO repitas un tema ya cubierto en `scripts/` sin avisar.
- NO escribas el concept.md completo antes de recibir luz verde en la Idea escogida.
