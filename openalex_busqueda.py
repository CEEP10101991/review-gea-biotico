#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Búsqueda OpenAlex — protocolo review-gea-biotico, sección 4.3, con cadena v2 (Enmienda 1).
Ejecutar DESDE la raíz del repo en copalera:  python3 openalex_busqueda.py
Salidas (en busqueda/exports/ y busqueda/):
  - openalex_<fecha>.json  (unión de registros crudos, deduplicada por ID de OpenAlex)
  - openalex_<fecha>.csv   (aplanado: id, doi, titulo, anio, revista, autores, resumen)
  - registro_ejecucion_openalex.md  (sintaxis final ejecutada + conteos + sensibilidad)

Adaptación de sintaxis (contingencia prefijada, acta sección 4.3 in fine):
OpenAlex no acepta comodines (*) dentro del search; se usan las frases de la cadena v2
sin comodín y se confía en el stemming propio de OpenAlex (association/associations,
analysis/analyses). La sintaxis final por consulta queda registrada en el .md.
"""
import urllib.request, urllib.parse, json, time, csv, datetime, sys, os

MAILTO = "saltamontes1991@gmail.com"   # polite pool
FECHA = datetime.date.today().isoformat()

# Bloque 1 — cadena v2 (Enmienda 1), sin comodines (stemming de OpenAlex)
BLOQUE1 = [
    '"landscape genomics"',
    '"landscape community genomics"',
    '"genotype-environment association"',
    '"genotype environment association"',
    '"genome-environment association"',
    '"genome-environmental analysis"',
    '"gene-environment association"',
    '"environmental association analysis"',
]
# Bloque 2 — acta sección 4.3 (consulta OpenAlex prefijada)
BLOQUE2 = ('("biotic interaction" OR pollinator OR herbivory OR frugivore OR '
           '"seed dispersal" OR microbiota OR pathogen OR disease OR predator)')

# Chequeo de sensibilidad prefijado: los 6 conocidos del barrido preliminar
CONOCIDOS = {
    "10.1093/molbev/msz078":        "Frachon 2019",
    "10.1093/molbev/msad036":       "Frachon 2023",
    "10.1093/molbev/msad093":       "Roux 2023",
    "10.1111/1462-2920.70108":      "Maillet 2025",
    "10.1111/evo.14023":            "Fraik 2020",
    "10.1038/s41559-023-02265-9":   "Beer 2024",
}

def get(url, intentos=5):
    for i in range(intentos):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 429:
                espera = 2 ** (i + 1)
                print(f"  429: esperando {espera}s...", file=sys.stderr)
                time.sleep(espera)
                continue
            raise
    raise RuntimeError("Demasiados 429; reintentar más tarde")

def abstract_desde_indice(inv):
    if not inv:
        return ""
    pos = {}
    for palabra, idxs in inv.items():
        for ix in idxs:
            pos[ix] = palabra
    return " ".join(pos[k] for k in sorted(pos))[:3000]

union, urls_ejecutadas, conteos = {}, [], []
for frase in BLOQUE1:
    expr = f'{frase} AND {BLOQUE2}'
    filtro = urllib.parse.quote(f"title_and_abstract.search:{expr}")
    cursor, n_consulta = "*", 0
    while cursor:
        url = (f"https://api.openalex.org/works?filter={filtro}"
               f"&per-page=200&cursor={urllib.parse.quote(cursor)}&mailto={MAILTO}")
        d = get(url)
        if n_consulta == 0:
            urls_ejecutadas.append((expr, d["meta"]["count"]))
            print(f"[{frase}] -> {d['meta']['count']} registros")
        for w in d["results"]:
            union[w["id"]] = w
        n_consulta += len(d["results"])
        cursor = d["meta"].get("next_cursor")
        time.sleep(0.2)
    conteos.append((frase, n_consulta))

print(f"\nUnión (dedup por ID OpenAlex): {len(union)} registros")

os.makedirs("busqueda/exports", exist_ok=True)
raw_path = f"busqueda/exports/openalex_{FECHA}.json"
with open(raw_path, "w") as f:
    json.dump(list(union.values()), f)

csv_path = f"busqueda/exports/openalex_{FECHA}.csv"
with open(csv_path, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["openalex_id", "doi", "titulo", "anio", "revista", "autores", "resumen"])
    for wk in union.values():
        doi = (wk.get("doi") or "").replace("https://doi.org/", "")
        rev = ((wk.get("primary_location") or {}).get("source") or {}).get("display_name", "")
        auts = "; ".join(a["author"]["display_name"] for a in (wk.get("authorships") or [])[:12])
        w.writerow([wk["id"], doi, wk.get("title") or "", wk.get("publication_year") or "",
                    rev, auts, abstract_desde_indice(wk.get("abstract_inverted_index"))])

# Sensibilidad
dois_union = {(wk.get("doi") or "").replace("https://doi.org/", "").lower()
              for wk in union.values()}
faltan = {d: n for d, n in CONOCIDOS.items() if d.lower() not in dois_union}
sens = "PASÓ (6/6)" if not faltan else f"FALLÓ: faltan {faltan}"
print("Chequeo de sensibilidad:", sens)

with open("busqueda/registro_ejecucion_openalex.md", "w") as f:
    f.write(f"# Ejecución OpenAlex — {FECHA}\n\n"
            f"API `title_and_abstract.search`, cadena v2 sin comodines (stemming de OpenAlex; "
            f"contingencia de sintaxis prefijada en el acta, sección 4.3). Polite pool: {MAILTO}.\n\n"
            f"| Consulta (sintaxis final) | Registros |\n|---|---|\n")
    for expr, c in urls_ejecutadas:
        f.write(f"| `{expr}` | {c} |\n")
    f.write(f"\nUnión deduplicada por ID de OpenAlex: **{len(union)}** registros "
            f"(`exports/openalex_{FECHA}.json`, `.csv`).\n\n"
            f"**Chequeo de sensibilidad (6 conocidos): {sens}**\n\n"
            f"Pendiente: deduplicar contra los 227 de WoS+Scopus y cribar solo los registros nuevos.\n")

print(f"\nListo: {raw_path}, {csv_path}, busqueda/registro_ejecucion_openalex.md")
