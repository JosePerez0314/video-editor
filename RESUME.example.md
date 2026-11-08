# RESUME

Punto de entrada de cada sesión. Los agentes lo leen al empezar junto con `CLAUDE.md`.
Copia este archivo a `RESUME.md` (que no se sube a git) y mantenlo al día.

**Actualizado:** AAAA-MM-DD

## 0 · En curso — leer esto primero

Arranque: `claude --agent shorts-executive-producer` → «Lee RESUME.md y sigue con <slug>». El director lee también el `project-log.md` del slug.

| Slug | Estilo | Estado | Siguiente paso |
|---|---|---|---|
| `<slug>` (<tema>) | estilo-gabriel / estilo-monigotes | Idea / Guion listo / Falta voz / Prueba / Render / Revisión / ENTREGADO Rn | … |

**Preguntas abiertas al creador:** …

## 1 · Cómo arrancar

```bash
cd <RUTA_PROYECTO>
claude                                    # sesión normal
claude --agent shorts-executive-producer  # producir un short completo
```

- No usar modo plan con agentes trabajando.
- Short nuevo: *«Quiero hacer un short sobre <tema>. Referencias: <links>.»*

## 2 · Lo que el creador ya decidió (no volver a preguntar)

- …

## 3 · Entorno

- Node 24 (`source ~/.nvm/nvm.sh && nvm use 24`), FFmpeg, Python 3.12, whisper.cpp.
- Claves de ElevenLabs en `.env`.
