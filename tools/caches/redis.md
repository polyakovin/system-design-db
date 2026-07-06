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

## Связанные материалы

- [Caching strategy](../../patterns/architecture-design/caching-strategy.md)
- [Rate limiting](../../patterns/architecture-design/rate-limiting.md)

