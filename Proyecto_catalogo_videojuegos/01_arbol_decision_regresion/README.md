# Árbol de decisión para regresión

En esta carpeta se encuentra el notebook del modelo de **árbol de decisión para regresión** aplicado al proyecto de videojuegos.

## Contexto del proyecto
Durante el desarrollo del proyecto se trabajó en dos etapas:

1. **Etapa exploratoria con datos sintéticos**  
   Se construyó un caso de estudio inicial para validar relaciones entre variables, métricas de regresión y comportamiento del modelo.

2. **Etapa final con datos reales**  
   Posteriormente, el proyecto se ajustó para trabajar con datos reales de videojuegos cargados en PostgreSQL.

## Contenido del notebook
El notebook de esta carpeta presenta el mismo modelo en dos escenarios:

- **Parte A: datos sintéticos**
- **Parte B: datos reales**

Ambas partes corresponden al modelo de **árbol de decisión para regresión**.

## Objetivo
Predecir la variable `rating` a partir de variables asociadas a los videojuegos.

## Datos sintéticos
En la fase exploratoria se usaron variables sintéticas para validar la lógica del modelo y analizar su desempeño en un entorno controlado.

## Datos reales
En la fase final se trabajó con **datos reales** cargados desde PostgreSQL en la tabla `juegos_csv`, construida a partir del archivo `data/igdb.csv`.

## Variables usadas en datos reales
- `release_year`
- `rating_count`
- `genre_count`
- `platform_count`
- `title_length`

## Variable objetivo
- `rating`

## Métricas evaluadas
- R²
- MSE
- RMSE
- MAE

## Resultado esperado
El notebook permite comparar el comportamiento del árbol de regresión en datos sintéticos y en datos reales, destacando las diferencias entre un entorno controlado y un escenario aplicado.