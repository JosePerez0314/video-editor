---
name: reutilizacion-materiales
description: Reutilizar escenarios, personajes, atrezo, SFX y scripts de videos anteriores en vez de empezar de cero. Al cerrar cada video se cataloga lo nuevo y lo más usado pasa a la parte común; al empezar un video se consulta solo el catálogo, no todos los proyectos.
---

# Skill: reutilización de materiales

Pedido del creador (2026-11-03): «cada vez que termine un video, que revise los materiales de los otros videos, para que pueda reutilizar y no necesariamente empezar de 0 … y lo que más lo utilice que lo guarde en una carpeta aparte para no siempre hacer el recorrido por todos los videos».

**Índice único:** `tools/architect/biblioteca/reutilizables/CATALOGO.md`. Es lo **único** que se lee al empezar; no se recorren los `exports/` ni los `Escenarios<Video>.tsx` de otros proyectos salvo que el catálogo apunte a una pieza concreta.

## 1 · Al empezar un video (editor, antes de la prueba de 10 s)
1. Lee `CATALOGO.md` y el `escenas.md` del video.
2. El `escenas.md` ya trae cada pieza marcada `[catálogo]` / `[nueva]` (lo hace el creative-producer desde 2026-11-04): **parte de esas marcas, no repitas el análisis**. Solo corrige una marca si la pieza del catálogo no sirve (dilo en el informe). Plan antiguo sin marcas → márcalo tú.
3. Construye **solo** lo nuevo. Importa lo común desde su sitio; no lo copies dentro del archivo del video.
4. **SFX, antes de todo** (creador: «que revise los efectos de sonido, todo lo que se pueda reutilizar que se reutilice»): repasa el «Inventario completo de SFX» del catálogo y reutiliza todo lo que sirva tal cual, recortado o retocado (tono, velocidad, filtro). Genera con ElevenLabs solo lo que no tenga equivalente, y anota en `render-log.md` cada SFX nuevo con el motivo («ninguno del inventario sirve porque…») y la cifra «SFX: N reutilizados, M nuevos».
5. En el informe de la prueba, di cuántas piezas se reutilizaron y cuántas fueron nuevas.

## 2 · Al cerrar un video (editor, en el mismo encargo del render final; sin agente aparte)
1. Añade al catálogo cada pieza nueva: nombre, archivo, estilo, qué es, video y usos = 1.
2. Suma 1 a «Usos» de cada pieza reutilizada y añade el video.
3. **Promoción (usos ≥ 2):** si una pieza se ha usado en 2 o más videos y todavía vive en un archivo de un video (`EscenariosHedy.tsx`, `EscenariosSoldado.tsx`…), **cópiala** a la parte común:
   - componentes → `tools/architect/src/reel/escenas/comun/<Pieza>.tsx` (exportada con props para lo que cambia: colores, textos, atrezo);
   - SFX → `tools/architect/biblioteca/sfx/comun/` (con su fila en `LICENCIAS.md`);
   - scripts → `tools/architect/biblioteca/reutilizables/plantillas/`.
   El original se queda donde está para no romper renders antiguos (regla global 3); los videos nuevos importan desde `comun/`. Pasa `npx vitest run` tras mover código.
4. Actualiza la fecha del catálogo y apunta en `render-log.md`: «catálogo: N nuevas, M reutilizadas, K promovidas».
5. Ejecuta `python3 tools/architect/biblioteca/reutilizables/comprobar_catalogo.py`: debe decir «CATALOGO al día». Detecta piezas y SFX sin catalogar **y promociones pendientes** (usos ≥ 2 sin copia en `comun/`). Si lista algo, complétalo antes de la señal.

## 3 · Reglas
- Nada de pieza nueva si una del catálogo sirve con un cambio de props.
- Una pieza promovida debe verse igual en el video original (comprueba un cuadro).
- Licencias: los SFX de ElevenLabs plan free se marcan como tales en el catálogo (solo registro; la licencia la gestiona el creador, sin avisos).
- El director revisa las cifras de reutilización en el análisis posterior (`presupuesto-tokens` §6): menos piezas nuevas = menos tokens de editor.
