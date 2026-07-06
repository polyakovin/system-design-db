---
title: Identifying Bottlenecks with USL
type: pattern
category: performance-and-scalability
tags: [scalability, usl, bottleneck, diagnostic, profiling, regression]
source: Practical Scalability Analysis with the Universal Scalability Law (Baron Schwartz, 2015)
added: 2026-07-06
---

# Identifying Bottlenecks with USL

## Проблема

Система не масштабируется. Непонятно, в чём причина: contention (кто-то кого-то ждёт) или coherency (координация съедает ресурсы). Традиционный profiling показывает горячие точки, но не различает природу bottleneck.

## Решение

USL-фиттинг как diagnostic tool:

1. **Собрать throughput для разных N**
2. **Fit USL** → получить α и β
3. **Интерпретировать:**

| Профиль | α | β | Диагноз |
|---|---|---|---|
| Contention-limited | > 0.05 | ≈ 0 | Sequential bottleneck, serialisation |
| Coherency-limited | ≈ 0 | > 0.001 | Coordination overhead, too much sync |
| Mixed | > 0.02 | > 0.001 | Оба фактора; нужно решать оба |
| Well-behaved | < 0.02 | < 0.0005 | Почти линейная scalability при данных N |

### Пример диагностики

```
Система А: α = 0.15, β = 0.0001 → Contention-limited
Действие: найти и устранить serialisation point (глобальный lock, single queue consumer)

Система Б: α = 0.01, β = 0.005 → Coherency-limited
Действие: уменьшить координацию (eventual consistency, batch sync, shard by key)

Система В: α = 0.08, β = 0.003 → Mixed
Действие: начать с contention (α вносит больший penalty при малых N), затем coherency
```

## Процесс диагностики

1. **Measure first:** никогда не предполагай, где bottleneck — собери данные
2. **Fit USL:** используй least-squares regression (Python: `scipy.optimize.curve_fit`)
3. **Compare α vs β penalty** при целевом N:
   - Contention penalty при N: `α(N-1)`
   - Coherency penalty при N: `β N(N-1)`
   - Что больше, то и bottleneck
4. **Fix, re-measure:** устрани bottleneck → повтори fit → проверь, что соответствующий коэффициент снизился
5. **Iterate:** после устранения одного bottleneck проявится следующий

## Практические замечания

- Достаточно 5-8 точек (разные N) для meaningful fit
- Данные должны быть из одной системы в одном состоянии (не смешивай тесты с разными конфигурациями)
- Выбросы (outliers) могут сильно исказить fit — исключай или перепроверяй

## Связанные материалы

- [Universal Scalability Law](universal-scalability-law.md)
- [Contention](contention.md)
- [Coherency](coherency.md)
- [Modelling real systems](modelling-real-systems.md)

## Источник

Baron Schwartz, *Practical Scalability Analysis with the Universal Scalability Law* (2015).
