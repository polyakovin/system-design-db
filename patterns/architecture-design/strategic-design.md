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

## Связанные материалы

- [Bounded Context](bounded-context.md)
- [Ubiquitous Language](ubiquitous-language.md)
- [Anti-Corruption Layer](anti-corruption-layer.md)
- [Distillation](distillation.md) — core domain vs supporting
- [Domain Events](domain-events.md) — отношения через события
- [Domain-Driven Design](../../sources/books/domain-driven-design.md) — Part III (Strategic Design), глава 14
- [Learning Domain-Driven Design](../../sources/books/learning-domain-driven-design.md) — глава 3 (Context Mapping)
