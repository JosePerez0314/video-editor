---
name: adaptacion-ingles
description: Cómo elegir y adaptar al español un reel en inglés de los canales que traduce @resultaaquee (Rick's Clips y afines), adelantándonos a RA y a Don Cabezón. Es el método que eligió cajeros-loteria (309K en TikTok a las 20 h). Fase A (explorar y puntuar candidatos) = shorts-social-strategist; fase B (concepto con traducción) = shorts-viral-strategist; el creador elige entre las dos.
---

# Adaptación de reels en inglés (método cajeros)

Creador, 2026-11-13: «sigamos la misma estrategia: explora los canales en inglés que resultaaquee copia y traduce, y adelantémonos; que el proceso de selección sea igual que el del cajero».
Base: `publicacion/analisis-redes-2026-11-11-resultaaquee.md` (§B: de dónde traduce RA) y `publicacion/analisis-redes-2026-11-11-estancamiento-voz.md` (§4.1: la tabla de la que salió cajeros).

## 1 · Fuentes
| Canal | Dónde | Papel |
|---|---|---|
| **Rick's Clips** | TikTok `@ricks0015` · IG `@ricks_clips01` | Fuente de 9 de 9 temas de RA. Publica unos 2 al día. |
| stickmans.explain | IG | Señal secundaria (resubidas de Rick's). |
| **@resultaaquee (RA)** | IG | Comprobar lo que ya hizo, para excluirlo. |
| **Don Cabezón** `@animeprageral` | TikTok | Competencia en español: traduce a Rick's en 0–9 días. Comprobar para excluir. |
| Nuestra cola y lo publicado | `calendario.md`, `scripts/` | Excluir lo que ya tenemos. |

Si aparece otro canal fuente de RA, se añade aquí con su dato.

## 2 · Fase A · Explorar y puntuar (social-strategist, Sonnet)
1. **Recoger de las DOS redes de Rick's (creador, 2026-11-13):** Instagram `@ricks_clips01` y TikTok `@ricks0015`, siempre las dos. Muchos temas salen en ambas con resultados muy distintos (cajeros: 12.4M en IG frente a 8.8K en TT), así que cada candidato lleva sus vistas en IG **y** en TT, más las de Don Cabezón si existe. Instagram: lista de reels de la cuadrícula (la anota el creador desde el móvil mientras Chrome no pueda abrir IG) y, por reel, `yt-dlp --print "%(upload_date)s|%(like_count)s|%(description)s"` sin cookies (da fecha, likes y título; las vistas salen de la cuadrícula). TikTok: Chrome en solo lectura.
   Los reels de Rick's de los últimos ~21 días (carril rápido, 3–6 d, y carril de cola, 11–22 d; ver §B4 del informe de RA), con fecha, vistas, likes, compartidos, guardados y URL. Fecha de TikTok = `id >> 32`.
2. **Cambio del creador (2026-11-21):** «hacer los videos nosotros no funciona por ahora, tenemos que buscar buen material para poder traducir de rick, no importa si resultaquee lo hizo o no, necesitamos que funcione». → Guiones propios en pausa; **el bucle no es obligatorio** (21-nov: «el video necesariamente no tiene que terminar en bucle»): no resta al puntuar; **lo que ya hizo RA ya no se excluye** (se anota su resultado como dato: si a RA le funcionó, es prueba de que el tema funciona en español). Se excluye solo lo nuestro y la ficción de gaming. El criterio que manda es pasar las fases de `fases-viralidad-tiktok.md`.
   *(Regla anterior, 13-nov, sustituida:)* **Excluir** solo lo que ya hicieron **RA** o nosotros, y la ficción de gaming. **Lo que ya hizo Don Cabezón NO se excluye: es la mejor pista de lo próximo que hará RA** (RA repitió a Don Cabezón en 4 de 5 casos). Si la versión de Don Cabezón funcionó (≥ 200K), sube en el orden.
   **Objetivo (creador, 2026-11-13): adelantarse a @resultaaquee.** Se gana publicando el tema antes que RA. Ventana: RA tarda 3.1–22 d desde Rick's (mediana 11.6 d). Para cada candidato, apunta la **edad** (días desde Rick's) y estima cuántos días quedan antes de que RA lo saque.
3. **Puntuar** cada candidato restante con la misma tabla de §4.1: tema (qué cuenta), fuente · fecha · vistas, por qué encaja, riesgo. Orden de preferencia, por lo medido en nuestra cuenta:
   - **Arriba:** personaje que hace algo indebido + dinero + trampa o giro, contado como **historia** (cajeros: 309K). Tema universal, que no exija saber historia ni ciencia.
   - **Bonus:** muchos guardados y compartidos en inglés (guardados/vistas ≥ 0.3 %), algo muy visual, que la versión en español aún no exista en ninguna red.
   - **Abajo:** dato o explicación sin personaje (soldado, voz-grabada, bushby: 33–625 vistas); cuentos que no son hechos; temas que solo valen en EE. UU. sin poder localizarlos.
   - **Vistas: usar la cifra más alta del tema en cualquier red** (Rick's IG, Rick's TT, Don Cabezón). El mismo reel de cajeros tuvo 12.4M en el IG de Rick's y solo 8.8K en su TikTok (`@ricks0015/video/7699674695724961037`): su TikTok rinde poco por la cuenta, no por el tema.
   - Que funcione en inglés **no** predice cuánto hará en español (RA ÷ EN va de 0.16× a 4.5×). Cajeros fue una excepción consciente: Don Cabezón ya lo había hecho y fracasó (2.3K).
4. **Entregar** `publicacion/analisis-redes-AAAA-MM-DD-candidatos-en.md`: los 5–9 mejores en tabla, una recomendación de 1–3 y los descartados con su motivo. Datos crudos en `publicacion/cuentas/<red>/<cuenta>/`.

**Seguridad de la cuenta (2026-11-12, la cuenta de IG quedó en revisión por «actividad no humana»):** Chrome **no abre instagram.com ni facebook.com** con la sesión del creador. Para un reel de IG concreto: `yt-dlp --skip-download --print` sin cookies (da la fecha y los likes, no las vistas). Si hace falta una cuadrícula de IG, se dice en el informe y lo comprueba el creador a mano. TikTok sí, con Chrome, en solo lectura y con pocas páginas.

## 2b · Tandas de 3 · modo recopilación (creador, 2026-11-13)
Palabras del creador: «no es necesario por mundos porque ahora estamos en modo recopilación, el gasto no importa, prefiero abarcar lo más posible y enriquecer la biblioteca, quita eso de los 3 videos mismo mundo, ya que lo que buscamos es viralidad como el del cajero».
- **Se eligen 3 temas a la vez y se producen los 3** salvo que el creador vete alguno (si veta uno, se sustituye por el siguiente mejor).
- **El único criterio es la viralidad, con la fórmula que funcionó en cajeros** (§2.3 «Arriba»): personaje que hace algo indebido + dinero + trampa o giro, contado como historia, tema universal que no exija saber historia ni ciencia; muchas vistas en las redes de Rick's (y Don Cabezón) y que RA aún no lo tenga. Todo de reels en inglés con la traducción tal cual (§4.4).
- **El mundo NO es criterio:** no se agrupan temas por mundo ni se penaliza un tema por necesitar escenarios nuevos. Variedad de mundos = biblioteca más rica, y en modo recopilación el gasto no importa.
- Al puntuar se anota el `mundo` solo como dato informativo (para el catálogo), nunca para ordenar.

## 3 · ✋ El creador elige

## 4 · Fase B · Concepto (viral-strategist, como `cajeros-loteria.concept.md`)
1. Descargar el original con `yt-dlp` a `ideas-virales/raw/<id>.mp4`, junto con su `.info.json`. Hacer una hoja de 12 cuadros en `ideas-virales/frames/<id>_sheet12.jpg`.
2. **Medir:** duración, palabras y ppm (Whisper large-v3), cuadros quietos en 0–3 s, ritmo de cambios, tipo de final (bucle o CTA).
3. Transcripción por beats: gancho, setup, desarrollo, micro-payoff, giro (en qué %), cierre.
4. **Guion = traducción literal**, como hace RA: mismas frases en el mismo orden y los mismos chistes. Solo se adaptan las muletillas y las unidades (pies → metros). Hay que contar con que el español sale un 10–19 % más largo.
   **Calidad de traducción = la de cajeros (creador, 2026-11-13: «traducir tal cual, que la calidad de traducción sea la misma que la del cajero»).** Patrón obligatorio: `scripts/sociedad/cajeros-loteria.guion-voz.md`. Eso significa:
   - **Enlaces del original en inglés, siempre (creador, 2026-11-14: «cuando se elija un tema en guion deja el link de la versión en inglés para yo depurarlo siempre, tanto de Instagram y TikTok, si no puedes pasarme el link de ambos mínimo de uno»).** El concept y el `guion-voz.md` llevan arriba los enlaces del reel original en **Instagram y TikTok** (mínimo uno; si falta, se dice cuál y por qué).
   - Transcripción propia del original con Whisper large-v3 y **tabla frase a frase** (t · original EN · traducción ES · nota) con todas las frases.
   - **Nada añadido ni quitado:** ni datos, ni casos, ni CTA, ni preguntas. Si el original tiene bucle, el bucle se mantiene.
   - Español natural y neutro, que suene dicho y no traducido. Los juegos de palabras se conservan si tienen equivalente (cajeros: «fishing» → «pescando»). Si no lo tienen, se anota la pérdida.
   - Cada adaptación (muletilla, unidad, moneda, cartel) se justifica en la nota de su fila.
   - Los hechos verificados del concept **no entran en la voz**: se quedan en el concept, para el comentario fijado y las respuestas.
5. **Hechos:** separar ficción de hecho real con `fact-vs-hypothesis`. Si el original simplifica algo, anotarlo en el concept para el creador.
6. **Coherencia visual con el hecho real:** el atrezo tiene que encajar con el caso real. Lección de cajeros: en pantalla salía un raspa y gana y la historia solo cuadra con boletos de sorteo; fue la objeción más votada.
7. El análisis del original va **antes** del guion, para no tener que rehacerlo (presupuesto-tokens §7).

**Animación igual que cajeros** (creador, 2026-11-13): el editor parte de `exports/cajeros-loteria/escenas_cajeros-loteria.py` + `sfx_cajeros.py` y usa su `final.mp4` como referencia visual; solo cambian la historia y el atrezo.

Después sigue el flujo normal: creative-producer → voz → prueba de 10 s → render. Estilo por defecto: el del último video que funcionó (`estilo-monigotes-3d`), salvo que el creador diga otro.

## 5 · La carrera (adelantarse)
- **El rival es @resultaaquee**, no Don Cabezón: Don Cabezón publica el mismo día que Rick's y no se le puede ganar, pero RA tarda entre 3 y 22 días. Prioridad: temas que RA **probablemente** hará pronto (Rick's reciente que le encaja, o ya hecho por Don Cabezón con éxito) y que podamos producir y publicar en menos días de los que le quedan a RA. Medir la carrera: anotar en §6 cuándo lo sacó RA (o si no lo sacó).
- **El día antes de publicar**, mirar el catálogo de Don Cabezón (y el de RA, si se puede sin Chrome en IG). Si ya lo publicaron, se publica igual en las redes donde no esté: un mismo tema ha rendido dos veces en redes distintas (3 de 3 casos, 03-nov).
- Objetivo de cola: **≥ 3 candidatos puntuados** siempre listos. Repetir la fase A cuando queden menos de 2.

## 6 · Registro de resultados (para afinar la puntuación)
| Video | Original EN | Tipo | Vistas EN | Nuestro TikTok 24 h | ¿RA lo sacó? | Nota |
|---|---|---|---|---|---|---|
| cajeros-loteria | Rick's IG De1kU12K-V9 | trampa + dinero + giro, historia | 12.4M | 309K a las 20 h | no (a 13-nov) | CTA binario casi sin respuestas; el bucle sí generó comentarios |
