---
title: Modelling Real Systems with USL
type: pattern
category: performance-and-scalability
tags: [scalability, usl, modelling, curve-fitting, regression, benchmarking]
source: Practical Scalability Analysis with the Universal Scalability Law (Baron Schwartz, 2015)
added: 2026-07-06
---

# Modelling Real Systems with USL

## Проблема

USL — модель. Чтобы она была полезной, нужно правильно собрать данные, fit параметры и интерпретировать результаты. Ошибки на любом шаге дают misleading прогнозы.

## Решение: 4-шаговый процесс

### 1. Сбор данных

- Измерять throughput для N = 1, 2, 4, 6, 8, 12, 16, ... (чем больше точек, тем лучше)
- Каждая точка — steady-state throughput, а не пиковый; дождаться стабилизации
- Контролировать environment: одинаковая нагрузка на узел, одинаковое железо, нет фоновых процессов
- Собрать минимум 5-8 точек для meaningful fit; для production — continuous measurement

### 2. Fitting USL

Использовать нелинейную регрессию (least squares):

```python
from scipy.optimize import curve_fit

def usl(N, lam, alpha, beta):
    return lam * N / (1 + alpha * (N - 1) + beta * N * (N - 1))

N_data = [1, 2, 4, 6, 8, 12, 16]
X_data = [1000, 1980, 3800, 5400, 6800, 8400, 8800]  # измеренный throughput

popt, pcov = curve_fit(usl, N_data, X_data, bounds=(0, [1e6, 0.99, 0.99]))
lam, alpha, beta = popt
```

### 3. Валидация fit

- **R²** должен быть > 0.95 (объясняет > 95% variance)
- **Residuals:** проверить, что остатки случайны, без systematic patterns
- **Parameter plausibility:** α и β должны быть в разумных диапазонах (0–0.5)
- **Cross-validation:** если данных много — fit на части, проверь на остатке

### 4. Интерпретация параметров

| Параметр | Физический смысл | Типичные значения |
|---|---|---|
| λ | Baseline throughput одного узла | Измеряется; должен совпадать с реальным single-node benchmark |
| α | Contention: доля времени, которую узел тратит на ожидание shared resource | 0.01–0.10 — typical; >0.20 — проблемный |
| β | Coherency: overhead координации на пару узлов | 10⁻⁴–10⁻² — typical; >10⁻² — серьёзный |

## Pitfalls

- **Экстраполяция за пределы данных:** USL fit для N=1..8 не предскажет поведение при N=100
- **Изменение характера bottleneck:** при разных N могут доминировать разные механизмы — модель усредняет
- **Нестационарность:** если система меняется (warmup, GC, background tasks), один fit не описывает все режимы
- **Overfitting:** с малым количеством точек USL может дать идеальный fit случайно

## Практический workflow

1. Снять baseline (N=1) для калибровки λ
2. Снять throughput для нескольких N
3. Fit USL → проверить R² и residuals
4. Если R² < 0.9 — искать problem: нестационарность, выбросы, смена режима
5. Использовать модель для capacity planning и диагностики

## Связанные материалы

- [Universal Scalability Law](universal-scalability-law.md)
- [Identifying bottlenecks](identifying-bottlenecks.md)
- [Capacity planning](capacity-planning.md)

## Источник

Baron Schwartz, *Practical Scalability Analysis with the Universal Scalability Law* (2015).
