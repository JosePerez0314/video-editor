---
name: animacion-monigotes-3d
description: Cómo se anima el formato 2D dentro de 3D (estilo-monigotes-3d, @resultaaquee de noviembre): monigotes billboard en sets 3D de CSS (`Set3d`), cámara 3D por claves que nunca para, golpes con desenfoque de la velocidad de la cámara, figuras en primer término en 2D (`delante`), sets genéricos por lugar, comprobaciones de bordes, obstáculos y franja, coste medido y errores conocidos. Para el formato plano usa `animacion-monigotes`.
---

# Animación de monigotes 3D (2D dentro de 3D)

**Perfil que manda:** `tools/architect/estilo/estilos/estilo-monigotes-3d/perfil.md` y su `aprendizajes.md` (24 errores ya cometidos). Esta skill explica **cómo se hace**. No mezcles este formato con `estilo-monigotes` (creador, 2026-11-11): monigote, subtítulos, voz y SFX se comparten; la imagen, la cámara y las comprobaciones son las de aquí.

**Video de referencia:** `nichos/shorts/exports/cajeros-loteria/` (generador `escenas_cajeros-loteria.py`, SFX `sfx_cajeros.py`, EDL `tools/architect/proyectos/2026-11-11-cajeros-loteria-r1/edicion-v3.json`). Cópialo como plantilla.

## 1 · Piezas (todas en `tools/architect/src/reel/escenas/`)
| Pieza | Archivo | Para qué |
|---|---|---|
| Capa 3D | `Set3d.tsx` | Contenedor `Set3d` (perspectiva CSS + mundo `preserve-3d`), cámara (`camaraEn`, `proyectar`, `focal`), `Plano` en teselas (`unaCara`), `Suelo`, `ParedLado` (`mira`), `ParedFondo`, `Caja3D` (`tesela`, 256 por defecto), `PlanoTumbado`, `Cuadro`, `PuertaBisagra` (`dorso`), `Billboard` (en teselas de 256; `desborde`: las del borde se alargan hacia fuera para lo que el dibujo pinta fuera de su caja), `MonigoteSet` (`tras`), `FigurasDelante` (de lejos a cerca, `ordenDelante`), `fila`, `Sobre2d`, `TEXTURAS`. Mundo: x derecha, y arriba (0 = suelo), z hacia el fondo. |
| Fotos sin render | `herramientas/fotos.ts` | `npx tsx herramientas/fotos.ts <edl> <hoja.jpg> --escala 0.75 --ancho 360 --cols 6 t1 t2@x:y:w:h …`: un bundle, cuadros sueltos y recortes al 100 % en una hoja (`angle` por defecto). Para iterar y para las comprobaciones. |
| Texto de cartel | `comun/Rotulo.tsx` | `maxAncho`: la letra se encoge hasta caber (`tamQueCabe`). Úsalo en todo cartel nuevo. |
| Escena del Reel | `Escena3d.tsx` + rama `set3d` de `CapaEscenas.tsx` | `tipo: set3d` en la EDL: registro de sets, figuras, atrezo, luces; desenfoque, transición, sacudida, viñeta y **burbuja** aplicados desde fuera. |
| Sets por lugar | `SetTienda.tsx`, `SetSalaEspera.tsx`, `SetVentanilla.tsx`, `SetCuarto.tsx`, `SetDespacho.tsx`, `SetExteriores.tsx` (carretera, mar), base `SetHabitacion.tsx` | Cada uno con su objeto de medidas (`TIENDA`, `SALA_ESPERA`…), `omitir` por grupos y textos/colores por props. **Antes de crear uno, adapta uno de estos** (CATALOGO). |
| Atrezo genérico | `Atrezo3d.tsx` | Lector, campanilla, papelera, cartera, reloj, pecera, sillas, cama, mesa, taquillas, impresora, cartel, foto, coche, yate, mansión, botón; en 2D: destello, gota, fuegos, brazo de palo, cuad (luz, cristal). |
| Atrezo del video | `Piezas<Video>.tsx` | Solo lo exclusivo (en cajeros: rasca, pantallita, columnas del corcho). |
| Personajes | `Monigote.tsx` | El mismo monigote del formato plano. Poses nuevas (p. ej. `sentado`) van aquí. |

## 2 · Generador (`escenas_<slug>.py --edl <edicion-vN.json>`)
Copia `escenas_cajeros-loteria.py`. Además de `Palabras`, `retocar_palabras`, `T` y la lista `Y` de subtítulos (igual que en el plano):
- **Cámara por claves 3D:** `mira(t, pos, objetivo, fov, curva, en)` deja el objetivo en el punto de pantalla `en`; `deriva(c, t, dz)` avanza la cámara por su eje (deriva lineal: **nunca quieta**); `curva: 'golpe'` = golpe de 6 cuadros (empieza 2 cuadros antes de la palabra, `g1(t)`). Patrón por plano: `[golpe, deriva] × n`.
- **Escena:** `esc3d(id, desde, hasta, set, camara, figuras, atrezo, trans, impactos, vineta, **params)`; `fig(id, quien, x, z, escala, claves, **extra)` con `y`, `espaldas`, `anda`, `desde`/`hasta`, `capa='delante'`, `giro_fijo`, `inclina` + `pivote`, `silueta`, `aspecto`, `tras={"y", "z"}` (canto del mostrador que la tapa: la figura no se dibuja por debajo).
- **Subtítulos (R2):** `SUBS_CENTRO` con `y_por_tiempo: True` (la franja cambia en el corte), `enlaces_extra`, `max_palabras_total: 3`, `min_bloque_s: 0.134`; puntuación copiada del guion palabra a palabra. La franja se elige **por plano** según lo que haya debajo, y el generador comprueba los puntos clave de cada plano (caras, objeto nombrado, carteles). Comprobación de bloques: `exports/cajeros-loteria/qa/r2_frames/medidas/bloques.ts <edl>` (marca CRUZA, CORTO, >3 PALABRAS, ENLACE SOLO).
- **Coordenadas del set** como constantes del generador (las mismas del `.tsx`), y `OBSTACULOS` / `RECINTO` por set.
- **Bucle:** `camara_cuadro0(t)` es la misma clave al principio y al final; el estado del set en la cola repite el del cuadro 0 (pose, atrezo, fase de las animaciones: p. ej. láser con inicio `dur − 2·D/3`).
- **Comprobaciones (sin avisos antes de renderizar):**
  1. `comprobar(nombre, cam, puntos, y_sub)`: puntos clave dentro de cuadro y fuera de la franja; carteles enteros en x 135–945 (sus dos bordes como puntos), en la primera y la última clave de cada empuje.
  2. `comprobar_bordes(E)`: ningún billboard (figura **o atrezo grande**: `ATREZO_BB`, yate, mansión, coche, botón, pecera) cruza un borde lateral. Si lo hace: reencuadre, `capa: 'delante'`, o — solo tras mirarlo a ≥ 4 cuadros/s y al 100 % — anótalo en `REVISADOS`.
  3. `comprobar_obstaculos(E)`: la cámara, cuadro a cuadro, fuera de las cajas del set (+140) y dentro de las paredes (si se quita el techo o la pared del fondo, se abre ese lado).
  4. `comprobar_carteles(E)` (R3): cada cartel de la lista `CARTELES` del set (banda y texto), en todas las claves de cámara y a mitad de cada deriva: entero (banda sin cortar, texto en x 135–945) o fuera del todo. Registra ahí todo cartel con texto de un set nuevo.
  5. Continuidad: cada escena empieza donde acaba la anterior.

## 3 · Cómo se ve (resumen del perfil)
- Todo en sets 3D; un set por lugar; cambio de encuadre cada 1–1.5 s, de sitio cada 2–4 s; barrido de 8 cuadros entre sitios, corte seco en los giros, zoom a través de 6 cuadros, burbuja para «en su cabeza». Sin fundidos.
- Primeros planos acercando la cámara (fov 34–40); planos generales fov 50–58; cenitales con cabeceo 86–89° y `omitir: ['techo']`.
- Figuras de frente a la cámara; de espaldas en primer término con `capa: 'delante'`; tumbadas con `giro_fijo: 0`, `inclina` 90 y `pivote` en la cadera (210); sentadas con la pose `sentado` o la clave `sentado`.
- Subtítulos: ABAJO 1380 / ARRIBA 950; cambian en cortes o golpes.

## 4 · Trampas del CSS 3D (cada una costó un error)
0. **Render y fotos siempre con `--gl=angle`** (`remotion.config.ts` ya lo fija). Con el OpenGL por defecto, Chrome recorta mal toda capa en perspectiva que cruza el borde del cuadro: figuras y atrezo rebanados por una vertical, tapas con franjas sin pintar. Es la causa de casi todos los fallos de cajeros R1.
1. Dentro del set, nada de `filter`, `opacity`, `mix-blend-mode`, `overflow`, `clip-path`, `mask`. Desenfoque, viñeta, transiciones y burbuja, fuera; luces y cristales, en `Sobre2d`. Un fondo `rgba` sí vale.
2. Planos en teselas (1024; laterales 256; suelos exteriores 2048–3000). Planos transparentes grandes, mejor no.
3. **Billboards grandes que salen del cuadro:** sin `angle` se recortan en una franja rectangular o desaparecen (ahora van en teselas de 256 como red de seguridad). Primer término y figuras enormes → `capa: 'delante'` (solo si nada del set queda delante de ellas).
8. **Nada apoyado exactamente en un plano** (pie de un billboard en y 0 sobre el suelo): súbelo unas unidades (coche: 12).
9. **Puertas abiertas:** lo que se ve detrás (pasillo) cerrado con suelo, techo, paredes y fondo; hoja con `dorso` para que el cartel no salga en espejo.
10. **Figura detrás de un mueble:** `tras` con el canto del mueble.
4. Claves con `null` en la EDL rompen la visibilidad (`t < null` es falso): quita la clave.
5. Lejos y grande → `nitidez: 1`; mundos exteriores acotados (≈ 12 000 × 15 000) con el cielo como degradado del `fondo` del Set3d.
6. Paredes partidas por un hueco: `origen` de textura. Pared derecha: `mira: -1`.
7. Travelling que acompaña a algo que hay que leer (coche, rótulo): `desenfoque_movimiento: false` en esa escena.

## 5 · Sonido
Igual que el formato plano (`sfx_<slug>.py` con `RECORTES` del catálogo y `colocaciones(E)` que leen los tiempos de la EDL: `puerta_frente`, `suena`, `saltan`, `cierra`, `pulsa`, `horas`, `columnas`, `desde` de las figuras, golpes de cámara). Barridos con whoosh (no todos), ráfaga al entrar en un sitio, cola con `whoosh-pasa` invertido. Densidad del proyecto (cajeros: 0.774 ev/s con 48 colocaciones; lo (–) del plan se quita primero). Diseño a 14 dB bajo la voz; real ≥ 10 dB medido sobre el mp4.

## 6 · Coste medido (4 núcleos, 1440×2560)
- **Con `--gl=angle` (R2): ≈ 0.15–0.19 s/cuadro.** Cajeros R2 completo (1860 cuadros): imagen 5 min 53 s, audio 2 min, montaje 1.5 min. Fotos sueltas con `fotos.ts`: ≈ 1.5 s/cuadro con el empaquetado. Lo de abajo es sin angle.
- Prueba de 5 s: 0.62 s/cuadro + 9 s fijos. Prueba de 10 s: 0.63 s/cuadro.
- Video completo cajeros R1 (62 s, 1860 cuadros, 21 escenas): **22 min 51 s de imagen (0.74 s/cuadro)** + ≈ 3 min de audio + ≈ 3 min de montaje. La burbuja (dos sets a la vez) es el tramo más lento. Una corrección en la cola: re-render solo de esos cuadros (`--frames=a-b`) y empalme.
- Iterar con `remotion still` en lote (un solo bundle, escala 0.25–0.3) y una hoja de contacto: ≈ 1.7 s por cuadro suelto; 56 cuadros ≈ 1.5 min.
- Trabajo (cajeros): 7 sets + atrezo genérico + generador completo ≈ un encargo largo; con los sets ya hechos, un video nuevo en sitios parecidos es sobre todo generador.

## 7 · Errores encontrados y cómo se evitan
| Error | Dónde | Cómo se evita |
|---|---|---|
| Cabeza «rectangular» y cuerpo rebanado de un billboard en primer término | prueba 10 s, 7.5–9.5 s | `capa: 'delante'` + `comprobar_bordes` |
| Figura enorme invisible | R1, primer plano de la placa | `capa: 'delante'` desde que pasa la puerta |
| Figura cortada arriba en el cuadro 0 | prueba 10 s | encuadre del cuadro 0 que se lea; mismo encuadre al final |
| Cámara atravesando una lámpara | prueba 10 s, «y se va» | rutas por fuera de los objetos + `comprobar_obstaculos` |
| Peinado que confunde el género | prueba 10 s | pelo coherente con el guion («el cajero» → corto) |
| Figura invisible por `hasta: null` | R1 | quitar la clave |
| Techo tapando el cenital | R1 (generador) | `omitir: ['techo']` |
| Carteles grandes que no caben en x 135–945 | R1 (generador) | carteles más pequeños o plano general para leerlos |
| Coche borroso en el travelling | R1 | sin desenfoque de movimiento en esa escena |
| Rejilla final visible solo 0.2 s | R1 | mover el corte siguiente a la palabra siguiente («agentes») |
| Yate, coche, señora y silueta rebanados por una vertical; foto del cartel desaparecida | R1 (review #1–#5) | `--gl=angle` (causa raíz) + billboards en teselas de 256 |
| Franja sin pintar en la tapa de la repisa (parecía que la señora atravesaba el mostrador) | R1 (review #3) | `angle` + `Caja3D` en teselas de 256; `tras` en la figura |
| Ruedas cortadas en horizontal y franja del camino sobre el coche | R1 (review #2) | pie del billboard 12 por encima del suelo |
| Barra del color de fondo por la puerta abierta y rendija oscura junto a la bisagra | R1 (review #6) | pasillo cerrado (suelo, techo, paredes) en teselas de 256 |
| Cartel de la puerta en espejo al abrirse | R1 (review #10) | `PuertaBisagra` con `dorso` |
| Texto más ancho que su cartel | R1 (review #9) | `Rotulo` con `maxAncho` |
| Subtítulo que cruza un corte en la franja del plano anterior | R1 (review #7) | `y_por_tiempo: true` |
| Subtítulo sobre la cara del agente, el yate, la mansión, el rasca del cuadro 0 | R1 (review #8 + repaso R2) | franja por plano + puntos clave por plano en el generador |
| Bloques «sospechoso Así», «hasta» suelto, 4 palabras | R1 (review #11) | puntuación del guion + `enlaces_extra`, `max_palabras_total`, `min_bloque_s` |
| `REVISADOS` silenciando a quien estaba mal | R1 (review #13) | solo tras mirar a ≥ 4 c/s y al 100 % |
| Personaje medio fuera del plano abierto | R1 (repaso R2, 38 s) | plano más abierto y centrado; puntos de manos y pies en `comprobar` |
| Mano que entra en la pantallita cortada en rectángulo (lo que el dibujo pinta fuera de su caja) | R2 (review #14, regresión de las teselas) | `Billboard` alarga las teselas del borde (`desborde`, por defecto el lado mayor); con `tras`, margen 0 abajo; validar cada cambio de capa con diferencia por bloques contra la versión anterior |
| Figura lejana pintada encima de lo que lleva en la mano una figura cercana (capa 2D) | R2 (review #15) | `FigurasDelante` pinta de lejos a cerca (`ordenDelante`) |
| Cartel cortado por el borde tras reencuadrar («ESTROS GANADORES», «TO…») | R2 (review #16) | `CARTELES` por set + `comprobar_carteles(E)` en todas las claves y derivas: entero (texto en x 135–945) o fuera del todo |

## 8 · Lista de comprobación (además de la de `edicion-escenas.md`)
- Generador sin avisos (franja, carteles, bordes, obstáculos, continuidad).
- Render y fotos con `--gl=angle`.
- Hoja de cuadros **a ≥ 4 cuadros/s** y recortes al 100 % de todo lo que toca un borde: ¿algún billboard o atrezo recortado o desaparecido? ¿Algún hueco del color de fondo o franja sin pintar en suelos, tapas o paredes? ¿Algo se ve a través de un mostrador? ¿Textos en espejo o más anchos que su cartel? ¿La cámara pasa por dentro de algo?
- Bloques de subtítulo (`bloques.ts`): sin CRUZA, CORTO, >3 PALABRAS ni ENLACE SOLO; puntuación igual al guion.
- ¿El último cuadro coincide con el primero (misma cámara, mismo estado)?
- `validar.ts` sin FAIL; ebur128 y ffprobe en spec; SFX medidos sobre el mp4.
- `comprobar_catalogo.py` = «CATALOGO al día».
