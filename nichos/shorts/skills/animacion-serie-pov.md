---
name: animacion-serie-pov
description: Cómo se hace un episodio del estilo-serie-pov (serie interactiva en segunda persona calcada de @coolfunstories4 «Stick Motion»): escena `serie` 2D en SVG, personajes «stick» de cabeza negra, HUD de día/hora/lugar/cuenta atrás, UI de móvil en POV, cortes secos con flash, sepia y barrido, subtítulos amarillos fijos en y 1460, pista de diálogo de varias voces, sonido medido contra el mismo momento del original, tarjeta de voto A/B, reutilización entre episodios, comprobaciones y costes medidos en alerta-nuclear-ep1. Ninguna regla de monigotes aplica.
---

# Animación serie POV («Stick Motion»)

**Perfil que manda:** `tools/architect/estilo/estilos/estilo-serie-pov/perfil.md` y su `aprendizajes.md`. Esta skill explica **cómo se hace**; si algo choca, gana el perfil.
**Errores de este estilo:** `nichos/shorts/skills/errores-serie-pov.md` (SP-1…). Se lee entero al empezar cada episodio o ronda.
**Episodio de referencia:** `nichos/shorts/exports/alerta-nuclear-ep1/` (R3, APPROVED 0/0/0). Generador `escenas_alerta-nuclear-ep1.py`, sonido `sfx_alerta.py`, diálogo `armar_dialogo.py`, proyecto `tools/architect/proyectos/2026-11-22-alerta-nuclear-ep1-r2/` (EDL renderizada `edicion-v4.render.json`). Cópialo como plantilla.
**Original medido:** `nichos/shorts/ideas-virales/raw/stickmotion/7704332615410617618.mp4` (+ `.words.json`), desarmado en `ideas/shorts/2026-11-22-stick-motion-recrear.md` (§1 planos, §2 animación, §3 audio con la tabla de SFX y sus segundos, §4 estructura, «Corrección del director»).

**Ninguna regla de monigotes aplica** (creador, 2026-11-22: «no lo quiero el estilo de monigotes, quiero ese del video original»). Ni «SFX ≥ 10 dB bajo la voz», ni ducking fijo, ni bucle, ni la prohibición de bloques de una palabra, ni subtítulos ARRIBA/ABAJO por plano, ni `revision-por-bloques` como obligación de monigotes (aquí se hace igual, pero porque funciona). De su código solo se reutilizan utilidades internas (cámara por puntos de `CapaEscenas`, barrido, desenfoque).

## 0 · Qué es y qué se calca
Serie en segunda persona («Imagina que despiertas…») por episodios; el público vota A/B en comentarios qué pasa en la siguiente parte.
- **Se calca del original:** dibujo plano con degradados, luces volumétricas y viñeta; personajes de cabeza negra; HUD; reglas en notas adhesivas; ritmo (plano medio 3.4 s, algo visible cada ≈ 1.7 s, 3 planos en los primeros ≈ 4 s); transiciones; subtítulos; ambiente sin música; niveles y timbre de cada sonido; tarjeta A/B sin bucle.
- **Se cambió (creador, «cositas»):** color de las sudaderas (tú turquesa `#1fb3a6`, vecino rojo ladrillo `#b5452c`), botones más grandes, mapa genérico (sin nombres reales), textos en español. El casco del vecino, como el original.
- **Se permite pasar de 90 s** (ep. 1: 88.97 s).

## 1 · Piezas (`tools/architect/src/reel/escenas/`)
| Pieza | Archivo | Para qué |
|---|---|---|
| Escena `serie` | rama `serie` de `CapaEscenas.tsx` → `EscenaSerieTodo` | 2D en SVG dentro de `CapaEscenas` (cámara por puntos limitada al lienzo, cortes, barrido, viñeta). HUD encima con `HudSerie` si la EDL trae `escenas.hud` |
| Prueba (pl. 1–5) | `SeriePov.tsx` | `CabezaStick`, `sirena()` (luz roja/azul cada 0.667 s), `bocaHabla()`, lugares `cuarto`, `fachada`, `skyline`, `movil` (POV: bloqueo, píldora, alertas que se apilan, notificación), `HudSerie`/`hudEn()`/`formatoCuenta()`, colores `SERIE`, fuente `cargarFuenteSerie()` |
| Resto de lugares | `SerieLugares.tsx` | `FiguraStick` (cuerpo entero por IK), `Haz` (linterna), `NotaRegla` («REGLA #N» con pop o `cae`), `popEntrada`, lugares `cuarto_tv`, `tv` (alerta + cuenta), `recibidor` (puerta 9C con golpes), `vestibulo` (de día, `seccion` con sótano y búnker en corte, globos «JA JA»), `primer_plano`, `escaleras` (planta enorme), `sotano` (escotilla con `asaEscotilla`), `bunker` (estantes, literas, radio, recuadros de inventario, temporizador, mapa, y en R2 `techo`/`escotilla_luz`/`escalera`/`bombilla`/`mapa_dx`), `mapa` (círculo, fecha, ruta punteada, «6 MIN»), `chat`, `tarjeta` |
| Efectos | `EscenaSerieTodo` (`params.efectos`) | `flash` [{t, d}], `tv_linea` {t, cuadros: 6}, `enfoca` {t, cuadros, px}, `sepia` |
| Subtítulos | `subtitulos_centro` con modo serie | `mayusculas`, `color_actual`, `resplandor_px`, `pop_desde`, `ancho_em` (sin ellos, la capa dibuja como antes) |
| Fuente | `biblioteca/fuentes/poppins/Poppins-ExtraBold.ttf` | OFL, con su fila en `LICENCIAS.md` |
| Pruebas | `pruebas/unit/serie-pov.test.ts` | 8 tests; correr con `npx vitest run pruebas/unit/serie-pov.test.ts` tras tocar cualquier pieza |

Para no romper lo aprobado, los lugares nuevos van en `SerieLugares.tsx` (o en un archivo nuevo del episodio), no en `SeriePov.tsx`; los cambios a un lugar ya usado, como **parámetros opcionales** que por defecto dibujan igual (así se hizo el pl. 24 en R2).

## 2 · Personajes «stick»
- **Cabeza** (`CabezaStick`): círculo negro con **filo de luz crema** `#f3e6c8` (arco, no contorno), `ojos` `pastilla` (neutral) / `redondos` (susto) / `cerrados` (dormido), `boca` `raya`/`o`; el cambio de ojos y boca es de un cuadro a otro, sin transición.
- **Boca que habla:** alterna raya/«o» cada 3 cuadros **solo dentro de los tramos `habla`** de ese personaje. El generador los saca de la pista de diálogo: `hablantes()` lee `dialogo_rN.json` (quién habla en cada tramo) y `habla_de(edl, quien, H)` junta sus palabras de la transcripción. El protagonista no habla nunca.
- **Cuerpo entero** (`FiguraStick`, `fig(x, y, h, quien, **kw)` en el generador): `x`, `y` = pies, `h` = alto; `pose` (`pie`, `tapa_ojos`, `dedo`, `senala_arriba`, `senala`, `carga`, `bolsa`, `movil`, `tira`, `estira`, `rie`, `gracias`, `brazos_atras`) con codo/rodilla por IK; `cambios` [{t, pose, ojos, boca, mira}]; `anda` {t0, t1, x0, x1, corre} (la fase depende de la distancia: los pies no patinan); `agacha`/`agacha_t`, `inclina`, `espaldas`, `mano_en` [x, y] (la mano va a un punto del mundo: asa de la escotilla), `objeto` caja/bolsa/móvil, `casco` + `linterna` + `haz` {largo, angulo, barre}, `tinte` (luz de sirena en el filo), `rebota` (risa).
- **Primer plano = la misma figura muy grande:** `fig(540, 2188, 1700, …)` (pies fuera del cuadro), cabeza de r ≈ 270 en y ≈ 760, lejos del HUD y de la franja.
- **Atrezo que identifica** (casco con linterna del vecino): en todos sus planos del presente; apagado de día en los flashbacks. Tabla de vestuario por plano en el plan.

## 3 · HUD fijo (firma de la serie)
En la EDL, `escenas.hud = {desde, hasta, dia: "DÍA 1", rotulo_cuenta: "IMPACTO EN", claves: [{t, hora, lugar, cuenta, roja}], ocultar: [{desde, hasta}]}`. El generador lo arma en `T["hud"]` y `T["hud_ocultar"]`.
- Arriba a la izquierda: punto rojo + «DÍA N», hora grande, lugar en gris espaciado (PISO 9 → ESCALERAS → SÓTANO → BÚNKER). Arriba a la derecha: cuenta atrás amarilla con resplandor.
- `cuenta` en segundos en el instante de la clave; baja 1 s por segundo real; **salta** en los cambios de lugar (nueva clave) y `roja: true` en el último tramo (ep. 1: en «ocho», 7:59). `cuenta: null` = aún no hay cuenta (aparece con la TV).
- Se esconde en los flashbacks (`ocultar` con los cuadros de entrada y salida).
- Nada del plano bajo el HUD que haya que leer: tapas, notas y números van fuera de y ≈ 0–380 (SP-21).

## 4 · UI de móvil en POV
- `movil` (SeriePov): bloqueo con hora, píldora «N ALERTAS» que cae con su palabra, alertas, notificación de mamá que cae con «mensaje». Con zoom progresivo la lista baja a la franja: **al caer la notificación, las alertas se apilan** («+N más») y el zoom final no pasa de 1.45 (SP-11).
- `chat` (SerieLugares): vibración, «escribiendo…» y burbuja. Burbuja en ≤ 3 líneas que quepan en su globo (#16) y zoom ≥ 1.4 para leerla.
- Todo el contenido recortado a la pantalla (`clipPath`, #30). **Tema oscuro** bajo la franja del subtítulo (SP-14): el chat claro del ep. 1 (#e5e2ea) lo aceptó el creador, pero no se repite.

## 5 · Cámara y transiciones
- Cámara por puntos: `punto(t, x, y, escala, curva)` (`suave`, `lineal`, `golpe` para el **punch-in** de 3–4 cuadros en un golpe: pl. 6 con la TV, pl. 15 con «de acero»). Empujes lentos, tilt y deriva; **sin sacudidas**.
- **Corte seco** = escena nueva con `fundido_cuadros: 0` (19 de 24 en el original). El corte cae `L = 0.03` s antes de su palabra; si lleva golpe a la altura de la voz, ≈ 0.6 s antes (SP-4).
- **Flash blanco** `efectos.flash` (d 0.15–0.35 s) y **encendido de TV** `tv_linea` (línea que se abre en 6 cuadros) en el corte a la TV.
- **Flashback sepia:** `efectos: {sepia: true, enfoca: {t, cuadros: 5 o 9, px: 24}}` + `ocultar` del HUD. El lugar se dibuja de día y el filtro lo vira; la sirena **no** se apaga en los flashbacks (medido).
- **Barrido** en los cambios de lugar con prisa: `trans={"tipo": "barrido", "dir": "izq"|"arriba", "cuadros": 6}`.
- Un plano no empieza vacío: cada cosa se queda hasta que entra la siguiente (#69).

## 6 · Subtítulos (modo serie)
`SUBS` del generador (copiar tal cual): Poppins ExtraBold 92 px, MAYÚSCULAS, blanco con la palabra que se dice en `#FFD21F` y resplandor 9 px, sombra, pop 0.4 → 1 en 2 cuadros, `y` **fija en 1460** (`y_por_tiempo: False`), ≤ 3 palabras, `pausa_corte_s` 0.3 (en las pausas desaparece), `enlaces_extra` con «cada», «se», «lo», «le», demostrativos, «su», «un», «una».
- Franja reservada **y 1385–1540** en todo el video (también POV y tarjeta). Lo que importa vive en y ≈ 300–1380.
- Se admiten bloques de una palabra (el original los usa), pero no una palabra de enlace sola con su coma: `SIN_COMA` (SP-13).
- Whisper junta palabras («Está a seis» → «Estás seis»): `PARTIR` antes de alinear con el guion. Comprobar 230/230 palabras contra el guion.
- **Objeto que nombra la voz = clave** desde su palabra: la cámara lo deja sobre y 1380 antes (SP-10).

## 7 · Varias voces (pista de diálogo)
Voces del ep. 1 (las genera el creador en ElevenLabs y las pega en `nichos/shorts/assets/audios/<slug>/`): narrador **David – Intense, Rapid, and Expressive** (`voz.mp3`), TV = David (`tv.mp3`), vecino **Murdock – Deep & commanding** (`vecino.mp3`), mamá **Kate 1 – Warm, Close and Natural** (`mama.mp3`).
1. **Transcribir cada archivo por separado** (whisper large-v3, palabra a palabra) y comparar cada uno con el guion. Si falta una palabra, se escala.
2. **`armar_dialogo.py [rN]`**: lista `TRAMOS` = (quién, archivo, inicio de habla, fin de habla, pausa ANTES) en el orden del guion. Cada voz se iguala a −18 LUFS con ganancia fija; cada tramo se corta con márgenes (`MARGEN_INI` 0.04, `MARGEN_FIN` 0.10) y fundidos de 15 ms; pausas del plan 0.3–0.7 s (0.7–1.4 tras los golpes de guion). Filtros: TV `highpass 300 + lowpass 3400 + acrusher` (altavoz), mamá `250–4500 Hz` (nota de voz). Sale `dialogo_rN.wav` + `dialogo_rN.json` (quién, origen, destino).
3. **Pausa antes del CTA** (creador: «para que la gente sienta y procese la pregunta»): el último tramo del narrador se parte en el **valle de energía** de `voz.mp3` (ep. 1: −73 dB a 50.10 s, con márgenes propios para no comerse el arranque de «Sígueme») y lleva `PAUSA_CTA` (ep. 1: 2.75 s). **Desde el 24-nov, regla fija en todos los episodios: `PAUSA_CTA = 3.0` s y después «Sígueme para la parte N» dicho** (creador: «siempre en todos los videos de este estilo, que la desicion dure 3 segundos igual y luego siganme para la siguiente parte»). Medido: 2.70 s entre palabras, 2.98 s de silencio de voz. Durante la pausa: los botones respiran, la cuenta roja baja y el ambiente sigue (con su caída del último segundo).
4. **Crudo sintético** con fondo `#272523` + `dialogo_rN.wav` + cola de la tarjeta → proyecto del architect: `ingesta` → `transcribir` → **sin cortes** (`keep` 0–fin y `transcripcion-base.json` con los tiempos de la transcripción; la propuesta automática se guarda en `cortes.auto.json`, SP-12) → `base --sin-encuadre` → `subtitulos --min-palabras 1 --max-palabras 3` → `director --sin-sfx` → `armar-edl` → `ajustar`.

## 8 · Sonido como el original (lo que sumerge en la historia)
Creador: «respete los tonos de audio del original» y «las alarmas son mas fuertes». **Cada nivel sale del original medido, nunca de una regla fija.**

**Ambiente** (`sfx_alerta.py` → una pista `ambiente.wav` desde el cuadro 0, sin música):
- **Sirena** = `sintesis-alerta-nuclear/sirena-dos-aullidos.wav` (local, dos aullidos que se cruzan en ≈ 700–1450 Hz, 5 s por vuelta; eco de ciudad al mezclar en `sirena()`). Continua y **sin agacharse con la voz**: ≈ 16 dB bajo la voz en las pausas, ≈ 6 dB más débil desde la puerta, fuera en la escalera. Dominante p5/p50/p95: original 609/949/1606 Hz, nuestra 621/932/1570.
- **Retumbo grave** 30–150 Hz todo el video (≈ 25 dB bajo la voz; escaleras 13.6, sótano con caldera 18.9, búnker con zumbido de bombilla 19–22 de fondo total). Tabla por tramo en `perfil.md` → Sonido.
- **Nota en La** (55/110/220 Hz) solo desde el CTA: −19.5 dB respecto a la voz, y la cola **baja** como en el original (−33 → −36 dBFS), no sube (SP-7).
- **Agachado mínimo por palabra** (`agachado_minimo`): solo si el pico de una palabra queda a < `MARGEN_MIN` = 10.5 dB del ambiente en el render, y lo justo.

**Cómo se mide (las trampas están en errores-serie-pov):**
- **Referencia = RMS de la voz en sus palabras** (original −13.9 dBFS, n = 219). Todo se expresa en dB frente a ese valor.
- **Fondo del original:** `medir_fondo.py <audio> <palabras|edl> [--voz stem] [--det] t0-t1 …`. En el original, con el detector (`--det`: tramas de 50 ms con 200–600 Hz bajo su mediana −18 dB y sin sibilantes > 4 kHz); en lo nuestro, con el stem (`--voz dialogo_rN.wav`). **Nunca en los huecos entre palabras de whisper**: meten sibilantes y tonos de alerta y dieron el falso «5 dB bajo la voz» (era ≈ 16, SP-2).
- **Nuestro sin voz = residuo:** `final.mp4 − dialogo_rN.wav` escalado por mínimos cuadrados (casa a 0 ms). Sobre el residuo se miden el timbre (centroide y dominante) y el nivel de cada SFX; con la voz encima, el centroide es el de la voz (el «5082 Hz» del botón A era la /s/ de «quedas»).
- **Ningún SFX tapa la voz:** margen por palabra **en 300–4000 Hz** (voz − residuo) sobre el mp4, con `qa/review_r1/medidas/negativas.py` (lista las palabras < 0 dB y los SFX que empiezan cerca) o `qa/review_r3/margen.py` (palabras elegidas). Meta: 0 palabras < 0 dB al inicio de frase y ninguna nueva respecto a la versión anterior. Un tono agudo corto (bip, botón) no cambia el RMS de banda entera pero tapa la consonante (SP-5). Falsos negativos por tiempos de whisper: si la voz está < −45 dBFS en la ventana, mirar el stem («te» 39.15 s: −17 dB falso; la «o» de 20 ms dura ≈ 140 ms).
- **SFX frente al original:** cada uno con su momento del original (`ORIGINAL` en `sfx_alerta.py`: segundo y banda; tabla de segundos en el informe §3) y `comparar_sfx.py --nuestro final.mp4 --edl … --sfx …`. **Ojo (SP-9, #91):** mide desde el inicio del archivo y la primera colocación de cada recorte. Para un SFX que se prepara antes del golpe (silbido 0.55 s antes del estallido) o un recorte que ya se usa para otra cosa, medir a mano en el golpe (`en` + desfase del pico) y en una ventana **sin voz** del original. Tabla por bandas (30–150, 150–1000, 1000–4000, 4000–12000 Hz) en el render-log.
- **Timbre:** un SFX grave en el original no lleva energía en 300 Hz–4 kHz; uno agudo no es grave (pop de cartel del original ≈ 5 kHz). Espectrogramas original / final / residuo del mismo momento (`showspectrumpic`, 30 Hz–8 kHz log).
- **Diseño ≠ render:** el render de Remotion sube el ambiente ≈ 2.7 dB frente a la voz (`RENDER_SUBE`); los recortes se normalizan a −16 dBFS de RMS activo (`RMS_RECORTE`) porque `ganancia_db` de la EDL no admite > 0 dB. Todo se vuelve a medir sobre el mp4.

**SFX puntuales:** diegéticos, a la altura de la voz como el original (tonos del móvil ≈ −2, mensaje −3, golpes graves de corte, puerta y escotilla 0…+7 en < 150 Hz). Densidad del original ≈ 0.29/s (≈ 25 golpes); el ep. 1 quedó en 70 colocaciones (aceptado por el creador, SP-8): lo que el original no tiene va bajo o fuera. **El golpe va antes de la palabra** (o en la pausa), nunca en la sílaba que abre una frase. Cada SFX tiene que **sonar a lo que se ve** (SP-6): la puerta, puño contra madera; el destello, silbido + estallido grave.
- Fuentes: catálogo primero (`CATALOGO.md`); síntesis local (sin gasto) para tonos, sirena, riser, zumbidos; ElevenLabs (`generar_sfx.py --lote … --si-gasto=N --key ELEVENLABS_API_KEY_3`) solo con gasto autorizado, saldo antes y después. **Nunca el tono EAS real** (853 + 960 Hz): la alarma de TV es propia (`alarma-tv.wav`).

## 9 · Tarjeta A/B final
- Escena `tarjeta` con `fondo` = el último lugar (oscurecido y desenfocado), `a`/`b` {t, lineas}, `cta` {t, lineas}, `respira` [desde, hasta] (los botones se alternan durante la pausa). Geometría `TARJETA`: botones 900×210 en y 760 y 1030, texto en 2 líneas a 62 px, CTA en y 1660 a 84 px.
- A aparece **antes** de la palabra que abre la pregunta (ep. 1: 0.17 s antes de «¿Te»), B con «corres». La tarjeta dura **4.0 s tras «parte dos»** (como el original). **Sin bucle.**
- Sonido: impacto de entrada, pop de cada botón, golpe del CTA y nota en La, todos al nivel del original (SP-7: el ep. 1 iba +3.7 y +2.9 dB en R1). Caída del fondo ≈ 1 s antes del CTA.
- Publicación: comentario fijado «Comenta A o B: la más votada decide la parte 2» (social-strategist). En la parte 2 el original abre con «PART 2 · LAST TIME…» y el sello «YOU VOTED: …» (`ideas/…stick-motion-recrear.md` §2, la otra parte): **pieza aún no construida**; si el plan la pide, se propone y se espera el ok.

## 10 · Flujo por episodio (meta ep. 2+: ≈ 0.9–1.3M sin ronda)
1. Leer: perfil + aprendizajes, `errores-serie-pov.md` entero, plan de escenas, `CATALOGO.md`, la parte del informe del original que toque. Nada de leer el render-log del ep. 1 entero.
2. **Reutilizar antes de construir:** `SeriePov.tsx`/`SerieLugares.tsx` (HUD, figuras, poses, notas, cuarto, recibidor, escaleras, sótano, búnker, mapa, chat, tarjeta, efectos); `armar_dialogo.py` (solo cambian `TRAMOS`, `PAUSA_CTA` y las rutas); `sfx_alerta.py` (ambiente, `RECORTES`, `ORIGINAL`, agachado mínimo); los SFX de `sintesis-alerta-nuclear/` y `elevenlabs-alerta-nuclear/`; `medir_fondo.py`, `comparar_sfx.py`, `medir_sfx_render.py`, `medir_visual.py`, `montar_prueba.py`, `empalmar_tramos.py`, `negativas.py`. **Los scripts llevan rutas y slug fijos** (`SLUG`, `DIALOGO`, `ORIG`, `P`/`EX` de `negativas.py`, que además lee `edicion-v2.render.json`): cámbialos al copiar. Al usarlos en un 2.º video, promover a `comun/` según `reutilizacion-materiales`. Si el plan pide > 5 piezas nuevas, avisar en el informe.
3. **Decidir antes del primer render:** voces, ambiente por tramo (medido en el original del episodio si lo hay) y densidad de SFX.
4. **Prueba de 10 s** (episodio nuevo): solo el tramo (`--frames=0-N`), audio del video entero (`--codec=wav`) y `montar_prueba.py --cuadros N --lra 2 --audio-entero`. Señal y parada hasta el ok.
5. **Paradas por bloque** (`revision-por-bloques.md`, 4/4) con hojas `qa/bloques/bN_a.jpg`; el generador sale con 1 si hay avisos.
6. **Render completo:** imagen `npx remotion render src/index.ts Reel salida/rN_imagen.mp4 --props=<edl.render.json> --muted --gl=angle --concurrency=4`, audio `--codec=wav` aparte, montaje con `montar_prueba.py --cuadros <total> --lra 2 --audio-entero`. **Uno detrás de otro**, nunca dos procesos pesados a la vez (SP-25). Antes de montar, `ffprobe` de cada pieza (un mp4 sin átomo moov = escrito a medias).
7. **Correcciones por tramos:** re-render solo de los cuadros que cambian (`--frames=a-b`) + `empalmar_tramos.py --base salida/rN_imagen.mp4 --tramo INICIO:archivo … --cuadros <total>` + audio entero renderizado aparte y `montar_prueba.py … --copiar-video`. Solo audio: render `--codec=wav` + `--copiar-video`. Después, diferencia por cuadro contra la versión anterior en **todo** el video (solo pueden cambiar los cuadros del encargo) y diff de `sfx_extra` contra la EDL **renderizada** antes (`*.render.json`, SP-24).
8. **Juntar los cambios del creador antes de lanzar una ronda** («¿algo más que cambiar?»): en el ep. 1 #5 y los sonidos llegaron con el editor ya lanzado y costaron una ronda más (≈ 280K).

## 11 · Comprobaciones antes del render (y antes de la señal)
- Generador `--solo-comprobar` con salida 0: comprobación 2D propia (`comprobar_2d`: textos enteros en cuadro o fuera del todo; claves fuera de y 1385–1540 mientras hay subtítulo; cada 2 cuadros, en cada punto de cámara y en el último cuadro de cada escena; cajas con tramo de tiempo opcional) + `comprobaciones_3d.py` (en `serie` todo es N/A salvo la continuidad entre escenas: anotarlo así). `REVISADOS` vacío al empezar.
- 230/230 palabras del guion en pantalla; sin puntuación doble (`[?!…]\.`).
- Hoja de cada bloque a 4 c/s y 10 c/s en flashes, barridos, entradas a flashback y tarjeta; recortes al 100 % de caras, notas y botones.
- Sonido sobre el mp4: fondo por tramo con el mismo detector que el original (± 2 dB) **hasta el último cuadro**, cola por bandas (55/110/220 Hz y 30–48 Hz), tabla de SFX por bandas en el golpe, margen por palabra en 300–4000 Hz, envolvente de la sirena p5–p95 ≤ 6 dB, pausa del CTA medida.
- `validar.ts` sin FAIL; ebur128 −14 ± 0.5 LUFS, LRA ≤ 2.5, pico ≤ −0.7 dBFS; ffprobe 1080×1920 30 fps.
- tsc limpio y `serie-pov.test.ts` en verde si se tocó código.
- `render-log.md`: tablas original-frente-a-nuestro, «Desvíos del plan» plano a plano, «Errores propios» (SP-N/#N), «errores-serie-pov: N/N revisados». `comprobar_catalogo.py` = «CATALOGO al día».

## 12 · Costes medidos (alerta-nuclear-ep1)
| Qué | Medido |
|---|---|
| Tokens del episodio 1 (primer video del estilo, 2 rondas) | ≈ 3.3M (previsto 1.8–2.5M) |
| Perfil + piezas + prueba de 10 s (editor) | 412K · remezcla de audio de la prueba 213K |
| Render completo pl. 6–25 con `SerieLugares.tsx` (editor) | 437K · revisión completa 310K |
| Ronda 1 (audio + pl. 24) | 232K · ronda 2 cortada ≈ 100K + retomar 178K · validación acotada 55K |
| Episodios siguientes (estimado, informe §5.5) | ≈ 0.9–1.3M sin ronda · ≈ 1.25–1.65M con una ronda |
| Render de imagen (`--gl=angle`, 4 núcleos) | prueba 356 cuadros ≈ 2 min · completo 2669 cuadros ≈ 6 min (≈ 0.13 s/cuadro) |
| Créditos ElevenLabs (SFX) | 80 (sirena de la prueba, luego sustituida por síntesis local) + 180 (9 tomas de puerta y destello, 6 usadas) |

## 13 · Lo que no se hace
- **Ninguna regla de monigotes** (ver arriba). Tampoco tope fijo de SFX bajo la voz ni ducking fijo: el nivel lo da el original.
- **Nunca `rm`** (ni `rm -f` dentro de un comando largo): dejó al editor 9 h parado esperando permiso. Vaciar un log: `: > archivo`; quitar algo: `mv` a `_papelera/`.
- No medir el fondo del original en los huecos de whisper ni el timbre con la voz encima.
- No añadir lo que el original no tiene (rótulos, gags, SFX a la altura de la voz) sin anotarlo como desvío.
- No reciclar un SFX del catálogo solo porque «es de puerta»: tiene que sonar a lo que se ve y parecerse al momento del original.
- No poner subtítulo blanco sobre una UI clara ni nada legible en la franja 1385–1540 o bajo el HUD.
- No tocar `SeriePov.tsx` ni lugares aprobados sin parámetros opcionales que dibujen igual por defecto.
- No sobrescribir `final.mp4` sin `final_rN.mp4`, ni la prueba que ve el creador (`prueba_10s_rN.mp4`).
- No gastar créditos sin autorización ni lanzar dos renders pesados a la vez.
