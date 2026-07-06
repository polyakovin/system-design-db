---
title: Capacity Planning with USL
type: pattern
category: performance-and-scalability
tags: [scalability, usl, capacity-planning, saturation, forecasting, provisioning]
source: Practical Scalability Analysis with the Universal Scalability Law (Baron Schwartz, 2015)
added: 2026-07-06
---

# Capacity Planning with USL

## Проблема

Традиционный capacity planning — экстраполяция из бенчмарков на одном узле: «если 1 сервер держит 1000 rps, то 10 серверов — 10000 rps». Это работает только при линейной масштабируемости, чего почти никогда нет.

## Решение

USL даёт количественную модель для прогнозирования:

1. **Собрать данные:** throughput для N = 1, 2, 4, 8, ... (чем больше точек, тем точнее fit)
2. **Fit USL:** regression для получения λ, α, β
3. **Прогноз:** X(N) для любого N из модели
4. **Найти saturation point:** N_max = floor(√((1-α)/β))
5. **Определить optimal N:** knee point по latency или marginal gain < 10%

### Пример расчёта

```
Дано: λ = 1000 rps, α = 0.02, β = 0.001
N_max = floor(√((1-0.02)/0.001)) = floor(√(980)) = 31 узлов
X(31) = (1000 × 31) / (1 + 0.02×30 + 0.001×31×30)
      = 31000 / (1 + 0.6 + 0.93) = 31000 / 2.53 ≈ 12253 rps

Сравнение с линейной экстраполяцией:
Линейный прогноз для 31 узла: 31000 rps
Реальный USL прогноз:      ~12253 rps → ошибка в 2.5x
```

## Практические выводы

- **Never extrapolate linearly:** α и β всегда > 0 в реальных системах
- **Diminishing returns начинаются рано:** часто уже после 4-8 узлов marginal gain падает ниже 50%
- **Saturation — не "стена":** throughput выходит на плато постепенно; разница между N=20 и N=30 может быть < 5%
- **Beta доминирует при больших N:** если β > 0.001, N_max часто удивительно мал (10-50 узлов)

## Когда linear extrapolation приемлема

- Система embarrassingly parallel (α ≈ 0, β ≈ 0)
- N мало (2-4 узла) — penalty terms ещё незначительны
- Quick estimate, а не точный прогноз

## Связанные материалы

- [Universal Scalability Law](universal-scalability-law.md)
- [Throughput vs latency](throughput-vs-latency.md)
- [Diminishing returns](diminishing-returns.md)

## Источник

Baron Schwartz, *Practical Scalability Analysis with the Universal Scalability Law* (2015). Neil Gunther, *Guerrilla Capacity Planning* (2007).
