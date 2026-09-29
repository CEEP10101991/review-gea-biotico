# Ejecución OpenAlex — 2026-09-29

API `title_and_abstract.search`, cadena v2 sin comodines (stemming de OpenAlex; contingencia de sintaxis prefijada en el acta, sección 4.3). Polite pool: saltamontes1991@gmail.com.

| Consulta (sintaxis final) | Registros |
|---|---|
| `"landscape genomics" AND ("biotic interaction" OR pollinator OR herbivory OR frugivore OR "seed dispersal" OR microbiota OR pathogen OR disease OR predator)` | 90 |
| `"landscape community genomics" AND ("biotic interaction" OR pollinator OR herbivory OR frugivore OR "seed dispersal" OR microbiota OR pathogen OR disease OR predator)` | 1 |
| `"genotype-environment association" AND ("biotic interaction" OR pollinator OR herbivory OR frugivore OR "seed dispersal" OR microbiota OR pathogen OR disease OR predator)` | 31 |
| `"genotype environment association" AND ("biotic interaction" OR pollinator OR herbivory OR frugivore OR "seed dispersal" OR microbiota OR pathogen OR disease OR predator)` | 31 |
| `"genome-environment association" AND ("biotic interaction" OR pollinator OR herbivory OR frugivore OR "seed dispersal" OR microbiota OR pathogen OR disease OR predator)` | 11 |
| `"genome-environmental analysis" AND ("biotic interaction" OR pollinator OR herbivory OR frugivore OR "seed dispersal" OR microbiota OR pathogen OR disease OR predator)` | 2 |
| `"gene-environment association" AND ("biotic interaction" OR pollinator OR herbivory OR frugivore OR "seed dispersal" OR microbiota OR pathogen OR disease OR predator)` | 51 |
| `"environmental association analysis" AND ("biotic interaction" OR pollinator OR herbivory OR frugivore OR "seed dispersal" OR microbiota OR pathogen OR disease OR predator)` | 12 |

Unión deduplicada por ID de OpenAlex: **189** registros (`exports/openalex_2026-09-29.json`, `.csv`).

**Chequeo de sensibilidad (6 conocidos): FALLÓ: faltan {'10.1093/molbev/msz078': 'Frachon 2019'}**

Pendiente: deduplicar contra los 227 de WoS+Scopus y cribar solo los registros nuevos.
