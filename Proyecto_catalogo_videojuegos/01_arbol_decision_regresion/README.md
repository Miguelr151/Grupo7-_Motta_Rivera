# Árbol de decisión para regresión

En esta carpeta se encuentra el notebook final del modelo de árbol de decisión para regresión aplicado al proyecto de videojuegos.

## Contexto del proyecto
Durante el desarrollo del proyecto se trabajó en dos etapas:

1. **Etapa exploratoria con datos sintéticos**  
   Se construyó un caso de estudio de regresión con variables sintéticas para validar relaciones, métricas y comportamiento de los modelos.

2. **Etapa final con datos reales**  
   Posteriormente, el proyecto se ajustó para trabajar con datos reales de videojuegos cargados en PostgreSQL, con el fin de aplicar el modelo sobre información real del dominio.

## Objetivo
Predecir la variable `rating` a partir de variables reales derivadas de los datos de videojuegos.

## Fuente de datos
En este notebook se trabajó con **datos reales** cargados desde PostgreSQL en la tabla `juegos_csv`, construida a partir del archivo `data/igdb.csv`.

## Variables usadas
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

## Resultado
El árbol permitió identificar qué variables explican mejor el rating, destacándose especialmente `rating_count`.

## Nota
Los notebooks con datos sintéticos se conservan en la carpeta `notebooks/` como parte del proceso de desarrollo y validación inicial del proyecto.