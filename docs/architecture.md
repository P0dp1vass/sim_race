# Архитектура MVP — AI Assistant for Simracing Setups

**Версия 2, 16.10.2026.** Запрос стал структурированным, добавлено хранение запросов и
отзывов (решение 2 из ALE-03 v2, 15.10) — это меняет раздел «Вне границ MVP» из версии 1.

## Выделение сервисов

В MVP — один HTTP-сервис: **Setup Recommendation Service** (FastAPI + SQLite). Frontend — клиент этого сервиса, не отдельный API-сервис (не имеет собственного публичного HTTP API, не описывается OpenAPI).

Если база правил или штат экспертов вырастут, «базу знаний» можно вынести в отдельный сервис с собственным API (CRUD над `parameters`/`rules`) — это не входит в MVP.

## Компоненты и границы

### Frontend
- Веб-форма: пилот выбирает машину, трассу, тип симптома (`understeer`/`oversteer`),
  фазу поворота (`entry`/`mid`/`exit`), опционально момент стинта, и пишет обязательный
  комментарий своими словами — 6 полей запроса ([api-contract.md](api-contract.md)).
- Состояния интерфейса: загрузка, рекомендация найдена, совпадений нет, ошибка запроса.
- Компонент рекомендации: отображает параметр, направление изменения, ожидаемый эффект
  и ограничения — всё, что пришло в ответе backend. Содержит ссылку на форму отзыва
  (`/feedback/{request_id}?rule_id=...`).
- Форма отзыва (ALE-04): появляется под карточкой или по сохранённой ссылке/`GET
  /api/v1/recommendations/{request_id}`, отправляет `POST /api/v1/feedback`.
- Frontend не хранит данные как источник истины и не содержит логику подбора
  рекомендаций — только валидация формы и отображение ответа backend. Последний запрос
  может кешироваться в localStorage как UX-удобство, не как хранилище.
- Общение с backend — исключительно через контракт ([api-contract.md](api-contract.md)):
  `GET /health`, `POST /api/v1/recommendations`,
  `GET /api/v1/recommendations/{request_id}`, `POST /api/v1/feedback`.

### Setup Recommendation Service (FastAPI)
- 4 эндпоинта: `GET /health`, `POST /api/v1/recommendations`,
  `GET /api/v1/recommendations/{request_id}`, `POST /api/v1/feedback`.
- Валидирует входящий запрос по контракту; при нарушении — 400 в формате контракта, не
  дефолтные 422 FastAPI.
- Сопоставляет структурированные поля запроса (`symptom_type`, `corner_phase`,
  `stint_moment`, членство `car`/`track` в `applicability`) с условиями экспертных
  правил в SQLite — точное совпадение значений, не текстовый поиск (см.
  [api-contract.md](api-contract.md)).
- Перед сравнением исключает из выборки правила, не прошедшие проверку — непроверенное
  правило не может попасть в ответ ни при каких условиях.
- Каждый запрос (валидный) сохраняется в таблицу `requests` вместе с исходом и списком
  совпавших `rule_id` — не только для отзыва, но и как лог нераспознанных симптомов —
  кандидатов в новые правила.
- Каждый отзыв сохраняется в `feedback`, привязан к `request_id`/`rule_id`.
- Не генерирует рекомендации произвольно — в MVP только детерминированный поиск по базе
  правил (граница с ML/LLM — [ml-llm-boundary.md](ml-llm-boundary.md), KIR-03).

### SQLite (доступ через SQLAlchemy ORM)
- Источник истины для параметров, правил, сохранённых запросов и отзывов. Доступ из
  кода — через модели SQLAlchemy, не сырые `sqlite3`-запросы (обоснование —
  [architecture-decisions.md](architecture-decisions.md), ADR 1; пример моделей — ветка
  `feature/sqlalchemy-data-layer`, пока без таблиц `requests`/`feedback` — требует
  обновления под версию 2).
- `parameters`: id, каноническое имя (словарь VAR-02, 71 параметр), единица измерения,
  описание влияния, диапазон/ограничения.
- `rules`: id, `symptom_type` (`understeer`/`oversteer`), `corner_phase`
  (`entry`/`mid`/`exit`), `stint_moment` (nullable), `parameter_id`, `direction`
  (`increase`/`decrease`), `change_description`, `expected_effect`, `limitations`,
  `applicability` (списки `car`/`track`), статус проверки, `basis`. Схема — VAR-03
  обновлённый.
- `requests` **(новое)**: `id` (UUID, он же `request_id`), 6 полей запроса, исход
  (`match`/`no_match`), список совпавших `rule_id`, время создания.
- `feedback` **(новое)**: `id`, `request_id` (FK → `requests.id`), `rule_id`, поля
  формы ALE-04 (`applied`, `symptom_result`, `new_problem`, `keep_change`, `clarity` и
  условные текстовые поля), время создания.
- `parameters`/`rules` наполняются командой данных (FED/VAR); `requests`/`feedback`
  пишет сам backend во время работы.

## Поток данных

### Рекомендация (POST /api/v1/recommendations)
1. Пилот заполняет форму на frontend (6 полей).
2. Frontend отправляет `POST /api/v1/recommendations`.
3. Backend валидирует запрос; при нарушении контракта — 400.
4. Backend ищет в SQLite правила среди статуса «разрешено к выдаче», у которых
   `symptom_type`/`corner_phase` совпали, `stint_moment` подходит, а `car`/`track`
   входят в `applicability`.
5. Backend сохраняет запрос в `requests` вместе с исходом.
6. Нет совпадений — `no_match` с `request_id`. Есть — до 3 рекомендаций (сначала
   совпавшие по `stint_moment`) с `request_id` — ответ `match`.
7. Frontend показывает результат: карточки рекомендаций, сообщение об отсутствии
   совпадения или ошибку.
8. Пилот проверяет рекомендацию в симуляторе (вне границ MVP-сервиса).

### Отзыв (POST /api/v1/feedback)
9. После заезда пилот открывает форму отзыва (под карточкой или по ссылке/`GET
   /api/v1/recommendations/{request_id}`).
10. Frontend отправляет `POST /api/v1/feedback` с `request_id`/`rule_id`, подставленными
    автоматически.
11. Backend проверяет, что `request_id` существует и `rule_id` был в его рекомендациях;
    сохраняет отзыв в `feedback`.

## Ответственность компонентов

| Компонент | Отвечает за | Не отвечает за |
|---|---|---|
| Frontend | форму ввода, состояния UI, отображение рекомендации и формы отзыва | подбор правил, хранение данных как источника истины, бизнес-логику |
| Setup Recommendation Service (FastAPI) | валидацию запросов, поиск правил, сохранение `requests`/`feedback`, формирование ответов, `/health` | генерацию произвольных советов, редактирование содержимого правил |
| SQLite | хранение параметров, правил, запросов и отзывов, статус проверки каждого правила | сопоставление запроса с правилом |

## Вне границ MVP

- Аутентификация и профили пользователей.
- Генерация рекомендаций через ML/LLM — граница зафиксирована отдельно в
  [ml-llm-boundary.md](ml-llm-boundary.md) (KIR-03).
- Поддержка нескольких автомобилей/трасс одновременно — MVP ограничен одним
  автомобилем и овальными трассами.
- ~~Хранение истории запросов пилота~~ — **больше не вне границ**: решено 15.10
  (ALE-03/ALE-04), таблицы `requests`/`feedback` выше. История используется для отзыва
  и как лог нераспознанных симптомов, не как личный кабинет пилота — без аутентификации
  доступ к своей истории идёт только по прямой ссылке с `request_id`, не по списку.

## Диаграммы

| Файл | Что показывает |
|---|---|
| [`diagrams/component.puml`](diagrams/component.puml) | Компоненты MVP и связи между ними |
| [`diagrams/sequence-recommendations.puml`](diagrams/sequence-recommendations.puml) | Поток запроса рекомендации: валидация, поиск, `match`/`no_match` |
| [`diagrams/sequence-internal-error.puml`](diagrams/sequence-internal-error.puml) | Поток внутренней ошибки (500) |
| [`diagrams/data-model.puml`](diagrams/data-model.puml) | Схема таблиц SQLite: `parameters`, `rules`, `requests`, `feedback` |

Сравнение решений и открытые вопросы — [architecture-decisions.md](architecture-decisions.md).
Граница с ML/LLM — [ml-llm-boundary.md](ml-llm-boundary.md) (KIR-03).
