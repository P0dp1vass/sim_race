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
| [`research/`](research/) | Исследование ниши симрейсинга (боли, спрос, пилотаж vs сетап) |
| [`planning/`](planning/) | Реестр задач спринта |
| [`assets/board-screenshots/`](assets/board-screenshots/) | Скриншоты доски проекта (цель, бэклог, roadmap) |

## Документация MVP

- [docs/architecture.md](docs/architecture.md) — выделение сервисов, границы
  frontend/Setup Recommendation Service/SQLite, поток данных, ответственность
  компонентов, ссылки на диаграммы.
- [docs/api-contract.md](docs/api-contract.md) — контракт `GET /health` и
  `POST /api/v1/recommendations`: поля запроса/ответа, ошибки, отсутствие совпадения.
- [docs/openapi/setup-recommendation-service.yaml](docs/openapi/setup-recommendation-service.yaml) —
  тот же контракт в формате OpenAPI 3.0 (для `/docs` и кодогенерации).
- [docs/diagrams/](docs/diagrams/) — компонентная, две потоковых (happy path, 500) и
  ER-диаграмма SQLite в формате PlantUML.
- [docs/architecture-decisions.md](docs/architecture-decisions.md) — сравнение
  альтернатив (ORM vs сырой SQL, алгоритм сопоставления жалобы) и список открытых
  вопросов, которые реестр задач не закрывает.

Ветка [`feature/sqlalchemy-data-layer`](https://github.com/P0dp1vass/sim_race/tree/feature/sqlalchemy-data-layer)
демонстрирует слой данных на SQLAlchemy ORM как альтернативу сырым `sqlite3`-запросам
(см. ADR 1 в `architecture-decisions.md`).

## Стек MVP

- Frontend — веб-форма ввода жалобы и отображения рекомендации (клиент, без своего API).
- Setup Recommendation Service — FastAPI, единый endpoint рекомендаций + health-check.
- Хранилище — SQLite: параметры сетапа и экспертные правила.

MVP — один backend-сервис, не микросервисная архитектура (обоснование — в
`docs/architecture.md`, раздел «Выделение сервисов»).

MVP работает для одного заранее выбранного автомобиля и овальных трасс iRacing;
рекомендации — только по проверенным экспертным правилам, без генерации произвольных
советов через ML/LLM (см. `docs/architecture.md`, раздел «Вне границ MVP»).
