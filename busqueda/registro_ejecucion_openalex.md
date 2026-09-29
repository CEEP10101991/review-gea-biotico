# Ejecución OpenAlex — 2026-09-29

API `title_and_abstract.search`, cadena v2 sin comodines (stemming de OpenAlex; contingencia de sintaxis prefijada en el acta, sección 4.3). Polite pool: saltamontes1991@gmail.com.

| Consulta (sintaxis final) | Registros |
|---|---|
| `"landscape genomics" AND (biotic OR "biotic interaction" OR "species interaction" OR pollinator OR pollination OR herbivory OR herbivore OR frugivore OR frugivory OR "seed dispersal" OR microbiota OR microbiome OR microbial OR pathogen OR disease OR predator OR predation OR mutualism OR mutualist OR mutualistic OR parasite OR parasitism OR parasitic)` | 126 |
| `"landscape community genomics" AND (biotic OR "biotic interaction" OR "species interaction" OR pollinator OR pollination OR herbivory OR herbivore OR frugivore OR frugivory OR "seed dispersal" OR microbiota OR microbiome OR microbial OR pathogen OR disease OR predator OR predation OR mutualism OR mutualist OR mutualistic OR parasite OR parasitism OR parasitic)` | 1 |
| `"genotype-environment association" AND (biotic OR "biotic interaction" OR "species interaction" OR pollinator OR pollination OR herbivory OR herbivore OR frugivore OR frugivory OR "seed dispersal" OR microbiota OR microbiome OR microbial OR pathogen OR disease OR predator OR predation OR mutualism OR mutualist OR mutualistic OR parasite OR parasitism OR parasitic)` | 47 |
| `"genotype environment association" AND (biotic OR "biotic interaction" OR "species interaction" OR pollinator OR pollination OR herbivory OR herbivore OR frugivore OR frugivory OR "seed dispersal" OR microbiota OR microbiome OR microbial OR pathogen OR disease OR predator OR predation OR mutualism OR mutualist OR mutualistic OR parasite OR parasitism OR parasitic)` | 47 |
| `"genome-environment association" AND (biotic OR "biotic interaction" OR "species interaction" OR pollinator OR pollination OR herbivory OR herbivore OR frugivore OR frugivory OR "seed dispersal" OR microbiota OR microbiome OR microbial OR pathogen OR disease OR predator OR predation OR mutualism OR mutualist OR mutualistic OR parasite OR parasitism OR parasitic)` | 19 |
| `"genome-environmental analysis" AND (biotic OR "biotic interaction" OR "species interaction" OR pollinator OR pollination OR herbivory OR herbivore OR frugivore OR frugivory OR "seed dispersal" OR microbiota OR microbiome OR microbial OR pathogen OR disease OR predator OR predation OR mutualism OR mutualist OR mutualistic OR parasite OR parasitism OR parasitic)` | 2 |
| `"gene-environment association" AND (biotic OR "biotic interaction" OR "species interaction" OR pollinator OR pollination OR herbivory OR herbivore OR frugivore OR frugivory OR "seed dispersal" OR microbiota OR microbiome OR microbial OR pathogen OR disease OR predator OR predation OR mutualism OR mutualist OR mutualistic OR parasite OR parasitism OR parasitic)` | 56 |
| `"environmental association analysis" AND (biotic OR "biotic interaction" OR "species interaction" OR pollinator OR pollination OR herbivory OR herbivore OR frugivore OR frugivory OR "seed dispersal" OR microbiota OR microbiome OR microbial OR pathogen OR disease OR predator OR predation OR mutualism OR mutualist OR mutualistic OR parasite OR parasitism OR parasitic)` | 14 |

**Diagnóstico por DOI de los 6 conocidos** (Enmienda 4): Frachon 2019: has_abstract=True; Frachon 2023: has_abstract=True; Roux 2023: has_abstract=True; Maillet 2025: has_abstract=True; Fraik 2020: has_abstract=True; Beer 2024: has_abstract=False

Unión deduplicada por ID de OpenAlex: **253** registros (`exports/openalex_2026-09-29.json`, `.csv`).

**Chequeo de sensibilidad (6 conocidos): PASÓ (6/6)**

Pendiente: deduplicar contra los 227 de WoS+Scopus y cribar solo los registros nuevos.
