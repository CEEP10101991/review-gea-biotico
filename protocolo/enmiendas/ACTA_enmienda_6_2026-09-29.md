# Enmienda 6 al protocolo de búsqueda — 29 de septiembre de 2026

**Protocolo enmendado:** `ACTA_protocolo_busqueda_review_2026-09-28.md` (commit 6f5d943), sección 4 (fuentes), con Enmiendas 1–5.
**Motivo:** al verificar la cifra de apertura del manuscrito contra el material suplementario de Dauphin et al. 2023 (base `mmc1.xlsx`, 278 estudios retenidos 2007–2021), se detectó que su categoría "Biotic/Both" (34 estudios) contiene registros que nuestras tres bases no recuperaron. Se añade, como brazo complementario declarado, el **cruce por lista de referencias (citation searching) contra esa base** — la revisión de referencia del campo — y se documenta el resultado completo.

## Verificación de la cifra de apertura (resultado colateral, para §1)

Recalculado de la base de los autores: **244/278 (87.8%) de los estudios retenidos usaron solo factores abióticos** — la redacción "cerca del 90%" es exacta; clima 254/278 (91.4%), topografía 98/278 (35.3%), suelo 32/278 (11.5%): idénticos a lo publicado. Ventana de búsqueda 2001–2021; casos retenidos 2007–2021. Nota que fortalece el argumento del review: la categoría "biótica" de esa base es laxa (incluye rasgos fenotípicos propios, clorofila satelital, nieve, ploidía o resistencia a insecticida), de modo que el 12.2% restante **sobreestima** los GEA con interacción interespecífica como predictor.

## Cruce contra nuestro universo cribado (326 registros)

De los 34 estudios "Biotic/Both" de Dauphin: 22 ya estaban en nuestro universo o en nuestro corpus (entre ellos Fraik 2020, Pais 2020, Vajana 2018, Frachon 2019, Garroway 2013 y la línea Wenzel — validación externa de la clasificación). Los 12 no recuperados por nuestras cadenas, evaluados con los criterios vigentes sobre la variable registrada por Dauphin y el título/resumen:

| Estudio | DOI | Variable "biótica" según Dauphin | Decisión |
|---|---|---|---|
| Rosenthal et al. 2021 | 10.1111/eva.13236 | Presión de depredación (densidad ponderada de piscívoros) | **A TEXTO COMPLETO** (ver abajo) |
| Zimmerman et al. 2021 | 10.1038/s41437-020-0352-6 | Nieve, viento, fenología (vegetación) | Excluir: proxies sin interactor (3d) |
| Maselko et al. 2020 | 10.1002/ece3.6378 | Clorofila | Excluir: proxy sin interactor (3d) |
| Silva et al. 2021 | 10.1111/mec.15780 | "Variables bióticas" oceanográficas | Excluir: capas de productividad sin interactor (3d) |
| Barbosa et al. 2021 | 10.1111/mec.16096 | Biomasa | Excluir: proxy sin interactor (3d) |
| Stronen et al. 2015 | 10.1002/ece3.1695 | Cobertura de nieve | Excluir: abiótico |
| van Boheemen & Hodgins 2020 | — | Rasgos fenotípicos propios | Excluir: no es interacción interespecífica |
| Rymer et al. 2010 | — | Rasgos florales propios | Excluir: ídem |
| Medina et al. 2021 | — | Talla corporal propia | Excluir: ídem |
| Ahrens et al. 2020 | — | Mapas de ploidía | Excluir: no es interacción |
| Sherpa et al. 2018 | 10.1093/gbe/evx267 | Resistencia a deltametrina | Ya en universo; excluido (no interactor) |
| Tonteri et al. 2010 / Wenzel & Piertney 2014 | 10.1111/j.1365-294X.2010.04573.x / 10.1111/mec.12833 | Mortalidad por parásito / carga parasitaria | Ya en universo; excluidos (3c: EST-SSRs / AFLP) |

## Rosenthal et al. 2021 — elegible a nivel resumen

*Poecilia reticulata* invasor en 18 poblaciones del archipiélago hawaiano; GBS, 12,254 SNPs, 282 individuos; LFMM con corrección por estructura y **un índice de presión de depredación medido (densidad ponderada de peces piscívoros por arroyo)** como quinto predictor (verificado contra el texto en PMC, 29/09/2026). Cumple (i)–(iii) y el criterio v2 de poblaciones (Enmienda 2: selección in situ, sin mejoramiento). Llenaría el nicho de depredación a escala poblacional. **Pendiente: texto completo** (10.1111/eva.13236, acceso abierto). Si se confirma, el corpus pasa a 18 y deben actualizarse §2, §3 (tabla), §8 y el diagrama de flujo (el brazo de citation searching se añade como fuente en el PRISMA).

## Resolución (29/09/2026, tarde)

Texto completo de Rosenthal et al. 2021 evaluado: **INCLUIDO**. Cumple (i) GEA espacial (LFMM con factores latentes, p calibradas, qvalue FDR<0.05) sobre 18 poblaciones; (ii) predictor biótico medido (índice de depredación por censos de esnórquel, ponderado por talla del depredador); (iii) GBS, 12,254 SNPs, 282 individuos; y el criterio v2 de poblaciones (invasoras bajo selección in situ). **El corpus queda en 18 estudios.** Decisión y extracción de 22 campos registradas en `cribado/decisiones_texto_completo_2026-09-28.csv` (fila CS-1) y `extraccion/tabla1_adiciones_2026-09-28.csv`. Flujo del brazo: 34 identificados en la base → 22 ya en el universo de bases → 12 evaluados → 11 excluidos con razón → 1 a texto completo → 1 incluido; se reporta en la columna "identificación por otros métodos (citation searching)" del diagrama PRISMA 2020.

## Causa del no-hallazgo y regla

El resumen de Rosenthal usa "environment association tests", variante no cubierta por ninguna de las ocho frases del bloque 1 v2. No se re-ejecutan las búsquedas por una variante singular; el brazo de citation searching declarado por esta enmienda cubre el hueco, y así se reporta en §2.

## Sin cambios

Cadenas ejecutadas (Enmiendas 1 y 4), criterios (Enmiendas 2–3), regla de arbitraje (Enmienda 5), plan de cribado.
