# Registro de ejecución de la búsqueda — 28 de septiembre de 2026

Protocolo: `protocolo/ACTA_protocolo_busqueda_review_2026-09-28.md` (commit 6f5d943) + enmiendas 1–3 (`protocolo/enmiendas/`).
Ejecutor: Emiliano (acceso vía pbidi UNAM); parsing y cribado asistidos por Claude, con validación pendiente del autor donde se indica en los CSV.

## Iteración 1 — cadena v1 (protocolo original)

| Base | Fecha | Cadena | Registros | Export |
|---|---|---|---|---|
| Web of Science (Core Collection) | 2026-09-28 | v1 (acta, sección 3) | 126 | `exports/wos_2026-09-28_iter1.ris` |
| Scopus | 2026-09-28 | v1 (acta, sección 3) | 144 | `exports/scopus_2026-09-28_iter1.csv` |

**Chequeo de sensibilidad: FALLÓ (3/6).** No recuperó Beer 2024 ("landscape community genomics"), Maillet 2025 ("genome-environmental analysis") ni el control Dorey (calibración). Causas documentadas en la Enmienda 1 → cadena v2 (bloque 1 ampliado).

Incidencia Scopus: error `RequestHeaderSectionTooLarge` vía pbidi; resuelto ejecutando en ventana de incógnito (sin cambio de sintaxis; Enmienda 1).

## Iteración 2 — cadena v2 (Enmienda 1) — DEFINITIVA

| Base | Fecha | Cadena | Registros | Export |
|---|---|---|---|---|
| Web of Science (Core Collection) | 2026-09-28 | v2 (Enmienda 1) | 194 | `exports/wos_2026-09-28_iter2.ris` |
| Scopus | 2026-09-28 | v2 (Enmienda 1) | 197 | `exports/scopus_2026-09-28_iter2.ris` |

**Chequeo de sensibilidad: PASÓ (6/6).** Los seis estudios conocidos del barrido preliminar fueron recuperados (ids 19, 45, 46, 69, 98, 134 en `cribado/dedup_iter2.csv`).

**OpenAlex (tercera base): PENDIENTE.** El piloto por API falló por límite de tasa (HTTP 429) y una URL demasiado larga (403) a través del proxy institucional. Queda como tarea: exportar vía interfaz web o reintentar API sin proxy, y correr la misma deduplicación contra los 227.

## Flujo (números finales, iteración 2)

```
Identificados:          391  (WoS 194 + Scopus 197)
Tras deduplicación:     227  (164 duplicados; DOI y título normalizado — cribado/scripts/dedup.py)
Excluidos título/resumen: 200  (razones por registro en cribado/decisiones_titulo_resumen_2026-09-28.csv)
A texto completo:        27  (17 INCLUIR-TC + 10 DUDOSO-TC)
Excluidos texto completo: 10  (razones por registro en cribado/decisiones_texto_completo_2026-09-28.csv)
INCLUIDOS (corpus):      17
```

Los 17 incluidos comprenden los 6 del barrido preliminar (declarados como conocimiento previo en el protocolo) + 11 nuevos: Sheppard 2022, Sheppard 2024, Pais 2020, Trumbo 2023, Smith 2019, Strickland 2023, Garroway 2013, Bellis 2020 (Enmienda 2), Vajana 2018 (Enmienda 2), Laccetti 2025 (Curr. Biol.) y Learmonth 2026 (Enmienda 3b). Laccetti 2025 (UFUG) quedó excluido a texto completo.

## Auditoría de correcciones/erratas del corpus

Revisión por búsqueda web (28/09/2026) de correcciones publicadas para los 17 incluidos + Dorey (control): **una encontrada** — Bellis et al. 2020, corrección PNAS 2025 (10.1073/pnas.2526590122; unidades de N del suelo, menor, no afecta los resultados bióticos; citar junto al original). Nota: la auditoría fue por búsqueda web, no contra el registro Crossref; el autor reportó haber hallado "un par" de correcciones — la segunda queda por identificar y verificar.
