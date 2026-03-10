#!/usr/bin/env python3

import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
from sqlalchemy import func
import sys
import os

# Permite importar scripts
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.database import SessionLocal
from scripts.models import Juego

# -----------------------------------------------------
# Configuración de página
# -----------------------------------------------------

st.set_page_config(
    page_title="Dashboard Videojuegos",
    page_icon="🎮",
    layout="wide"
)

st.title("🎮 Dashboard Avanzado - Análisis de Videojuegos")
st.markdown("---")

db = SessionLocal()

# -----------------------------------------------------
# PESTAÑAS
# -----------------------------------------------------

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Vista General",
    "📈 Histórico",
    "🔍 Análisis",
    "📋 Catálogo"
])

# =====================================================
# TAB 1 - VISTA GENERAL
# =====================================================

with tab1:

    st.subheader("Estadísticas Generales")

    col1, col2, col3 = st.columns(3)

    total_juegos = db.query(func.count(Juego.id)).scalar()
    rating_promedio = db.query(func.avg(Juego.rating)).scalar()
    votos_totales = db.query(func.sum(Juego.rating_count)).scalar()

    with col1:
        st.metric("🎮 Total Juegos", total_juegos)

    with col2:
        st.metric("⭐ Rating Promedio", f"{rating_promedio:.2f}")

    with col3:
        st.metric("🗳️ Total Votos", votos_totales)

    st.markdown("---")

    # TOP RATING

    juegos_top = db.query(
        Juego.nombre,
        Juego.rating
    ).filter(
        Juego.rating != None
    ).order_by(
        Juego.rating.desc()
    ).limit(10).all()

    df_top = pd.DataFrame(juegos_top, columns=["Juego", "Rating"])

    fig = px.bar(
        df_top,
        x="Rating",
        y="Juego",
        orientation="h",
        title="Top videojuegos por rating",
        color="Rating"
    )

    st.plotly_chart(fig, use_container_width=True)

# =====================================================
# TAB 2 - HISTÓRICO
# =====================================================

with tab2:

    st.subheader("Videojuegos por Año de Lanzamiento")

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

    df = pd.DataFrame(registros, columns=["Año", "Cantidad"])

    fig = px.line(
        df,
        x="Año",
        y="Cantidad",
        markers=True,
        title="Cantidad de videojuegos por año"
    )

    st.plotly_chart(fig, use_container_width=True)

# =====================================================
# TAB 3 - ANÁLISIS
# =====================================================

with tab3:

    st.subheader("Análisis de Rating vs Votos")

    registros = db.query(
        Juego.nombre,
        Juego.rating,
        Juego.rating_count
    ).filter(
        Juego.rating != None
    ).all()

    df = pd.DataFrame(registros, columns=["Juego", "Rating", "Votos"])

    fig = px.scatter(
        df,
        x="Rating",
        y="Votos",
        size="Votos",
        hover_name="Juego",
        title="Relación entre rating y número de votos"
    )

    st.plotly_chart(fig, use_container_width=True)

# =====================================================
# TAB 4 - CATÁLOGO
# =====================================================

with tab4:

    st.subheader("Catálogo Completo de Videojuegos")

    juegos = db.query(Juego).all()

    data = []

    for j in juegos:

        data.append({
            "Nombre": j.nombre,
            "Rating": j.rating,
            "Votos": j.rating_count,
            "Fecha Lanzamiento": j.fecha_lanzamiento
        })

    df = pd.DataFrame(data)

    st.dataframe(
        df.sort_values("Rating", ascending=False),
        use_container_width=True
    )

db.close()