---
title: Diminishing Returns in Scalability
type: pattern
category: performance-and-scalability
tags: [scalability, usl, diminishing-returns, marginal-gain, economics, provisioning]
source: Practical Scalability Analysis with the Universal Scalability Law (Baron Schwartz, 2015)
added: 2026-07-06
---

# Diminishing Returns in Scalability

## Проблема

Добавление ресурсов (серверов, CPU cores, threads) даёт всё меньший прирост throughput. Инвестиции растут линейно, отдача — сублинейно. Без quantitative understanding этого эффекта команды over-provision, тратят деньги впустую.

## Решение: Marginal Gain Analysis через USL

Marginal gain от добавления N-го узла:

```
ΔX(N) = X(N) - X(N-1)
```

Из USL: ΔX(N) монотонно убывает (при α > 0 или β > 0).

### Пример

```
λ = 1000, α = 0.02, β = 0.001

N=1:  X = 1000
N=2:  X = 1984   Δ = +984   (98% эффективность)
N=4:  X = 3846   Δ = +931*  (93% средняя)
N=8:  X = 7168   Δ = +830*  (83% средняя)
N=16: X = 11707  Δ = +567   (57% средняя)
N=32: X = 12238  Δ = +33    (3% средняя)
N=64: X = 7112   Δ = -80    (отрицательный!)
```

*Средний marginal gain на шаге

## Три фазы diminishing returns

| Фаза | N | Marginal gain | Что делать |
|---|---|---|---|
| Effective scaling | 1–8 | > 70% | Добавлять ресурсы — выгодно |
| Diminishing returns | 8–N_knee | 10–70% | Добавлять осторожно, считать cost/benefit |
| Waste | > N_knee | < 10% | Не добавлять; искать bottleneck или менять архитектуру |

## Почему diminishing returns неизбежны

1. **Contention (α):** каждый новый узел увеличивает конкуренцию для всех существующих. Эффект линейный по N.
2. **Coherency (β):** каждый новый узел увеличивает coordination overhead для всех пар. Эффект квадратичный по N.
3. **Amdahl ceiling:** serial fraction создаёт абсолютный потолок speedup, к которому система приближается асимптотически.

## Практическая эвристика

- Если marginal gain < 20% при добавлении N→N+1 узлов, дальнейшее горизонтальное масштабирование — пустая трата
- Лучше вложиться в **устранение bottleneck** (уменьшить α или β), чем в добавление узлов
- При N > 2 × N_knee/2 дальнейшие инвестиции в scale-out почти всегда неоправданы

## Связь с экономикой

- Стоимость узлов растёт линейно: cost(N) = N × cost_per_node
- Отдача растёт сублинейно: X(N) < λN (кроме embarrassingly parallel)
- → существует оптимальное N с точки зрения cost/throughput

## Связанные материалы

- [Universal Scalability Law](universal-scalability-law.md)
- [Capacity planning](capacity-planning.md)
- [Linear scalability](linear-scalability.md)

## Источник

Baron Schwartz, *Practical Scalability Analysis with the Universal Scalability Law* (2015).
