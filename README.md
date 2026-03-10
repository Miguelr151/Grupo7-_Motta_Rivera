# 🎮 Catálogo de Videojuegos - ETL con IGDB y PostgreSQL

Este proyecto implementa un **pipeline ETL (Extract, Transform, Load)**
que extrae información de videojuegos desde la API de **IGDB**, procesa
los datos y los almacena en una base de datos **PostgreSQL** para su
posterior análisis.

El objetivo es construir un **catálogo de videojuegos** que permita
analizar información como:

-   videojuegos mejor calificados
-   juegos con mayor cantidad de votos
-   distribución de juegos por año de lanzamiento

------------------------------------------------------------------------

# 📊 Arquitectura del Proyecto

El proyecto sigue la arquitectura clásica de un **pipeline ETL**.

IGDB API\
↓\
Extractor ETL\
↓\
Transformación de Datos\
↓\
PostgreSQL Database\
↓\
Consultas Analíticas

------------------------------------------------------------------------

# 📁 Estructura del Proyecto

catalogo_videojuegos │ ├── scripts │ ├── extractor_db.py │ ├──
consultas.py │ ├── database.py │ └── models.py │ ├── alembic │ ├── logs
│ ├── .env │ ├── README.md └── postgres_setup.md

------------------------------------------------------------------------

# 🛠 Tecnologías Utilizadas

-   Python 3
-   PostgreSQL
-   SQLAlchemy
-   Alembic
-   Pandas
-   IGDB API
-   Twitch OAuth

------------------------------------------------------------------------

# ⚙️ Instalación

## 1. Clonar el repositorio

git clone https://github.com/tu-usuario/catalogo_videojuegos.git\
cd catalogo_videojuegos

------------------------------------------------------------------------

## 2. Crear entorno virtual

python3 -m venv venv\
source venv/bin/activate

------------------------------------------------------------------------

## 3. Instalar dependencias

pip install -r requirements.txt

------------------------------------------------------------------------

# 🔑 Variables de entorno

Crear un archivo `.env` con:

TWITCH_CLIENT_ID=tu_client_id\
TWITCH_CLIENT_SECRET=tu_client_secret\
TWITCH_TOKEN_URL=https://id.twitch.tv/oauth2/token\
IGDB_BASE_URL=https://api.igdb.com/v4

IGDB_LIMIT=50

DB_HOST=localhost\
DB_PORT=5432\
DB_USER=postgres\
DB_PASSWORD=tu_password\
DB_NAME=catalogo_videojuegos

------------------------------------------------------------------------

# 🚀 Ejecutar el ETL

python scripts/extractor_db.py

------------------------------------------------------------------------

# 📊 Ejecutar análisis

python scripts/consultas.py

Esto mostrará:

-   Top videojuegos por rating
-   Juegos con más votos
-   Videojuegos por año

------------------------------------------------------------------------

# 📌 Funcionalidades

✔ Extracción de datos desde IGDB\
✔ Transformación de datos\
✔ Carga en PostgreSQL\
✔ Consultas analíticas con Python

------------------------------------------------------------------------

# 👨‍💻 Autor
Miguel Angel Rivera Lozano - Dayana Stephania 

Proyecto desarrollado para aprendizaje de **ETL y análisis de datos con
Python y PostgreSQL**.
