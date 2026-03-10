#!/usr/bin/env python3
import os
import requests
import json
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import logging

# Cargar variables de entorno
load_dotenv()

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/etl.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class IGDBExtractor:
    """
    ETL Extractor para IGDB (requiere autenticación vía Twitch).
    Mantiene la misma estructura general del extractor Weatherstack:
    - __init__(): lee variables .env
    - extraer_datos(): consulta API
    - procesar_respuesta(): transforma a dict plano
    - ejecutar_extraccion(): recorre lista (equivalente a CIUDADES)
    """

    def __init__(self):
        # Credenciales Twitch (obligatorias)
        self.client_id = os.getenv('TWITCH_CLIENT_ID')
        self.client_secret = os.getenv('TWITCH_CLIENT_SECRET')

        # URLs
        self.token_url = os.getenv('TWITCH_TOKEN_URL', 'https://id.twitch.tv/oauth2/token')
        self.igdb_base_url = os.getenv('IGDB_BASE_URL', 'https://api.igdb.com/v4')

        # Config ETL (equivalente a CIUDADES en tu proyecto anterior)
        # Lista de búsquedas o categorías que quieres consultar (separadas por coma)
        # Ejemplo: IGDB_QUERIES=zelda,mario,fortnite
        self.queries = os.getenv('IGDB_QUERIES', 'zelda,mario').split(',')

        # Ajustes de consulta
        self.limit = int(os.getenv('IGDB_LIMIT', '25'))
        self.endpoint = os.getenv('IGDB_ENDPOINT', 'games')

        if not self.client_id or not self.client_secret:
            raise ValueError("TWITCH_CLIENT_ID o TWITCH_CLIENT_SECRET no configuradas en .env")

        # Obtener token de acceso
        self.access_token = self.obtener_token()

    def obtener_token(self):
        """Obtiene el access token de Twitch usando client credentials."""
        try:
            params = {
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "grant_type": "client_credentials"
            }
            r = requests.post(self.token_url, params=params, timeout=10)
            r.raise_for_status()
            data = r.json()
            token = data.get("access_token")

            if not token:
                raise ValueError("No se obtuvo access_token desde Twitch.")

            logger.info("✅ Token de Twitch obtenido correctamente.")
            return token

        except Exception as e:
            logger.error(f"❌ Error obteniendo token de Twitch: {str(e)}")
            raise

    def extraer_juegos(self, query_text):
        """Extrae datos de videojuegos desde IGDB para un término de búsqueda."""
        try:
            url = f"{self.igdb_base_url}/{self.endpoint}"
            headers = {
                "Client-ID": self.client_id,
                "Authorization": f"Bearer {self.access_token}"
            }

            # IGDB usa un lenguaje de query propio en el body (texto plano)
            body = (
                "fields name, first_release_date, rating, rating_count, "
                "genres.name, platforms.name, cover.url; "
                f'search "{query_text.strip()}"; '
                f"limit {self.limit};"
            )

            response = requests.post(url, headers=headers, data=body, timeout=10)

            # Si token expiró, lo refrescamos una vez
            if response.status_code == 401:
                logger.warning("⚠️ Token expirado. Renovando token...")
                self.access_token = self.obtener_token()
                headers["Authorization"] = f"Bearer {self.access_token}"
                response = requests.post(url, headers=headers, data=body, timeout=10)

            response.raise_for_status()
            data = response.json()

            logger.info(f"✅ Datos extraídos para query: {query_text.strip()}")
            return data

        except Exception as e:
            logger.error(f"❌ Error extrayendo datos para query {query_text}: {str(e)}")
            return None

    def procesar_respuesta(self, juegos, query_text):
        """Convierte la respuesta IGDB en una lista de dicts planos (listos para CSV/JSON)."""
        try:
            resultados = []

            for juego in juegos:
                genres = juego.get("genres", [])
                platforms = juego.get("platforms", [])
                cover = juego.get("cover", {})

                resultados.append({
                    "query": query_text.strip(),
                    "id": juego.get("id"),
                    "nombre": juego.get("name"),
                    "fecha_lanzamiento": juego.get("first_release_date"),
                    "rating": juego.get("rating"),
                    "rating_count": juego.get("rating_count"),
                    "generos": ", ".join([g.get("name") for g in genres if g.get("name")]) if genres else None,
                    "plataformas": ", ".join([p.get("name") for p in platforms if p.get("name")]) if platforms else None,
                    "cover_url": cover.get("url"),
                    "fecha_extraccion": datetime.now().isoformat()
                })

            return resultados

        except Exception as e:
            logger.error(f"❌ Error procesando respuesta: {str(e)}")
            return []

    def ejecutar_extraccion(self):
        """Ejecuta la extracción para todas las queries (equivalente a ciudades)."""
        datos_extraidos = []
        logger.info(f"Iniciando extracción para {len(self.queries)} queries...")

        for q in self.queries:
            juegos = self.extraer_juegos(q)
            if juegos:
                datos_procesados = self.procesar_respuesta(juegos, q)
                datos_extraidos.extend(datos_procesados)

        return datos_extraidos


if __name__ == "__main__":
    try:
        extractor = IGDBExtractor()
        datos = extractor.ejecutar_extraccion()

        # Guardar como JSON
        os.makedirs("data", exist_ok=True)
        with open('data/igdb_raw.json', 'w', encoding="utf-8") as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)
        logger.info("📁 Datos guardados en data/igdb_raw.json")

        # Guardar como CSV
        df = pd.DataFrame(datos)
        df.to_csv('data/igdb.csv', index=False, encoding="utf-8")
        logger.info("📁 Datos guardados en data/igdb.csv")

        print("\n" + "="*50)
        print("RESUMEN DE EXTRACCIÓN")
        print("="*50)
        if df.empty:
            print("No se extrajeron datos.")
        else:
            print(df.to_string(index=False))
        print("="*50)

    except Exception as e:
        logger.error(f"Error en extracción: {str(e)}")
