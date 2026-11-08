---
name: metricas-viralidad
description: Definiciones y fórmulas con las que el social strategist mide «viral», «consistente» y «cuenta que despegó rápido» (vara de @resultaaquee). Evita comparar manzanas con peras entre redes y cuentas.
---

# Métricas de viralidad y consistencia

## Definición del creador
**Consistencia = como @resultaaquee: en 2–4 semanas desde su primer video, videos muy virales y *todos* virales.** Las cuentas grandes se conservan como referencia secundaria de formato; las nuevas son el objetivo de réplica.

## Umbrales
- **Viral** = ≥ 100K vistas. **Muy viral** = ≥ 1M. (Mediana de @resultaaquee ≈ 16K likes en sus 20 reels.)
- **Pico aislado** = máx/mediana > 20, o ≥ 10× la mediana con el resto bajo (ej. Mangel Ciencia 354, BODYVERSE 3D).

## Fórmulas por cuenta (sobre los últimos 30–40 videos)
1. Fecha del primer video de la muestra (TikTok: `id >> 32`; YouTube: `upload_date`).
2. **Ventana 28 d** desde ese video: `n`, mediana, % ≥100K, nº ≥1M.
3. Mediana global, máx/mediana, videos/día.
4. Etiqueta: **Arranque rápido** (cuenta nueva, ≥ 60 % ≥100K en 28 d) · **Madura consistente** (≥ 80 % ≥100K) · **Picos** (el resto).
5. Excluir **anclados** al calcular la mediana, pero anotarlos (suelen ser los picos).

## Referencias medidas (27-oct-2026)
- @resultaaquee (27 reels, 14 días): mediana 223K, 70 % ≥100K, 85 % ≥60K, 4 ≥1M; los 4 bajo 20K tienen 1–2 días. **Esta es la vara de «consistente».**
- dr.marinbu (TikTok): 31/32 ≥100K. XpressTV (YT): 30/30 ≥1M. Por Dentro De Todo (YT, 12 días): 70 % ≥100K.

## Límites que se dicen siempre
Vistas acumuladas ≠ primeras 48 h · cuentas homónimas en otras redes pueden no ser la misma · `view_count` de yt-dlp en listados está redondeado · una muestra sin el pico antiguo subestima el techo.
