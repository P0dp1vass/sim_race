# Технические ограничения сетапов для автомобиля класса NASCAR Cup Series Next Gen (Gen 7)

## Универсальные значения по умолчанию

### Колеса

| Поле | Тип значения | Нижний предел | Верхний предел | Особенности |
|---|---|---|---|---|
| `lf_cold_pressure_psi` | number | 15.0 | 25.0 | Шаг регулировки 0.5 psi. Можно изменять на пит-стопе в тех же пределах с тем же шагом |
| `lr_cold_pressure_psi` | number | 15.0 | 25.0 | Шаг регулировки 0.5 psi. Можно изменять на пит-стопе в тех же пределах с тем же шагом |
| `rf_cold_pressure_psi` | number | 40.0 | 50.0 | Шаг регулировки 0.5 psi. Можно изменять на пит-стопе в тех же пределах с тем же шагом |
| `rr_cold_pressure_psi` | number | 40.0 | 50.0 | Шаг регулировки 0.5 psi. Можно изменять на пит-стопе в тех же пределах с тем же шагом |

### `setup_values.front`

| Поле | Тип | Нижний предел | Верхний предел | Особенности |
|---|---|---|---|---|
| `nose_weight_pct` | number | 48.2 | 52.5 | Шаг регулировки около 0.07 |
| `cross_weight_pct` | number | 45.0 | 75.0 | Непрерывное значение. Calculated, cannot be adjusted directly |
| `steering_pinion_in_per_rev` | enum `1.57`, `1.83`, `2.08`, `2.36`, `2.64`, `2.87`, `3.15` | `1.57` | `3.15` | Выбираемое из списка значение |
| `steering_offset_deg` | number | -30 | 30 | Шаг регулировки 1 градус. Отрицательное значение - смещение руля против часовой стрелки, положительное - по часовой |
| `front_mc` | enum `19/32`, `5/8`, `11/16`, `3/4`, `13/16`, `27/32`, `7/8`. `15/16`, `1` | `19/32` | `1` | Выбираемое из списка значение. Измеряется в дюймах |
| `rear_mc` | enum `19/32`, `5/8`, `11/16`, `3/4`, `13/16`, `27/32`, `7/8`. `15/16`, `1` | `19/32` | `1` | Выбираемое из списка значение. Измеряется в дюймах |
| `front_brake_bias_pct` | number | 21.3 | 78.7 | Весь спектр недостижим при выбранных тормозных цилиндрах. `front_mc` и `rear_mc` определяют нижний, верхний пределы, а также шаг регулировки. Для каждой комбинации все три характеристики уникальны. Например, при конфигурации `front_mc`=`7/8`, `rear_mc`=`27/32` нижний предел 42.6, верхний предел 54.6, шаг регулировки около 0.27. Можно изменять прямо во время гонки во всем доступном диапазоне | 

### `setup_values.front_arb`

| Поле | Тип | Нижний предел | Верхний предел | Особенности |
|---|---|---|---|---|
| `front_arb_diameter_in` | number | 1.375 | 2.000 | Шаг регулировки 0.625 |
| `front_arb_arm_position` | enum `P1`-`P5` | `P1` | `P5` | `P1` - softest, `P5` - stiffest |
| `front_arb_link_slack_in` | number | 5.799 | -0.251 | Пределы не перепутаны: крутится в противоположную сторону (увеличение ползунка -> уменьшение значения). Шаг регулировки различается, в рабочих пределах около 0.002-0.010 in. Все положительные значения дают `front_arb_preload_ft_lbs` = 0 = const. БОльшие отрицательные значения по модулю увеличивают по модулю `front_arb_preload_ft_lbs` < 0. Например, `front_arb_link_slack_in` = 0.003 -> `front_arb_preload_ft_lbs` = 0, `front_arb_link_slack_in` = -0.002 -> `front_arb_preload_ft_lbs` = -12.4, `front_arb_link_slack_in` = -0.004 -> `front_arb_preload_ft_lbs` = -31.0 |
| `front_arb_preload_ft_lbs` | number | -120.0 | 0 | Непрерывное значение. Calculated, cannot be adjusted directly. Предельное значение может отличаться в зависимости от конфигурации шасси. Напрямую зависит от `front_arb_link_slack_in` и любых косвенных изменений `cross_weight_pct` (при ненулевом значении). Влияет на `cross_weight_pct`, `<lf,lr,rf,rr>_corner_weight_lbs`, `<lf,rf,rr>_ride_height_in`, `<lf,lr,rf,rr>_camber_deg`, `<lf,rf>_caster_deg`. Например, увеличение по модулю `front_arb_preload_ft_lbs`: -12.4 -> -31.0 приводит к `cross_weight_pct`: 51.7 -> 52.0, `lf_corner_weight_lbs`: 906 -> 900, `rf_corner_weight_lbs`: 962 -> 968, `lr_corner_weight_lbs`: 913 -> 919, `rr_corner_weight_lbs`: 845 -> 839, `lf_ride_height_in`: 1.557 -> 1.557 (уменьшение меньше, чем 0.001), `rf_ride_height_in`: 1.890 -> 1.893, `rr_ride_height_in`: 1.733 -> 1.736, `lf_camber_deg`: +5.7 -> +5.8, `rf_camber_deg`: -5.4 -> -5.4 (движение в сторону -5.5 меньше, чем 0.1 deg), `lr_camber_deg`: +4.0 -> +4.0 (движение в сторону +4.1 меньше, чем 0.1 deg), `rr_camber_deg`: -3.9 -> -3.9 (движение в сторону -4.0 меньше, чем 0.1 deg), `lf_caster_deg`: +8.3 -> +8.3 (движение в сторону +8.4 меньше, чем 0.1 deg), `rf_caster_deg`: +10.7 -> +10.7 (незначительное изменение, можно приближенно считать константой) | 
| `front_arb_attached` | boolean | false | true | Быстрое присоединение/отсоединение Front ARB. Перед выполнением любых spring/ride heights adjustments нужно increase link slack and unhook the ARB. Attach and reduce link slack when done. |

### `setup_values.front_corners`

| Поле | Тип | Нижний предел | Верхний предел | Особенности |
|---|---|---|---|---|
| `lf_corner_weight_lbs` | number | 100 | 2000 | Непрерывное значение. Calculated, cannot be adjusted directly. |
| `rf_corner_weight_lbs` | number | 100 | 2000 | Непрерывное значение. Calculated, cannot be adjusted directly. |
| `lf_ride_height_in` | number | 0.500 | 4.140 | Непрерывное значение. Calculated, cannot be adjusted directly. Управляется любым из `<lf,lr,rf,rr>_shock_collar_offset_in`. В отличие от других машин, минимальный предел на Next Gen далеко не обязательно достигается для избежания bottoming. |
| `rf_ride_height_in` | number | 0.500 | 3.000 | Непрерывное значение. Calculated, cannot be adjusted directly. Управляется любым из `<lf,lr,rf,rr>_shock_collar_offset_in`. |
| `lf_shock_collar_offset_in` | number | 0.000 | 7.000 | Шаг регулировки 0.0155. Например (все значения даны при unattached Front/Rear ARB; при attached ARBs порядок изменений другой, но в ту же сторону), увеличение на 1 клик `lf_shock_collar_offset_in` 4.375 -> 4.391 дает: `lf_corner_weight_lbs`: 897 -> 893, `rf_corner_weight_lbs`: 970 -> 975, `lr_corner_weight_lbs`: 922 -> 926, `rr_corner_weight_lbs`: 836 -> 832, `lf_ride_height_in`: 1.565 -> 1.555, `rf_ride_height_in`: 1.886 -> 1.879, `rr_ride_height_in`: 1.717 -> 1.718, `cross_weight_pct`: 52.2 -> 52.4 |
| `rf_shock_collar_offset_in` | number | 0.000 | 7.000 | Шаг регулировки 0.0155. Например (все значения даны при unattached Front/Rear ARB; при attached ARBs порядок изменений другой, но в ту же сторону), увеличение на 1 клик `rf_shock_collar_offset_in` 3.516 -> 3.531 дает: `lf_corner_weight_lbs`: 897 -> 901, `rf_corner_weight_lbs`: 970 -> 966, `lr_corner_weight_lbs`: 922 -> 918, `rr_corner_weight_lbs`: 836 -> 840, `lf_ride_height_in`: 1.565 -> 1.556, `rf_ride_height_in`: 1.886 -> 1.875, `rr_ride_height_in`: 1.717 -> 1.712, `cross_weight_pct`: 52.2 -> 52.0 |
| `lf_spring_rate_lbs_per_in` | number | 400 | 4600 | Шаг регулировки 25 |
| `rf_spring_rate_lbs_per_in` | number | 400 | 4600 | Шаг регулировки 25 |
| `lf_ls_compression_clicks` | integer | 1 | 10 | Min damping at 1 setting. Max damping at 10 setting. |
| `rf_ls_compression_clicks` | integer | 1 | 10 | Min damping at 1 setting. Max damping at 10 setting. |
| `lf_hs_compression_clicks` | integer | 1 | 10 | Min damping at 1 setting. Max damping at 10 setting. |
| `rf_hs_compression_clicks` | integer | 1 | 10 | Min damping at 1 setting. Max damping at 10 setting. |
| `lf_hs_comp_slope_clicks` | integer | 1 | 10 | Min damping at 1 setting. Max damping at 10 setting. |
| `rf_hs_comp_slope_clicks` | integer | 1 | 10 | Min damping at 1 setting. Max damping at 10 setting. |
| `lf_ls_rebound_clicks` | integer | 1 | 10 | Min damping at 1 setting. Max damping at 10 setting. |
| `rf_ls_rebound_clicks` | integer | 1 | 10 | Min damping at 1 setting. Max damping at 10 setting. |
| `lf_hs_rebound_clicks` | integer | 1 | 10 | Min damping at 1 setting. Max damping at 10 setting. |
| `rf_hs_rebound_clicks` | integer | 1 | 10 | Min damping at 1 setting. Max damping at 10 setting. |
| `lf_hs_rebound_slope_clicks` | integer | 1 | 10 | Min damping at 1 setting. Max damping at 10 setting. |
| `rf_hs_rebound_slope_clicks` | integer | 1 | 10 | Min damping at 1 setting. Max damping at 10 setting. |
| `lf_camber_deg` | number | +0.9 | +6.0 | Шаг регулировки около 0.1. Inward (negative) or outward (positive) lean of the wheel |
| `rf_camber_deg` | number | -6.0 | -1.5 | Шаг регулировки около 0.1. Inward (negative) or outward (positive) lean of the wheel |
| `lf_caster_deg` | number | +8.0 | +12.4 | Шаг регулировки около 0.2. How much the steering axis is leaned back (positive) or forward (negative) |
| `rf_caster_deg` | number | +9.2 | +16.8 | Шаг регулировки около 0.2. How much the steering axis is leaned back (positive) or forward (negative) |
| `lf_toe_in_native` | string | `-8/32` | `+2/32` | Шаг регулировки 1/32. Измеряется в натуральных дробях дюймов. Крайние значения могут отличаться в зависимости от конфигурации шасси | 
| `rf_toe_in_native` | string | `-8/32` | `+2/32` | Шаг регулировки 1/32. Измеряется в натуральных дробях дюймов. Крайние значения могут отличаться в зависимости от конфигурации шасси | 

### `setup_values.rear_corners`

| Поле | Тип | Нижний предел | Верхний предел | Особенности |
|---|---|---|---|---|
| `lr_corner_weight_lbs` | number | 100 | 2000 | Непрерывное значение. Calculated, cannot be adjusted directly. |
| `rr_corner_weight_lbs` | number | 100 | 2000 | Непрерывное значение. Calculated, cannot be adjusted directly. |
| `rr_ride_height_in` | number, optional for LR if not provided | 0.500 | 3.000 | Непрерывное значение. Calculated, cannot be adjusted directly. Управляется любым из `<lf,lr,rf,rr>_shock_collar_offset_in`. Для машины Next Gen высота LR и RR одинаковая, используется одно значение |
| `lr_shock_collar_offset_in` | number | 0.000 | 7.000 | Шаг регулировки 0.0155. Можно изменять во время пит-стопа с шагом регулировки 0.031 до 10 кликов вперед/назад относительно значения в сетапе. Например (все значения даны при unattached Front/Rear ARB; при attached ARBs порядок изменений другой, но в ту же сторону), увеличение в гараже на 1 клик `lr_shock_collar_offset_in` 5.266 -> 5.281 дает:  `lf_corner_weight_lbs`: 897 -> 902, `rf_corner_weight_lbs`: 970 -> 966, `lr_corner_weight_lbs`: 922 -> 918, `rr_corner_weight_lbs`: 836 -> 840, `lf_ride_height_in`: 1.565 -> 1.562, `rf_ride_height_in`: 1.886 -> 1.887, `rr_ride_height_in`: 1.717 -> 1.714, `cross_weight_pct`: 52.2 -> 52.0 |
| `rr_shock_collar_offset_in` | number | 0.000 | 7.000 | Шаг регулировки 0.0155. Можно изменять во время пит-стопа с шагом регулировки 0.031 до 10 кликов вперед/назад относительно значения в сетапе. Например (все значения даны при unattached Front/Rear ARB; при attached ARBs порядок изменений другой, но в ту же сторону), увеличение в гараже на 1 клик `rr_shock_collar_offset_in` 4.125 -> 4.141 дает: `lf_corner_weight_lbs`: 897 -> 893, `rf_corner_weight_lbs`: 970 -> 975, `lr_corner_weight_lbs`: 922 -> 927, `rr_corner_weight_lbs`: 836 -> 831, `lf_ride_height_in`: 1.565 -> 1.567, `rf_ride_height_in`: 1.886 -> 1.885, `rr_ride_height_in`: 1.717 -> 1.704, `cross_weight_pct`: 52.2 -> 52.5 |
| `lr_spring_rate_lbs_per_in` | number | 400 | 4600 | Шаг регулировки 25 |
| `rr_spring_rate_lbs_per_in` | number | 400 | 4600 | Шаг регулировки 25 |
| `lr_ls_compression_clicks` | integer | 1 | 10 | Min damping at 1 setting. Max damping at 10 setting. |
| `rr_ls_compression_clicks` | integer | 1 | 10 | Min damping at 1 setting. Max damping at 10 setting. |
| `lr_hs_compression_clicks` | integer | 1 | 10 | Min damping at 1 setting. Max damping at 10 setting. |
| `rr_hs_compression_clicks` | integer | 1 | 10 | Min damping at 1 setting. Max damping at 10 setting. |
| `lr_hs_comp_slope_clicks` | integer | 1 | 10 | Min damping at 1 setting. Max damping at 10 setting. |
| `rr_hs_comp_slope_clicks` | integer | 1 | 10 | Min damping at 1 setting. Max damping at 10 setting. |
| `lr_ls_rebound_clicks` | integer | 1 | 10 | Min damping at 1 setting. Max damping at 10 setting. |
| `rr_ls_rebound_clicks` | integer | 1 | 10 | Min damping at 1 setting. Max damping at 10 setting. |
| `lr_hs_rebound_clicks` | integer | 1 | 10 | Min damping at 1 setting. Max damping at 10 setting. |
| `rr_hs_rebound_clicks` | integer | 1 | 10 | Min damping at 1 setting. Max damping at 10 setting. |
| `lr_hs_rebound_slope_clicks` | integer | 1 | 10 | Min damping at 1 setting. Max damping at 10 setting. |
| `rr_hs_rebound_slope_clicks` | integer | 1 | 10 | Min damping at 1 setting. Max damping at 10 setting. |
| `lr_camber_deg` | number | -0.8 | +4.0 | Шаг регулировки около 0.2. Inward (negative) or outward (positive) lean of the wheel |
| `rr_camber_deg` | number | -4.0 | -1.8 | Шаг регулировки около 0.2. Inward (negative) or outward (positive) lean of the wheel |
| `lr_toe_in__native` | string | `-5/32` | `+6/32` | Шаг регулировки 1/32. Измеряется в натуральных дробях дюймов. Крайние значения могут отличаться в зависимости от конфигурации шасси | 
| `rr_toe_in__native` | string | `-0/32` | `+6/32` | Шаг регулировки 1/32. Измеряется в натуральных дробях дюймов. Крайние значения могут отличаться в зависимости от конфигурации шасси | 

### `setup_values.rear`

| Поле | Тип | Нижний предел | Верхний предел | Особенности |
|---|---|---|---|---|
| `rear_final_drive_ratio` | number | 3.341 | 5.474 | Для каждой конкретной трассы есть заблокированный очень короткий диапазон из 1-3 значений. Например, в Pocono есть выбор только между 3.580, 3.636, 3.684 |
| `rear_diff_preload_ft_lbs` | number | 0 | 75 | Шаг регулировки 5 |
| `rear_arb_diameter_in` | number | 1.375 | 2.000 | Шаг регулировки 0.625 |
| `rear_arb_arm_position` | enum `P1`-`P5` | `P1` | `P5` | `P1` - softest, `P5` - stiffest |
| `rear_arb_preload_ft_lbs` | number | 0 | -120.0 | Непрерывное, но, в отличие от Front ARB, напрямую изменяемое значение. Предельное значение может отличаться в зависимости от конфигурации шасси. Клики вправо дают увеличение преднатяга по модулю. Влияет на `cross_weight_pct`, `<lf,lr,rf,rr>_corner_weight_lbs`, `<lf,rf,rr>_ride_height_in`, `<lf,lr,rf,rr>_camber_deg`, `<lf,rf>_caster_deg`. Например, увеличение по модулю `rear_arb_preload_ft_lbs`: -61.3 -> -82.4 приводит к `cross_weight_pct`: 51.7 -> 51.4, `lf_corner_weight_lbs`: 906 -> 912, `rf_corner_weight_lbs`: 962 -> 956, `lr_corner_weight_lbs`: 913 -> 908, `rr_corner_weight_lbs`: 845 -> 850, `lf_ride_height_in`: 1.557 -> 1.555, `rf_ride_height_in`: 1.890 -> 1.891, `rr_ride_height_in`: 1.733 -> 1.737, `lf_camber_deg`: +5.7 -> +5.8, `rf_camber_deg`: -5.4 -> -5.4 (движение в сторону -5.5 меньше, чем 0.1 deg), `lr_camber_deg`: +4.0 -> +4.0 (движение в сторону +4.1 меньше, чем 0.1 deg), `rr_camber_deg`: -3.9 -> -3.9 (движение в сторону -4.0 меньше, чем 0.1 deg), `lf_caster_deg`: +8.3 -> +8.3 (движение в сторону +8.2 меньше, чем 0.1 deg), `rf_caster_deg`: +10.7 -> +10.7 (движение в сторону +10.6 меньше, чем 0.1 deg) | 
| `rear_arb_attached` | boolean | false | true | Быстрое присоединение/отсоединение Rear ARB. Перед выполнением любых spring/ride heights adjustments нужно unhook the ARB. Attach when done. |

## Различия при `aero_package`=`shorttrack`

### Колеса

| Поле | Тип значения | Нижний предел | Верхний предел | Особенности |
|---|---|---|---|---|
| `lf_cold_pressure_psi` | number | 10.0 | 20.0 | Шаг регулировки 0.5 psi. Можно изменять на пит-стопе в тех же пределах с тем же шагом |
| `lr_cold_pressure_psi` | number | 10.0 | 20.0 | Шаг регулировки 0.5 psi. Можно изменять на пит-стопе в тех же пределах с тем же шагом |
| `rf_cold_pressure_psi` | number | 20.0 | 30.0 | Шаг регулировки 0.5 psi. Можно изменять на пит-стопе в тех же пределах с тем же шагом |
| `rr_cold_pressure_psi` | number | 20.0 | 30.0 | Шаг регулировки 0.5 psi. Можно изменять на пит-стопе в тех же пределах с тем же шагом |

## Различия при `aero_package`=`road`

### Колеса

| Поле | Тип значения | Нижний предел | Верхний предел | Особенности |
|---|---|---|---|---|
| `lf_cold_pressure_psi` | number | 15.0 | 25.0 | Шаг регулировки 0.5 psi. Можно изменять на пит-стопе в тех же пределах с тем же шагом |
| `lr_cold_pressure_psi` | number | 15.0 | 25.0 | Шаг регулировки 0.5 psi. Можно изменять на пит-стопе в тех же пределах с тем же шагом |
| `rf_cold_pressure_psi` | number | 15.0 | 25.0 | Шаг регулировки 0.5 psi. Можно изменять на пит-стопе в тех же пределах с тем же шагом |
| `rr_cold_pressure_psi` | number | 15.0 | 25.0 | Шаг регулировки 0.5 psi. Можно изменять на пит-стопе в тех же пределах с тем же шагом |

### `setup_values.front_arb`
| Поле | Тип | Нижний предел | Верхний предел | Особенности |
|---|---|---|---|---|
| `front_arb_preload_ft_lbs` | number | -120.0 | 120.0 | Идея параметра аналогична, но появляются положительные значения |

### `setup_values.rear`
| Поле | Тип | Нижний предел | Верхний предел | Особенности |
|---|---|---|---|---|
| `rear_arb_preload_ft_lbs` | number | 120.0 | -120.0 | Идея параметра аналогична, но появляются положительные значения |
