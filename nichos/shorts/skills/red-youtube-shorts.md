---
name: red-youtube-shorts
description: Cómo funciona YouTube Shorts para nuestro canal, con datos reales (XpressTV, CdeCiencia, Por Dentro De Todo, 1Cell1Life): cómo medir con yt-dlp, títulos, descripción, duración y cadencia. La usa el shorts-social-strategist.
---

# YouTube Shorts

## Medir (el más fácil de automatizar)
- Lista de un canal: `yt-dlp --flat-playlist --playlist-end 40 -J "https://www.youtube.com/channel/<ID>/shorts"` → `entries[].view_count` (redondeado) y `channel_follower_count`.
- Por video: `yt-dlp --skip-download --print "%(id)s|%(upload_date)s|%(duration)s|%(view_count)s|%(like_count)s|%(comment_count)s|%(title)s" https://www.youtube.com/shorts/<id>` (en paralelo con `xargs -P 8`).
- Descubrir: en Chrome, buscar y pulsar el chip **Shorts**; sacar `a[href*="/shorts/"]` y luego los canales con yt-dlp. La búsqueda de texto de yt-dlp (`ytsearchN:`) devuelve sobre todo videos largos: no sirve para Shorts.
- Ojo: la muestra de «últimos 30» puede no incluir el pico del canal (BODYVERSE 3D: 8.6M fuera de los últimos 40).

## Datos medidos (27-oct-2026)
| Canal | Resultado |
|---|---|
| XpressTV (17.4M) | 30/30 ≥1M, mediana 3.0M; 3D del cuerpo/objetos, ~31 s |
| CdeCiencia (5.16M) | 83 % ≥100K; experimentos con objetos, ~28 s |
| Por Dentro De Todo (96.9K, nuevo) | 30 Shorts en 12 días, 70 % ≥100K; 3D cuerpo humano, ~32 s |
| 1Cell1Life (37K, nuevo) | 11 Shorts en 7 días, 7/11 ≥100K |
Likes/vistas 2.5–3.4 %; comentarios/vistas 0.005–0.03 %.

## Texto
- **Título = pregunta o afirmación corta** (≤ 60 caracteres), 1 emoji y **los hashtags al final del título** (`#Shorts` + 2 de tema, p. ej. `#curiosidades #historia`; título completo ≤ 100 caracteres) (creador, 2026-11-14: «en youtube los hashdags vayan junto con el titulo y no descripcion»). Ej. observados: «¿Por qué los mosquitos siempre te pican a ti? 🦟», «Deja de cortarte las uñas así!!».
- Los canales grandes mezclan títulos ES/EN; no está probado que ayude a un canal nuevo.
- Descripción: una línea que repite la pregunta + CTA. **Sin hashtags en la descripción**: van en el título.
- Duración: 25–35 s en los consistentes. Publicar el mismo día o el siguiente a Instagram.

## Portada
Se elige un cuadro del propio video; no diseñar miniatura (ver `portadas-shorts.md`). Efecto en Shorts de portada subida: **no verificado**.
