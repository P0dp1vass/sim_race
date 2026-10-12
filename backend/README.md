# backend — ветка feature/sqlalchemy-data-layer

Эта ветка — альтернативная реализация слоя данных ROD-02 через SQLAlchemy ORM вместо
сырых запросов `sqlite3`. Обоснование и сравнение с альтернативами — в
[`docs/architecture-decisions.md`](../docs/architecture-decisions.md) (ADR 1), схема
таблиц — в [`docs/architecture.md`](../docs/architecture.md) и
[`docs/diagrams/data-model.puml`](../docs/diagrams/data-model.puml).

## Что внутри

- `app/database.py` — engine, сессия, `Base` для деклараций моделей.
- `app/models.py` — модели `Parameter` и `Rule`, поля 1:1 со схемой `parameters`/`rules`
  из `architecture.md`.
- `app/init_db.py` — создаёт таблицы по моделям (`python -m app.init_db`).

## Запуск

```bash
cd backend
python -m venv .venv && . .venv/Scripts/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m app.init_db   # создаст setup_assistant.db рядом с backend/
```

## Статус

Только слой данных (модели + создание таблиц) — демонстрация подхода для решения по
ADR 1. Endpoint'ы (`/health`, `/api/v1/recommendations`), поиск правил и наполнение
базой (ROD-01, ROD-03, ROD-04, VAR-04) в этой ветке не реализованы — это задачи
отдельных карточек реестра, не предмет этого сравнения.
