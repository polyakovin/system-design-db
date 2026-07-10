---
title: Service Mesh
url: https://istio.io/latest/docs/concepts/what-is-service-mesh/
type: url
category: tools
tags: [service-mesh, istio, linkerd, envoy, sidecar, networking, observability]
added: 2026-07-10
status: starter
---

# Service Mesh

Выделенный инфраструктурный слой для управления межсервисным взаимодействием в микросервисной архитектуре. Реализуется через sidecar-прокси (обычно Envoy), перехватывающие весь входящий и исходящий трафик сервиса. Примеры: Istio, Linkerd, Consul Connect, AWS App Mesh, Kuma, Cilium Service Mesh.

## Где применять

- **Microservices communication** — управление трафиком между сотнями сервисов (timeouts, retries, circuit breakers).
- **Mutual TLS (mTLS)** — шифрование и аутентификация между сервисами без изменений в коде приложений.
- **Traffic routing** — canary, blue-green, mirroring (shadow traffic) на уровне mesh.
- **[Observability](../../patterns/production-operations/observability.md)** — автоматический сбор metrics (4 Golden Signals), distributed tracing и access logs для каждого запроса между сервисами.
- **Fault injection** — тестирование resilience (задержки, ошибки) без изменения кода.
- **[Rate limiting](../../patterns/architecture-design/rate-limiting.md) и access control** — политики на уровне сервиса, а не приложения.

## Сильные стороны

- **Вынос networking из кода** — retries, timeouts, circuit breakers, service discovery — всё настраивается через политики, не через библиотеки.
- **Zero-trust security** — mTLS между каждым сервисом автоматически, без SDK.
- **Единый слой [observability](../../patterns/production-operations/observability.md)** — каждый запрос между сервисами автоматически трассируется и логируется.
- **Платформонезависимость** — mesh работает на уровне сети; сервисы могут быть написаны на любом языке.
- **Gradual adoption** — можно внедрять сервис за сервисом, не затрагивая остальные.

## Ограничения

- **Операционная сложность** — Istio требует управления control plane (Pilot, Mixer, Citadel). Linkerd проще, но менее функционален.
- **Дополнительная задержка** — каждый запрос проходит через sidecar-прокси (обычно <2ms p99, но для high-throughput систем суммируется).
- **Resource overhead** — sidecar потребляет CPU и память на каждом pod'е; в большом кластере overhead значителен.
- **[Debugging](../../patterns/fundamentals/debugging.md) сложнее** — появляется дополнительный слой; чтобы понять, почему запрос не прошёл, нужно смотреть логи service mesh + сервиса + Envoy.
- **Vendor lock-in risk** — привязка к control plane конкретного mesh; migration между Istio/Linkerd/Consul нетривиальна.
- **Не решает проблемы бизнес-логики** — если сервис неправильно обрабатывает запросы, mesh это не исправит.

## Design notes

- **Sidecar vs node-proxy** — sidecar (по одному proxy на сервис) даёт изоляцию; node-proxy (один на ноду) эффективнее, но слабее изоляция.
- **Control plane vs data plane** — data plane (Envoy) обрабатывает трафик; control plane (Istiod) управляет конфигурацией. Разделение важно для scalability.
- **Mesh expansion** — подключай VMs, bare metal и serverless к mesh через ingress gateway.
- **mTLS permissive mode** — на этапе миграции mTLS в permissive режиме (принимает как TLS, так и plaintext).
- **[Observability](../../patterns/production-operations/observability.md) first** — начинай внедрение mesh с observability, затем security, затем traffic management.

## Связанные материалы

- [Load balancing](../../patterns/architecture-design/load-balancing.md)
- [Observability](../../patterns/production-operations/observability.md)
- [Deployment strategy](../../patterns/production-operations/deployment-strategy.md)
- [Tools OVERVIEW](../OVERVIEW.md)
