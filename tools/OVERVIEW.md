# Tools — overview

Раздел хранит canonical страницы технологий, которые часто участвуют в системном дизайне. Здесь фиксируются практическая роль, сильные стороны, ограничения и связи с паттернами.

## Databases

- [PostgreSQL](databases/postgresql.md) — relational primary store, transactions, indexes, extensions.
- [MySQL](databases/mysql.md) — relational store для high-read web workloads и managed environments.
- [MongoDB](databases/mongodb.md) — document store для flexible schema и aggregate-oriented reads.
- [Cassandra](databases/cassandra.md) — wide-column store для high-write distributed workloads.

## Caches

- [Redis](caches/redis.md) — in-memory data structure store для cache, counters, locks и queues.

## Messaging

- [Kafka](messaging/kafka.md) — durable event log для streams, replay и fanout.
- [RabbitMQ](messaging/rabbitmq.md) — broker для task queues и routing-heavy messaging.

## Observability

- [Prometheus](observability/prometheus.md) — metrics collection, alerting rules и time series.
- [Grafana](observability/grafana.md) — dashboards и visual exploration для operational signals.

## Как устроен раздел

Каждая страница технологии отвечает на четыре вопроса:

- где применять;
- какие сильные стороны;
- какие ограничения;
- с какими паттернами связана.

Если технология используется в заметках `patterns/`, ссылка должна вести на ее canonical страницу.

