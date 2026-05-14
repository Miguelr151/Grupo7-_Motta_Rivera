# Regresión logística binaria

En esta carpeta se encuentra el notebook del modelo de **regresión logística binaria** aplicado al proyecto de videojuegos.

## Contexto del proyecto
Durante el desarrollo del proyecto se trabajó en dos etapas:

1. **Etapa exploratoria con datos sintéticos**  
   Se construyó un caso de estudio inicial para validar la lógica de clasificación binaria y el comportamiento del modelo.

2. **Etapa final con datos reales**  
   Posteriormente, el proyecto se ajustó para trabajar con datos reales de videojuegos cargados en PostgreSQL.

## Contenido del notebook
El notebook de esta carpeta presenta el mismo modelo en dos escenarios:

- **Parte A: datos sintéticos**
- **Parte B: datos reales**

Ambas partes corresponden al modelo de **regresión logística binaria**.

## Objetivo
Clasificar videojuegos en dos clases:
- `1`: rating alto
- `0`: rating menor al umbral

## Definición de la variable binaria
Se construyó la variable `rating_bin` así:
- `rating_bin = 1` si `rating >= 65`
- `rating_bin = 0` si `rating < 65`

## Datos sintéticos
En la fase exploratoria se usaron datos sintéticos para validar la clasificación binaria, revisar probabilidades predichas y comparar el modelo base frente a una versión balanceada.

## Datos reales
En la fase final se trabajó con **datos reales** cargados desde PostgreSQL en la tabla `juegos_csv`, construida a partir del archivo `data/igdb.csv`.

## Variables usadas en datos reales
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
Se aplicó **oversampling** sobre el conjunto de entrenamiento para analizar el efecto del balanceo de clases tanto en datos sintéticos como en datos reales.

## Resultado esperado
El notebook permite comparar cómo se comporta la regresión logística binaria en datos sintéticos y en datos reales, así como observar el impacto del oversampling en la detección de la clase minoritaria.