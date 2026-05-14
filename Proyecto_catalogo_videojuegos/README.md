# 🎮 Catálogo de Videojuegos - ETL, Regresión y Clasificación con PostgreSQL

Este proyecto corresponde a la materia de **Minería de Datos** y combina un proceso de **ETL (Extract, Transform, Load)** con la construcción de modelos de **regresión** y **clasificación** aplicados al dominio de videojuegos.

El proyecto extrae información desde la API de **IGDB**, procesa los datos y los almacena en **PostgreSQL** para su posterior análisis y modelado.

## Objetivos del proyecto

El proyecto permitió trabajar sobre:

- construcción de un catálogo de videojuegos
- análisis exploratorio de datos
- modelos de regresión
- modelos de clasificación binaria
- comparación entre datos sintéticos y datos reales

---

# 📊 Arquitectura general del proyecto

El proyecto sigue una arquitectura tipo ETL:

IGDB API  
↓  
Extractor ETL  
↓  
Transformación de Datos  
↓  
PostgreSQL Database  
↓  
Consultas Analíticas y Modelos de Minería de Datos

---

# 🧪 Metodología de trabajo

El desarrollo se realizó en dos etapas:

## 1. Etapa exploratoria con datos sintéticos
En esta fase se construyó un caso de estudio inicial con datos sintéticos para validar:

- relaciones entre variables
- correlación
- métricas de regresión
- comportamiento de los modelos

Estos notebooks se conservan en la carpeta `notebooks/` como parte del proceso de desarrollo.

## 2. Etapa final con datos reales
En la fase final el proyecto se ajustó para trabajar con **datos reales de videojuegos**, usando información proveniente de `data/igdb.csv`, cargada a PostgreSQL en la tabla `juegos_csv`.

Sobre esos datos se construyeron los modelos finales organizados por carpetas para la entrega.

---
# 📁 Estructura final de entrega

```text
Proyecto_catalogo_videojuegos/
│
├── 01_arbol_decision_regresion/
│   ├── arbol_decision_regresion_videojuegos.ipynb
│   └── README.md
│
├── 02_regresion_logistica_binaria/
│   ├── regresion_logistica_binaria_videojuegos.ipynb
│   └── README.md
│
├── 03_arbol_clasificacion_binaria/
│   ├── arbol_clasificacion_binaria_videojuegos.ipynb
│   └── README.md
│
├── 04_proyecto_aula_excel/
│   └── Proyecto_Aula.xlsx
│
├── data/
│   ├── igdb.csv
│   └── videojuegos_sinteticos.csv
│
├── notebooks/
│   ├── regresion_sintetica_1000.ipynb
│   └── regresion_videojuegos.ipynb
│
├── scripts/
├── alembic/
├── logs/
├── README.md
└── postgres_setup.md
---
````
## Descripción de las carpetas finales

### 01_arbol_decision_regresion
Contiene el notebook final del **árbol de decisión para regresión** aplicado sobre datos reales de videojuegos, usando como variable objetivo `rating`.

### 02_regresion_logistica_binaria
Contiene el notebook final de **regresión logística binaria**, donde se construye la variable `rating_bin` para clasificar videojuegos en dos clases.

### 03_arbol_clasificacion_binaria
Contiene el notebook final del **árbol de decisión para clasificación binaria**, también usando la variable `rating_bin`.

### 04_proyecto_aula_excel
Contiene el archivo de Excel diligenciado como parte de la entrega del proyecto.

---

# 🛠 Tecnologías Utilizadas

- Python 3
- PostgreSQL
- SQLAlchemy
- Alembic
- Pandas
- Scikit-learn
- IGDB API
- Twitch OAuth
- Jupyter Notebook

---

# ⚙️ Instalación

## 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd Proyecto_catalogo_videojuegos
`````
## 2. Crear entorno virtual

```bash
python -m venv venv
`````
## 3. Activar entorno virtual

### En Windows
```bash
venv\Scripts\activate
```

## 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# 🔑 Variables de entorno

Crear un archivo `.env` con:

```env
TWITCH_CLIENT_ID=tu_client_id
TWITCH_CLIENT_SECRET=tu_client_secret
TWITCH_TOKEN_URL=https://id.twitch.tv/oauth2/token
IGDB_BASE_URL=https://api.igdb.com/v4
IGDB_LIMIT=50

DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=tu_password
DB_NAME=catalogo_videojuegos
```

---

# 🚀 Ejecutar el ETL

```bash
python scripts/extractor_db.py
```

---

# 📊 Ejecutar análisis

```bash
python scripts/consultas.py
```

Esto permite consultar, por ejemplo:

- videojuegos mejor calificados
- juegos con mayor cantidad de votos
- distribución por año de lanzamiento

---

# 🤖 Modelos trabajados

En la entrega final se desarrollaron los siguientes modelos:

- Árbol de decisión para regresión
- Regresión logística binaria
- Árbol de decisión para clasificación binaria

Todos los modelos finales fueron organizados en carpetas independientes con su respectivo `README.md`.

---

# 📌 Funcionalidades del proyecto

✔ Extracción de datos desde IGDB  
✔ Transformación de datos  
✔ Carga en PostgreSQL  
✔ Consultas analíticas con Python  
✔ Modelos de regresión  
✔ Modelos de clasificación binaria  
✔ Comparación entre datos sintéticos y reales  

---

# 👨‍💻 Autores

- Miguel Angel Rivera Lozano
- Dayana Stephany Motta Camayo

Proyecto desarrollado para aprendizaje de **ETL, minería de datos, regresión y clasificación con Python y PostgreSQL**.
