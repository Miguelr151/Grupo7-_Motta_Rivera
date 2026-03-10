import os
import sys
from logging.config import fileConfig

from sqlalchemy import create_engine
from sqlalchemy import pool

from alembic import context
from dotenv import load_dotenv

# ==========================
# Cargar variables .env
# ==========================

load_dotenv()

# Permitir imports desde el proyecto
sys.path.insert(0, '.')

# ==========================
# Importar DB y modelos
# ==========================

from scripts.database import DATABASE_URL, Base
from scripts import models  # ⚠️ IMPORTANTE: para que Alembic detecte tablas

# ==========================
# Configuración Alembic
# ==========================

config = context.config

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata de modelos
target_metadata = Base.metadata

# Establecer URL de conexión
config.set_main_option("sqlalchemy.url", DATABASE_URL)


# ==========================
# MIGRACIONES OFFLINE
# ==========================

def run_migrations_offline():
    """Ejecuta migraciones sin conexión directa"""

    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True
    )

    with context.begin_transaction():
        context.run_migrations()


# ==========================
# MIGRACIONES ONLINE
# ==========================

def run_migrations_online():
    """Ejecuta migraciones conectándose a la BD"""

    connectable = create_engine(
        DATABASE_URL,
        poolclass=pool.NullPool
    )

    with connectable.connect() as connection:

        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True
        )

        with context.begin_transaction():
            context.run_migrations()


# ==========================
# EJECUCIÓN
# ==========================

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()