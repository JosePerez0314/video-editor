#!/usr/bin/env python3
"""Comprobación automática de los 4 pilares del guion (skill guion-4-pilares.md).

Uso: python3 nichos/shorts/herramientas/comprobar_guion.py <slug>.guion-voz.md
Sale con 0 si pasa (puede haber AVISOS) y con 1 si hay algún ERROR.
Umbrales sacados de ideas-virales/ANALISIS-series-es.md (24-nov-2026).
"""
import re
import sys
import unicodedata

import yaml

UMBRALES = {
    "primera_frase_max_s": 8.0,        # D1
    "primera_frase_max_palabras": 25,  # D1
    "textual_max_t_s": 2.0,            # D4
    "max_hueco_tension_s": 9.0,        # D5
    "ultimo_dato_min_frac": 0.75,      # D6
    "revelacion_min_frac": 0.65,       # D7
    "min_beats": 4,
    "max_tropos": 2,                   # D16: 3 o más = aviso
    "max_entonces": 3,                 # D17
    "cta_min_s": 6.0,                  # D12
    "cta_max_s": 18.0,                 # D12
    "dur_serie_min_s": 60.0,           # D13
    "dur_serie_max_s": 110.0,          # D13
    "pps_min": 2.4,                    # D14 (palabras por segundo de video)
    "pps_max": 2.9,
}
APERTURAS_EVITAR = [  # D9
    (r"^este es \w+", "«Este es X…» (Paco, el de menos fuerza en su grupo)"),
    (r"^¿?\s*qué harías si", "«¿Qué harías si…?» (Abigail, el de menos vistas)"),
    (r"^hola\b", "saludo"),
]
PALABRAS_DORMIDO = ["dormid", "ojos cerrados", "duerme", "durmiendo"]
CTA_MITAD = r"\b(s[ií]gueme|dale like|dale me gusta|suscr[ií]bete)\b"

errores, avisos, oks = [], [], []


def norm(s):
    s = unicodedata.normalize("NFD", str(s).lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^\w\s?¿]", " ", s).split()


def contiene(texto, frase):
    t, f = " ".join(norm(texto)), " ".join(norm(frase))
    return bool(f) and f in t


def falla(msg, numerico, adaptacion):
    (avisos if (numerico and adaptacion) else errores).append(msg)


def vacio(v):
    return v is None or (isinstance(v, str) and not v.strip()) or v == []


def main(ruta):
    md = open(ruta, encoding="utf-8").read()
    m = re.search(r"```ficha-4-pilares\n(.*?)```", md, re.S)
    if not m:
        print(f"ERROR · {ruta}: falta el bloque ```ficha-4-pilares``` (skill guion-4-pilares.md)")
        return 1
    f = yaml.safe_load(m.group(1)) or {}
    resto = md[: m.start()] + md[m.end():]
    bloques = re.findall(r"```[^\n]*\n(.*?)```", resto, re.S)
    texto = "\n".join(bloques) if bloques else resto
    estilo = f.get("estilo", "")
    serie = estilo == "estilo-serie-pov"
    adapt = f.get("modo") == "adaptacion"
    dur = float(f.get("duracion_s") or 0)
    g, r, p, c = (f.get(k) or {} for k in ("gancho", "retencion", "profundizacion", "cta"))

    if dur <= 0:
        errores.append("duracion_s vacía")
        dur = 1.0

    # ---- 1 · Gancho
    for k in ("verbal", "premisa_quien", "premisa_amenaza", "curiosidad", "textual", "visual_cuadro0"):
        if vacio(g.get(k)):
            errores.append(f"Gancho: falta `{k}`")
    verbal = g.get("verbal") or ""
    if verbal and not contiene(texto, verbal):
        errores.append("Gancho: la frase `verbal` no aparece literal en el guion")
    np = len(norm(verbal))
    if np > UMBRALES["primera_frase_max_palabras"]:
        falla(f"Gancho: primera frase de {np} palabras (máx. {UMBRALES['primera_frase_max_palabras']})", True, adapt)
    fin = g.get("fin_primera_frase_s")
    if fin is None:
        errores.append("Gancho: falta `fin_primera_frase_s`")
    elif float(fin) > UMBRALES["primera_frase_max_s"]:
        falla(f"Gancho: la primera frase acaba a {fin} s (máx. {UMBRALES['primera_frase_max_s']})", True, adapt)
    v0 = " ".join(norm(verbal))
    for pat, nombre in APERTURAS_EVITAR:
        if re.search(pat, v0):
            avisos.append(f"Gancho: apertura a evitar: {nombre}")
    if v0.startswith("imagina") and not serie:
        avisos.append("Gancho: «Imagina…» solo está admitido en estilo-serie-pov (plan-escenas.md)")
    tt = g.get("textual_t_s")
    if tt is not None and float(tt) > UMBRALES["textual_max_t_s"]:
        falla(f"Gancho: el texto ancla entra a {tt} s (máx. {UMBRALES['textual_max_t_s']})", True, adapt)
    if g.get("cuadro0_despierto_o_movimiento") is not True:
        falla("Gancho: el cuadro 0 no tiene a alguien despierto o algo en movimiento", False, adapt)
    vis = " ".join(norm(g.get("visual_cuadro0") or ""))
    if any(w in vis for w in PALABRAS_DORMIDO):
        falla("Gancho: el cuadro 0 describe a alguien dormido (0/10 virales lo hacen)", False, adapt)
    if not errores:
        oks.append("Gancho (verbal, textual y visual)")

    # ---- 2 · Retención
    n_err = len(errores)
    for k in ("revelacion", "pregunta_sin_resolver", "competencia_suelta", "nuestro_giro"):
        if vacio(r.get(k)):
            errores.append(f"Retención: falta `{k}`")
    if not vacio(r.get("nuestro_giro")) and contiene(r.get("competencia_suelta") or "", r.get("nuestro_giro")):
        errores.append("Retención: `nuestro_giro` repite lo que hace la competencia")
    rev = r.get("revelacion_t_s")
    if rev is None:
        errores.append("Retención: falta `revelacion_t_s`")
    elif float(rev) / dur < UMBRALES["revelacion_min_frac"]:
        falla(f"Retención: revelación al {100*float(rev)/dur:.0f} % (mín. {100*UMBRALES['revelacion_min_frac']:.0f} %)", True, adapt)
    ult = r.get("ultimo_dato_nuevo_t_s")
    if ult is None:
        errores.append("Retención: falta `ultimo_dato_nuevo_t_s`")
    elif float(ult) / dur < UMBRALES["ultimo_dato_min_frac"]:
        falla(f"Retención: último dato nuevo al {100*float(ult)/dur:.0f} % (mín. {100*UMBRALES['ultimo_dato_min_frac']:.0f} %)", True, adapt)
    subs = sorted(float(x) for x in (r.get("subidas_tension_s") or []))
    fin_t = float(c.get("t_inicio_s") or dur)
    if not subs:
        errores.append("Retención: faltan `subidas_tension_s`")
    else:
        puntos = [0.0] + subs + [fin_t]
        huecos = [(b - a, a, b) for a, b in zip(puntos, puntos[1:]) if b >= a]
        peor = max(huecos)
        if peor[0] > UMBRALES["max_hueco_tension_s"]:
            falla(f"Retención: {peor[0]:.1f} s sin subir la tensión ({peor[1]:.1f}→{peor[2]:.1f} s; máx. {UMBRALES['max_hueco_tension_s']})", True, adapt)
    if len(errores) == n_err:
        oks.append("Retención")

    # ---- 3 · Profundización
    n_err = len(errores)
    beats = p.get("beats") or []
    if len(beats) < UMBRALES["min_beats"]:
        errores.append(f"Profundización: {len(beats)} beats (mín. {UMBRALES['min_beats']})")
    if vacio(p.get("diferenciador")):
        errores.append("Profundización: falta `diferenciador`")
    if serie and p.get("persona") != 2:
        falla("Profundización: en estilo-serie-pov la narración va en 2.ª persona (`persona: 2`)", False, adapt)
    tropos = p.get("tropos") or []
    if len(tropos) > UMBRALES["max_tropos"]:
        msg = f"Profundización: {len(tropos)} tropos saturados ({', '.join(tropos)})"
        if vacio(p.get("tropos_justificacion")):
            errores.append(msg + " sin `tropos_justificacion`")
        else:
            avisos.append(msg + " (justificados)")
    n_ent = len(re.findall(r"\bentonces\b", texto, re.I))
    if n_ent > UMBRALES["max_entonces"]:
        avisos.append(f"Profundización: «entonces» {n_ent} veces (máx. {UMBRALES['max_entonces']})")
    cta_frase = c.get("frase") or ""
    corte = int(len(texto) * 0.7)  # lo pedido en el 70 % inicial del texto cuenta como «a mitad»
    if re.search(CTA_MITAD, texto[:corte], re.I):
        avisos.append("Profundización: pide seguir/like a mitad del video (solo al final)")
    if serie and not (UMBRALES["dur_serie_min_s"] <= dur <= UMBRALES["dur_serie_max_s"]):
        falla(f"Profundización: duración {dur:.0f} s fuera de {UMBRALES['dur_serie_min_s']:.0f}–{UMBRALES['dur_serie_max_s']:.0f} s", True, adapt)
    pal = len(norm(texto))
    pps = pal / dur
    if not (UMBRALES["pps_min"] <= pps <= UMBRALES["pps_max"]):
        avisos.append(f"Profundización: {pps:.2f} palabras/s de video ({pal} palabras en {dur:.0f} s; rango {UMBRALES['pps_min']}–{UMBRALES['pps_max']})")
    if len(errores) == n_err:
        oks.append("Profundización")

    # ---- 4 · CTA
    n_err = len(errores)
    for k in ("frase", "opcion_a", "coste_a", "opcion_b", "coste_b", "razon_para_volver"):
        if vacio(c.get(k)):
            errores.append(f"CTA: falta `{k}`")
    if cta_frase and not contiene(texto, cta_frase):
        errores.append("CTA: la `frase` no aparece literal en el guion")
    if cta_frase and "?" not in cta_frase and not re.search(r"coment|vota|elige", cta_frase, re.I):
        errores.append("CTA: la frase final no pregunta ni pide elegir (un «Sígueme» solo no es CTA)")
    if c.get("en_pantalla") is not True:
        errores.append("CTA: las opciones A/B no están en pantalla (`en_pantalla: true`)")
    if c.get("comenta_dicho") is not True:
        avisos.append("CTA: no se dice «Comenta A si… o B si…» (recomendado: 3 de los 4 grandes)")
    if c.get("t_inicio_s") is None:
        errores.append("CTA: falta `t_inicio_s`")
    else:
        bloque = dur - float(c["t_inicio_s"])
        if not (UMBRALES["cta_min_s"] <= bloque <= UMBRALES["cta_max_s"]):
            falla(f"CTA: bloque de {bloque:.1f} s (rango {UMBRALES['cta_min_s']:.0f}–{UMBRALES['cta_max_s']:.0f} s)", True, adapt)
    if len(errores) == n_err:
        oks.append("CTA")

    if f.get("excepcion_creador"):
        avisos.append(f"Excepción del creador: {f['excepcion_creador']}")

    print(f"Comprobación 4 pilares · {ruta}")
    print(f"estilo {estilo or '¿?'} · modo {f.get('modo', 'propio')} · {dur:.0f} s · {pal} palabras")
    for o in oks:
        print(f"  OK     {o}")
    for a in avisos:
        print(f"  AVISO  {a}")
    for e in errores:
        print(f"  ERROR  {e}")
    print("RESULTADO:", "NO PASA (corregir antes de entregar)" if errores else "PASA")
    return 1 if errores else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
