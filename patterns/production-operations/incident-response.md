# Incident response

## Проблема

Во время инцидента команда теряет время, если заранее не определены ownership, severity, communication и rollback paths.

## Решение

Подготовь lightweight process:

- severity levels и owner;
- first response checklist;
- mitigation before root cause;
- communication channel;
- timeline capture;
- blameless postmortem и action items.

## Tradeoffs

Process должен помогать, а не тормозить. Маленькой команде достаточно короткого runbook и clear escalation path.

## Когда применять

- Production system обслуживает пользователей.
- Есть on-call или support rotation.
- Downtime влияет на деньги, trust или legal obligations.

## Связанные материалы

- [Availability and reliability](../fundamentals/availability-and-reliability.md)
- [Observability](observability.md)
- [Deployment strategy](deployment-strategy.md)

