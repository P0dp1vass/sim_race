# VAR-03 — Шаблон экспертного правила

## Поля правила

| Поле | Назначение |
|---|---|
| `rule_id` | Уникальный идентификатор правила. |
| `symptom_type` | Тип проблемы: `understeer` (недостаточная поворачиваемость) или `oversteer` (избыточная поворачиваемость). |
| `corner_phase` | Фаза поворота: `entry` (вход), `mid` (середина), `exit` (выход). |
| `stint_moment` | Момент появления проблемы: `from_start` (сразу) или `after_laps` (по ходу стинта); `null` — подходит для любого момента. |
| `parameter` | Каноническое название параметра из VAR-02. |
| `direction` | Направление изменения параметра: `increase` или `decrease`. |
| `change_description` | Что и на сколько изменить. |
| `expected_effect` | Ожидаемый эффект изменения. |
| `limitations` | Ограничения применения правила. |
| `applicability` | Область применимости: списки автомобилей (`car`) и овальных трасс (`track`), для которых правило подходит. |
| `status` | Внутренний статус проверки правила; для выдачи используется только статус «разрешено к выдаче». Пользователю не передаётся. |
| `basis` | Техническое основание правила (источник). Входит в ответ API; отображение пользователю определяется интерфейсом. |

## Шаблон

```json
{
  "rule_id": "",
  "symptom_type": "",
  "corner_phase": "",
  "stint_moment": null,
  "parameter": "",
  "direction": "",
  "change_description": "",
  "expected_effect": "",
  "limitations": "",
  "applicability": {
    "car": [],
    "track": []
  },
  "status": "",
  "basis": ""
}
```

## Соответствие с KIR-02 и ALE-03

`POST /api/v1/recommendations` принимает структурированные поля `car`, `track`, `symptom_type`, `corner_phase`, необязательное `stint_moment` и обязательный `comment` (3–500 символов).

Поиск правила выполняется по `symptom_type`, `corner_phase` и, если передано, `stint_moment`; `car` и `track` проверяются по `applicability`. Поле `comment` в поиске не участвует. Поле `symptom_condition` и поиск по подстрокам не используются.

В ответ `match` передаются `rule_id`, `parameter`, `direction`, `change_description`, `expected_effect`, `limitations`, `basis`. Поле `status` в ответ не включается. Выдаются только правила со статусом «разрешено к выдаче»; если таких совпадений нет, возвращается `no_match`.
