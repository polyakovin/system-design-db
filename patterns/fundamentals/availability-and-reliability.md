# Availability and reliability

## Проблема

High availability часто называют целью, но без SLO, failure budget и recovery plan это остается пожеланием.

## Решение

Опиши надежность через observable promises:

- SLO для critical paths;
- allowed error budget;
- redundancy для critical components;
- health checks и automated failover;
- graceful degradation для degraded dependencies;
- tested restore path для данных.

## Tradeoffs

Больше redundancy повышает стоимость и operational complexity. Иногда правильнее снизить blast radius, чем строить полностью active-active систему.

## Когда применять

- Система обслуживает critical user workflow.
- Downtime имеет прямую стоимость.
- Есть stateful components и сложный recovery path.

## Связанные материалы

- [Replication strategy](../architecture-design/replication-strategy.md)
- [Load balancing](../architecture-design/load-balancing.md)
- [Incident response](../production-operations/incident-response.md)
- [Multi-region architecture](../advanced/multi-region-architecture.md)

