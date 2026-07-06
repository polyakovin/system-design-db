# API design

## Проблема

Слабый API contract делает систему хрупкой: клиенты зависят от случайных деталей, retries создают дубли, а изменения требуют coordinated deploy.

## Решение

Проектируй contract вокруг stable resources и explicit behavior:

- versioning и backward compatibility;
- idempotency keys для небезопасных retries;
- pagination для больших коллекций;
- explicit error model;
- request limits и timeout budget;
- schema evolution rules.

## Tradeoffs

Более строгий contract требует дисциплины и документации, зато снижает coupling между клиентами и backend.

## Рекомендации из DDIA

- Schema evolution должна поддерживать rolling upgrades: new code reads old data, old code tolerates new data.
- Избегай language-specific serialization formats для long-lived storage и public contracts, если нет явной compatibility strategy.
- Backward и forward compatibility зависят не только от format, но и от правил изменения fields, defaults, enums и required semantics.
- Для message-passing APIs фиксируй delivery guarantees, idempotency и replay behavior так же явно, как request/response schema.

## Когда применять

- Public или multi-team API.
- Mobile clients с долгим update cycle.
- Workflows с retries и payments.

## Связанные материалы

- [Rate limiting](rate-limiting.md)
- [Consistency models](../fundamentals/consistency-models.md)
- [Observability](../production-operations/observability.md)
- [Designing Data-Intensive Applications](../../sources/books/designing-data-intensive-applications.md)
