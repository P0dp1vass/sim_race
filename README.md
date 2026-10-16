# AI Assistant for Simracing Setups

Веб-сервис с ИИ-ассистентом, который помогает пилоту симрейсинга калибровать и
персонализировать настройки машины: пилот описывает жалобу на поведение машины,
сервис находит разрешённое экспертное правило и возвращает конкретную, проверяемую
рекомендацию по изменению сетапа.

## Структура репозитория

| Папка | Что внутри |
|---|---|
| [`docs/`](docs/) | Техническая документация MVP: архитектура, контракт API, диаграммы |
| [`docs/openapi/`](docs/openapi/) | Машиночитаемый контракт API (OpenAPI 3.0) |
| [`docs/diagrams/`](docs/diagrams/) | Диаграммы компонентов, потоков и данных (PlantUML) |
| [`product/`](product/) | Сценарий, критерии приёмки, форма обратной связи (Алёна, ALE-01…04) |
| [`knowledge-base/`](knowledge-base/) | Источники, словарь параметров, экспертные правила (Вардгес, Фёдор — VAR-01…04, nextgen_*) |
| [`research/`](research/) | Исследование ниши симрейсинга (боли, спрос, пилотаж vs сетап) |
| [`planning/`](planning/) | Реестр задач спринта |
| [`assets/board-screenshots/`](assets/board-screenshots/) | Скриншоты доски проекта (цель, бэклог, roadmap) |

## Документация MVP (v2, 16.10.2026)

- [docs/architecture.md](docs/architecture.md) — выделение сервисов, границы
  frontend/Setup Recommendation Service/SQLite (теперь включая `requests`/`feedback`),
  поток данных, ответственность компонентов, ссылки на диаграммы.
- [docs/api-contract.md](docs/api-contract.md) — контракт 4 эндпоинтов: `GET /health`,
  `POST /api/v1/recommendations` (структурированный запрос, 6 полей),
  `GET /api/v1/recommendations/{request_id}`, `POST /api/v1/feedback`.
- [docs/openapi/setup-recommendation-service.yaml](docs/openapi/setup-recommendation-service.yaml) —
  тот же контракт в формате OpenAPI 3.0 (для `/docs` и кодогенерации).
- [docs/ml-llm-boundary.md](docs/ml-llm-boundary.md) — граница между экспертными
  правилами и ML/LLM (KIR-03): что в MVP, что осталось за бортом и почему это пробел
  данных, а не повод добавлять модель.
- [docs/quality-metrics.md](docs/quality-metrics.md) — метрики качества рекомендаций
  и порядок фиксации теста (KIR-04).
- [docs/diagrams/](docs/diagrams/) — компонентная, две потоковых и ER-диаграмма SQLite
  (`parameters`, `rules`, `requests`, `feedback`) в формате PlantUML.
- [docs/architecture-decisions.md](docs/architecture-decisions.md) — обоснование
  принятых решений (SQLAlchemy, структурированный матчинг вместо текстового поиска) и
  список открытых вопросов, которые реестр задач не закрывает.

Ветка [`feature/sqlalchemy-data-layer`](https://github.com/P0dp1vass/sim_race/tree/feature/sqlalchemy-data-layer)
даёт пример моделей SQLAlchemy (`Parameter`, `Rule`) по принятому решению (ADR 1) —
справочный материал для ROD-02; пока не обновлена под схему v2 (`requests`/`feedback`).

## Стек MVP

- Frontend — веб-форма структурированного запроса и формы отзыва (клиент, без своего API).
- Setup Recommendation Service — FastAPI, 4 эндпоинта (health, рекомендации, повторный
  просмотр запроса, отзыв).
- Хранилище — SQLite через SQLAlchemy ORM: параметры, правила, запросы, отзывы.

MVP — один backend-сервис, не микросервисная архитектура (обоснование — в
`docs/architecture.md`, раздел «Выделение сервисов»).

MVP работает для одного заранее выбранного автомобиля и овальных трасс iRacing;
рекомендации — только по проверенным экспертным правилам, без генерации произвольных
советов через ML/LLM (см. `docs/ml-llm-boundary.md`).
