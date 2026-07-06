---
title: Universal Scalability Law (USL)
type: pattern
category: performance-and-scalability
tags: [scalability, usl, contention, coherency, throughput, model]
source: Practical Scalability Analysis with the Universal Scalability Law (Baron Schwartz, 2015)
added: 2026-07-06
---

# Universal Scalability Law (USL)

## Проблема

Amdahl's Law предсказывает scalability только через serial fraction, игнорируя cost of coordination между параллельными узлами. В реальных системах throughput часто падает после достижения пика — поведение, которое Amdahl не объясняет.

## Решение

USL (Neil Gunther, 1993) моделирует throughput как функцию от N узлов с двумя penalty terms:

```
X(N) = (λ N) / (1 + α(N-1) + β N(N-1))
```

Где:
- **λ** — baseline throughput на одном узле (scale factor)
- **α** — contention coefficient (0 ≤ α < 1): стоимость конкуренции за shared resources
- **β** — coherency coefficient (0 ≤ β < 1): стоимость поддержания consistency между N узлами
- **N** — количество параллельных узлов/процессоров/threads

## Три режима

| Параметры | Поведение |
|---|---|
| α = 0, β = 0 | Linear scalability: X(N) = λN |
| α > 0, β = 0 | Amdahl scaling: throughput выходит на плато (saturates) |
| α > 0, β > 0 | Retrograde scaling: throughput достигает пика и падает |

## Ключевые инсайты

- Contention (α) растёт линейно с N: каждый новый узел конкурирует с N-1 существующими.
- Coherency (β) растёт квадратично с N: каждый узел должен координироваться с N-1 другими, cost ~ O(N²).
- Квадратичный penalty от β доминирует при больших N — поэтому throughput всегда падает после некоторого N_max.

## Peak throughput и N_max

Из USL можно вывести:
- **N_max** = floor(√((1-α)/β)) — количество узлов, дающее максимальный throughput
- **X_max** = X(N_max) — пиковый throughput, после которого добавление узлов снижает производительность

## Связанные материалы

- [Amdahl's Law](amdahls-law.md)
- [Gustafson's Law](gustafsons-law.md)
- [Contention](contention.md)
- [Coherency](coherency.md)
- [Throughput vs latency](throughput-vs-latency.md)
- [Modelling real systems](modelling-real-systems.md)

## Источник

Baron Schwartz, *Practical Scalability Analysis with the Universal Scalability Law* (2015). Neil Gunther, *Guerrilla Capacity Planning* (2007) — оригинальная формулировка USL.
