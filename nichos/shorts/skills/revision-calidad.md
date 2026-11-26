---
name: revision-calidad
description: Las 30 comprobaciones medibles del shorts-quality-reviewer (cada una sale de un error real del editor) y cómo atribuir cada hallazgo.
---

# Revisión de calidad de un short

## Lista de comprobación (sale de errores reales del editor; aplícala entera)
**Además (creador, 2026-11-12):** recorre `nichos/shorts/skills/errores-edicion.md` (errores ya cometidos, con su severidad). Un error de esa lista que se repite sube un nivel y se marca «repetido: #N».

Severidad sugerida entre corchetes. Usa la EDL para saber en qué segundo se dice cada palabra.

**A · Specs** — `ffprobe` y `ebur128` literales.
1. 1080×1920, 30 fps, h264 + aac, duración 20–90 s. [CRITICAL si falla]
2. I = −14 ± 0.5 LUFS, LRA ≤ 2.5 LU, Peak ≤ −0.7 dBFS. [MAJOR]

**B · Audio y texto**
3. La voz es la del creador (`assets/audios/<slug>/voz*.mp3`) sin regenerar ni acelerar: duración del habla ≈ duración del mp3; transcribe o compara palabras con `guion-voz.md` en orden. Falta o sobra una palabra. [CRITICAL]
4. Ningún dato en pantalla sin fuente; ninguna `[hipótesis:]` sin cerrar del concepto. [CRITICAL]

**C · Sincronía**
5. Cada escena entra en la palabra que la nombra: toma 6–8 pares palabra → escena (cuadro a ese segundo y 0.5 s después). Desfase > 0.5 s. [MAJOR] (error real: storyboard con ritmo estimado y TTS más rápido → todo desfasado).
6. Subtítulos sincronizados: p95 del desfase ≤ 0.1 s (`qa.ts` o medición propia). [MAJOR]

**D · Qué se ve**
7. Sin pantalla vacía ni cuadro negro (hoja cada 1 s; busca cuadros casi uniformes). [MAJOR]
8. Sin un emoji o icono por palabra, sin formas geométricas apiladas fingiendo caras u órganos, sin texto plano como visual principal, sin iconos de relleno que no se están diciendo. [MAJOR] (rechazos del creador en R1–R4).
9. Los gráficos son del tema (ondas, sonido, personas), no estadística genérica (barras, cuadrículas). [MINOR]
10. Los mecanismos se muestran por partes, cada una en su momento. [MINOR]

10b. **3D (pudding-millas, 2026-11-13; se le escaparon al reviewer y los vio el creador):** cada figura junto a un vehículo o mueble se lee claramente delante, detrás o al lado (nunca «metida dentro»), y nada del set la cruza ni le sale de la cabeza (errores #29); todo marco con forma (ventanilla, pantalla, espejo) recorta su contenido (#30). Recórtalos al 100 %. [MAJOR / MINOR]
10c. Todo texto de atrezo, también el que está tumbado en mesas o suelos, se lee entero en cada plano (#31); el texto que sostiene un personaje se lee hasta el último cuadro (#33). [MAJOR si es repetido]

**E · Ritmo y transiciones**
11. Ningún tramo > 3 s sin cambio visible (mide con `ffmpeg … select='gt(scene,0.02)'` o compara cuadros cada 0.5 s), salvo un gráfico construyéndose. [MAJOR]
12. No hay cortes donde no cambia lo que se muestra (dos planos seguidos de la misma escena separados por corte). [MINOR] (rechazo del creador en R6).
13. Transiciones = fundido corto sin efectos ni bajón a negro: en cada cambio, el brillo medio no cae a ~0 (`signalstats` YAVG). [MAJOR] (rechazo en R6: «demasiado bruscas»).

**F · Subtítulos y legibilidad**
14. Estilo «selección» del perfil (Figtree, palabra por palabra, gris/blanco, recuadro azul en la clave). [MAJOR si es otro estilo]
15. Ningún subtítulo tapa un gráfico, etiqueta, UI de móvil o chat: cuadros a resolución completa de cada toma con gráficos. [MAJOR] (rechazo en R8).
16. Ninguna etiqueta se solapa con otra ni se sale del cuadro (zona segura x 135–945). [MINOR]
17. Las frases no terminan en palabra de enlace ni dejan 1–2 palabras colgando. [MINOR]

**G · Final**
18. Hay ≥ 1 s después de la última palabra (no corta en seco). [MAJOR] (rechazo en R8: «acaba muy brusco»).
19. Bucle: SSIM entre el primer y el último cuadro ≥ 0.95 (`ffmpeg -i final.mp4 … ssim`), sin subtítulos ni etiquetas en el último. [MINOR si el plan pide bucle]
20. Sin fundido a negro al final (rompe el bucle). [MINOR]

**H · Contrato con el plan y el concepto**
21. Hook en los primeros 3 s con la acción del concepto; CTA presente; giro (~70 %) presente. [MAJOR si falta uno]
22. Cada escena del `escenas.md` aprobado está en el video, en su orden. Escena cambiada sin aprobación. [MAJOR, atribución ejecución]

## Según el estilo del proyecto
El proyecto dice qué estilo usa (`project-log.md`, `escenas.md`). Con **`estilo-monigotes`**, las comprobaciones 13, 14 y 15 se miden contra su `perfil.md`:
- **13:** golpes y barridos con desenfoque, cortes secos solo en golpes de guion. No se exigen fundidos.
- **14:** `subtitulos_centro`: 1–2 palabras, Archivo Black, contorno negro, fijos en y ≈ 1350, sin recuadro.
- **15:** franja y 1300–1400 libre.
Además, no se exigen capítulos ni cabecera de fuente.

Con **`estilo-monigotes-3d`** (2D dentro de sets 3D; perfil `tools/architect/estilo/estilos/estilo-monigotes-3d/`, skill `animacion-monigotes-3d.md`), 13–15 se miden contra **su** perfil (cámara que nunca para, desenfoque de barrido hasta 22 px, subtítulo arriba/abajo por plano), y además:
- **3D-a:** ningún monigote recortado, rebanado por un corte vertical, con la cabeza «rectangular» o que desaparece. Revisa a ≥ 4 cuadros/s los planos con figuras cerca de la cámara o saliendo por un borde (error real: cajeros-loteria, prueba de 10 s, 7.5–9.5 s; y R1, primer plano de la placa). [MAJOR]
- **3D-b:** sin huecos del color de fondo en suelos ni paredes, y la cámara no atraviesa objetos (lámparas, paredes). [MAJOR]
- **3D-c · Comprobación automática común (creador, 2026-11-20):** el reviewer corre el **mismo** script que el editor sobre la EDL final y adjunta su salida: `python3 escenas_<slug>.py --edl <edl> --solo-comprobar` (o, en generadores antiguos, `python3 tools/architect/biblioteca/reutilizables/comun/comprobaciones_3d.py --edl <edl final> --generador nichos/shorts/exports/<slug>/escenas_<slug>.py --salida nichos/shorts/exports/<slug>/qa/comprobaciones.txt`). Aviso abierto = hallazgo con su #N y la severidad de `errores-edicion.md`. Los ACEPTADO se miran una vez. **Lo que el script cubre (#3, #4, #5, #10, #15, #29, #31, #32, #33, #48, #53, #65) no se vuelve a buscar cuadro a cuadro**; la revisión a ojo se centra en lo que el script no mide (lista «no automatizado» en la cabecera del módulo: oclusiones #55/#59, canto inclinado con cámara girada, figuras en sofá, piezas con «texto sin comprobar»). Un ✓ a ojo en #5, #29 o #48 solo vale con recorte al 100 % o medida en px. [MAJOR si hay aviso abierto]

**I · Sonido y texto en pantalla** (salen de hedy-lamarr-wifi R2, 2026-11-02; se aplican siempre que el estilo lleve SFX)
23. Hay efectos de sonido diegéticos de lo que pasa en pantalla y no hay música (si el perfil lo pide). Densidad audible de 0.3–0.4/s. Un video «solo voz» es MAJOR (corrección del creador). [MAJOR]
24. Sincronía de SFX a ±1 cuadro con su objeto: flash, sello, teclas, saltos… Compara el inicio de cada evento con el cuadro en que el objeto aparece o golpea. [MINOR; MAJOR si son varios]
25. Ningún SFX enmascara la voz: ≥ 10 dB bajo el pico de voz dentro de cada sílaba, **medido sobre el mp4** (el render sube los SFX 2–4 dB respecto al diseño; scripts en `exports/hedy-lamarr-wifi/qa/review_r3/medidas/`). **Y ningún objeto importante queda mudo** por una regla que no venga de las refs o del creador (error real: «ningún SFX sobre palabra clave»). [MAJOR]
26. Cada rótulo y cartel cumple la lista «No decir» del concepto, igual que la voz (error real: «= 88 FRECUENCIAS» sin «hasta»). [MINOR; CRITICAL si es un dato falso]
27. Ningún cartel cortado por el encuadre ni tapado por un personaje, medido en el cuadro final de cada empuje de cámara. [MINOR]
28. Bloques de subtítulo: ninguno es una sola palabra de enlace («Su», «Si», «En», «Ni»…) ni termina en una («Pero tus»). [MINOR]
29. Empalmes de voz (`voz-v2.mp3`…): sin clic (salto entre muestras en el corte frente al p99.9 de la voz) y nivel ±1 dB. Que suene natural lo confirma el creador. [MAJOR si hay clic]
30. Licencia de voz y SFX: la gestiona el creador (2026-11-03); no se anota ni se escala. [no aplica]

## Errores del video (siempre, creador 2026-11-13)
Al final de cada `review.md`: todos los hallazgos con `#N repetido` / `NUEVO`, y `errores-edicion.md` actualizado (nuevos como fila; repetidos con «Evitar» más concreto). Ver «Cómo se alimenta esta lista» en esa skill.

## Atribución
- **Concepto** (strategist): la idea o el dato fallan aunque se ejecuten bien.
- **Plan** (creative-producer): el guion o el plan de escenas piden algo que contradice el perfil o no se entiende.
- **Director** (executive-producer): el encargo al especialista metió una regla que no sale del creador ni de las refs (caso real: «ningún SFX sobre palabra clave»). Atribúyelo así, aunque el editor la ejecutara bien.
- **Ejecución** (video-editor): el plan era correcto y el video no lo cumple. Es la atribución por defecto de los puntos C, D, E, F y G.

