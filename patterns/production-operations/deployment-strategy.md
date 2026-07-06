# Deployment strategy

## Проблема

Deploy может быть основным источником downtime, если rollout, migrations и rollback не спроектированы заранее.

## Решение

Выбирай rollout под risk:

- rolling deploy для small stateless changes;
- blue-green для быстрого switchback;
- canary для проверки на части traffic;
- feature flags для separation deploy и release;
- backward-compatible schema migrations.

## Tradeoffs

Чем безопаснее rollout, тем больше automation и discipline он требует. Canary без хороших signals дает ложное чувство безопасности.

## Когда применять

- Частые релизы.
- Много клиентов или tenants.
- Stateful migrations.

## Связанные материалы

- [Load balancing](../architecture-design/load-balancing.md)
- [Observability](observability.md)
- [Incident response](incident-response.md)

