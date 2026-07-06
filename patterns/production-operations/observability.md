# Observability

## Проблема

Система может быть technically up, но пользователи видят ошибки, slow paths или partial failure. Без signal design команда узнает об этом слишком поздно.

## Решение

Собери минимальный signal set:

- metrics для SLO и saturation;
- logs для событий и context;
- traces для request path и dependency latency;
- dashboards для operational decisions;
- alerts только на actionable symptoms.

## Tradeoffs

Больше signals не значит лучше. Нужны high-signal dashboards, иначе команда утонет в noise.

## Когда применять

- Любой production service.
- Любая async система с delayed failures.
- Любой critical user workflow.

## Связанные материалы

- [Availability and reliability](../fundamentals/availability-and-reliability.md)
- [Latency and throughput](../fundamentals/latency-and-throughput.md)
- [Incident response](incident-response.md)
- [Prometheus](../../tools/observability/prometheus.md)
- [Grafana](../../tools/observability/grafana.md)

