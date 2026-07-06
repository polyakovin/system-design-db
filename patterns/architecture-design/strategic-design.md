---
title: Strategic Design
type: pattern
category: ddd
tags: [ddd, domain-driven-design, strategic-design, context-map, architecture]
source: Domain-Driven Design (Eric Evans, 2010)
added: 2026-07-06
---

# Strategic Design

## Проблема

Когда система растёт, отношения между Bounded Contexts становятся запутанными: команды дублируют модели, интеграции ломаются, зависимости становятся циклическими.

## Решение

Strategic Design — это Context Map: явное описание всех Bounded Contexts и отношений между ними. Карта делает видимыми точки интеграции, ownership и организационные границы.

## Типы отношений между Bounded Contexts (Context Map Patterns)

### Partnership
Две команды сотрудничают, интерфейсы согласуются совместно. Успех одной зависит от успеха другой.

### Shared Kernel
Два BC разделяют общую часть модели (обычно core concepts). Требует тесной координации — любое изменение общего кода влияет на оба контекста.

### Customer–Supplier
Один BC (Supplier) предоставляет сервис, другой (Customer) потребляет. Supplier учитывает нужды Customer, но решения принимает самостоятельно.

### Conformist
Customer принимает модель Supplier как есть, без адаптации. Не требует координации, но жертвует качеством модели на стороне Customer.

### Anti-Corruption Layer (ACL)
Customer защищает свою модель от модели Supplier через слой трансляции. Самый сложный, но самый надёжный паттерн интеграции.

### Open Host Service
Supplier предоставляет универсальный API (REST/gRPC), доступный разным потребителям. Противоположность point-to-point интеграции.

### Published Language
Формальный, хорошо документированный формат обмена (XML Schema, Protobuf, JSON Schema). Часто используется вместе с Open Host Service.

### Separate Ways
BC не интегрируются напрямую. Команды идут разными путями — дешевле, чем строить сложную интеграцию, когда выгода невелика.

## Tradeoffs

Плюсы: ясность границ, осознанный выбор паттернов интеграции, организационная прозрачность.
Минусы: требует постоянной актуализации карты, сложность оценки стоимости каждого паттерна.

## Practical Integration Patterns (Vaughan Vernon, Chapter 13)

### Integration mechanisms

Vernon maps context-map relationships to concrete integration technologies:

| Relationship | Mechanism | Chapter |
|---|---|---|
| Partnership / Shared Kernel | Shared code (jar/lib), RPC | Often combined with RPC |
| Customer–Supplier | REST, gRPC, SOAP | Supplier publishes API |
| Conformist | Same as Supplier's API, no translation | Simplest consumer |
| Anti-Corruption Layer | REST/RPC adapter + translator | ACL wraps external API |
| Open Host Service | REST/gRPC + Published Language | Broad API, documented |
| Published Language | XML Schema, JSON Schema, Protobuf, Avro | Formal contract |
| Separate Ways | No integration — manual duplication if needed | Cheaper than bad integration |

### RPC vs. REST vs. Messaging

Vernon's decision framework:

- **RPC (gRPC, SOAP):** good for synchronous request-response within a trust boundary. Tight coupling — consumer depends on supplier's interface. Use when latency is low and failure propagation is acceptable.
- **REST (resource-oriented):** good for open-host services. Consumers follow links (HATEOAS), reducing coupling to URL structure. Use for publishing APIs to unknown consumers.
- **Messaging (events/commands over a broker):** best for asynchronous integration. Decouples sender from receiver in time and space. Use for eventual consistency and cross-BC workflows. Requires idempotent consumers.

### Implementing Published Language

A published language is a shared schema, not a shared library:
- Protobuf/Thrift for binary (gRPC)
- JSON Schema / OpenAPI for REST
- Avro with schema registry for event streams (Kafka)

Vernon warns: "schema is the contract, not the code." Consumers generate their DTOs from the schema. Never share domain model classes — that leaks the model across BC boundaries.

### Separate Ways: when to walk away

Vernon's criteria for choosing Separate Ways:
1. The two contexts have fundamentally incompatible models.
2. The cost of building and maintaining integration exceeds the cost of manual duplication.
3. The integration would create an unwanted organisational dependency.

Example: a reporting context that extracts data via nightly batch — no direct integration needed.

### Context mapping in practice

Vernon's iterative approach:
1. Start with an event storming or whiteboard session — draw boxes for each context, arrows for relationships.
2. Label each arrow with the relationship pattern (partnership, customer-supplier, etc.).
3. For each relationship, pick the integration mechanism (RPC, REST, messaging, or separate ways).
4. Revisit the map every 3–6 months — teams reorganise, contexts split, patterns change.

## Связанные материалы

- [Bounded Context](bounded-context.md)
- [Ubiquitous Language](ubiquitous-language.md)
- [Anti-Corruption Layer](anti-corruption-layer.md)
- [Distillation](distillation.md) — core domain vs supporting
- [Domain Events](domain-events.md) — отношения через события
- [Event Sourcing](event-sourcing.md)
- [CQRS](cqrs.md) — read models across contexts
- [Domain-Driven Design](../../sources/books/domain-driven-design.md) — Part III (Strategic Design), глава 14
- [Learning Domain-Driven Design](../../sources/books/learning-domain-driven-design.md) — глава 3 (Context Mapping)
- [Implementing Domain-Driven Design](../../sources/books/implementing-domain-driven-design.md) — глава 13 (Integrating Bounded Contexts)
