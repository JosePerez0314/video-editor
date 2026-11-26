#!/usr/bin/env python3
"""Estimación del consumo de la sesión (5 h) y semanal de Claude sin abrir el navegador.

Suma los tokens que Claude Code guarda en local (~/.claude/projects/**/*.jsonl, hilo
principal y subagentes) y los convierte a % con una calibración que alimenta el creador
con sus lecturas reales (/usage o Ajustes → Uso).

Uso:
  python3 consumo_sesion.py                      # estimación actual
  python3 consumo_sesion.py --calibrar 32 62     # guarda una lectura real (sesión %, semanal %)
  python3 consumo_sesion.py --detalle            # tokens por modelo en la ventana

Límites conocidos: solo ve lo que corre en ESTE equipo con Claude Code (no claude.ai web
ni otros equipos); los pesos por modelo y por caché son hipótesis que se corrigen con las
calibraciones. Creador, 2026-11-24: «usa la segunda, e iremos alimentando hasta que le atines bien».
"""
import argparse, glob, json, os, statistics
from datetime import datetime, timedelta, timezone

RAIZ = os.path.expanduser('~/.claude/projects')
CAL = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'consumo_calibracion.json')
VENTANA = timedelta(hours=5)
# Reinicio semanal (hora local). Visto en claude.ai el 21-nov: «sáb 02:00».
REINICIO_SEMANAL = {'dia': 5, 'hora': 2}  # lunes=0 … sábado=5
# Pesos (hipótesis iniciales; la calibración absorbe el error global, no el reparto).
PESO_MODELO = {'opus': 1.0, 'sonnet': 0.6, 'haiku': 0.2}
PESO_CACHE_LECTURA = 0.0  # 24-nov: con 0.1 el editor daba +100 puntos en 40 min (imposible); la caché no parece contar


def familia(modelo):
    m = (modelo or '').lower()
    for f in PESO_MODELO:
        if f in m:
            return f
    return 'opus'


def leer_eventos():
    vistos, ev = set(), []
    for f in glob.glob(os.path.join(RAIZ, '**', '*.jsonl'), recursive=True):
        try:
            fh = open(f, encoding='utf-8', errors='ignore')
        except OSError:
            continue
        with fh:
            for linea in fh:
                if '"usage"' not in linea:
                    continue
                try:
                    d = json.loads(linea)
                except ValueError:
                    continue
                msg = d.get('message') or {}
                u = msg.get('usage')
                ts = d.get('timestamp')
                if not u or not ts:
                    continue
                clave = (msg.get('id'), d.get('requestId'))
                if clave != (None, None):
                    if clave in vistos:
                        continue
                    vistos.add(clave)
                t = datetime.fromisoformat(ts.replace('Z', '+00:00'))
                fam = familia(msg.get('model'))
                bruto = (u.get('input_tokens', 0) + u.get('output_tokens', 0)
                         + u.get('cache_creation_input_tokens', 0))
                lect = u.get('cache_read_input_tokens', 0)
                peso = PESO_MODELO[fam] * (bruto + PESO_CACHE_LECTURA * lect)
                ev.append((t, fam, bruto, lect, peso))
    ev.sort()
    return ev


def inicio_bloque(ev, ahora):
    """Bloques de 5 h: empieza con el primer mensaje tras expirar el anterior."""
    ini = None
    for t, *_ in ev:
        if t > ahora:
            break
        if ini is None or t >= ini + VENTANA:
            ini = t
    if ini is None or ahora >= ini + VENTANA:
        return None
    return ini


def inicio_semana(ahora_local):
    d = ahora_local.replace(hour=REINICIO_SEMANAL['hora'], minute=0, second=0, microsecond=0)
    d -= timedelta(days=(d.weekday() - REINICIO_SEMANAL['dia']) % 7)
    if d > ahora_local:
        d -= timedelta(days=7)
    return d


def sumar(ev, desde, hasta):
    r = {'peso': 0.0, 'por_modelo': {}}
    for t, fam, bruto, lect, peso in ev:
        if desde <= t <= hasta:
            r['peso'] += peso
            m = r['por_modelo'].setdefault(fam, [0, 0])
            m[0] += bruto
            m[1] += lect
    return r


def cargar_cal():
    if os.path.exists(CAL):
        return json.load(open(CAL))
    return []


def factor(cal, campo_pct, campo_tok):
    xs = [c[campo_tok] / c[campo_pct] for c in cal if c.get(campo_pct)]
    return statistics.median(xs) if xs else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--calibrar', nargs=2, type=float, metavar=('SESION', 'SEMANAL'))
    ap.add_argument('--detalle', action='store_true')
    a = ap.parse_args()

    ahora = datetime.now(timezone.utc)
    ahora_local = datetime.now().astimezone()
    ev = leer_eventos()
    ini = inicio_bloque(ev, ahora)
    ses = sumar(ev, ini, ahora) if ini else {'peso': 0.0, 'por_modelo': {}}
    sem_ini = inicio_semana(ahora_local).astimezone(timezone.utc)
    sem = sumar(ev, sem_ini, ahora)

    if a.calibrar:
        cal = cargar_cal()
        cal.append({'fecha': ahora_local.isoformat(timespec='minutes'),
                    'sesion_pct': a.calibrar[0], 'semanal_pct': a.calibrar[1],
                    'tok_sesion': round(ses['peso']), 'tok_semana': round(sem['peso'])})
        json.dump(cal, open(CAL, 'w'), indent=1, ensure_ascii=False)
        print(f'Calibración guardada ({len(cal)} lecturas) en {CAL}')

    cal = cargar_cal()
    # Recalcula los tokens de cada calibración con los pesos actuales (así cambiar un peso no la invalida).
    for c in cal:
        tc = datetime.fromisoformat(c['fecha']).astimezone(timezone.utc)
        ic = inicio_bloque(ev, tc)
        c['tok_sesion'] = sumar(ev, ic, tc)['peso'] if ic else 0
        c['tok_semana'] = sumar(ev, inicio_semana(tc.astimezone()).astimezone(timezone.utc), tc)['peso']
    ks, kw = factor(cal, 'sesion_pct', 'tok_sesion'), factor(cal, 'semanal_pct', 'tok_semana')
    # Con 2+ lecturas: pendiente entre lecturas (Δtokens/Δ%) + desfase (uso que no vemos o de antes del bloque).
    off_s = off_w = 0.0
    def ajuste(cp, ct):
        ps = [(c[ct], c[cp]) for c in cal]
        pend = [(b[0]-a[0])/(b[1]-a[1]) for a, b in zip(ps, ps[1:]) if b[1] > a[1] and b[0] > a[0]]
        if not pend:
            return None, 0.0
        k = statistics.median(pend)
        return k, statistics.median([p - t/k for t, p in ps])
    k2, o2 = ajuste('sesion_pct', 'tok_sesion')
    if k2: ks, off_s = k2, o2
    k3, o3 = ajuste('semanal_pct', 'tok_semana')
    if k3: kw, off_w = k3, o3
    fin = (ini + VENTANA).astimezone() if ini else None
    print(f'Bloque de 5 h: {ini.astimezone():%H:%M} → {fin:%H:%M}' if ini else 'Bloque de 5 h: sin actividad (sesión reiniciada)')
    print(f'Tokens ponderados · sesión {ses["peso"]/1e3:,.0f}K · semana (desde {inicio_semana(ahora_local):%a %d %H:%M}) {sem["peso"]/1e3:,.0f}K')
    if ks:
        print(f'≈ Sesión {off_s + ses["peso"]/ks:.0f} % · ≈ {ks/1e3:,.1f}K por punto ({len(cal)} calibraciones)')
    if kw:
        print(f'≈ Semanal {off_w + sem["peso"]/kw:.0f} % · ≈ {kw/1e3:,.1f}K por punto')
    if not (ks or kw):
        print('Sin calibrar: pasa una lectura real con --calibrar SESION SEMANAL')
    if a.detalle:
        for fam, (b, l) in sorted(ses['por_modelo'].items()):
            print(f'  {fam}: {b/1e3:,.0f}K directos · {l/1e3:,.0f}K de caché (sesión)')


if __name__ == '__main__':
    main()
