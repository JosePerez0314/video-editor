---
name: edicion-escenas
description: Cómo edita el shorts-video-editor: entorno (Node 24, whisper), pipeline modo solo-audio del architect, piezas de dibujo disponibles, reglas aprendidas con el creador y lista de comprobación visual.
---

# Edición con escenas (architect / Remotion)

## Entorno (comprobado en Linux, 2026-10-27)

- **Node 24** obligatorio para el architect: `source ~/.nvm/nvm.sh && nvm use 24 >/dev/null && npx tsx …` en cada llamada (el Node por defecto es 20).
- Whisper ya configurado por `.claude/settings.json` → `env` (`EDITOR_WHISPER_CLI`, `EDITOR_VAD_CLI`). Modelo large-v3 en `~/.cache/video-editor/modelos/`.
- Herramientas excluidas del sandbox del architect (`transcribir`, `render`, `qa`, `editar`, `cara`) van **solas** en su llamada Bash.
- `npx remotion render|still … --concurrency` ≤ 4 (la máquina tiene 4 núcleos). Para prototipos: `npx remotion still src/index.ts Reel <png> --props=<edl> --frame=N --scale=0.35` y borradores `npx remotion render … --scale=0.3`.
- Permisos: el proyecto tiene una allowlist en `.claude/settings.json`; **no hace falta modo bypass** y nunca trabajes en modo plan (bloquea toda escritura).

## Qué estilo usa el proyecto (léelo primero)
El canal tiene **tres estilos**, en `tools/architect/estilo/estilos/`. El proyecto dice cuál usa en `project-log.md` y en el `escenas.md`; si no lo dice, pregunta al director.
- **`estilo-gabriel`** (voz-grabada): escenas de noche, fundidos de 0.4 s, subtítulos «selección» arriba. Las reglas 1–18 de abajo están escritas para este estilo.
- **`estilo-monigotes`** (hedy-lamarr-wifi, refs de @resultaaquee): monigotes, golpes de cámara con desenfoque cada 1–1.5 s, `subtitulos_centro` que se mueven por plano (ABAJO y≈1380, ARRIBA y≈950 en planos abiertos; cambian solo en los cortes) y **efectos de sonido diegéticos sin música**. Su `perfil.md` gana sobre las reglas 6–11 de abajo. Lee también su `aprendizajes.md` (los 9 errores ya cometidos). Cómo se anima: skill `animacion-monigotes.md`.
- **`estilo-monigotes-3d`** (cajeros-loteria, refs de @resultaaquee de noviembre): monigotes 2D dentro de sets 3D (`set3d`), cámara 3D que nunca para, figuras en primer término en 2D (`delante`). **Va aparte de `estilo-monigotes`** (creador, 2026-11-11). Perfil `estilo-monigotes-3d/perfil.md` + `aprendizajes.md`; cómo se anima: skill `animacion-monigotes-3d.md`.
- **Antes de entregar** (cualquier estilo de monigotes): recorre `nichos/shorts/skills/errores-edicion.md` y anota en `render-log.md` «errores-edicion: N/N revisados» (creador, 2026-11-12).

## Pipeline modo solo-audio (explainer sin crudo)

1. **Crudo sintético:** `ffmpeg -f lavfi -i color=c=0x272523:s=1080x1920:r=30 -i <voz> -shortest -c:v libx264 -c:a aac crudo_rN.mp4`.
2. **Proyecto architect** (slug `<fecha>-<slug>-rN`, estilo `estilo-gabriel`, control total): `ingesta` → `transcribir` → `cortes --velocidad 1` sin quitar nada → `base` → `subtitulos` → `director` → `armar-edl`. Omite `cara` y `encuadre`. Palabras mal transcritas → `biblioteca/vocabulario.json` → `correcciones` y re-transcribir.
3. **Edición nueva** con `ajustar.ts --desde N` (nunca sobrescribas una `edicion-vN.json`). `inserts: []`.
4. **Generador de escenas** `escenas_<slug>.py --edl <edicion>`: escribe en la EDL `escenas`, `ilustracion` (solo etiquetas sueltas) y `subtitulos_seleccion`, y fija `duracion_s` = última palabra + 1.2 s.
5. **Prototipo** (stills) → ok del creador → **render** `npx tsx herramientas/render.ts <proyecto> --version N`.
6. **Entrega**: respaldar `final.mp4` → `final_r(N-1).mp4`; escalar a 1080×1920 con el audio del render y fundido de audio 0.3 s al final (nunca fundido de imagen: rompe el bucle).
7. **Verificar** (ffprobe, ebur128, hoja, cuadros) y documentar.

Talking-head: pipeline completo de `/editar` del architect (4 checkpoints con el creador), y las mismas reglas de ritmo, subtítulos y final.

## Herramientas de dibujo disponibles (no inventes otras sin ok)

- Capa `escenas` (`src/estilo/escenas.ts`, `src/reel/escenas/`): `cuarto` (cuarto de noche + personajes con poses `reposo|grabando|escuchando|mirando`, expresiones `neutra|mueca|sorpresa|duda|sonrisa`, colores, espejo, `ondas` de sonido), `cabeza` (corte de perfil: aire/hueso, cerebro, anticipo, pulso, hueso apagado/rojo), `oido` (canal, tímpano, huesecillos, cóclea, atajo), `ondas` (suma/resta/comparar), `vida` (personaje en tres edades), `movil`, `chat`, más `espectro`/`anos` (estadística genérica: **evitar**). Cámara por `puntos`, `fundido_cuadros`, capítulos y cabecera de fuente.
- Capa `ilustracion`: etiquetas, retículas, flechas, líneas, paneles. Úsala solo para etiquetas puntuales (CTA, «NO ES PSICOLÓGICO»), no como visual principal.
- `subtitulos_seleccion` (`src/estilo/subtitulos-seleccion.ts`).
- **estilo-monigotes:** `subtitulos_centro` (`src/estilo/subtitulos-centro.ts`, `SubtitulosCentro.tsx`); cámara `curva: suave|lineal|golpe`, `desenfoque_movimiento`, `impactos`, `fundido_cuadros: 0` = corte seco; `Monigote.tsx` (reparto hedy, antheil, oficial, espectador, jefe, empleado; 8 expresiones y 8 poses); escenas `escenario` (`Escenario.tsx`, `EscenariosHedy.tsx`). Generador de ejemplo: `nichos/shorts/exports/hedy-lamarr-wifi/escenas_hedy-lamarr-wifi.py`.
- **SFX:** campo `sfx_extra` de la EDL; biblioteca `tools/architect/biblioteca/sfx/` (skill `tools/architect/.claude/skills/sfx/SKILL.md`), síntesis `herramientas/sfx/sintesis.ts`. Script de ejemplo que coloca y comprueba: `nichos/shorts/exports/hedy-lamarr-wifi/sfx_r3.py`.
- Una pieza nueva se programa en `src/reel/escenas/`, se registra en `src/estilo/escenas.ts`, lleva prueba en `pruebas/unit/` y se documenta en el perfil del estilo.

## Reglas aprendidas (cada una salió de un rechazo del creador)

**Visuales**
1. **Contar con un mundo, no con un objeto por palabra.** Personaje en su escenario + cortes tipo esquema + gráficos del tema + UI (móvil, chat). Prohibido: un emoji/icono por palabra, formas geométricas apiladas para fingir caras u órganos, texto plano como visual principal, pantalla vacía, iconos de relleno que no se están diciendo.
2. **Cada visual dice literalmente lo que dice la voz en ese momento** y entra en esa palabra.
3. **Mecanismos por partes**: cada pieza del mecanismo con su momento (ej. aire: boca → rebote → canal → tímpano → cóclea; hueso: mandíbula → pulso por el hueso → atajo a la cóclea).
4. **Gráficos del tema**, no estadística genérica (nada de barras o cuadrículas si el tema es una onda, un sonido, una persona). Ej.: ondas de voz que se suman/restan; el personaje en varias edades para «toda tu vida».
5. Estilo de referencia: 2D plano de noche (DedXqPENbLm, DemtYpjNWPc), neón para esquemas, datos en monoespaciada, capítulos «1 El aire».

**Ritmo y transiciones**
6. **Planos de ≤ 3 s, pero solo se corta cuando cambia lo que se muestra.** Si la misma escena sigue, la cámara viaja con suavidad entre encuadres (`camara.puntos`), sin cortes.
7. **Transiciones: fundido de 0.4 s (12 cuadros), la escena nueva entra encima de la anterior.** Sin efectos, sin bajón a negro, sin zooms bruscos.
8. Nada de quedarse >3 s en la misma imagen haciendo zoom, salvo un gráfico mientras se construye.

**Subtítulos**
9. Estilo «selección» (referencia Dege5ORIPxv): Figtree, arriba al centro (y 360), palabra por palabra al ritmo de la voz, la actual en blanco 700 con entrada desenfocada, las dichas en gris 400, recuadro azul con dos puntos en la palabra clave de cada frase.
10. Frases ≤5 palabras, cortadas en puntuación o pausas > 0.3 s; nunca terminan en palabra de enlace ni dejan 1–2 palabras colgando.
11. **Nunca tapan un gráfico:** en tomas con algo importante arriba bajan a la zona libre (móvil 1400, chat 1430, cabeza 1540, ondas 1250 en voz-grabada). Cada frase decide su altura al empezar y no se mueve mientras se lee. Comprueba con cuadros a resolución completa.

**Final**
12. **Nunca cortar en seco:** 1.2 s de cola tras la última palabra. En esa cola el personaje vuelve a la pose y la cámara al encuadre del primer cuadro, las etiquetas se van, el reloj y el decorado coinciden con el inicio → bucle sin salto. Fundido solo de audio.

**Técnica**
13. Todos los tiempos desde las palabras; con voz nueva solo se re-ejecuta el generador.
14. Duraciones en milésimas redondeadas hacia abajo (nada puede pasar de `duracion_s`).
15. Remotion no aplica el esquema a las props: cada capa hace `Esquema.parse()` para los valores por defecto.
16. Medidas de texto (cajas de resaltado) solo cuando la fuente ya cargó (`delayRender` + `document.fonts.load`).
17. Fuentes nuevas: solo OFL/CC0, con su fila en `tools/architect/biblioteca/LICENCIAS.md` y sha256.
18. Revisa siempre: etiquetas que se solapan, textos que se salen del cuadro, el chat o el móvil tapados por subtítulos.

## Reglas aprendidas en hedy-lamarr-wifi (2026-11-02, estilo-monigotes)
19. **Comprueba las fuentes de sonido al empezar, no al final:** `biblioteca/sfx/` puede estar vacía. Kenney da 403 al curl (no te saltes el bloqueo: el creador baja los zips). Para la key de ElevenLabs, haz `GET /v1/user/subscription` (gratis) y comprueba que tiene `sound_generation`. Plan y saldo, al director.
20. **Efectos de sonido = lo que pasa en pantalla** (el piano suena a teclas, la puerta que se abre suena a puerta, el sello a golpe). Sin música. Los tiempos salen de la EDL (aparición o golpe del objeto) y la sincronía se mide a ±1 cuadro.
21. **Los SFX pueden ir encima de la voz** con un tope de nivel: ≥ 10 dB bajo el pico de voz de cada sílaba. **No quites un SFX por caer sobre una palabra** (error R2: el rotulador del «Mentira» y los blips de «auriculares» se quedaron mudos). Si una regla del encargo contradice las referencias, avisa al director antes de aplicarla.
22. **Un cambio solo de audio no re-renderiza la imagen:** renderiza solo el audio y móntalo con `-c:v copy` sobre el `final.mp4`, y vuelve a medir con ebur128.
23. **El texto en pantalla también cumple la lista «No decir»** del concepto: «= HASTA 88 FRECUENCIAS», nunca «= 88 FRECUENCIAS». Repasa cada rótulo contra la lista antes de renderizar.
24. **Subtítulo fijo ⇒ franja y 1300–1400 vacía de todo lo importante:** fechas, trofeos, huchas, torpedos, teclas. Compruébalo en cada toma, en el cuadro inicial **y en el final del empuje**.
25. **Los empujes no cortan carteles** ni un personaje tapa letras (error R2: CTA, «ANTEPASADO», paneles de 1962). Mide el cuadro final de cada empuje.
26. **Ningún bloque de subtítulo es una sola palabra de enlace** («Su», «Si», «En», «Ni», «y», «de»): pégalo al siguiente.
27. **Compara la transcripción con el guion palabra por palabra:** ElevenLabs puede comerse palabras cortas (la «o»). Si falta una, pide al creador esa frase sola y empálmala en un silencio (nivel y EQ igualados, fundido de 20 ms, `voz-v2.mp3`; `voz.mp3` no se toca). Ejemplo: `exports/hedy-lamarr-wifi/empalme_frase_final.py`.
28. **`select='gt(scene,0.3)'` no mide el ritmo** de un estilo con golpes de cámara: mide cuadro a cuadro.
29. **Termina siempre con tu informe y tu sección en `render-log.md`,** aunque el render corra en segundo plano. En R3 el video quedó hecho, pero no hubo informe ni sección, y el director tuvo que comprobarlo a mano.

30. **El tope de los SFX se mide sobre el mp4 renderizado** (R3): el render los subió 2–4 dB respecto al diseño, y el periódico quedó a 6.4 dB de la voz. Usa `exports/hedy-lamarr-wifi/qa/review_r3/medidas/sfx_capa.py` y `sfx_puntos.py` después del render.
31. **Al mover un cartel para arreglar algo, vuelve a medirlo entero**: zona segura x 135–945 (R3: ANTEPASADO acabó en x 72).
32. **Una palabra de enlace tampoco puede cerrar un bloque de dos** («Pero tus» / «auriculares»): la regla de `subtitulos_centro` mira el final del bloque, no solo los bloques de una palabra.

## Lista de comprobación visual (hoja cada 2 s + cuadros sueltos)
- ¿Cada escena cae en su frase? (anota 4–6 pares palabra → escena con su segundo).
- ¿Algún tramo > 3 s sin cambio visible? ¿Algún corte donde no cambia nada?
- ¿Algún subtítulo encima de un gráfico, etiqueta o UI? ¿Alguna etiqueta encima de otra?
- ¿Algún cuadro vacío, negro o con un fundido raro?
- ¿Algún emoji, icono suelto o texto plano haciendo de visual principal?
- ¿El último cuadro coincide con el primero?
- ¿(monigotes) Algo importante en la franja y 1300–1400, en el cuadro inicial o final de cada empuje? ¿Algún cartel cortado o tapado?
- ¿(monigotes) Suena todo lo que aparece? ¿Cada SFX cae en su cuadro y ≥ 10 dB bajo la voz? ¿Sin música?
- ¿Algún rótulo contradice la lista «No decir»?
