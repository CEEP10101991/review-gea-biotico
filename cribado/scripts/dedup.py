#!/usr/bin/env python3
"""Deduplicación de exports de búsqueda sistemática (WoS RIS, Scopus CSV, OpenAlex JSON).

Uso:  python3 dedup.py ../busqueda/exports/ -o ../deduplicados.csv
Regla (acta, sección 5.1): clave primaria = DOI normalizado; sin DOI, título normalizado.
Se conserva el registro con más campos llenos; la columna fuente_bases acumula las bases.
Este script no filtra ni excluye: solo colapsa duplicados. El cribado es aparte.
"""
import argparse, csv, json, re, sys
from pathlib import Path

def norm_doi(d):
    if not d: return ""
    d = d.strip().lower()
    d = re.sub(r"^(https?://)?(dx\.)?doi\.org/", "", d)
    d = re.sub(r"^doi:\s*", "", d)
    return d

def norm_title(t):
    return re.sub(r"[^a-z0-9]", "", (t or "").lower())

def parse_ris(path):
    recs, cur = [], {}
    tagmap = {"TI": "titulo", "T1": "titulo", "AB": "resumen", "PY": "anio",
              "Y1": "anio", "DO": "doi", "JO": "revista", "T2": "revista", "JF": "revista"}
    for line in path.read_text(errors="replace").splitlines():
        m = re.match(r"^([A-Z][A-Z0-9])  - ?(.*)$", line)
        if not m: continue
        tag, val = m.group(1), m.group(2).strip()
        if tag == "TY":
            cur = {"autores": []}
        elif tag == "ER":
            if cur: recs.append(cur); cur = {}
        elif tag == "AU":
            cur.setdefault("autores", []).append(val)
        elif tag in tagmap:
            k = tagmap[tag]
            if k == "anio": val = val[:4]
            if k not in cur or not cur[k]: cur[k] = val
    return recs

def parse_csv(path):
    recs = []
    with open(path, newline="", encoding="utf-8-sig", errors="replace") as f:
        for row in csv.DictReader(f):
            low = {k.strip().lower(): (v or "").strip() for k, v in row.items() if k}
            recs.append({
                "titulo": low.get("title") or low.get("article title") or low.get("titulo", ""),
                "anio": (low.get("year") or low.get("publication year") or "")[:4],
                "doi": low.get("doi", ""),
                "revista": low.get("source title") or low.get("journal") or low.get("revista", ""),
                "resumen": low.get("abstract") or low.get("resumen", ""),
                "autores": [a.strip() for a in re.split(r";|\|", low.get("authors") or low.get("author full names", "")) if a.strip()],
            })
    return recs

def parse_openalex_json(path):
    data = json.loads(path.read_text(errors="replace"))
    works = data.get("results", data if isinstance(data, list) else [])
    recs = []
    for w in works:
        recs.append({
            "titulo": w.get("display_name", ""),
            "anio": str(w.get("publication_year", "")),
            "doi": norm_doi(w.get("doi", "")),
            "revista": ((w.get("primary_location") or {}).get("source") or {}).get("display_name", ""),
            "resumen": "",  # OpenAlex da abstract_inverted_index; reconstruir si se necesita
            "autores": [(a.get("author") or {}).get("display_name", "") for a in w.get("authorships", [])],
        })
    return recs

def base_from_name(name):
    n = name.lower()
    for b in ("wos", "scopus", "openalex"):
        if b in n: return b
    return name

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("exports_dir")
    ap.add_argument("-o", "--out", default="deduplicados.csv")
    args = ap.parse_args()
    d = Path(args.exports_dir)
    allrecs = []
    for p in sorted(d.iterdir()):
        if p.suffix.lower() == ".ris": recs = parse_ris(p)
        elif p.suffix.lower() == ".csv": recs = parse_csv(p)
        elif p.suffix.lower() == ".json": recs = parse_openalex_json(p)
        else: continue
        for r in recs: r["fuente_bases"] = base_from_name(p.name)
        print(f"{p.name}: {len(recs)} registros", file=sys.stderr)
        allrecs.extend(recs)
    seen, out = {}, []
    for r in allrecs:
        key = ("doi", norm_doi(r.get("doi"))) if norm_doi(r.get("doi")) else ("ti", norm_title(r.get("titulo")))
        if not key[1]:
            out.append(r); continue
        if key in seen:
            prev = seen[key]
            prev["fuente_bases"] = ";".join(sorted(set(prev["fuente_bases"].split(";")) | {r["fuente_bases"]}))
            if sum(bool(v) for v in r.values()) > sum(bool(v) for v in prev.values()):
                r["fuente_bases"] = prev["fuente_bases"]
                seen[key] = r
                out[out.index(prev)] = r
        else:
            seen[key] = r
            out.append(r)
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "doi", "titulo", "anio", "revista", "autores", "fuente_bases", "resumen"])
        for i, r in enumerate(out, 1):
            w.writerow([i, norm_doi(r.get("doi", "")), r.get("titulo", ""), r.get("anio", ""),
                        r.get("revista", ""), "; ".join(r.get("autores", [])), r.get("fuente_bases", ""), r.get("resumen", "")])
    print(f"Total: {len(allrecs)} → deduplicados: {len(out)} → {args.out}", file=sys.stderr)

if __name__ == "__main__":
    main()
