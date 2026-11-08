---
name: viral-rubric
description: Rúbrica de 18 puntos para puntuar un concepto viral y emitir veredicto (candidato / viable / reescribir). Codifica las mecánicas de los breakouts y los modos de fallo. Reutilizable por viral-strategist (durante ideación) y quality-reviewer (durante inspección final).
---

# viral-rubric

Rúbrica cuantitativa para decidir si un concepto se produce o se reescribe. Deriva de `ideas-virales/ANALISIS.md` §6.bis y §6.ter.

## Cuándo invocarla

- Durante la generación de ideas, para elegir entre 3 candidatas (`viral-idea-generation`).
- Durante la validación de un concept.md ya escrito.
- Durante la revisión final del video renderizado, para contrastar la ejecución con el potencial del concepto (`quality-reviewer`).

## Entrada

Un concepto con al menos: hook, 4 beats visuales descritos, bucles, CTA, duración objetivo.

## Salida

Tabla de 12 celdas con puntuación + total + veredicto + lista de celdas a corregir.

---

## Rúbrica — 18 puntos distribuidos en 6 bloques

### A · ACTIVACIÓN (3 pts) — filtro para romper al millón

**A1 (2 pts) · ¿El hook pide tocar / mirar / sentir algo del viewer AHORA mismo?**
- 2 = sí, acción corporal explícita (@sovera "tu brazo se levantará solo")
- 1 = alude a algo que el viewer tiene cerca sin pedir acción (@loconstruiste "ese tac-tac cuando cruzas en coche")
- 0 = pregunta pasiva de biblioteca (@nuncateloexplicaron "¿cómo sabe Google Maps…?")

**A2 (1 pt) · ¿Es un objeto / fenómeno que el viewer vio esta semana?**
- 1 = sí
- 0 = tema abstracto / lejano

### B · APILAMIENTO (3 pts) — filtro para romper los 400K

**B1 (2 pts) · ¿La primera frase apila 2–3 promesas distintas?**
- 2 = tres promesas (@loconstruiste "por qué no se cae / qué hay bajo el río / qué es el tac-tac")
- 1 = dos promesas
- 0 = una sola promesa

**B2 (1 pt) · ¿La primera palabra importante cae antes del s1?**
- 1 = sí, el audio arranca directo con la palabra clave
- 0 = introducción, logo, silencio

### C · RETENCIÓN VISUAL (3 pts) — test del audio apagado

**C1 (2 pts) · ¿El visual CONSTRUYE el mecanismo frase por frase?**
- 2 = construcción progresiva pieza a pieza (@loconstruiste, @resultaaquee electro, @sovera)
- 1 = cambia de escena con el audio pero no construye nada acumulativo
- 0 = ilustración decorativa (@thebioloco, @nuncateloexplicaron)

**C2 (1 pt) · ¿Hay 2–4 beats visuales distintos en el DESARROLLO (sin reutilizar plano)?**
- 1 = sí
- 0 = reutiliza planos o solo tiene 1 beat visual sostenido

### D · BUCLES Y PAYOFF (4 pts)

**D1 (2 pts) · ¿Hay bucle abierto que solo cierra en el último beat (o no cierra)?**
- 2 = dos bucles anidados (@sovera: "tu brazo se levantará" + "1 de 4 no les pasa, nadie sabe por qué")
- 1 = un bucle que cierra claro al final
- 0 = sin bucle, todo se explica a medida

**D2 (1 pt) · ¿Hay twist a ~70% apto para compartir/etiquetar?**
- 1 = sí
- 0 = no

**D3 (1 pt) · ¿Micro-payoffs cada 10–15s en el valle 40–60%?**
- 1 = sí (al menos 2 micro-payoffs: cifra, revelación parcial, visual satisfactorio)
- 0 = no

### E · CTA Y ALGORITMO (3 pts)

**E1 (2 pts) · ¿El CTA fuerza respuesta?**
- 2 = pregunta binaria con 2 opciones (@historiasparanormales "FUERA o SOFÁ") o reto físico (@sovera)
- 1 = pregunta abierta razonable (@loconstruiste "cuál puente has cruzado")
- 0 = CTA genérico ("comenta qué piensas") o ausente

**E2 (1 pt) · ¿Hay doble gancho activante también al inicio, no solo al final?**
- 1 = sí (ej. pregunta observable embebida en el hook)
- 0 = el gancho activante solo va al cierre (@chispalogica)

### F · FORMATO (2 pts)

**F1 (2 pts) · Duración objetivo del concepto**
- 2 = 60–90s (sweet spot)
- 1 = 50–59s o 91–100s
- 0 = fuera de 50–100s. 30s demasiado corto; >100s solo si usa capítulos numerados tipo @chispalogica

---

## Umbrales

| Puntuación | Veredicto | Acción |
|---|---|---|
| **16–18** | 🟢 Candidato a producir | Alto potencial de breakout. Pasar al concept.md |
| **13–15** | 🟡 Viable | Producible, pero pulir las celdas por debajo del máximo antes |
| **< 13** | 🔴 Reescribir | No producir. Volver a la generación de ideas con cambio de ángulo |

Si recomiendas producir con < 13, debes dar razón explícita (ej. "serie de prueba para medir estilo visual").

---

## Formato de salida

```markdown
### Rúbrica — <título del concepto>

| Celda | Pts | Nota + reel análogo |
|---|---:|---|
| A1 — Activación corporal | X/2 | <justificación citando @autor id> |
| A2 — Objeto cotidiano | X/1 | … |
| B1 — Promesas apiladas | X/2 | … |
| B2 — Primera palabra <s1 | X/1 | … |
| C1 — Visual construye | X/2 | … |
| C2 — Beats distintos | X/1 | … |
| D1 — Bucle abierto | X/2 | … |
| D2 — Twist 70% | X/1 | … |
| D3 — Micro-payoffs | X/1 | … |
| E1 — CTA fuerza respuesta | X/2 | … |
| E2 — Doble gancho inicio | X/1 | … |
| F1 — Duración 60–90s | X/2 | … |
| **TOTAL** | **X/18** | **<veredicto emoji + palabra>** |

**Modos de fallo (§6.ter):**
- Evita: <F1 / F2 / …>
- Comete: <F? / ninguno>
- Techo esperable: ~<X> likes

**Celdas a corregir antes de producir** (si aplica):
- <celda>: <qué cambiar>
```

---

## Reglas de puntuación

1. **Cada celda cita un reel del ANALISIS.md** o un principio concreto. No puntuar "por sensación".
2. **Si una celda está en el límite** entre 1 y 2, prefiere el valor menor. La rúbrica es optimista por diseño; se compensa con exigencia.
3. **No sumar sin mostrar celdas.** La transparencia por celda es parte del valor — permite reescribir solo lo que está roto.
4. **No ocultar puntuaciones bajas.** Si una idea saca 10/18, dilo claro y recomienda reescribir, aunque el usuario parezca enamorado del tema.

## Reutilización en `quality-reviewer`

Cuando esta skill se invoca sobre un video **renderizado** (no un concepto), las celdas se reinterpretan como ejecución:
- A1 — ¿El hook ejecutado activa al viewer? (ver el frame 0–3s, no la intención)
- C1 — ¿El visual final construye? (ver los beats renderizados, no la planificación)
- etc.

La rúbrica cuantifica el **gap** entre concepto puntuado y video entregado. Un video que ejecuta por debajo del concepto es `NEEDS_REVISION`.

## Anti-patterns

- NO des un total sin tabla de celdas.
- NO uses esta skill sobre un pitch verbal sin estructura. Si no hay hook, beats, bucles y CTA definidos, usa primero `viral-pattern-execution`.
- NO ajustes la rúbrica para que la idea del usuario pase. Si no pasa, no pasa.
