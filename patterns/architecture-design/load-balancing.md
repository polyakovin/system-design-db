# Load balancing

## Проблема

Один entrypoint или один backend instance становится bottleneck и single point of failure.

## Решение

Поставь routing layer между clients и serving nodes:

- health checks исключают broken nodes;
- routing algorithm распределяет load;
- connection draining защищает deploys;
- retries ограничены timeout budget;
- sticky routing применяется только если state нельзя вынести.

## Tradeoffs

Load balancer добавляет hop и operational surface. Неправильные retries могут усилить outage, поэтому retry policy должна учитывать saturation.

## Когда применять

- Есть несколько serving instances.
- Нужен zero-downtime deploy.
- Нужно отделить public ingress от internal topology.

## Связанные материалы

- [Availability and reliability](../fundamentals/availability-and-reliability.md)
- [Deployment strategy](../production-operations/deployment-strategy.md)
- [Rate limiting](rate-limiting.md)

