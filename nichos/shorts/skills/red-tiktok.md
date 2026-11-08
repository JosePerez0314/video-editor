---
name: red-tiktok
description: Cómo funciona TikTok para nuestro canal, medido en cuentas reales (dr.marinbu, Humanigma, GoldenLab): qué muestra el buscador y el perfil, extracción de datos con Chrome, formato, descripciones, hashtags y anclados. La usa el shorts-social-strategist.
---

# TikTok

## Qué se ve (observado 27-oct-2026, con la sesión del creador)
- **Buscador** (`/search/video?q=`): cada tarjeta muestra **likes**, no vistas, autor y fecha. Sirve para descubrir cuentas, no para medir.
- **Perfil** (`/@cuenta`): la cuadrícula muestra **vistas por video** (solo se pintan tras hacer scroll). Seguidores y likes totales arriba. Los videos **anclados** salen primero marcados «Anclado».
- Fecha del video: el ID cifra la hora → `fecha = datetime.fromtimestamp(int(id) >> 32)`. Sirve para saber cuándo arrancó una cuenta.

## Extracción con Chrome (funciona)
1. `navigate` al perfil, `scroll` abajo 10–15 ticks y de vuelta arriba (para que pinten las vistas).
2. `javascript_tool`: `[...document.querySelectorAll('[data-e2e="user-post-item"]')].map(e=>{const a=e.querySelector('a');return a.href.split('/video/')[1]+' '+e.innerText.replace(/\n/g,' ')})` y `[data-e2e="followers-count"]` para seguidores.
3. **No devuelvas `location`/URL completa en el JS**: el filtro lo bloquea («Cookie/query string data»). Devuelve solo IDs y números.

## Lo que se repite en las cuentas que funcionan
- **dr.marinbu** (479.7K seg.): 31/32 videos ≥100K, 20/32 ≥1M; 2D cartoon de órganos con cara; descripción = pregunta + `#cartoon #animation #doctor #shorts`.
- **Humanigma** (9.5K seg., 7 semanas): 3D realista del cuerpo, preguntas; 45 % ≥100K, picos de 5.2M y 1.7M.
- **GoldenLab / Future Frames:** crecen por 2–3 videos enormes **anclados** (1–14M); el resto ronda 10–50K.
- Duración típica de las cuentas consistentes: 25–35 s.

## Publicar (texto listo para pegar)
- Descripción = la misma pregunta del video + 2–3 hashtags de formato (`#animacion #curiosidades` + tema). Sin cadenas largas.
- Anclar (por el creador) los 2–3 mejores videos del arranque.
- Hora: 1–3 h después de Instagram el mismo día (ver `publicacion-multired.md`).

## Límites
Sin vistas en buscador; cuentas con pocos videos dan fechas poco fiables; TikTok puede pedir verificación: parar y avisar.
