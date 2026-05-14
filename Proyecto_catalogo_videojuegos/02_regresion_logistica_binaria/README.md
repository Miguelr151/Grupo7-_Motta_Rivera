# Regresión logística binaria

En esta carpeta se encuentra el notebook final del modelo de regresión logística binaria aplicado al proyecto de videojuegos.

## Contexto del proyecto
Durante el desarrollo del proyecto se trabajó en dos etapas:

1. **Etapa exploratoria con datos sintéticos**  
   Se construyó un caso de estudio inicial para validar la lógica de clasificación y el comportamiento de los modelos.

2. **Etapa final con datos reales**  
   Posteriormente, el proyecto se ajustó para trabajar con datos reales de videojuegos cargados en PostgreSQL.

## Objetivo
Clasificar videojuegos en dos clases:
- 1 = rating alto
- 0 = rating menor al umbral

## Definición de la variable binaria
Se construyó la variable `rating_bin` así:
- `rating_bin = 1` si `rating >= 65`
- `rating_bin = 0` si `rating < 65`

## Fuente de datos
En este notebook se trabajó con **datos reales** cargados desde PostgreSQL en la tabla `juegos_csv`, construida a partir del archivo `data/igdb.csv`.

## Variables usadas
- `release_year`
- `rating_count`
- `genre_count`
- `platform_count`
- `title_length`

## Métricas evaluadas
- Accuracy
- Precision
- Recall
- F1-score
- Matriz de confusión

## Balanceo
Se aplicó oversampling sobre el conjunto de entrenamiento para revisar el efecto del balanceo de clases.

## Resultado
La comparación entre el modelo base y el modelo con oversampling permitió analizar cómo cambia la detección de la clase minoritaria al balancear el entrenamiento.

## Nota
Los notebooks con datos sintéticos se conservan en la carpeta `notebooks/` como parte del proceso de validación inicial del proyecto.