#!/usr/bin/env python3
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy import Index
from scripts.database import Base


class Juego(Base):
    """
    Tabla principal de videojuegos obtenidos desde IGDB
    """
    __tablename__ = "juegos"

    id = Column(Integer, primary_key=True, autoincrement=True)

    igdb_id = Column(Integer, unique=True, index=True)

    nombre = Column(String(255), nullable=False)

    fecha_lanzamiento = Column(DateTime)

    rating = Column(Float)
    rating_count = Column(Integer)

    generos = Column(String(255))
    plataformas = Column(String(255))

    cover_url = Column(String(500))

    fecha_extraccion = Column(DateTime, default=datetime.utcnow, index=True)

    fecha_creacion = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        Index("idx_juego_rating", "rating"),
    )

    def __repr__(self):
        return f"<Juego(id={self.igdb_id}, nombre='{self.nombre}', rating={self.rating})>"