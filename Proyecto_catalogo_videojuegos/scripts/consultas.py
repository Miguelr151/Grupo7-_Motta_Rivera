#!/usr/bin/env python3

"""
CONSULTAS DE ANÁLISIS SOBRE LA BASE DE DATOS DE VIDEOJUEGOS

Este script permite analizar los datos almacenados en PostgreSQL
después de ejecutar el ETL.

Consultas incluidas:

1️⃣ Top videojuegos por rating
2️⃣ Juegos con más votos
3️⃣ Cantidad de juegos por año
"""

import sys
import os

# Permite importar la carpeta scripts correctamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
from sqlalchemy import func

from scripts.database import SessionLocal
from scripts.models import Juego

# Crear sesión de base de datos
db = SessionLocal()


# =====================================================
# TOP VIDEOJUEGOS POR RATING
# =====================================================

def juegos_mejor_rating():
    """
    Obtiene los 10 videojuegos con mejor puntuación.
    """

    registros = db.query(
        Juego.nombre,
        Juego.rating
    ).filter(
        Juego.rating != None
    ).order_by(
        Juego.rating.desc()
    ).limit(10).all()

    df = pd.DataFrame(registros, columns=["Juego", "Rating"])

    print("\n🎮 TOP 10 VIDEOJUEGOS POR RATING")
    print(df.to_string(index=False))


# =====================================================
# VIDEOJUEGOS CON MÁS VOTOS
# =====================================================

def juegos_mas_votados():
    """
    Obtiene los videojuegos con mayor cantidad de votos.
    """

    registros = db.query(
        Juego.nombre,
        Juego.rating_count
    ).filter(
        Juego.rating_count != None
    ).order_by(
        Juego.rating_count.desc()
    ).limit(10).all()

    df = pd.DataFrame(registros, columns=["Juego", "Cantidad de Votos"])

    print("\n⭐ JUEGOS MÁS VOTADOS")
    print(df.to_string(index=False))


# =====================================================
# CANTIDAD DE VIDEOJUEGOS POR AÑO
# =====================================================

def juegos_por_anio():
    """
    Cuenta cuántos videojuegos hay por año de lanzamiento.
    """

    registros = db.query(
        func.extract("year", Juego.fecha_lanzamiento).label("anio"),
        func.count(Juego.id)
    ).filter(
        Juego.fecha_lanzamiento != None
    ).group_by(
        "anio"
    ).order_by(
        "anio"
    ).all()

    df = pd.DataFrame(registros, columns=["Año", "Cantidad de Juegos"])

    print("\n📅 VIDEOJUEGOS POR AÑO")
    print(df.to_string(index=False))


# =====================================================
# EJECUCIÓN DEL SCRIPT
# =====================================================

if __name__ == "__main__":

    try:

        print("\n" + "=" * 60)
        print("ANÁLISIS DE VIDEOJUEGOS - POSTGRESQL")
        print("=" * 60)

        juegos_mejor_rating()
        juegos_mas_votados()
        juegos_por_anio()

        print("\n" + "=" * 60 + "\n")

    finally:
        db.close()