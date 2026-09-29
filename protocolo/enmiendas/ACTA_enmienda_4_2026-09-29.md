# Enmienda 4 al protocolo de búsqueda — 29 de septiembre de 2026

**Protocolo enmendado:** `ACTA_protocolo_busqueda_review_2026-09-28.md` (commit 6f5d943), sección 4.3 (OpenAlex), con Enmiendas 1–3.
**Motivo:** la ejecución de OpenAlex (29/09/2026, 189 registros) falló el chequeo de sensibilidad por base: no recuperó Frachon et al. 2019 (10.1093/molbev/msz078).

## Diagnóstico (verificado contra el PDF de Frachon 2019)

1. El bloque 2 de la consulta OpenAlex prefijada en la sección 4.3 difería del bloque 2 ejecutado en WoS y Scopus: usaba la frase `"biotic interaction"` y omitía el término suelto `biotic`, además de `"species interaction"`, `mutualis*` y `parasit*`.
2. El resumen de Frachon 2019 contiene "biotic adaptation" y "plant–plant interactions", pero **no** la frase "biotic interaction". En WoS/Scopus el registro se recupera por el término suelto `biotic`; en la consulta OpenAlex 4.3, no había término que lo capturara.
3. El chequeo de sensibilidad prefijado del acta (sección 6) se define sobre la **búsqueda combinada**, que sigue en 6/6 (WoS y Scopus recuperan los seis). El fallo aquí es de la base individual y de la transcripción de la cadena, y se corrige para mantener la congruencia entre bases.

## Corrección: bloque 2 de OpenAlex alineado con WoS/Scopus

OpenAlex no acepta comodines; los troncos con `*` de la cadena v2 se expanden a variantes explícitas (el stemming propio de OpenAlex cubre plurales). Bloque 2 v2 para OpenAlex:

```
(biotic OR "biotic interaction" OR "species interaction" OR pollinator OR pollination OR herbivory OR herbivore OR frugivore OR frugivory OR "seed dispersal" OR microbiota OR microbiome OR microbial OR pathogen OR disease OR predator OR predation OR mutualism OR mutualist OR mutualistic OR parasite OR parasitism OR parasitic)
```

El bloque 1 (cadena v2, Enmienda 1, sin comodines) no cambia. La sintaxis final ejecutada por consulta queda en `busqueda/registro_ejecucion_openalex.md`.

## Regla de interpretación prefijada para el re-run

- Si el re-run recupera Frachon 2019: sensibilidad por base 6/6; se procede a deduplicar contra los 227 y a cribar solo los registros nuevos.
- Si NO lo recupera pese al bloque 2 corregido, la causa restante es de cobertura de metadatos de la base (p. ej., registro sin resumen indexado en OpenAlex, frecuente en revistas de Oxford University Press): se documenta con la verificación por DOI que imprime el script (campo `has_abstract`), se declara como limitación de la tercera base en §2 del manuscrito, y el chequeo combinado (6/6 en WoS+Scopus) sostiene la búsqueda.

## Sin cambios

Cadenas de WoS y Scopus ya ejecutadas (Enmienda 1), criterios (Enmiendas 2–3), plan de cribado y reporte.
