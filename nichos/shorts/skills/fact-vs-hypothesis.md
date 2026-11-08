---
name: fact-vs-hypothesis
description: Etiquetado inline de afirmaciones factuales en concept.md, scripts y guiones técnicos. 3 etiquetas, flujo de verificación con WebSearch, criterio de bloqueo. Reutilizable por viral-strategist, creative-producer y quality-reviewer.
---

# fact-vs-hypothesis

Ningún video sale a producción con una hipótesis sin cerrar. Esta skill define cómo marcar los claims y cuándo verificar.

## Cuándo invocarla

- Al escribir la **narrativa cruda** de un `concept.md`.
- Al revisar un **guion técnico** antes del render.
- Al cerrar **hipótesis pendientes** antes de aprobar un video.

## Las 3 etiquetas

Cada afirmación factual en la narrativa lleva **una y solo una** etiqueta inline:

### `[hecho: <fuente>]`
Dato verificado con fuente concreta citable.

Ejemplos:
- `El cerebro humano pesa unos 1.3 kg de media [hecho: enciclopedia, aritmética consensuada].`
- `En 2011 el NRDC midió el consumo vampiro de casas de EE. UU. en 5–10% [hecho: NRDC 2011, chispalogica DedXqPENbLm cita la misma fuente].`

Reglas:
- La fuente debe ser **nombrable**, no "según varios estudios". Mínimo: institución, año, o cálculo aritmético directo.
- Si usas una cifra concreta (año, porcentaje, peso, distancia), **obligatorio** `[hecho: …]`.
- Vale citar otro reel del `ANALISIS.md` como respaldo *circunstancial*, no como fuente primaria.

### `[hipótesis: <qué falta verificar>]`
Claim que suena bien pero no has verificado todavía. Hay que cerrarla antes del render.

Ejemplos:
- `Los babilonios eligieron base 60 porque contaban falanges con el pulgar [hipótesis: teoría común, verificar en historia de las matemáticas antes de narrar].`
- `A 1 de cada 4 personas el brazo no se levanta [hipótesis: sovera lo afirma pero no cita estudio; buscar o atenuar la cifra].`

Reglas:
- La etiqueta debe decir **qué** falta: fuente, cifra exacta, nombre propio, mecanismo.
- Las hipótesis se listan en §10 del `concept.md` como checkbox.
- **No se renderiza con hipótesis abiertas** salvo autorización explícita del usuario.

### `[común]`
Hecho de dominio público obvio que no requiere fuente.

Ejemplos:
- `El agua es H2O [común].`
- `Una hora tiene 60 minutos [común].`
- `Las palomas vuelan [común].`

Reglas:
- Si dudas si es "común" o "hecho con fuente", úsala como `[hecho: ...]` y cita algo mínimo.
- No abuses de `[común]` para evitar verificar.

---

## Flujo de verificación

Cuando una hipótesis necesita cerrarse:

### 1 · WebSearch primero
```
WebSearch "<claim exacto en comillas>" + modificador contextual
```
Ejemplo: `WebSearch "base 60 babilonios falanges pulgar origen"`.

Si el primer page de resultados **confirma con fuente nombrable** → convertir a `[hecho: <fuente citada>]`.

### 2 · WebFetch de la mejor fuente
Si WebSearch encuentra una página que parece sólida (Wikipedia, institución, paper, libro), hacer `WebFetch` sobre la URL con un prompt específico: "¿Confirma que X? ¿Cita fuente primaria?".

### 3 · Decisión
- **Confirmada con fuente nombrable** → `[hecho: <fuente>]`
- **No confirmada o fuentes contradictorias** → mantener `[hipótesis: ...]` y:
  - Reescribir la narración para **atenuar** el claim ("una teoría dice que…", "parece ser que…")
  - O eliminar el claim si no es esencial
  - O listar en §10 del concept.md como bloqueante — pedir decisión del usuario

### 4 · Nunca inventar fuente
Si no encuentras fuente, no "aproximes" una. "Según estudios" no es una fuente, es un camuflaje. Mejor atenuar el lenguaje.

---

## Reglas estrictas

1. **Cifras concretas (números, años, nombres propios) exigen fuente.** No hay excepción.
2. **Atenuación de hipótesis** es preferible a inventar fuente. "Parece que…", "una teoría dice…", "podría ser que…" son aceptables para hipótesis que no cierran.
3. **Las hipótesis abiertas bloquean el render.** El `executive-producer` las revisa antes de dar luz verde al editor.
4. **El usuario puede sobrescribir** una hipótesis abierta diciendo "déjalo así, es narrativo". En ese caso, en el concept.md se marca `[hipótesis: usuario-aceptada]` y queda registro.
5. **Las fuentes son citables en el video o en el caption.** Si narras "según la NRDC", ese chip puede aparecer en pantalla (como hace @chispalogica con "DATOS · NRDC / BERKELEY LAB" en el frame).

---

## Aplicación en el concept.md

En §3 (narrativa cruda), cada frase factual etiquetada:
```
> El invertebrado más grande del planeta es el calamar colosal [hecho: Architeuthis dux, Guinness], que puede medir hasta 14 metros [hecho: estimaciones de ejemplares varados, biología marina]. Pero casi nunca se le ha visto vivo en su hábitat [hipótesis: filmaciones en vida salvaje antes de 2012 — verificar fecha exacta de primer filmado].
```

En §10 (verificaciones pendientes):
```
- [ ] Fecha del primer filmado de calamar colosal vivo (hipótesis en §3 beat 2)
- [ ] Confirmar máximo 14 m vs 12 m — hay rangos en distintas fuentes
```

El `executive-producer` no deja pasar un concepto al `creative-producer` sin §10 vacía o con cada checkbox marcado como "resuelto" o "aceptado por usuario".

---

## Reutilización en otros agentes

- **`creative-producer`** — hereda las etiquetas del concept.md al guion técnico sin perderlas. Si re-redacta una frase, mantiene la etiqueta.
- **`quality-reviewer`** — chequea que ninguna hipótesis sin cerrar llegó al video final. Si la detecta en subtítulos o narración ya renderizada, emite `NEEDS_REVISION`.

## Anti-patterns

- NO uses "según estudios recientes" / "está demostrado que" / "los expertos dicen". Son ruido, no fuentes.
- NO cites otro reel como fuente primaria de un hecho científico. El reel refuerza el patrón narrativo, no la evidencia.
- NO uses `[hecho: ...]` sin algo nombrable en el campo fuente.
- NO cierres una hipótesis sin WebSearch previo. Confirmar con 1 fuente mínimo.
- NO rendering con hipótesis abierta y sin autorización.
