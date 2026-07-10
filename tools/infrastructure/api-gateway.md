---
title: API Gateway
url: https://microservices.io/patterns/apigateway
type: url
category: tools
tags: [api-gateway, gateway, reverse-proxy, routing, microservices]
added: 2026-07-10
status: starter
---

# API Gateway

Единая точка входа для клиент-серверного взаимодействия в микросервисной архитектуре. Принимает внешние запросы и маршрутизирует их к соответствующим внутренним сервисам, применяя cross-cutting concerns. Примеры: Kong, AWS API Gateway, NGINX Plus, Envoy (как gateway), Traefik, Zuul, Apache APISIX.

## Где применять

- Микросервисная архитектура — единый endpoint для клиентов вместо N сервисов.
- API composition — агрегация ответов от нескольких сервисов в одном ответе.
- Authentication и authorization — централизованная проверка JWT, API keys, OAuth2.
- [Rate limiting](../../patterns/architecture-design/rate-limiting.md) и throttling — защита backend от перегрузки.
- Request/response трансформация — протокольные мосты (REST ↔ gRPC), заголовки, форматы.
- SSL termination и certificate management.
- API versioning routing — `/v1/` → v1 сервисы, `/v2/` → v2.
- Service discovery integration — маршрутизация по имени сервиса через Consul, Eureka, DNS.

## Сильные стороны

- **Скрывает внутреннюю структуру** — клиенты знают только API Gateway, не эндпоинты каждого сервиса.
- **Cross-cutting concerns в одном месте** — auth, [rate limiting](../../patterns/architecture-design/rate-limiting.md), logging, CORS не дублируются в каждом сервисе.
- **Упрощает клиентов** — клиент делает один запрос вместо N (API composition).
- **Protocol translation** — gateway может принимать HTTP и проксировать в gRPC, GraphQL, WebSocket.
- **Blue-green и canary routing** — можно направлять % трафика на новую версию сервиса на уровне gateway.

## Ограничения

- **Single point of failure** — если gateway падает, вся система недоступна; нужна репликация и health checks.
- **Дополнительная задержка** — каждый запрос проходит через gateway (обычно <5ms, но для latency-critical систем заметно).
- **Gateway становится монолитом** — если в gateWay накапливается слишком много логики, он превращается в bottleneck и SPOF на уровне кода.
- **Сложность обновления** — gateway — критический компонент; его обновление требует осторожности и тестов.
- **API composition vs frontend flexibility** — gateway фиксирует contract агрегации; если клиенту нужны другие данные, gateway нужно менять.

## Design notes

- **Gateway должен быть stateless** — всё состояние (сессии, rate limit counters) выносят в [Redis](../../tools/caches/redis.md)/внешнее хранилище.
- **Prefer passive health checks** — gateway проверяет backend по liveness endpoint; при failure исключает из роутинга.
- **Circuit breaker** — gateway может возвращать fallback/cached response при падении backend.
- **Разделяй gateway по типам клиентов** — mobile gateway (JSON-light), web gateway (SSR), third-party gateway (full API) — разный composition и [rate limiting](../../patterns/architecture-design/rate-limiting.md).
- **Backend-for-Frontend (BFF) pattern** — отдельный gateway для каждого клиентского приложения (iOS, Android, Web).

## Связанные материалы

- [Load balancing](../../patterns/architecture-design/load-balancing.md)
- [Rate limiting](../../patterns/architecture-design/rate-limiting.md)
- [API Design](../../patterns/architecture-design/api-design.md)
- [Caching strategy](../../patterns/architecture-design/caching-strategy.md)
- [Tools OVERVIEW](../OVERVIEW.md)
