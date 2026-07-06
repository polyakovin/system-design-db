---
title: Gustafson's Law
type: pattern
category: performance-and-scalability
tags: [scalability, gustafson, scaled-speedup, weak-scaling, amdahl]
source: Practical Scalability Analysis with the Universal Scalability Law (Baron Schwartz, 2015)
added: 2026-07-06
---

# Gustafson's Law

## Формулировка

```
S(N) = N - α(N-1)
```

Где:
- **S(N)** — scaled speedup на N процессорах
- **α** — serial fraction (та же, что в USL и Amdahl)
- **N** — количество процессоров

## Проблема

Amdahl's Law предполагает **fixed problem size** (strong scaling): тот же объём работы, больше процессоров. Но в реальности с ростом вычислительных ресурсов люди решают **большие задачи** (weak scaling).

Gustafson's Law (John Gustafson, 1988) утверждает: «с увеличением N мы масштабируем задачу, а не просто распараллеливаем фиксированную».

## Scaled speedup vs fixed-size speedup

| | Amdahl (strong scaling) | Gustafson (weak scaling) |
|---|---|---|
| Problem size | Fixed | Scales with N |
| Serial work | Constant | Constant (не растёт) |
| Parallel work | Фиксирован, делится на N | Растёт пропорционально N |
| Speedup ceiling | 1/(1-p) | Практически линейный |
| Применимость | Фиксированный batch job | Растущий workload (web traffic, data processing) |

## Пример

```
p = 0.95 (5% serial), N = 16

Amdahl: S(16) = 1 / (0.05 + 0.95/16) = 1 / (0.05 + 0.059) = 1 / 0.109 ≈ 9.2x
Gustafson: S(16) = 16 - 0.05 × 15 = 16 - 0.75 = 15.25x
```

Gustafson даёт ~15x speedup, Amdahl — только ~9x. Разница в том, что Gustafson предполагает рост задачи.

## Gustafson vs USL

Gustafson's Law — scaled speedup без coherency penalty (β = 0). Как и Amdahl, он не учитывает coordination cost.

В терминах системного дизайна: Gustafson ближе к реальности для web services — traffic растёт, вы добавляете серверы, и каждый обрабатывает свою долю запросов. Но coherency (β) всё равно проявится при больших N.

## Когда применять

- Web/API servers: трафик растёт органически, добавляем серверы
- Data processing: размер данных растёт с количеством worker'ов
- Оценка масштабируемости horizontally-scaled systems

## Связанные материалы

- [Amdahl's Law](amdahls-law.md)
- [Universal Scalability Law](universal-scalability-law.md)
- [Linear scalability](linear-scalability.md)

## Источник

John Gustafson, "Reevaluating Amdahl's Law" (1988). Baron Schwartz, *Practical Scalability Analysis with the Universal Scalability Law* (2015).
