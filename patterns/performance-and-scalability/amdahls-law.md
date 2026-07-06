---
title: Amdahl's Law
type: pattern
category: performance-and-scalability
tags: [scalability, amdahl, usl, serial-fraction, speedup, theoretical-limit]
source: Practical Scalability Analysis with the Universal Scalability Law (Baron Schwartz, 2015)
added: 2026-07-06
---

# Amdahl's Law

## Формулировка

```
S(N) = 1 / ((1 - p) + p/N)
```

Где:
- **S(N)** — speedup на N процессорах
- **p** — доля кода, которая может быть распараллелена (0 ≤ p ≤ 1)
- **1 - p** — serial fraction, которая выполняется последовательно

## Проблема

Amdahl's Law (Gene Amdahl, 1967) показывает, что speedup ограничен serial fraction. Даже при бесконечном числе процессоров:

```
S(∞) = 1 / (1 - p)
```

Если 5% кода serial (p = 0.95), максимальный speedup = 20x, независимо от N.

## Amdahl как частный случай USL

Amdahl's Law — это **coherency-free USL** (β = 0):

```
USL с β=0: X(N) = (λ N) / (1 + α(N-1))
```

Где α = (1-p)/p — contention parameter, вытекающий из serial fraction.

В USL-терминах: Amdahl моделирует **только contention** (α), предполагая нулевую coherency (β = 0). Поэтому Amdahl предсказывает только saturation (плато), но не retrograde scaling (падение throughput).

## Ограничения Amdahl's Law

- **Нет coherency:** не учитывает coordination cost между параллельными узлами
- **Fixed problem size:** предполагает, что объём работы фиксирован (strong scaling)
- **Нет retrograde scaling:** throughput только выходит на плато, никогда не падает
- **Идеализированная модель:** нет queueing, нет resource contention за hardware

## Когда применять

- Оценка верхней границы speedup для фиксированного workload
- Аргумент против over-parallelisation: «20% serial code → максимум 5x speedup»
- Baseline для сравнения: если реальный speedup сильно ниже Amdahl prediction → есть дополнительный bottleneck (coherency)

## Связанные материалы

- [Universal Scalability Law](universal-scalability-law.md)
- [Gustafson's Law](gustafsons-law.md)
- [Linear scalability](linear-scalability.md)

## Источник

Gene Amdahl, "Validity of the Single Processor Approach to Achieving Large Scale Computing Capabilities" (1967). Baron Schwartz, *Practical Scalability Analysis with the Universal Scalability Law* (2015).
