# Enmienda 1 al protocolo de búsqueda — 28 de septiembre de 2026

**Protocolo enmendado:** `ACTA_protocolo_busqueda_review_2026-09-28.md` (commit 6f5d943).
**Motivo:** (1) incidencia técnica en Scopus durante la ejecución; (2) fallo de la prueba de sensibilidad (acta, sección 6) en la primera ejecución.

## 1. Incidencia técnica en Scopus

La cadena de la sección 4.2 produjo el error `RequestHeaderSectionTooLarge` (límite 8192 bytes). Resolución: el error se debía a cookies acumuladas de la sesión institucional (proxy pbidi UNAM), no a la cadena. Se ejecutó en ventana de incógnito con la **cadena íntegra, sin modificación alguna de sintaxis ni de términos**. No hubo desviación del protocolo en la cadena de Scopus; esta sección se registra solo como incidencia técnica y su resolución.

## 2. Fallo de la prueba de sensibilidad (primera ejecución, 28/09/2026)

Ejecución: WoS Core Collection (126 registros) + Scopus (144 registros); 270 → 166 tras deduplicación por DOI/título. Recuperados 4 de los 6 estudios conocidos (Frachon 2019, Fraik 2020, Frachon 2023, Roux 2023, en ambas bases). **No recuperados:** Beer et al. 2024, Maillet et al. 2025, Dorey et al. 2024.

Causa, verificada contra los PDF:
- Beer et al. 2024 se describe como "landscape community genomics framework" (resumen, p. 293): la frase exacta "landscape genomics" no aparece con las palabras adyacentes, y el resumen no usa "genotype-environment association".
- Maillet et al. 2025 usa la keyword "genome–environmental analysis" (portada), variante no cubierta por ninguna frase del bloque 1.
- Dorey et al. 2024 no es un GEA y no contiene ninguna frase del bloque 1: su requisito de recuperación (acta, sección 6) estaba mal calibrado, porque el bloque 1 restringe deliberadamente al corpus GEA y ese estudio es el contraste de evolución experimental, incorporado por conocimiento previo.

## 3. Cambios al protocolo

**3.1 Bloque 1 de la cadena (términos GEA), versión 2.** Se añaden las variantes "landscape community genomics", "genome-environmental analys*" y "gene-environment association*". No se añade "community genomics" a secas: arrastraría el corpus de metagenómica microbiana sin ganancia de sensibilidad para la pregunta (la variante compuesta ya recupera a Beer 2024).

- WoS (Advanced Search):

```
TS=(("landscape genomics" OR "landscape community genomics" OR "genotype-environment association*" OR "genotype environment association*" OR "genome-environment association*" OR "genome-environmental analys*" OR "gene-environment association*" OR "environmental association analys*") AND (biotic OR "biotic interaction*" OR "species interaction*" OR pollinat* OR herbivor* OR frugivor* OR "seed dispersal" OR microbio* OR pathogen* OR disease OR predat* OR mutualis* OR parasit*))
```

- Scopus (Advanced Search):

```
TITLE-ABS-KEY(("landscape genomics" OR "landscape community genomics" OR "genotype-environment association*" OR "genotype environment association*" OR "genome-environment association*" OR "genome-environmental analys*" OR "gene-environment association*" OR "environmental association analys*") AND (biotic OR "biotic interaction*" OR "species interaction*" OR pollinat* OR herbivor* OR frugivor* OR "seed dispersal" OR microbio* OR pathogen* OR disease OR predat* OR mutualis* OR parasit*))
```

- OpenAlex: misma ampliación del bloque 1 sobre la URL de la sección 4.3 del acta.

**3.2 Criterio de sensibilidad, versión 2.** La búsqueda combinada debe recuperar los **seis GEA** conocidos (Frachon 2019, Fraik 2020, Frachon 2023, Roux 2023, Beer 2024, Maillet 2025). Se retira el requisito de recuperar Dorey et al. 2024, por la mala calibración descrita en 2; la prueba de que las razones de exclusión discriminan se hará sobre los registros no elegibles que la búsqueda sí devuelva (p. ej. estudios sin dimensión espacial o sin predictor biótico).

**3.3 Re-ejecución.** Conforme a la sección 6 del acta, la búsqueda se re-ejecuta ÍNTEGRA en todas las bases con la cadena v2. Los exports de la primera ejecución se conservan en `busqueda/exports/` como evidencia de la iteración 1, y el diagrama de flujo reporta la iteración final.

## 4. Sin cambios

Pregunta PECO, criterios de elegibilidad, bloque 2 de la cadena, plan de cribado y convenciones de reporte permanecen como en el acta.
