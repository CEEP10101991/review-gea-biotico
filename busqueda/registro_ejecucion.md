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

**OpenAlex (tercera base): EJECUTADA (29/09/2026, desde copalera).** El piloto del 28/09 por proxy institucional falló (429/403); la ejecución definitiva corrió por API con polite pool. Corrida 1 (bloque 2 del acta 4.3): 189 registros, sensibilidad por base FALLÓ (Frachon 2019) → diagnóstico contra el PDF: el bloque 2 de OpenAlex estaba descalibrado respecto de WoS/Scopus (frase "biotic interaction" en lugar del término suelto `biotic`, sin "species interaction"/mutualis*/parasit*) → **Enmienda 4** (bloque 2 v2 alineado, sin comodines, con diagnóstico por DOI). Corrida definitiva: **253 registros**, sensibilidad **PASÓ (6/6)**; los 6 conocidos están en OpenAlex, 5 con resumen indexado (Beer 2024 sin resumen: `has_abstract=False`, recuperado por título). Detalle por consulta en `registro_ejecucion_openalex.md`. Deduplicación contra los 227: **99 exclusivos de OpenAlex**, cribados el 29/09 (`cribado/decisiones_titulo_resumen_openalex_2026-09-29.csv`): 96 EXCLUIR + 3 preprints elegibles a nivel resumen, excluidos por la regla de la **Enmienda 5** (solo estudios arbitrados; los preprints se citan como evidencia emergente). **Aporte neto de OpenAlex al corpus: 0. Corpus final: 17.**

## Flujo (números finales, iteración 2)

```
Identificados:          644  (WoS 194 + Scopus 197 + OpenAlex 253)
Tras deduplicación:     326  (227 WoS+Scopus + 99 exclusivos de OpenAlex)
Excluidos título/resumen: 299  (200 + 96 + 3 preprints por Enmienda 5; razones por registro en cribado/)
A texto completo:        27
Excluidos texto completo: 10  (razones por registro en cribado/decisiones_texto_completo_2026-09-28.csv)
INCLUIDOS (corpus):      18  (17 de bases + 1 por citation searching, Enmienda 6)
```

Los 17 incluidos comprenden los 6 del barrido preliminar (declarados como conocimiento previo en el protocolo) + 11 nuevos: Sheppard 2022, Sheppard 2024, Pais 2020, Trumbo 2023, Smith 2019, Strickland 2023, Garroway 2013, Bellis 2020 (Enmienda 2), Vajana 2018 (Enmienda 2), Laccetti 2025 (Curr. Biol.) y Learmonth 2026 (Enmienda 3b). Laccetti 2025 (UFUG) quedó excluido a texto completo.

## Búsqueda complementaria por referencias — citation searching (Enmienda 6, 29/09/2026)

Cruce contra la base suplementaria de Dauphin et al. 2023 (mmc1; 278 estudios retenidos, 34 con variable biótica): 22 ya en nuestro universo; 12 evaluados con los criterios vigentes; 11 excluidos con razón (acta de la Enmienda 6); 1 a texto completo e **INCLUIDO**: Rosenthal et al. 2021 (10.1111/eva.13236; depredación medida como predictor, gupis de Hawai). Causa del no-hallazgo por cadenas: variante "environment association tests". **Corpus final: 18 estudios** (6 preliminares + 11 de bases + 1 por citation searching).

## Auditoría de correcciones/erratas del corpus

Revisión por búsqueda web (28/09/2026) de correcciones publicadas para los 17 incluidos + Dorey (control): **una encontrada** — Bellis et al. 2020, corrección PNAS 2025 (10.1073/pnas.2526590122; unidades de N del suelo, menor, no afecta los resultados bióticos; citar junto al original). Nota: la auditoría fue por búsqueda web, no contra el registro Crossref; el autor reportó haber hallado "un par" de correcciones — la segunda queda por identificar y verificar.
