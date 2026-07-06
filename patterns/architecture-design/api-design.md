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

## Когда применять

- Public или multi-team API.
- Mobile clients с долгим update cycle.
- Workflows с retries и payments.

## Связанные материалы

- [Rate limiting](rate-limiting.md)
- [Consistency models](../fundamentals/consistency-models.md)
- [Observability](../production-operations/observability.md)

