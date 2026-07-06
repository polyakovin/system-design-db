# Distributed transactions

## Проблема

Операция затрагивает несколько systems of record, и partial success создает inconsistent user-visible state.

## Решение

Сначала попробуй уменьшить transaction boundary. Если это невозможно, выбери coordination model:

- saga для последовательности local transactions и compensating actions;
- transactional outbox для надежной публикации events после write;
- two-phase commit только при строгой необходимости и контролируемых participants;
- idempotency и reconciliation jobs для recovery.

## Tradeoffs

Strong coordination повышает correctness, но ухудшает availability и operational simplicity. Saga легче масштабируется, но требует явного handling для compensations.

## Когда применять

- Payment, booking, inventory или entitlement workflows.
- Нельзя потерять event после state change.
- Есть несколько owners данных.

## Связанные материалы

- [Consistency models](../fundamentals/consistency-models.md)
- [Queues and streams](../architecture-design/queues-and-streams.md)
- [API design](../architecture-design/api-design.md)

