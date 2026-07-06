---
title: Redis
url: https://redis.io/
type: url
category: tools
tags: [cache, in-memory]
added: 2026-07-06
status: starter
---

# Redis

In-memory data structure store для low-latency cache, counters, rate limits, lightweight queues и coordination primitives.

## Где применять

- Cache-aside layer.
- Short-lived session or token state.
- Counters, leaderboards и rate limit state.
- Lightweight coordination where loss model is acceptable.

## Сильные стороны

- Very low latency.
- Rich data structures.
- Simple operational model for many cache workloads.
- Useful atomic operations.

## Ограничения

- Memory cost can dominate.
- Persistence mode must match durability needs.
- Eviction policy and hot keys require monitoring.

## Design notes

Перед внедрением назови stale tolerance, eviction behavior и recovery behavior after restart.

## Рекомендации из DDIA

- Cache is derived data unless explicitly designed otherwise; system correctness should survive cache loss or rebuild.
- If cache stores coordination state, use leases with clear expiry and fencing tokens where stale holders can cause damage.
- Write-through и explicit invalidation reduce stale windows, but increase coupling with the primary write path.
- Monitor hot keys and eviction behavior because cache efficiency depends on workload skew, not only average QPS.

## Связанные материалы

- [Caching strategy](../../patterns/architecture-design/caching-strategy.md)
- [Rate limiting](../../patterns/architecture-design/rate-limiting.md)
- [Designing Data-Intensive Applications](../../sources/books/designing-data-intensive-applications.md)
