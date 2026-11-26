---
name: animacion-monigotes
description: Cómo se anima el formato plano de monigotes (estilo-monigotes, refs @resultaaquee de octubre): escenarios 2D frontales con `Escenario`, personajes `Monigote`, cámara 2D por puntos con golpes y desenfoque, subtítulos centro y SFX diegéticos. Para el formato 2D dentro de 3D usa `animacion-monigotes-3d`.
---

# Animación de monigotes (formato plano)

**Perfil que manda:** `tools/architect/estilo/estilos/estilo-monigotes/perfil.md` y su `aprendizajes.md`. Esta skill explica **cómo se hace**; las reglas son las del perfil y no se cambian aquí. Si el proyecto dice `estilo-monigotes-3d`, no es esta skill: usa `animacion-monigotes-3d.md` (creador, 2026-11-11: «una skill para cada uno», sin mezclarlos).

Videos hechos así (consulta el catálogo antes de abrirlos): **hedy-lamarr-wifi** (referencia del estilo, `escenas_hedy-lamarr-wifi.py` + `sfx_r3.py`), **soldado-flor-que-no-existia** (`escenas_soldado-flor-que-no-existia.py`, `camino()` de golpes), **bushby-vuelta-al-mundo-a-pie** (`escenas_bushby-vuelta-al-mundo-a-pie.py`, con `comprobar_carteles`) y la prueba de **kunst**.

## 1 · Piezas
| Pieza | Archivo | Para qué |
|---|---|---|
| `Monigote` | `src/reel/escenas/Monigote.tsx` | Personaje base: cabeza redonda blanca, cuerpo cápsula, palos. `REPARTO` (aspectos por personaje), `claves` por tiempo (`expresion`, `pose`, `habla`, `mirada`, `objeto`, `salto`, `parpadeo`, `asiente`, `niega`, `golpe`), `busto`, `espaldas`, `tinte`, `luz`. Poses y gestos nuevos van **aquí**, nunca en un archivo de video. |
| `Escenario` | `src/reel/escenas/Escenario.tsx` | Escena `tipo: escenario`: `fondo` (registro `FONDOS_ESCENARIO`), `personajes` (con `anda` x/y/escala, `desde`/`hasta`, `delante`), `desenfoque_fondo`, `atrezo`, `letreros`, `globos`, `piezas`, `recuerdos`. Cada fondo tiene capa `fondo` y `frente` (lo que tapa a los personajes: mostradores, mesas). |
| Fondos | `EscenariosHedy.tsx`, `EscenariosSoldado.tsx`, `EscenariosKunst.tsx`, `EscenariosBushby.tsx` y `comun/` | Dibujos SVG 1080×1920 con margen para que la cámara empuje y barra. Lo usado en ≥ 2 videos está en `comun/` (Letrero, Globo, Burbuja, Corcho, Garita, Luz, Rotulo, Papeleria, Clima). |
| Cámara | `CapaEscenas.tsx` | `camara.puntos` = `[{t, x, y, escala, curva}]` en la base 1080×1920; `curva: suave | lineal | golpe`; `desenfoque_movimiento`; `impactos` (`sacudida`, `lineas`); `transicion` (`barrido` con `dir`, `zoom`); `fundido_cuadros: 0` = corte seco. En `escenario` la cámara no sale del lienzo (`limitarCamara`). |
| Subtítulos | `src/estilo/subtitulos-centro.ts`, `SubtitulosCentro.tsx` | `subtitulos_centro` con `posiciones` [{desde, hasta, y}] para los tramos que no van en y 1380. |
| SFX | campo `sfx_extra` de la EDL, biblioteca `tools/architect/biblioteca/sfx/` | Colocados por un script `sfx_<slug>.py`. |

## 2 · Generador de escenas (`escenas_<slug>.py --edl <edicion-vN.json>`)
Copia el de bushby (el más completo). Partes:
1. `retocar_palabras(edl)`: solo texto en pantalla (puntuación del guion, palabras que whisper descartó, bloques de ≤ 3 palabras). Nunca cambia tiempos.
2. `Palabras`: busca frases en orden (`P.en("frase")`, `P.fin_de("frase")`); **todos los tiempos salen de ahí**, menos `L = 0.03` s para que el cambio caiga un pelo antes de la palabra.
3. Un diccionario `T` con el instante de cada golpe (`T["5b"] = w("Bushby") - L`).
4. Helpers `escena(id, desde, hasta, fondo, personajes, puntos, impactos, trans, **params)`, `per(quien, x, y, escala, claves)`, `clave(t, **kw)`, `punto(t, x, y, escala, curva)`.
5. `camino(cambios, encuadres, desde, hasta)`: un golpe de 6 cuadros (empieza 2 cuadros antes de la palabra) a cada encuadre y **deriva ×1.05** entre golpes, para que la cámara nunca esté quieta.
6. Lista `Y` de posiciones del subtítulo por tramo (ABAJO 1380 por defecto, ARRIBA 950 en planos abiertos), que **solo cambian en un corte**.
7. `comprobar_carteles(E, Y)`: cada cartel en cada punto de cámara, con la cámara limitada al lienzo: entero en x 135–945, dentro de cuadro y fuera de la franja del subtítulo. Sin avisos antes de renderizar.
8. `duracion_s` = última palabra + 1.2 s (cola del bucle).

## 3 · Ritmo y cámara (del perfil)
- Un cambio cada 1.0–1.5 s; ningún tramo > 3 s. Casi todo son golpes de cámara con desenfoque (≤ 14 px) dentro del mismo escenario; deriva lenta entre golpes.
- Corte seco solo en golpes de guion (uno cada ~6–8 s); barrido entre escenarios. Nada de fundidos.
- Planos generales con personajes a escala ≥ 1.4; primeros planos ×1.9–2.4 con fondo desenfocado (nunca lo que la voz nombra).

## 4 · Subtítulos
Archivo Black blanco con contorno negro, 1–2 palabras (3 solo con «de la …»), sin color. ABAJO y ≈ 1380 (franja 1310–1450 libre) o ARRIBA y ≈ 950 (880–1060 libre). Ningún bloque empieza ni termina en palabra de enlace.

## 5 · Sonido
- `sfx_<slug>.py` (copia de `sfx_bushby.py` / `sfx_cajeros.py`): `RECORTES` (origen del catálogo, inicio, duración, fundidos, semitonos, invertir, filtro) y `colocaciones(E)`, que **saca los tiempos de la EDL** (aparición o golpe del objeto). Tope de diseño 14 dB bajo el pico de voz de cada sílaba, sobre la suma; el real ≥ 10 dB se mide sobre el mp4 con `medir_sfx_render.py`.
- Sin música ni ambiente continuo; ráfagas de 1–1.8 s al entrar en un sitio; todo lo que aparece o actúa suena. Densidad: la del perfil (0.3–0.4 ev/s) o la que fije el creador para el proyecto (≈ 0.77 «para experimentar»).
- Primero el inventario de SFX de `CATALOGO.md`; ElevenLabs solo con autorización y anotando créditos.

## 6 · Render y entrega
1. `validar.ts` sin FAIL.
2. Imagen: `npx remotion render src/index.ts Reel <salida>.mp4 --props=<edl> --muted` (1440×2560). Audio: `--codec=wav` del video entero.
3. Montaje: `montar_prueba.py` (loudnorm de 2 pasadas a −14 LUFS, LRA objetivo 2, escala 1080×1920 lanczos, CRF 16). Si solo cambia el audio, `--copiar-video`.
4. Medir: ffprobe, ebur128 (−14 ±0.5, LRA ≤ 2.5, pico ≤ −0.7), `medir_sfx_render.py`, hoja de cuadros y primer/último cuadro (SSIM ≥ 0.95).

## 7 · Lista de comprobación (la de `edicion-escenas.md` más)
- ¿Algo clave en la franja del subtítulo en el primer o el último cuadro de cada empuje? ¿Algún cartel cortado o tapado?
- ¿Suena todo lo que aparece, a ±1 cuadro, ≥ 10 dB bajo la voz, sin música?
- ¿Rótulos dentro de la lista «No decir»?
- ¿Bloques de una sola palabra de enlace?
- `comprobar_catalogo.py` = «CATALOGO al día».

## 8 · Errores aprendidos en otros formatos que también valen aquí
| Error | Dónde | Cómo se evita |
|---|---|---|
| El subtítulo cruza un corte y se queda en la franja (ARRIBA/ABAJO) del plano anterior, encima de lo clave del plano nuevo (una placa, una boca, un gorro) | cajeros-loteria R1 (estilo-monigotes-3d, review #7; 15 bloques, 95 cuadros) | El render fijaba la y al empezar cada bloque. Con `subtitulos_centro.y_por_tiempo: true` la y sale del tramo de `posiciones` en cada instante y cambia en el corte, con la imagen. Comprueba con `exports/cajeros-loteria/qa/r2_frames/medidas/bloques.ts <edl>` que ningún bloque marque CRUZA. |
