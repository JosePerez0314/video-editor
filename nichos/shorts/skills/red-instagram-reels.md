---
name: red-instagram-reels
description: Cómo funciona Instagram Reels para nuestro canal: qué muestra, qué se puede medir sin sesión, horarios, descripción, CTA, bio y portada. Instagram es la red con la referencia buena (@resultaaquee). La usa el shorts-social-strategist.
---

# Instagram Reels

**Es la red de referencia del canal.** El único caso medido de «todos virales en 2–4 semanas» es @resultaaquee (20 reels en 14 días, 71.9K seguidores; ver `lanzamiento-cuenta.md`).

## Qué se ve y cómo medirlo
- Perfil → pestaña Reels (`/<cuenta>/reels/`): **sin sesión** se ven ~12 reels con vistas. Cierra el aviso con la X; **no pulses «Continuar con Facebook»** (login/OAuth: lo hace el creador).
- Vistas = texto de la tarjeta (`a[href*="/reel/"]`, p. ej. «11,9 mil», «1,1 M»). Likes/comentarios/fecha/descripción: `yt-dlp --dump-json` (sin `view_count`).
- **Con sesión** la pestaña Reels pinta todo el perfil con scroll (leer `a[href*="/reel/"]`); el 27-oct mostró 20 reels aunque la cuenta tenía ≥27 (6 códigos recientes solo salieron sin sesión: De_YBVFIjuY, De9ROc5IlxL, De7XuF6oN9M, De6rmNwIHzR, De1Z-djoBmx, Deznz97ojFB). **Contrastar siempre ambas vistas / el contador de publicaciones** antes de dar el total.
- Todo son vistas acumuladas. Orden de la cuadrícula: el más nuevo primero; los últimos 3–5 reels siempre parecen bajos porque aún acumulan.

## Qué funciona (medido en @resultaaquee)
- Volumen: 3 reels/día los 2 primeros días, luego ~2/día. Horas 10, 15 y 21 h (España).
- Tema: objeto que el espectador tiene en la mano o puede comprobar ya. Historia/abstracto rinde 5–10× menos; el reel-promo de su producto es el más bajo (1.8K).
- Descripción: pregunta corta + 1 emoji, **sin hashtags**. CTA fijo desde el día 3 (embudo a su web: no aplica sin producto).
- Bio: una línea de promesa + link.

## Portada
Automática (cuadro del video) en los 20 reels. No diseñar portada: ver `portadas-shorts.md` y `publicacion/analisis-portadas.md`.

## Qué NO se sabe aún
Retención y vistas de las primeras 48 h; efecto de hashtags (no se usan). Se miden con las métricas que comparta el creador (ver `seguimiento-resultados.md`).
