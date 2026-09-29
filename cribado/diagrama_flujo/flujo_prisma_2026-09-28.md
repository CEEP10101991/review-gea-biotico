# Diagrama de flujo (PRISMA 2020, versión texto) — actualizado 29/09/2026 (tres bases)

Versión gráfica pendiente. Números auditables contra `busqueda/` y `cribado/`.

```
IDENTIFICACIÓN
  Registros identificados en bases de datos:        644
    Web of Science (Core Collection):               194
    Scopus:                                         197
    OpenAlex (corrida definitiva, Enmienda 4):      253
  Registros eliminados por duplicación:             318
    (164 dentro de WoS+Scopus; 154 de OpenAlex ya presentes en WoS+Scopus)

CRIBADO
  Registros cribados (título/resumen):              326  (227 WoS+Scopus + 99 exclusivos de OpenAlex)
  Registros excluidos:                              299
    Cribado WoS+Scopus (28/09):                     200
    Cribado OpenAlex (29/09):                        96
    Preprints elegibles excluidos por regla (Enm. 5): 3

ELEGIBILIDAD
  Informes evaluados a texto completo:               27
  Informes excluidos (con razón):                    10
    Sin GEA con predictor biótico medido:             5   (ids 13, 85, 99, 142, 150)
    Sin datos genómicos de descubrimiento (Enm. 3c):  4   (ids 82, 111, 137, 138)
    Proxy de recurso sin interactor (Enm. 3d):        1   (id 57, Mendes 2022)

INCLUIDOS
  Estudios incluidos en la síntesis:                 17
    Del barrido preliminar (conocimiento previo):     6
    Nuevos de la búsqueda sistemática:               11
    Aportados exclusivamente por OpenAlex:            0
```

Notas de transparencia: los 6 del barrido preliminar se declararon en el protocolo antes de ejecutar; el chequeo de sensibilidad combinado pasó 6/6 en las tres bases (OpenAlex requirió la Enmienda 4). Los 3 preprints elegibles a nivel resumen quedan fuera por la regla de la Enmienda 5 y se citan como evidencia emergente.
