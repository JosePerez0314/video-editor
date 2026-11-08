---
name: red-facebook-reels
description: Cómo funciona Facebook Reels para nuestro canal según lo observado: qué métricas se ven, por qué no hay cuenta de referencia, cómo usarlo (resiembra) y cómo extraer datos con Chrome. La usa el shorts-social-strategist.
---

# Facebook Reels

## Hallazgos (27-oct-2026)
- **No existe una cuenta tipo @resultaaquee en nuestro estilo.** Las referencias de Instagram casi no existen en Facebook (loconstruiste.mx: 0 seguidores, reels de 3 y 8 vistas; Chispa Lógica 4 seguidores).
- El mismo contenido que hace millones en TikTok se queda corto: Dr. Marinbu 8–272 vistas (página de 10K seguidores); Asael Isaías (órganos 3D) 1–4K.
- Lo que sí acumula millones son **reposteos de clips ajenos** con presentador superpuesto (Jaime Ciencia: 120M/142K, mediana 10–30K) y personas hablando a cámara. No replicable.

## Papel en la estrategia
**Red de resiembra:** el mismo `final.mp4` 1–3 h después de TikTok. No decide temas ni calendario; se mide aparte.

## Cómo medir con Chrome
- Buscador (`/search/videos/?q=`): muestra reacciones/comentarios/compartidos, **no vistas**. `/search/reels/` da error. Páginas: `/search/pages/?q=`.
- **Vistas solo en la pestaña Reels de cada página** (`/<página>/reels/` o `profile.php?id=<id>&sk=reels_tab`), tarjetas con «1,2 mil», «1,4 mill.». Hacer scroll para que carguen.
- El JS con cookies/URL se bloquea; leer con capturas o `get_page_text` (el texto sale a veces con letras sueltas intercaladas).

## Texto
Descripción corta con la pregunta; hashtags opcionales (los reposteos virales usan 3–4). Sin CTA de embudo.

## Límites
Sin vistas fuera de la pestaña Reels; páginas sin historial no permiten medir «arranque».
