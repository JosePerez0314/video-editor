---
name: protocolo-nocturno
description: Modo desatendido del director (shorts-executive-producer). Se activa cuando el creador dice que se va a dormir o que no estará ("me voy a dormir", "quiero dormir", "modo noche", "trabaja sin mí"). Prioriza terminar el trabajo en curso sin interrupciones, deja todo lo que requiera permiso para el final en una cola de aprobaciones y entrega un resumen al volver.
---

# Skill: protocolo nocturno (NIGHT EXECUTION PROTOCOL)

Pedido del creador (2026-11-04): «para cuando te diga que quiero dormir lo actives … para que deje todo al final, y lo de los permisos, si aplica, se queden al final para no interrumpir el trabajo». Antes: «tu prioridad es acabarlo».

## 0 · Al activarlo (antes de que el creador se vaya)
1. Comprueba en un comando que los permisos que harán falta están en `.claude/settings.json` (`npx`, `node`, `python3`, `ffmpeg`, `curl`, `cp`, `mv`…). Si falta alguno **imprescindible**, pídelo ahora, no a mitad de la noche.
2. Recuerda al creador: dejar el ordenador encendido, sin suspender, y la sesión abierta.
3. Escribe en el `project-log.md` del slug: «Protocolo nocturno activado» + objetivo de la noche + sus palabras.
4. Crea o vacía la cola: `nichos/shorts/aprobaciones-pendientes.md`.

## 1 · Reglas de ejecución
1. Ejecuta todo lo que **no** necesite autorización explícita del creador.
2. **Nunca** interrumpas el trabajo para pedir permiso en operaciones no críticas.
3. Si una operación necesita aprobación, **no la hagas**: apúntala en la cola (§3) y sigue.
4. Sigue con tareas independientes siempre que se pueda.
5. **Nunca** te saltes el sistema de permisos, restricciones de seguridad ni requisitos de autorización (ni `bypassPermissions`, ni editar `settings.json` para autoconcederse permisos, ni rodeos para hacer lo mismo por otra vía).
6. No supongas que una aprobación pendiente se ha concedido.
7. **Alternativas autorizadas antes que cola:** p. ej. en lugar de `rm`, mover a `_papelera/` con `mv` o dejar el archivo; en lugar de sobrescribir, versionar `_rN`.
8. **Solo emergencias de verdad despiertan al creador:** sin esa acción el objetivo de la noche no se puede terminar *y* no hay alternativa. Aun así, primero termina todo lo demás.

## 2 · Reglas propias de shorts (aprendidas)
- **Un solo agente Opus a la vez** (el límite de 5 h cortó dos renders el 2026-11-03). Investigación y análisis, no de noche salvo que no haya render.
- **Límite de uso (429 «5-hour limit · resets HH:MM»):** anota hora y estado en el disco, arma un temporizador hasta la hora de reinicio + 5 min (`sleep` con Bash en segundo plano) y relanza el encargo **desde lo que haya en disco**, sin rehacer.
- **En cada encargo nocturno añade:** «Modo desatendido: si un comando necesita permiso, no lo ejecutes; usa una alternativa autorizada o anótalo en tu informe y sigue. No esperes respuesta del creador.»
- Flujo habitual: terminar render → comprobar en disco (ffprobe, ebur128, sha256, `comprobar_catalogo.py`) → revisión → **como máximo la ronda automática 1** → parar. No hay entregas finales ni decisiones creativas sin el creador.
- Gastos (ElevenLabs, etc.): solo los ya autorizados para ese video.
- Informes cada 45 min: siguen escribiéndose en el chat aunque nadie los lea.

## 3 · Cola de aprobaciones (`nichos/shorts/aprobaciones-pendientes.md`)

| # | Operación | Por qué necesita autorización | Agente que la pide | Qué bloquea / dependencias | Hora |
|---|---|---|---|---|---|

## 4 · Resumen al volver (en el chat y al final del `project-log.md`)
1. **Completado** (con rutas y medidas verificadas).
2. **Fallido** (causa y si se reintentó).
3. **Bloqueado** (qué lo bloquea).
4. **Aprobaciones pendientes** (la cola, numerada, para responder «sí 1, 3; no 2»).
5. **Siguientes pasos recomendados.**
6. Tokens de la noche (líneas `tokens ·`).

Prioridad: ejecución autónoma **segura**, sin comprometer seguridad ni integridad de los datos.
