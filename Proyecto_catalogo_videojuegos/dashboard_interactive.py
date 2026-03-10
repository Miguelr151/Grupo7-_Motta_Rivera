#!/usr/bin/env python3

import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
from sqlalchemy import and_
import sys
import os

# Permite importar scripts
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.database import SessionLocal
from scripts.models import Juego

st.set_page_config(
    page_title="Dashboard Interactivo Videojuegos",
    page_icon="🎮",
    layout="wide"
)

# CSS simple
st.markdown("""
<style>
.metric-box {
    background-color: #f0f2f6;
    padding: 20px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("🎮 Dashboard Interactivo - Catálogo de Videojuegos")

db = SessionLocal()

# -----------------------------------------------------
# SIDEBAR FILTROS
# -----------------------------------------------------

st.sidebar.markdown("### 🔧 Controles")

# Obtener juegos
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

# Filtro por nombre
buscar = st.sidebar.text_input("🔎 Buscar videojuego")

# Filtro por rating
rating_min = st.sidebar.slider("⭐ Rating mínimo", 0.0, 100.0, 0.0)

# Filtro por votos
votos_min = st.sidebar.slider("🗳️ Votos mínimos", 0, int(df["Votos"].max()), 0)

# Filtro por año
anios = sorted(df["Año"].dropna().unique())

anios_seleccionados = st.sidebar.multiselect(
    "📅 Años",
    options=anios,
    default=anios
)

# -----------------------------------------------------
# FILTRADO
# -----------------------------------------------------

df_filtrado = df.copy()

if buscar:
    df_filtrado = df_filtrado[df_filtrado["Nombre"].str.contains(buscar, case=False)]

df_filtrado = df_filtrado[
    (df_filtrado["Rating"] >= rating_min) &
    (df_filtrado["Votos"] >= votos_min) &
    (df_filtrado["Año"].isin(anios_seleccionados))
]

# -----------------------------------------------------
# KPIs
# -----------------------------------------------------

if not df_filtrado.empty:

    st.markdown("### 📊 Indicadores")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🎮 Juegos",
            len(df_filtrado)
        )

    with col2:
        st.metric(
            "⭐ Rating Promedio",
            f"{df_filtrado['Rating'].mean():.2f}"
        )

    with col3:
        st.metric(
            "🗳️ Votos Totales",
            int(df_filtrado["Votos"].sum())
        )

    with col4:
        st.metric(
            "🏆 Mejor Rating",
            f"{df_filtrado['Rating'].max():.2f}"
        )

    st.markdown("---")

    # -------------------------------------------------
    # GRÁFICOS
    # -------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("#### ⭐ Top videojuegos por rating")

        top_rating = df_filtrado.sort_values(
            "Rating", ascending=False
        ).head(10)

        fig = px.bar(
            top_rating,
            x="Rating",
            y="Nombre",
            orientation="h",
            color="Rating"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        st.markdown("#### 🗳️ Juegos con más votos")

        top_votos = df_filtrado.sort_values(
            "Votos", ascending=False
        ).head(10)

        fig = px.bar(
            top_votos,
            x="Votos",
            y="Nombre",
            orientation="h",
            color="Votos"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # -------------------------------------------------
    # SCATTER
    # -------------------------------------------------

    st.markdown("#### 📈 Relación Rating vs Votos")

    fig = px.scatter(
        df_filtrado,
        x="Rating",
        y="Votos",
        size="Votos",
        hover_name="Nombre"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # -------------------------------------------------
    # HISTÓRICO
    # -------------------------------------------------

    st.markdown("#### 📅 Videojuegos por año")

    juegos_anio = df_filtrado.groupby("Año").size().reset_index(name="Cantidad")

    fig = px.line(
        juegos_anio,
        x="Año",
        y="Cantidad",
        markers=True
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # -------------------------------------------------
    # TABLA
    # -------------------------------------------------

    st.markdown("#### 📋 Catálogo")

    columnas = st.multiselect(
        "Columnas",
        df_filtrado.columns.tolist(),
        default=["Nombre", "Rating", "Votos", "Fecha Lanzamiento"]
    )

    st.dataframe(
        df_filtrado[columnas].sort_values("Rating", ascending=False),
        use_container_width=True
    )

    # Descargar CSV
    csv = df_filtrado.to_csv(index=False)

    st.download_button(
        "⬇️ Descargar CSV",
        csv,
        f"videojuegos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        "text/csv"
    )

else:

    st.warning("No hay datos con esos filtros")

db.close()