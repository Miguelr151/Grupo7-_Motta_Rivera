# 🗄 Configuración de PostgreSQL

Este documento explica cómo configurar PostgreSQL para el proyecto
**Catálogo de Videojuegos**.

------------------------------------------------------------------------

# 1️⃣ Instalar PostgreSQL (Ubuntu)

sudo apt update\
sudo apt install postgresql postgresql-contrib

Verificar instalación:

psql --version

------------------------------------------------------------------------

# 2️⃣ Ingresar a PostgreSQL

sudo -u postgres psql

------------------------------------------------------------------------

# 3️⃣ Crear base de datos

CREATE DATABASE catalogo_videojuegos;

Ver bases de datos:

`\l`{=tex}

------------------------------------------------------------------------

# 4️⃣ Salir de PostgreSQL

```{=tex}
\q
```

------------------------------------------------------------------------

# 5️⃣ Configurar variables de entorno

Crear archivo `.env` en la raíz del proyecto:

DB_HOST=localhost\
DB_PORT=5432\
DB_USER=postgres\
DB_PASSWORD=tu_password\
DB_NAME=catalogo_videojuegos

------------------------------------------------------------------------

# 6️⃣ Ejecutar migraciones

Crear migración:

alembic revision --autogenerate -m "create juegos table"

Aplicar migración:

alembic upgrade head

------------------------------------------------------------------------

# 7️⃣ Verificar tablas

Entrar nuevamente:

sudo -u postgres psql

Conectarse a la base:

`\c c`{=tex}atalogo_videojuegos

Ver tablas:

```{=tex}
\dt
```
Debe aparecer:

juegos\
alembic_version

------------------------------------------------------------------------

# 8️⃣ Ver datos almacenados

Consultar videojuegos:

SELECT \* FROM juegos LIMIT 10;

Contar registros:

SELECT COUNT(\*) FROM juegos;

------------------------------------------------------------------------

# Resultado

Después de ejecutar el ETL, la base contendrá videojuegos con:

-   nombre
-   rating
-   número de votos
-   fecha de lanzamiento
-   portada
-   fecha de extracción
