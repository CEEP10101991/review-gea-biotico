# Acta de preinscripción — Protocolo de búsqueda sistemática

**Proyecto:** Artículo de revisión "Interacciones bióticas (planta-animal) en los análisis de asociación genotipo-ambiente dentro de bosques tropicales estacionales" (actividad académica complementaria, Doctorado en Ciencias Biológicas, UNAM; semestre 2027-1).
**Autor:** César Emiliano Escalona Prado.
**Fecha de redacción:** 28 de septiembre de 2026.
**Estado:** protocolo congelado, PENDIENTE DE EJECUTAR. La búsqueda no se ejecuta antes del commit de este documento al repositorio público. La fecha y el hash del commit constituyen la evidencia de prespecificación.

## 1. Propósito

Fijar, antes de ejecutar, todas las decisiones de la búsqueda sistemática y del cribado que alimentan la sección de Métodos del artículo de revisión, para que el conteo de estudios elegibles tenga estatus confirmatorio. Cualquier desviación posterior se documenta en una enmienda fechada aparte; este documento no se edita después del commit.

## 2. Pregunta estructurada (PECO adaptado)

- **P (población):** poblaciones naturales de cualquier taxón con datos genómicos poblacionales o individuales georreferenciados.
- **E (exposición):** variación espacial de una interacción biótica interespecífica, cuantificada e incluida como predictor.
- **C (comparador):** predictores abióticos en el mismo análisis.
- **O (resultado):** asociación genotipo-ambiente (GEA) espacial.

## 3. Criterios de elegibilidad

**Inclusión (los tres a la vez):**
1. Análisis de asociación genotipo-ambiente espacial sobre poblaciones naturales.
2. Al menos un predictor que cuantifique una interacción biótica interespecífica (comunidad de interactores, prevalencia de enfermedad, densidad de un socio o antagonista, índices funcionales derivados de la interacción).
3. Datos genómicos a nivel poblacional o individual georreferenciado.

**Exclusión:**
- Evolución experimental (se trata como rama contrafactual en la introducción, no como parte del cuerpo revisado).
- GWAS de fenotipos de interacción sin dimensión espacial.
- Estudios donde lo biótico entra únicamente como covariable de control y no como predictor de interés.
- Sin restricción de fecha, idioma ni taxón.

## 4. Bases y cadenas de búsqueda (exactas, congeladas)

Sin filtros de fecha ni idioma. Se exportan TODOS los registros (RIS o CSV con resumen), anotando fecha de consulta y conteo total por base (captura de pantalla del conteo).

**4.1 Web of Science Core Collection (Advanced Search):**

```
TS=(("landscape genomics" OR "genotype-environment association" OR "genotype environment association" OR "environmental association analysis" OR "genome-environment association") AND (biotic OR "biotic interaction" OR "species interaction" OR pollinat* OR herbivor* OR frugivor* OR "seed dispersal" OR microbio* OR pathogen* OR disease OR predat* OR mutualis* OR parasit*))
```

**4.2 Scopus (Advanced Search):**

```
TITLE-ABS-KEY(("landscape genomics" OR "genotype-environment association" OR "genotype environment association" OR "environmental association analysis" OR "genome-environment association") AND (biotic OR "biotic interaction" OR "species interaction" OR pollinat* OR herbivor* OR frugivor* OR "seed dispersal" OR microbio* OR pathogen* OR disease OR predat* OR mutualis* OR parasit*))
```

**4.3 OpenAlex (API, consulta reproducible):**

```
https://api.openalex.org/works?filter=title_and_abstract.search:("landscape genomics" OR "genotype-environment association" OR "environmental association analysis") AND ("biotic interaction" OR pollinator OR herbivory OR frugivore OR "seed dispersal" OR microbiota OR pathogen OR disease OR predator)
```

**Contingencia de sintaxis (prefijada):** si una base rechaza comodines dentro de comillas o la longitud de la cadena, la cadena se parte en dos búsquedas combinadas con OR en el historial de la base, sin alterar los términos; el ajuste se registra en la enmienda correspondiente con la sintaxis final ejecutada.

## 5. Plan de cribado

1. **Deduplicación** por DOI y por título normalizado (script; se conserva el registro con metadatos más completos).
2. **Cribado por título y resumen** contra los criterios de la sección 3, con razón de exclusión registrada por cada registro descartado. Primer cribado: asistente (Claude); validación de todos los dudosos y de una muestra de los descartados: el autor.
3. **Texto completo** de todo lo que pase el cribado; decisión final de inclusión por el autor, con razón de exclusión registrada por artículo.
4. **Reporte:** conteos por etapa (identificados → deduplicados → cribados → evaluados a texto completo → incluidos) en diagrama de flujo tipo PRISMA/ROSES, más tabla de excluidos en texto completo con razón.

## 6. Validación de sensibilidad (prefijada)

La búsqueda combinada debe recuperar los seis estudios conocidos por barrido preliminar (agosto 2026):

1. Frachon et al. 2019 — 10.1093/molbev/msz078
2. Fraik et al. 2020 — 10.1111/evo.14023
3. Frachon et al. 2023 — 10.1093/molbev/msad036
4. Roux et al. 2023 — 10.1093/molbev/msad093
5. Beer et al. 2024 — 10.1038/s41559-023-02265-9
6. Maillet et al. 2025 — 10.1111/1462-2920.70108

Si alguno no aparece, la cadena se ajusta y TODA la búsqueda se re-ejecuta en todas las bases, documentando la iteración en enmienda fechada. Además, Dorey et al. 2024 (10.1038/s41467-024-49383-x) debe aparecer en los resultados y quedar excluido por el criterio de evolución experimental: sirve de prueba de que las razones de exclusión discriminan.

## 7. Qué NO decide este protocolo

La síntesis es cualitativa y crítica (rúbrica de estándares metodológicos prespecificada en el manuscrito, §6); no se realizará metaanálisis. Esta acta congela la búsqueda y el cribado; la interpretación de los estudios incluidos corresponde al manuscrito.

## 8. Regla de enmiendas

Este documento no se modifica después del commit. Toda desviación (sintaxis rechazada por una base, base inaccesible, criterio ambiguo ante un caso concreto) se registra en un archivo nuevo `ACTA_enmienda_N_fecha.md` en el mismo directorio, con la decisión y su razón. El manuscrito reporta protocolo y enmiendas.
