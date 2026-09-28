# review-gea-biotico

Artículo de revisión: **Interacciones bióticas (planta-animal) en los análisis de asociación genotipo-ambiente dentro de bosques tropicales estacionales**.
Actividad académica complementaria, Doctorado en Ciencias Biológicas, UNAM (semestre 2027-1).
Autor: César Emiliano Escalona Prado. Tutora principal: Dra. Alejandra Citlalli Moreno Letelier.

Método: revisión sistemática con síntesis crítica cualitativa (sin metaanálisis), con protocolo de búsqueda preinscrito.

## Estructura

```
protocolo/            Acta de preinscripción del protocolo de búsqueda (NO se edita tras el commit)
  enmiendas/          Desviaciones del protocolo, una por archivo fechado
busqueda/
  exports/            Registros crudos exportados por base (RIS/CSV/JSON), con fecha en el nombre
  capturas/           Capturas de pantalla de los conteos por base, con fecha
cribado/
  scripts/            Deduplicación y utilidades
  diagrama_flujo/     Conteos por etapa y figura PRISMA/ROSES
  *.csv               Decisiones de cribado con razón por registro
extraccion/           Workbook de fichas (v3) y export plano de la Tabla 1
manuscrito/           Borradores, figuras, referencias (.bib)
actas_sesion/         Nota de estado de cada sesión de trabajo (3 líneas)
cronograma.md         Plan de trabajo R1–R9
```

## Flujo de trabajo

1. **Preinscripción**: `protocolo/ACTA_protocolo_busqueda_review_2026-09-28.md` se commitea y pushea ANTES de ejecutar la búsqueda. El timestamp verificable es el push a GitHub (y el release `v0.1-protocolo`).
2. **Búsqueda**: WoS + Scopus (acceso UNAM) + OpenAlex (API). Exports crudos a `busqueda/exports/`, sin edición manual.
3. **Cribado**: deduplicación con `cribado/scripts/dedup.py`; decisiones título-resumen y texto completo en los CSV de `cribado/`, con razón de exclusión por registro.
4. **Extracción**: instrumento de 22 campos (workbook de fichas, hoja `11_Tabla1_Review`).
5. **Manuscrito**: borradores versionados en `manuscrito/borradores/`.

## Reglas

- El acta de protocolo no se modifica después del commit; toda desviación va en `protocolo/enmiendas/ACTA_enmienda_N_FECHA.md`.
- Los exports de `busqueda/` son evidencia: no se editan ni se filtran a mano.
- El manuscrito no cita cifras del caso *Bursera* fuera del estado auditado (traspaso 01/09/2026).
- Cada sesión de trabajo cierra con nota de estado en `actas_sesion/`.

## Licencia

Por definir antes de publicar el repo (sugerencia: CC-BY 4.0 para textos y datos de cribado; MIT para scripts).

## Cómo citar el protocolo

> Escalona Prado, C.E. (2026). Protocolo preinscrito de búsqueda sistemática: interacciones bióticas como predictores en GEA. Repositorio GitHub [URL], commit [hash], release v0.1-protocolo.
