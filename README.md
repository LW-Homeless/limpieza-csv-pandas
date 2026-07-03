# Limpieza CSV con Pandas

Proyecto del roadmap de [Data Analyst](https://roadmap.sh/data-analyst/projects) de roadmap.sh.

Limpieza de un dataset sintético de empleados usando un flujo de trabajo estructurado en 5 etapas reutilizables.

---

## Descripción

El dataset contiene problemas comunes en datos reales: problemas de encoding, formatos de fecha incorrectos, tipos de datos mezclados y valores categóricos inconsistentes.

El objetivo no es solo limpiar este archivo, sino construir un proceso repetible aplicable a cualquier dataset.

---

## Flujo de trabajo

| Etapa | Descripción |
|---|---|
| 1. Load | Carga del dataset manejando encoding y delimitadores |
| 2. Inspect | Inspección inicial antes de cualquier modificación |
| 3. Clean | Corrección de tipos, fechas y valores categóricos |
| 4. Review | Auditoría de los cambios realizados |
| 5. Export | Exportación del dataset limpio |

---

## Técnicas aplicadas

- Manejo de encoding y delimitadores en la carga
- Asignación explícita de tipos de datos con `dtype`
- Conversión de fechas con `pd.to_datetime()` y `errors='coerce'`
- Exportación del dataset limpio

---

# Video demostración
![alt text](https://github.com/LW-Homeless/limpieza-csv-pandas/blob/main/Clean-csv.gif)

## Dataset

[Messy Employee Dataset](https://www.kaggle.com/datasets/desolution01/messy-employee-dataset) — Kaggle

---

## Tecnologías

`Python` `Pandas`

---

## Recursos

- [Proyecto en roadmap.sh](https://roadmap.sh/projects/clean-csv)
