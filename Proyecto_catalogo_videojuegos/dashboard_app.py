#!/usr/bin/env python3

import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import sys
import os

# Permite importar la carpeta scripts
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.database import SessionLocal
from scripts.models import Juego

# -----------------------------------------------------
# Configuración de la página
# -----------------------------------------------------

st.set_page_config(
    page_title="Dashboard Videojuegos",
    page_icon="🎮",
    layout="wide"
)

st.title("🎮 Dashboard de Videojuegos - IGDB ETL")
st.markdown("---")

# -----------------------------------------------------
# Conexión a base de datos
# -----------------------------------------------------

db = SessionLocal()

try:

    juegos = db.query(Juego).all()

    data = []

    for j in juegos:

        data.append({
            "Nombre": j.nombre,
            "Rating": j.rating,
            "Votos": j.rating_count,
            "Fecha Lanzamiento": j.fecha_lanzamiento,
            "Año": j.fecha_lanzamiento.year if j.fecha_lanzamiento else None
        })

    df = pd.DataFrame(data)

    # -----------------------------------------------------
    # Sidebar filtros
    # -----------------------------------------------------

    st.sidebar.title("🔎 Filtros")

    anios = sorted(df["Año"].dropna().unique())

    anio_filtro = st.sidebar.multiselect(
        "Seleccionar años",
        options=anios,
        default=anios
    )

    df_filtrado = df[df["Año"].isin(anio_filtro)]

    # -----------------------------------------------------
    # Métricas principales
    # -----------------------------------------------------

    st.subheader("📊 Métricas principales")

    col1, col2, col3 = st.columns(3)

    with col1:

        promedio_rating = df_filtrado["Rating"].mean()

        st.metric(
            "⭐ Rating promedio",
            f"{promedio_rating:.2f}"
        )

    with col2:

        juego_mejor = df_filtrado.sort_values(
            "Rating", ascending=False
        ).iloc[0]

        st.metric(
            "🏆 Mejor juego",
            juego_mejor["Nombre"]
        )

    with col3:

        total_juegos = len(df_filtrado)

        st.metric(
            "🎮 Total juegos",
            total_juegos
        )

    st.markdown("---")

    # -----------------------------------------------------
    # GRÁFICOS
    # -----------------------------------------------------

    st.subheader("📈 Visualizaciones")

    col1, col2 = st.columns(2)

    # TOP 10 RATING

    with col1:

        top_rating = df_filtrado.sort_values(
            "Rating", ascending=False
        ).head(10)

        fig = px.bar(
            top_rating,
            x="Rating",
            y="Nombre",
            orientation="h",
            title="Top 10 videojuegos por rating",
            color="Rating"
        )

        st.plotly_chart(fig, use_container_width=True)

    # MÁS VOTADOS

    with col2:

        top_votos = df_filtrado.sort_values(
            "Votos", ascending=False
        ).head(10)

        fig = px.bar(
            top_votos,
            x="Votos",
            y="Nombre",
            orientation="h",
            title="Top videojuegos con más votos",
            color="Votos"
        )

        st.plotly_chart(fig, use_container_width=True)

    # -----------------------------------------------------
    # JUEGOS POR AÑO
    # -----------------------------------------------------

    st.subheader("📅 Juegos por año")

    juegos_anio = df_filtrado.groupby("Año").size().reset_index(name="Cantidad")

    fig = px.line(
        juegos_anio,
        x="Año",
        y="Cantidad",
        markers=True,
        title="Cantidad de videojuegos por año"
    )

    st.plotly_chart(fig, use_container_width=True)

    # -----------------------------------------------------
    # TABLA
    # -----------------------------------------------------

    st.subheader("📋 Tabla de videojuegos")

    st.dataframe(
        df_filtrado.sort_values(
            "Rating", ascending=False
        ),
        use_container_width=True
    )

finally:

    db.close()