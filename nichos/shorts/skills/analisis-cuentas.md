---
name: analisis-cuentas
description: Cómo analizar una cuenta de referencia de shorts con datos reales (fechas, horas, vistas, likes, comentarios, descripciones) usando yt-dlp y el navegador. La usa el shorts-social-strategist.
---

# Análisis de una cuenta

1. **Lista de reels:** abrir `https://www.instagram.com/<cuenta>/reels/` con Claude in Chrome, hacer scroll hasta el final y sacar los códigos y vistas de los enlaces `a[href*="/reel/"]` (el texto de cada tarjeta trae las vistas).
2. **Datos por reel:** `yt-dlp --dump-json --no-download "https://www.instagram.com/reel/<código>/"` → `timestamp`, `like_count`, `comment_count`, `description`. Guardar en `nichos/shorts/publicacion/cuentas/<cuenta>/<código>.json`. (Instagram no da `view_count` por yt-dlp: las vistas salen del perfil.)
3. **Tabla** ordenada por fecha: día desde el primer reel, hora (pasar a la zona horaria del público), tema, vistas, likes, comentarios, CTA de la descripción.
4. **Conclusiones (5–6):** volumen y ritmo, horas, qué temas despegan y cuáles no, fórmula de descripción, CTA y embudo, cuándo llegó el primer breakout.
5. **Límites a decir siempre:** vistas acumuladas (no de las primeras 48 h), redes que bloquean (TikTok suele pedir verificación), cuentas homónimas en otras redes que no son la misma.

Ejemplo hecho: @resultaaquee (`lanzamiento-cuenta.md`).

Para TikTok, YouTube y Facebook, y para elegir qué medir (consistencia, arranque rápido), ver `investigacion-redes-chrome.md` y `metricas-viralidad.md`. Informe vigente: `publicacion/analisis-redes-2026-10.md`.
