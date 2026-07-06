---
title: Practical Scalability Analysis with the Universal Scalability Law
url: https://github.com/rocky-191/Awesome-CS-Books/raw/master/SoftwareEngineering/Architecture/2015-Practical%20Scalability%20Analysis%20With%20The%20Universal%20Scalability%20Law.pdf
type: book
category: sources
tags: [architecture, software-design, scalability, usl, book]
added: 2026-07-06
status: indexed
---

# Practical Scalability Analysis with the Universal Scalability Law

**Автор:** Baron Schwartz
**Год:** 2015

Количественный анализ масштабируемости через Universal Scalability Law (USL). Модель Гюнтера: contention (α), coherency (β) и их влияние на throughput под нагрузкой. Включает Amdahl's Law и Gustafson's Law как частные случаи, capacity planning через USL-фиттинг, диагностику bottlenecks, анализ diminishing returns, superlinear scalability через cache/NUMA эффекты.

Источник: [Awesome-CS-Books / Architecture](https://github.com/rocky-191/Awesome-CS-Books/tree/master/SoftwareEngineering/Architecture)

## Практическая ценность

Ключевой источник для quantitative scalability analysis. Используется в patterns/performance-and-scalability/.

## Разобранные концепции

- [Universal Scalability Law](../../patterns/performance-and-scalability/universal-scalability-law.md) — core formula
- [Contention](../../patterns/performance-and-scalability/contention.md) — α coefficient
- [Coherency](../../patterns/performance-and-scalability/coherency.md) — β coefficient
- [Throughput vs latency](../../patterns/performance-and-scalability/throughput-vs-latency.md) — curves, knee point
- [Capacity planning](../../patterns/performance-and-scalability/capacity-planning.md) — saturation, optimal N
- [Identifying bottlenecks](../../patterns/performance-and-scalability/identifying-bottlenecks.md) — USL diagnostics
- [Linear scalability](../../patterns/performance-and-scalability/linear-scalability.md)
- [Amdahl's Law](../../patterns/performance-and-scalability/amdahls-law.md)
- [Gustafson's Law](../../patterns/performance-and-scalability/gustafsons-law.md)
- [Modelling real systems](../../patterns/performance-and-scalability/modelling-real-systems.md)
- [Superlinear scalability](../../patterns/performance-and-scalability/superlinear-scalability.md)
- [Diminishing returns](../../patterns/performance-and-scalability/diminishing-returns.md)

## Статус

Добавлено: 2026-07-06. Последнее обновление: 2026-07-06 (распаковано в 12 canonical-заметок).
