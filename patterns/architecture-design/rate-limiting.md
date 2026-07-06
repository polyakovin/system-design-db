# Rate limiting

## Проблема

Один client, tenant или endpoint может забрать общий ресурс и ухудшить систему для остальных.

## Решение

Введи explicit limits:

- fixed window для простых quotas;
- sliding window для более ровного контроля;
- token bucket для burst allowance;
- per-tenant limits для fairness;
- clear error response и retry-after semantics.

## Tradeoffs

Слишком жесткие limits вредят legitimate traffic. Слишком мягкие limits не защищают shared resources. Хороший limiter должен быть observable и explainable.

## Когда применять

- Public API.
- Multi-tenant system.
- Expensive endpoints или third-party dependencies.

## Связанные материалы

- [API design](api-design.md)
- [Load balancing](load-balancing.md)
- [Observability](../production-operations/observability.md)

