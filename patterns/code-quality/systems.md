---
title: Systems
category: patterns
tags: [clean-code, systems, dependency-injection, separation-of-concerns, scaling]
source: clean-code.md
added: 2026-07-06
---

# Systems

## Проблема

Системы, где construction и use перемешаны, становятся жёсткими и нетестируемыми. Зависимости создаются внутри бизнес-логики (`new RealDependency()`), что делает замену на mock или другую реализацию невозможной без изменения кода.

## Решение

### Separation of main

- Construction должен быть отделён от use. `main` (или composition root) конструирует граф объектов; остальная система его использует.
- Ни один модуль не должен сам создавать свои зависимости. Зависимости приходят извне.
- Все зависимости текут в одном направлении: от composition root к листьям.

### Dependency Injection (DI)

- Объект не отвечает за создание своих зависимостей. Они **инжектируются** (через конструктор, сеттер или интерфейс).
- Контейнер (Spring, Dagger, Guice) управляет графом объектов.
- Inversion of Control: фреймворк вызывает твой код, а не твой код — фреймворк.
- **Ленивая инициализация** нарушает separation of concerns: объект знает слишком много (как создать зависимость, когда, при каких условиях). Выноси в factory, которая инжектится.
- Преимущества DI: тестируемость, заменяемость, явный контракт зависимостей.

### Cross-cutting concerns

- Persistence, logging, transactions — пронизывают всю систему. AOP (Aspect-Oriented Programming) решает: декораторы, прокси, аннотации.
- «Аспекты» в plain Java: Proxy, Wrapper/Decorator.

### Scaling up

- Системы не строятся сразу большими. Начинай с простого, но с чистыми границами (separated construction, thin adapters).
- **Big Design Up Front (BDUF) is harmful**: ты не знаешь всех требований заранее. Итеративно расширяй, опираясь на чистые абстракции.
- **Domain-Specific Languages (DSL)**: самый мощный инструмент, когда domain хорошо понят. Инкапсулирует сложность за выразительным языком.

### Use standards wisely

- Стандарты упрощают reuse и найм, но добавляют сложность. Используй когда они действительно упрощают, а не ради моды.

## Tradeoffs

- DI-контейнер добавляет сложность. В малых проектах — manual DI через конструктор.
- AOP — мощный, но дебаг через прокси неприятен. Annotation-based проще для понимания.

## Связанные материалы

- [Classes](classes.md)
- [Boundaries](boundaries.md)
- [Clean Code](../../sources/books/clean-code.md)
