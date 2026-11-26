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
Título, una línea de qué es, **en adaptaciones de reels en inglés, el bloque «Original en inglés» con los enlaces de Instagram y TikTok (mínimo uno; creador, 2026-11-14)**, **un único bloque de código** con el texto hablado completo en párrafos cortos (uno por idea), sin tiempos ni notas dentro. Debajo, «Ajustes en ElevenLabs»: modelo multilingüe más reciente, español, velocidad ~0.9 (estilo-monigotes: 1.0), estabilidad ~50 %. La licencia de ElevenLabs la gestiona el creador (2026-11-03): no añadas avisos. Última línea: «Pega el mp3 en `nichos/shorts/assets/audios/<slug>/voz.mp3`». **Esa carpeta la crea siempre el creative-producer al escribir el guion** (`mkdir -p nichos/shorts/assets/audios/<slug>`; creador, 2026-11-13), para que el creador solo pegue el mp3.

Criterios antiguos (voz-grabada, estilo-gabriel): 2.ª persona, giro ~70 %, CTA binario, 150–200 palabras. **En monigotes y monigotes-3d mandan los criterios de abajo (2026-11-19).**

## Criterios del guion para pasar las fases de TikTok (creador, 2026-11-19)
- **Sin momentos muertos** (creador, 2026-11-20: «al comienzo del video no quiero nada estático, muchos cortes, y no quiero momentos muertos en los videos, porque donde se muera ahí es donde scrollean»). En el plan: 0–3 s con ≥ 4 cambios y nada estático; ninguna toma de > 1.5 s sin algo nuevo en pantalla; si una frase larga cae en un solo plano, se parte o se le pone acción dentro.
Fuente: `skills/fases-viralidad-tiktok.md` (§4–§4g, con los datos). Prioridad del creador: «la tasa de finalización, las repeticiones del video, generar más compartidos y comentarios». Cada guion lleva al final una tabla corta «cómo pasa cada fase» y una tabla **por función** frente a cajeros (función · cajeros en una línea · nuestra frase).

**Fase 1 (3 s)**
- Primera palabra = **verbo de acción** o paradoja («Escaneó», «Cambió», «Cargó la escopeta»). Nada de fecha, lugar, «imagina» ni orden al espectador. (Excepción: en `estilo-serie-pov` manda `guion-4-pilares.md`, que admite «Imagina que…» con la premisa entera en la frase; 24-nov.)
- La falta (lo indebido) dicha antes de ~3 s; lo que está en juego (dinero, premio, saldo) dicho y **legible en pantalla desde el cuadro 0**.

**Fase 2 (finalización y repeticiones)**
- Entre 0:02 y 0:10, cada frase hace avanzar la historia o siembra una pista. Cero relleno.
- «¿Lo pillan? / ¿se sale con la suya?» abierto hasta el giro, al **62–66 %** (comprobar: palabra del giro / total).
- **Giro con inversión de papeles** y **pistas sembradas a la vista** desde el principio, legible por la imagen en ~4 planos. Mecanismo propio, no el de cajeros.
- Tras el giro, ≈ 75–80 palabras: castigo corto y datos reales. El final nunca muestra al culpable libre.
- **Bucle de contenido**: la última frase lleva a la primera escena o queda abierta y la completa la primera (una sola frase al empalmar). Sin moraleja, pregunta ni despedida. Avisa en «Ajustes de ElevenLabs» de que, si el texto acaba en coma, ElevenLabs puede inventar una sílaba al final y hay que cortarla.
- Duración 59–62 s (David 1.2 ≈ 3.6 palabras/s medido en cajeros y clonación: ~215–225 palabras).

**Fase 3 (compartidos y comentarios)**
- Situación que el público **ha vivido en persona**: el espectador se ve como posible víctima.
- La **lección práctica** («por eso siempre…») **no se dice en la voz**: la saca el público (y la siembra el comentario fijado).
- Nada de pregunta para juzgar en la voz (en cajeros, 0 respuestas).
- «Esto pasa de verdad» con datos de 2+ fuentes; si hay escena dramatizada, el aviso «Historia basada en hechos reales» va en la descripción.

**Copias y palabras**
- Guion propio sobre otro video: se copia **la estructura**, nunca las palabras, la situación, el escenario, los personajes ni el mecanismo del giro.
- No se ajusta un guion aprobado hasta que el creador diga «ajústalo»; un solo archivo por guion (sin copias ni versiones sueltas: el creador pidió «no hagas md de mas»).

**En el plan de escenas** (las metas que el editor mide con `medir_visual.py`): un cambio de plano cada ~1.2 s y 4 en 0–3 s; luz en todo el video (0 % de cuadros oscuros, también la noche y los interiores); cámara siempre en movimiento (≤ 5 % de cuadros quietos); el cuadro 0 sin la cara del culpable si el bucle lo mostraría libre; **cada lugar que nombra la voz se reconoce** en imagen (una «cocina» no puede ser un rectángulo liso, #66); **objetos únicos** (llavero, bolsa, tarjeta) en un solo sitio por escena en la tabla de vestuario (#53).

## Lecciones de hedy-lamarr-wifi (2026-11-02)
- **Duración de la voz:** calcula con el ritmo medido de la voz y velocidad que se van a usar, no con el de otro video. Con Alonso salió:
  - 2.4–2.53 palabras/s a velocidad 0.9: 192 palabras dieron 76–80 s;
  - ≈ 2.56 palabras/s a velocidad 1.0: 164 palabras dieron 64 s.
  - **David a velocidad 1.2** (estilo-monigotes-3d, método cajeros): 270 palabras dieron 66.8 s, ≈ 4.0 palabras/s (pudding-millas, 2026-11-13).

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

## Vestuario y música (2026-11-17, ladron-que-movia-muebles)
- **Tabla de vestuario y atrezo por escena** (personaje × escena → puesto / quitado / en la mano, con su motivo). Sin gags que no estén en el original salvo que el creador los pida. El reviewer la comprueba (errores #52–#53).
- **Si el video lleva música** (decisión del creador): el plan fija la fuente, los tramos según la historia (con la transcripción real si ya hay voz) y el nivel frente al original **antes** de la prueba de 10 s.

