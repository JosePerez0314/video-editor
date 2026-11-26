---
name: revision-por-bloques
description: Revisión visual corta que hace el editor MIENTRAS construye el video, por bloques de escenas, antes del render final. 3–4 paradas por video, 2 hojas de 24–30 cuadros cada una sacadas con fotos.ts (sin render), con una lista corta de los errores visuales que ya se escaparon. Arregla en el generador sobre la marcha para que el render final salga limpio y no haga falta una ronda de corrección. Obligatoria en estilo-monigotes y estilo-monigotes-3d.
---

# Skill: revisión por bloques mientras se construye

Pedido del creador (2026-11-13): «crea una skill dedicada a eso, a revisar esas partes antes del render final, que sea mientras vaya creando, así no deja esas revisiones al último».

**Por qué:** en pudding-millas, corregir después del render costó ≈ 627K (rondas R3 + R4, revisión más cara y revisión acotada), el 28 % del video. Cada ronda hace que el agente vuelva a arrancar y leer el contexto, que se rendericen otra vez los tramos y que se compare el video entero. Un fallo que se ve en una foto antes del render se arregla en el generador y no cuesta ningún render.

**Coste previsto:** ≈ 8K por parada × 4 ≈ 32K, más 30–50K de arreglos sobre la marcha ≈ **60–80K por video**. Ahorro esperado: **300–450K** (normalmente evita una ronda entera). Si una parada pasa de 15K, la hoja tiene demasiados cuadros o demasiada resolución.

## 1 · Cuándo parar
- **3–4 paradas por video**, una al terminar cada bloque de escenas del generador (≈ 6–8 escenas, o 15–20 s de voz). Con 25 escenas: E1–E7 · E8–E13 · E14–E19 · E20–fin.
- **La parada es parte de construir el bloque.** No se empieza el bloque siguiente con el anterior sin revisar, y no se dejan todas las revisiones para el final.
- La prueba de 10 s cuenta como la primera parada si cubre el primer bloque.
- Si un arreglo cambia código común (sets, `Monigote`, `Escena3d`), vuelve a mirar solo los cuadros afectados de los bloques ya revisados.

## 2 · Cómo sacar las hojas (sin render)
- Primero corre la **comprobación automática común** (creador, 2026-11-20), la misma que usa el reviewer: `python3 tools/architect/biblioteca/reutilizables/comun/comprobaciones_3d.py --edl <edl> --revisados nichos/shorts/exports/<slug>/qa/revisados.json --salida nichos/shorts/exports/<slug>/qa/comprobaciones.txt` (en el generador: `import comprobaciones_3d as c3d`, `c3d.anadir_opcion(ap)`, `c3d.solo_comprobar(a, E, REVISADOS)` y `c3d.comprobar_todo(E, REVISADOS)`; los generadores nuevos llevan `--solo-comprobar`). Más la franja y los puntos clave del generador. **Si sale con 1, no se pasa al bloque siguiente ni se renderiza.** Los avisos aceptados van a `revisados.json` con su motivo; solo el creador acepta un #48 o un #5. **Lo que se puede detectar con un script no se mira con los ojos.** En #5, #29 y #48 un ✓ a ojo solo vale con recorte al 100 % o medida en px. Ningún aviso pasa al bloque siguiente sin estar arreglado o metido en `REVISADOS` tras mirarlo al 100 %.
- **2 hojas por parada, de 24–30 cuadros cada una** (unos 48–60 cuadros por parada, ≈ 3–4 cuadros por segundo del bloque), con `herramientas/fotos.ts` (≈ 1.5 s por cuadro, sin render):
  `npx tsx herramientas/fotos.ts <edl> qa/bloques/b<N>_<a|b>.jpg --escala 0.75 --ancho 360 --cols 6 t1 t2 …`
- **Qué cuadros elegir:** primero y último de cada plano, el cuadro final de cada empuje o deriva, el momento en que algo entra, sale, cae o aparece (textos, cifras, objetos lanzados) y el último cuadro de cada plano con texto. En los cortes sobra con un cuadro a cada lado.
- **Nunca 60 cuadros en una sola imagen:** las miniaturas quedan de ~180 px y no se lee un cartel cortado. Nada de cuadros sueltos uno a uno: cada imagen se queda en el contexto y encarece todo lo que viene después.
- Si algo es dudoso, haz un recorte al 100 % solo de esa zona (`t@x:y:w:h`). No repitas la hoja entera.

## 3 · Qué mirar (lista corta: solo lo visual que ya se escapó)
Números de `errores-edicion.md`:
1. **Figuras junto a vehículos y muebles (#29):** ¿se leen delante, detrás o al lado? ¿Están «metidas dentro»? ¿Las cruza un poste o les sale algo de la cabeza?
2. **Marcos con forma (#30):** ventanillas, pantallas o espejos con su contenido recortado, sin que nada asome.
3. **Textos enteros (#15, #31):** carteles de pared, de mesa y de suelo, completos en x 135–945 o fuera del todo, también en la clave final de cada empuje.
4. **Textos que aparecen (#32):** no nacen tapados por otra capa, no pisan etiquetas y no salen de x 135–945.
5. **Texto en la mano (#33):** se lee entero hasta el último cuadro del plano.
6. **Franja del subtítulo (#20):** no tapa caras, carteles ni lo que nombra la voz.
7. **Cuerpos y bordes (#14):** nadie con medio cuerpo fuera ni cortado, salvo en los cuadros de golpe ya revisados.
8. **Edificios y sets:** completos o cortados a propósito, sin costados sin tejado ni teselas sin pintar.

La sincronía, el audio, los SFX y las especificaciones **no** se miran aquí: se comprueban una vez sobre el render final.

## 4 · Qué hacer con lo que encuentres
- Arréglalo en el generador o en la pieza **antes de seguir** y vuelve a sacar solo los cuadros arreglados (una hoja pequeña).
- **Error nuevo** (no está en la lista): añádelo a `errores-edicion.md` con el número siguiente y súmalo a la lista del §3 si es visual.
- **Duda de diseño** (cambiar lo que dice el plan): no la decidas tú. Anótala para el informe y sigue.

## 5 · Registro
En `render-log.md`, una línea por parada:
`bloque N (E–E, t0–t1 s) · hojas b<N>_a/b · M hallazgos: #x …, arreglados / pendientes`
Y al final: «revisión por bloques: 4/4 paradas, M arreglos». El reviewer lo lee: un fallo de la lista del §3 que llegue al render final con su bloque marcado «sin hallazgos» es un error de proceso del editor, y sube un nivel de severidad.
