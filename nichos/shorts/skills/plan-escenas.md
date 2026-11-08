---
name: plan-escenas
description: Cómo planear las escenas ilustradas de un short explainer (sustituye al antiguo storyboard). Lo usa el shorts-creative-producer para escribir `<slug>.escenas.md`, el editor para construir el generador de escenas y el reviewer para comprobar que se cumplió.
---

# Plan de escenas

El video se cuenta con **un mundo**, no con un objeto por palabra. Referencias del lenguaje: `ideas-virales/raw/DedXqPENbLm.mp4` (cuarto de noche + corte del cargador + datos) y `DemtYpjNWPc.mp4` (personaje simple actuando en su escenario). Ejemplo construido: voz-grabada (`nichos/shorts/exports/voz-grabada/escena_r7.py`, `render-log.md` § R7–R9).

## Estilo del proyecto (primero)
Hay dos estilos (`tools/architect/estilo/estilos/`):
- **`estilo-gabriel`**: el de este documento por defecto.
- **`estilo-monigotes`**: si el creador pasa refs de @resultaaquee o pide una historia con monigotes. Escribe el estilo elegido en el `escenas.md`. Con monigotes mandan su `perfil.md` y su `aprendizajes.md`:
  - un cambio cada 1–1.5 s con golpes de cámara, sin fundidos;
  - subtítulos que se mueven según la toma (creador, 2026-11-03): cada toma indica ARRIBA (y ≈ 950, franja libre 880–1060) o ABAJO (y ≈ 1380, franja libre 1310–1450); solo cambian en cortes secos y el primer y último cuadro van igual para que el bucle no salte;
  - sin capítulos ni cabecera;
  - columna de **SFX** en la tabla.

## Pasos
1. **Elegir el mundo:** escenario + personaje + hora + paleta. Debe poder volver al final (bucle).
2. **Cortar el guion de voz en tramos de idea** (5–20 por video). Cada tramo = una escena con su frase literal.
3. **Para cada tramo, elegir la escena** que lo muestra literalmente: el personaje actuando (`cuarto`), un corte tipo esquema del mecanismo (`cabeza`, `oido`), un gráfico del tema (`ondas`, `vida`), la UI que usaría el personaje (`movil`, `chat`). Si no existe, marcarla **NUEVA** y describirla.
4. **Dentro de cada escena, decidir qué cambia** cada ≤3 s (una pieza del mecanismo, un gesto, una etiqueta) y cómo se mueve la cámara (puntos de encuadre). Cambios de escena solo cuando cambia lo que se muestra.
5. **Capítulos** (1, 2, 3…) para las partes del mecanismo y **cabecera de fuente** con el dato del concepto.
6. **Subtítulos «selección»** arriba; marcar las tomas donde arriba hay algo importante para que bajen.
7. **Final:** cola de ~1.2 s, vuelta a la pose y encuadre del inicio, sin texto.

## Formato de `<slug>.escenas.md`
```markdown
---
slug: <slug>
aprobado_fecha: YYYY-MM-DD   # solo tras el ok del creador
---
## Mundo
<escenario, personaje, paleta, hora; referencia que lo justifica>

## Escenas
| # | Frase (literal) | Escena | Qué se ve y qué cambia | Cámara | Etiqueta / capítulo | Subtítulos | SFX (si el estilo los lleva) |
|---|---|---|---|---|---|---|---|

## Capítulos y cabecera
## Final en bucle
## Piezas nuevas (si hay)
```

## Prohibido (rechazos del creador)
Un emoji o icono por palabra · formas geométricas apiladas fingiendo caras u órganos · texto plano como visual principal · pantalla vacía · iconos de relleno · barras/cuadrículas de estadística genérica · cortes donde no cambia nada · transiciones con efecto · final que corta en seco.

## Formato de `<slug>.guion-voz.md`
Título, una línea de qué es, **un único bloque de código** con el texto hablado completo en párrafos cortos (uno por idea), sin tiempos ni notas dentro. Debajo, «Ajustes en ElevenLabs»: modelo multilingüe más reciente, español, velocidad ~0.9 (estilo-monigotes: 1.0), estabilidad ~50 %. La licencia de ElevenLabs la gestiona el creador (2026-11-03): no añadas avisos. Última línea: «Pega el mp3 en `nichos/shorts/assets/audios/<slug>/voz.mp3`».

Criterios: texto del concepto en 2.ª persona, hook en la primera frase, giro ~70 %, CTA binario; 150–200 palabras (60–90 s a velocidad 0.9). Ejemplo: `nichos/shorts/scripts/ciencia/voz-grabada.guion-voz.md`.

## Lecciones de hedy-lamarr-wifi (2026-11-02)
- **Duración de la voz:** calcula con el ritmo medido de la voz y velocidad que se van a usar, no con el de otro video. Con Alonso salió:
  - 2.4–2.53 palabras/s a velocidad 0.9: 192 palabras dieron 76–80 s;
  - ≈ 2.56 palabras/s a velocidad 1.0: 164 palabras dieron 64 s.

  En estilo-monigotes el creador prefiere la **velocidad 1.0**. Para 60–68 s: **155–170 palabras**. Cada generación de ElevenLabs varía unos segundos; da al creador recortes ya marcados (frases para quitar o recuperar).
- **Carteles y rótulos del plan** cumplen la lista «No decir» igual que la voz: escribe el texto exacto de cada uno («= HASTA 88 FRECUENCIAS»).
- **Planea los SFX** con la escena: cada objeto que aparece o actúa lleva su sonido (piano → teclas, sello → golpe, puerta que se abre → puerta). Si planeas una puerta, haz que se abra en la imagen. Sin música.
- **Frases con la cifra exacta de la fuente:** «Si el enemigo bloquea tu frecuencia, tu torpedo se pierde», nunca «se queda con tu torpedo». Comprueba los verbos contra el texto de la fuente primaria (la patente).
- Evita frases que dependan de una palabra muy corta, como «o», en la pregunta final: ElevenLabs puede comérsela. Si es imprescindible, avisa al editor para que lo compruebe.

## Antes de entregar el plan
- Cada frase del guion tiene su escena; ninguna es «un objeto por palabra».
- Ninguna escena se queda > 3 s sin un cambio planeado; los cambios dentro de una escena son movimientos de cámara.
- Gráficos del tema; final en bucle planeado.
- Con el creador ya contento: cambios mínimos, de menor a mayor, y una recomendación.

## Reutilización (2026-11-04)
Antes de planear, lee `tools/architect/biblioteca/reutilizables/CATALOGO.md`. En la tabla de escenas, marca cada escenario, monigote, accesorio y SFX como `[catálogo]` o `[nueva]`; con más de 3 nuevas, justifícalo en una línea. En la cabecera, anota el nivel de ambiente y la densidad de SFX (del perfil del estilo; si no están, pregunta al creador en el mismo ✋ del guion).
