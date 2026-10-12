"""Создаёт таблицы parameters/rules по моделям SQLAlchemy.

Использование: python -m app.init_db
"""

from . import models  # noqa: F401 — импорт регистрирует модели в Base.metadata
from .database import Base, engine


def init_db() -> None:
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
