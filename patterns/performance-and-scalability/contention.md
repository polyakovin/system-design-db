---
title: Contention (α coefficient)
type: pattern
category: performance-and-scalability
tags: [scalability, usl, contention, bottleneck, serialization, queueing]
source: Practical Scalability Analysis with the Universal Scalability Law (Baron Schwartz, 2015)
added: 2026-07-06
---

# Contention (α coefficient)

## Проблема

Параллельные workers конкурируют за shared resources — lock, очередь, пул соединений, shared data structure. С ростом N вероятность contention растёт, и workers проводят всё больше времени в ожидании, а не в productive work.

## Решение

В USL contention моделируется коэффициентом **α** (0 ≤ α < 1):

```
Contention penalty: α(N-1)
```

Каждый из N узлов конкурирует с (N-1) другими → penalty растёт линейно.

## Типичные источники contention

- **Serialisation points:** global lock, single-threaded queue consumer, exclusive write lock
- **Shared mutable state:** один счётчик, одна hash table, один connection pool
- **Hardware contention:** memory bus, CPU cache lines (false sharing), disk I/O queue
- **Database contention:** row-level locks under high-concurrency writes, single primary in replication

## Как измерить

Собрать throughput data для разных N → fit USL → извлечь α.

- α ≈ 0: система почти не страдает от contention (редко)
- α ≈ 0.01–0.05: лёгкая contention, system близка к линейной при малых N
- α > 0.1: значительная contention, throughput быстро выходит на плато
- α > 0.3: серьёзный sequential bottleneck, масштабирование почти не даёт выигрыша

## Устранение contention

- **Eliminate the serialisation point:** shard lock по ключам, заменить exclusive lock на read-write lock, использовать lock-free структуры данных
- **Reduce critical section:** вынести работу за пределы блокировки
- **Partition the resource:** разделить shared state так, чтобы разные workers работали с независимыми partitions
- **Batch operations:** амортизировать cost захвата lock на группе операций

## Tradeoffs

- Устранение contention часто добавляет complexity (sharding logic, eventual consistency)
- Иногда contention — сознательный выбор: serial execution проще для correctness; если throughput достаточен, оптимизация не нужна

## Связанные материалы

- [Universal Scalability Law](universal-scalability-law.md)
- [Coherency](coherency.md)
- [Identifying bottlenecks](identifying-bottlenecks.md)

## Источник

Baron Schwartz, *Practical Scalability Analysis with the Universal Scalability Law* (2015).
