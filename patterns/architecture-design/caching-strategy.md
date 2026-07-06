# Caching strategy

## Проблема

Повторные чтения дорогих данных увеличивают latency и нагрузку на primary systems. Но кэш легко превращается в источник stale data и hard-to-debug behavior.

## Решение

Выбери cache boundary и invalidation model:

- cache-aside для простого read-heavy path;
- write-through, если нужно синхронно обновлять cached representation;
- TTL для данных, где stale window приемлем;
- explicit invalidation для critical freshness;
- request coalescing для hot keys.

## Tradeoffs

Кэш уменьшает latency и load, но добавляет consistency risk, memory cost и eviction behavior. Сначала оцени hit rate и blast radius stale data.

## Рекомендации из DDIA

- Считай cache derived data, а не source of truth, если только бизнес-инвариант явно не допускает потерю состояния.
- Для критичного freshness лучше обновлять cache из change log или explicit invalidation, чем надеяться на TTL как единственный механизм.
- При cache rebuild оцени cold-start load: восстановление derived state не должно обрушить primary store.
- Если cache участвует в coordination, явно опиши failure model, expiry и fencing, иначе stale lock может превратиться в data corruption.

## Когда применять

- Данные читаются часто и меняются редко.
- Downstream dependency дорогая или медленная.
- Есть понятная stale tolerance.

## Связанные материалы

- [Latency and throughput](../fundamentals/latency-and-throughput.md)
- [Storage selection](storage-selection.md)
- [Redis](../../tools/caches/redis.md)
- [Designing Data-Intensive Applications](../../sources/books/designing-data-intensive-applications.md)
