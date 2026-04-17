from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from infrastructure.settings.base import Settings


def build_engine(settings: Settings):
    return create_engine(settings.sc_db_url, future=True) if settings.sc_db_url else None


def build_session_factory(settings: Settings):
    engine = build_engine(settings)
    return sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True) if engine else None

