---
title: Linear Scalability
type: pattern
category: performance-and-scalability
tags: [scalability, usl, linear-scaling, embarrassingly-parallel, theoretical-limit]
source: Practical Scalability Analysis with the Universal Scalability Law (Baron Schwartz, 2015)
added: 2026-07-06
---

# Linear Scalability

## Проблема

Интуитивное ожидание: «добавим вдвое больше серверов — получим вдвое больше throughput». В реальности это почти никогда не так.

## Решение

Линейная scalability — частный случай USL при α = 0 и β = 0:

```
X(N) = λ N
```

Throughput растёт прямо пропорционально N. Это **теоретический предел**, а не реалистичное ожидание.

## Когда возможна (почти) линейная scalability

- **Embarrassingly parallel workloads:** каждый запрос полностью независим (static file serving, map over независимых элементов)
- **Shared-nothing architecture:** узлы не разделяют состояние, не координируются
- **Read-only workloads:** нет write contention, нет replication lag, нет cache invalidation
- **Малые N:** при N ≤ 4 penalty terms часто пренебрежимо малы

## Почему линейной scalability почти не бывает

Даже в embarrassingly parallel системе есть:
- **Network I/O:** разделяемая сетевая карта, switch bandwidth
- **Load balancer:** единая точка, через которую проходят все запросы
- **Shared infrastructure:** DNS, service discovery, monitoring agents
- **Amdahl's fraction:** любая serial часть кода создаёт ceiling

## Как проверить

Fit USL к данным и посмотри на α и β:
- α < 0.01 и β < 0.0001 при измеренных N → поведение близко к линейному при этих N
- Но при больших N даже малые α и β дадут отклонение

## Не путать с

- **Horizontal scaling ≠ linear scalability:** система может scale horizontally (добавление узлов даёт прирост), но нелинейно
- **Scale-out efficiency:** отношение реального throughput к линейному прогнозу; 80% efficiency при 10 узлах — хороший результат

## Связанные материалы

- [Universal Scalability Law](universal-scalability-law.md)
- [Amdahl's Law](amdahls-law.md)
- [Diminishing returns](diminishing-returns.md)

## Источник

Baron Schwartz, *Practical Scalability Analysis with the Universal Scalability Law* (2015).
