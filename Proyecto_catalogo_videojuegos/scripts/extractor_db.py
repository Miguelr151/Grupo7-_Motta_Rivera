#!/usr/bin/env python3

"""
ETL DE VIDEOJUEGOS USANDO IGDB

Este script realiza un proceso ETL:

EXTRACT
Obtiene datos de videojuegos desde la API de IGDB (usando autenticación de Twitch)

TRANSFORM
Procesa los datos obtenidos y los convierte al formato que necesita la base de datos

LOAD
Guarda los datos procesados en PostgreSQL usando SQLAlchemy
"""

import sys
import os

# -----------------------------------------------------
# IMPORTANTE
# -----------------------------------------------------
# Esto permite que Python encuentre la carpeta "scripts"
# aunque estemos ejecutando el archivo desde otro lugar.
# Evita errores como:
# ModuleNotFoundError: No module named 'scripts'
# -----------------------------------------------------

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import requests
import logging
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy.exc import IntegrityError

# Importamos conexión y modelo de base de datos
from scripts.database import SessionLocal
from scripts.models import Juego

# -----------------------------------------------------
# CARGAR VARIABLES DEL .ENV
# -----------------------------------------------------

load_dotenv()

# -----------------------------------------------------
# CONFIGURACIÓN DEL SISTEMA DE LOGS
# -----------------------------------------------------
# Guarda logs en archivo y también los muestra en consola

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/etl.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


# =====================================================
# CLASE PRINCIPAL DEL ETL
# =====================================================

class IGDBETL:

    def __init__(self):
        """
        Inicializa el ETL cargando configuraciones y creando conexión a la BD
        """

        # Credenciales de Twitch para autenticarse en IGDB
        self.client_id = os.getenv("TWITCH_CLIENT_ID")
        self.client_secret = os.getenv("TWITCH_CLIENT_SECRET")

        # URLs de las APIs
        self.token_url = os.getenv("TWITCH_TOKEN_URL")
        self.base_url = os.getenv("IGDB_BASE_URL")

        # Cantidad de resultados por búsqueda
        self.limit = int(os.getenv("IGDB_LIMIT", 50))

        # Palabras clave que se usarán para buscar juegos
        self.queries = ["zelda", "mario", "halo"]

        # Crear sesión de base de datos
        self.db = SessionLocal()

        # Obtener token de acceso a IGDB
        self.access_token = self.obtener_token()


    # -------------------------------------------------
    # OBTENER TOKEN DE TWITCH
    # -------------------------------------------------

    def obtener_token(self):
        """
        Obtiene el access_token necesario para consumir la API de IGDB.
        """

        try:

            params = {
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "grant_type": "client_credentials"
            }

            response = requests.post(self.token_url, params=params)
            response.raise_for_status()

            token = response.json().get("access_token")

            if not token:
                raise ValueError("No se pudo obtener access_token")

            logger.info("Token de Twitch obtenido correctamente")

            return token

        except Exception as e:

            logger.error(f"Error obteniendo token de Twitch: {e}")
            raise


    # -------------------------------------------------
    # EXTRAER DATOS DE IGDB
    # -------------------------------------------------

    def extraer_juegos(self, query):
        """
        Consulta la API de IGDB para obtener videojuegos
        según una palabra clave.
        """

        try:

            url = f"{self.base_url}/games"

            headers = {
                "Client-ID": self.client_id,
                "Authorization": f"Bearer {self.access_token}"
            }

            # Query en el lenguaje de IGDB
            body = f"""
            fields name,first_release_date,rating,rating_count,cover.url;
            search "{query}";
            limit {self.limit};
            """

            response = requests.post(url, headers=headers, data=body)
            response.raise_for_status()

            data = response.json()

            logger.info(f"{len(data)} juegos encontrados para: {query}")

            return data

        except Exception as e:

            logger.error(f"Error extrayendo juegos para '{query}': {e}")
            return []


    # -------------------------------------------------
    # TRANSFORMAR DATOS
    # -------------------------------------------------

    def procesar_juego(self, juego):
        """
        Convierte la respuesta de la API en un formato
        compatible con la base de datos.
        """

        try:

            # IGDB devuelve timestamp UNIX
            release_timestamp = juego.get("first_release_date")

            fecha_lanzamiento = None
            if release_timestamp:
                fecha_lanzamiento = datetime.utcfromtimestamp(release_timestamp)

            # Arreglar URL de portada
            cover = juego.get("cover") or {}
            cover_url = cover.get("url")

            if cover_url and cover_url.startswith("//"):
                cover_url = "https:" + cover_url

            return {
                "igdb_id": juego.get("id"),
                "nombre": juego.get("name"),
                "fecha_lanzamiento": fecha_lanzamiento,
                "rating": juego.get("rating"),
                "rating_count": juego.get("rating_count"),
                "cover_url": cover_url,
                "fecha_extraccion": datetime.utcnow()
            }

        except Exception as e:

            logger.error(f"Error procesando juego: {e}")
            return None


    # -------------------------------------------------
    # GUARDAR DATOS EN POSTGRESQL
    # -------------------------------------------------

    def guardar_en_bd(self, datos):
        """
        Inserta los datos del videojuego en la base de datos.
        Evita duplicados usando igdb_id.
        """

        try:

            # Verificar si el juego ya existe
            juego_existente = self.db.query(Juego).filter_by(
                igdb_id=datos["igdb_id"]
            ).first()

            if juego_existente:
                return

            # Crear objeto ORM
            juego = Juego(**datos)

            # Insertar en BD
            self.db.add(juego)
            self.db.commit()

            logger.info(f"Juego guardado: {datos['nombre']}")

        except IntegrityError:

            self.db.rollback()

        except Exception as e:

            self.db.rollback()
            logger.error(f"Error guardando juego: {e}")


    # -------------------------------------------------
    # EJECUTAR EL ETL COMPLETO
    # -------------------------------------------------

    def ejecutar(self):
        """
        Ejecuta todo el pipeline ETL
        """

        try:

            logger.info("Iniciando ETL de videojuegos")

            for query in self.queries:

                juegos = self.extraer_juegos(query)

                for juego in juegos:

                    datos = self.procesar_juego(juego)

                    if datos:
                        self.guardar_en_bd(datos)

            logger.info("ETL finalizado correctamente")

        except Exception as e:

            logger.error(f"Error en ETL: {e}")

        finally:

            # Cerrar conexión a la base de datos
            self.db.close()


# =====================================================
# EJECUCIÓN DEL SCRIPT
# =====================================================

if __name__ == "__main__":

    etl = IGDBETL()
    etl.ejecutar()