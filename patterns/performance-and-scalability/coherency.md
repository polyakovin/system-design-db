---
title: Coherency (β coefficient)
type: pattern
category: performance-and-scalability
tags: [scalability, usl, coherency, consistency, coordination, consensus, cache-coherency]
source: Practical Scalability Analysis with the Universal Scalability Law (Baron Schwartz, 2015)
added: 2026-07-06
---

# Coherency (β coefficient)

## Проблема

Когда N узлов работают параллельно, каждый должен знать о состоянии других или согласовывать свои действия. Cost координации растёт с N, и при больших N становится доминирующим penalty.

## Решение

В USL coherency моделируется коэффициентом **β** (0 ≤ β < 1):

```
Coherency penalty: β N(N-1)
```

Квадратичная зависимость: каждый узел должен обмениваться информацией с (N-1) другими, и этот penalty растёт как O(N²).

## Типичные источники coherency

- **Cache coherency (hardware):** каждый CPU core должен видеть consistent view of memory; cache invalidation traffic растёт с числом cores
- **Distributed consensus:** Raft/Paxos — каждый узел обменивается сообщениями с кворумом; cost растёт с размером кластера
- **Replication:** primary → replica синхронизация; каждый новый replica добавляет нагрузку на primary
- **Gossip protocols:** background communication между узлами для membership, failure detection
- **Shared-nothing coordination:** two-phase commit, distributed locks с heartbeat

## Как измерить

Собрать throughput data → fit USL → извлечь β.

- β ≈ 0: система не страдает от coherency overhead (однопоточная, или coordination вынесена за critical path)
- β > 0.001 (10⁻³): заметный coherency penalty при средних N (10-50 узлов)
- β > 0.01 (10⁻²): coherency доминирует, throughput падает быстро после пика

## Устранение coherency

- **Reduce coordination:** eventual consistency вместо strong consistency; отказ от distributed transactions
- **Batch coordination:** агрегировать обновления, синхронизироваться реже
- **Hierarchical coordination:** tree-based gossip вместо all-to-all
- **Partition by affinity:** узлы, работающие с разными данными, не нуждаются в координации
- **Avoid false sharing на CPU:** выравнивание cache lines, per-core структуры данных

## Ключевое отличие от contention

Contention (α) — workers ждут друг друга (queueing). Coherency (β) — workers обмениваются информацией, даже когда не конфликтуют. Coherency — это «налог на параллелизм», который платится всегда, а contention — только при конфликте.

## Связанные материалы

- [Universal Scalability Law](universal-scalability-law.md)
- [Contention](contention.md)
- [CAP theorem](../fundamentals/cap-theorem.md)

## Источник

Baron Schwartz, *Practical Scalability Analysis with the Universal Scalability Law* (2015). Neil Gunther, *Guerrilla Capacity Planning* (2007).
