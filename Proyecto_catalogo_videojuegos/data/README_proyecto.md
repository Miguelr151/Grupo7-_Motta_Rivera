# 🎮 Análisis de Videojuegos

### ETL · EDA · Modelos de Regresión

------------------------------------------------------------------------

## 📌 Descripción del Proyecto

Este proyecto tiene como objetivo analizar un catálogo de videojuegos
almacenado en una base de datos PostgreSQL, aplicando técnicas de
ingeniería y análisis de datos como:

-   🔄 ETL (Extracción, Transformación y Carga)\
-   📊 Análisis Exploratorio de Datos (EDA)\
-   🤖 Modelos de regresión lineal (simple y múltiple)

El enfoque principal es estudiar la relación entre la **popularidad**
(cantidad de votos) y la **calificación** (rating) de los videojuegos.

------------------------------------------------------------------------

## 🧱 Estructura del Proyecto

    Proyecto_catalogo_videojuegos/
    │
    ├── scripts/
    │   ├── database.py
    │   ├── models.py
    │   ├── extractor.py
    │   └── consultas.py
    │
    ├── notebooks/
    │   └── analisis_videojuegos.ipynb
    │
    ├── data/
    │   └── graficas/
    │
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## ⚙️ Tecnologías Utilizadas

-   Python\
-   Pandas\
-   NumPy\
-   Matplotlib\
-   Seaborn\
-   Scikit-learn\
-   Statsmodels\
-   PostgreSQL\
-   SQLAlchemy

------------------------------------------------------------------------

## 🔄 Proceso ETL

1.  Extraer datos\
2.  Transformar datos\
3.  Cargar en PostgreSQL

------------------------------------------------------------------------

## 📊 Análisis Exploratorio de Datos (EDA)

-   Limpieza de datos\
-   Estadísticas descriptivas\
-   Histogramas\
-   Boxplots\
-   Correlación\
-   Scatter plots

------------------------------------------------------------------------

## 🤖 Modelos

### Modelo Simple

-   rating_count → rating

### Modelo Múltiple

-   rating_count\
-   log_votos\
-   anio

------------------------------------------------------------------------

## 📈 Evaluación

-   R²\
-   MSE\
-   RMSE\
-   MAE

------------------------------------------------------------------------

## 📊 Supuestos

-   Normalidad\
-   Homocedasticidad\
-   Multicolinealidad

------------------------------------------------------------------------

## 📌 Conclusiones

-   La popularidad influye en el rating\
-   No es el único factor\
-   El modelo múltiple mejora resultados

------------------------------------------------------------------------

## 🚀 Autor

Miguel Rivera - Dayana Motta
