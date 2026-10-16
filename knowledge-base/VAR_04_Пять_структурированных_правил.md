# VAR-04 — Структурированные экспертные правила

**Основа:** FED-04 `nextgen_cheat_sheet_recommendations_v1.0.md`, VAR-02, VAR-03 (согласование с ALE-03).

Из FED-04 перенесены пять кандидатных способов с приоритетом P1 для симптомов, однозначно сопоставимых с фазами API. Все правила сохраняют исходный статус `draft_not_allowed` и не разрешены к выдаче до проверки FED-05. Список трасс в FED-04 не указан, поэтому `applicability.track` оставлен пустым; это не означает применимость ко всем трассам. `stint_moment: null` отражает отсутствие уточнения момента стинта в выбранных правилах.

## Правило 02-P1

```json
{
  "rule_id": "02-P1",
  "symptom_type": "understeer",
  "corner_phase": "entry",
  "stint_moment": null,
  "parameter": "front_brake_bias_pct",
  "direction": "decrease",
  "change_description": "Уменьши `front_brake_bias_pct` на 1 доступный шаг.",
  "expected_effect": "Небольшое смещение баланса назад может облегчить вращение на входе при отпускании тормоза.",
  "limitations": "Остановиться, если появляется блокировка задних колёс или резкий oversteer. Доступный шаг зависит от главных цилиндров.",
  "applicability": {
    "car": [
      "NASCAR Cup Series Next Gen (Gen 7)"
    ],
    "track": []
  },
  "status": "draft_not_allowed",
  "basis": "SRC-02; SRC-07"
}
```

## Правило 03-P1

```json
{
  "rule_id": "03-P1",
  "symptom_type": "understeer",
  "corner_phase": "mid",
  "stint_moment": null,
  "parameter": "front_arb_arm_position",
  "direction": "decrease",
  "change_description": "Переведи `front_arb_arm_position` на 1 позицию мягче (например, P4 → P3).",
  "expected_effect": "Более мягкий передний стабилизатор уменьшает креновую жёсткость передней оси и может уменьшить understeer.",
  "limitations": "P1 — минимум жёсткости, P5 — максимум. Проверять отдельно от диаметра и преднатяга.",
  "applicability": {
    "car": [
      "NASCAR Cup Series Next Gen (Gen 7)"
    ],
    "track": []
  },
  "status": "draft_not_allowed",
  "basis": "SRC-01; SRC-02"
}
```

## Правило 05-P1

```json
{
  "rule_id": "05-P1",
  "symptom_type": "understeer",
  "corner_phase": "exit",
  "stint_moment": null,
  "parameter": "rear_arb_arm_position",
  "direction": "increase",
  "change_description": "Переведи `rear_arb_arm_position` на 1 позицию жёстче (например, P2 → P3).",
  "expected_effect": "Может уменьшить understeer на выходе.",
  "limitations": "Повышает риск oversteer под газом; не использовать при потере заднего сцепления.",
  "applicability": {
    "car": [
      "NASCAR Cup Series Next Gen (Gen 7)"
    ],
    "track": []
  },
  "status": "draft_not_allowed",
  "basis": "SRC-01; SRC-02"
}
```

## Правило 07-P1

```json
{
  "rule_id": "07-P1",
  "symptom_type": "oversteer",
  "corner_phase": "entry",
  "stint_moment": null,
  "parameter": "front_brake_bias_pct",
  "direction": "increase",
  "change_description": "Увеличь `front_brake_bias_pct` на 1 доступный шаг.",
  "expected_effect": "Смещение баланса вперёд может уменьшить вращение на входе и повысить стабильность торможения.",
  "limitations": "Остановиться при чрезмерном understeer или блокировке передних колёс; шаг зависит от цилиндров.",
  "applicability": {
    "car": [
      "NASCAR Cup Series Next Gen (Gen 7)"
    ],
    "track": []
  },
  "status": "draft_not_allowed",
  "basis": "SRC-02; SRC-07"
}
```

## Правило 10-P1

```json
{
  "rule_id": "10-P1",
  "symptom_type": "oversteer",
  "corner_phase": "exit",
  "stint_moment": null,
  "parameter": "rear_arb_arm_position",
  "direction": "decrease",
  "change_description": "Переведи `rear_arb_arm_position` на 1 позицию мягче (например, P4 → P3).",
  "expected_effect": "Может уменьшить резкость реакции задней оси на выходе.",
  "limitations": "Возможен рост understeer; проверять отдельно от преднатяга.",
  "applicability": {
    "car": [
      "NASCAR Cup Series Next Gen (Gen 7)"
    ],
    "track": []
  },
  "status": "draft_not_allowed",
  "basis": "SRC-01; SRC-02"
}
```

**Соответствие FED-04:** `02/P1`, `03/P1`, `05/P1`, `07/P1`, `10/P1`. В `direction` использовано явно указанное направление действия из FED-04 вместо несовместимого с VAR-03 значения `conditional`. Остальные кандидаты P2–P6 в этот набор из пяти правил не включены.
