# Ejecución de la búsqueda

Las cadenas exactas y las reglas están congeladas en `../protocolo/ACTA_protocolo_busqueda_review_2026-09-28.md` (sección 4). No ejecutar antes del commit+push del acta.

Por cada base:
1. Pegar la cadena tal cual (sin filtros de fecha/idioma).
2. Captura de pantalla del conteo total → `capturas/BASE_AAAA-MM-DD.png`.
3. Exportar TODOS los registros con resumen → `exports/BASE_AAAA-MM-DD.ris` (o .csv).
   - WoS: Export → RIS → "Full Record" (en lotes de 1000 si hace falta; numerar `_p1`, `_p2`).
   - Scopus: Export → CSV → marcar Abstract y todos los campos de cita.
   - OpenAlex: la URL del acta (sección 4.3), paginada con `&per-page=200&cursor=*` → JSON.
4. Anotar en `registro_ejecucion.md`: base, fecha, conteo, quién ejecutó, incidencias.

Cualquier ajuste de sintaxis exigido por una base → enmienda fechada en `../protocolo/enmiendas/`, ANTES de continuar.
