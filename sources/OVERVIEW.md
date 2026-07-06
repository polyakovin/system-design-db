# Sources

Раздел хранит provenance: книги, статьи, доклады, документацию и разборы, из которых были извлечены выводы для canonical заметок.

## Как добавлять источник

1. Создать файл по шаблону [source.md](../meta/templates/source.md).
2. Положить его в подходящую подпапку внутри `sources/`.
3. Добавить короткое описание: что это, почему важно, какие заметки обновлены.
4. Перенести устойчивые выводы в `patterns/` или `tools/`, не превращая source-карточку в большую копию содержания.
5. Запустить `python3 meta/scripts/validate.sh`.

## Категории

- Books and long-form materials.
- Learning platforms and interview-prep websites.
- Engineering articles and postmortems.
- Vendor docs and architecture guides.
- Talks and conference materials.

## Websites

- [Hello Interview](websites/hello-interview.md) — interview-prep platform with a system design learning track, technology summaries, patterns, and worked question breakdowns.
- [A Philosophy of Software Design](websites/a-philosophy-of-software-design.md) — конспект книги John Ousterhout про управление сложностью в софтверном дизайне

## Videos

- [System Design Interviews (YouTube)](videos/youtube-system-design.md) — подборка 8 видео: Uber, Netflix, WhatsApp, Twitter, YouTube, Amazon, URL Shortener, mock interview.
- [System Design (VK Video)](videos/vk-system-design.md) — подборка 8 русскоязычных видео: разборы архитектур и mock интервью.

## Learning Platforms

- [System Design Course Platforms](websites/system-design-course-platforms.md) — платные курсы: Grokking System Design (DesignGurus), Grokking OOD, Educative.io, Karpov.Courses (рус.), Stanford Databases (edX). Статус: referenced.

## Blogs

- [System Design Blogs & Channels](websites/system-design-blogs.md) — подборка 8 блогов/каналов: System Design One, ByteByteGo (сайт/YouTube/блог), Владислав Всеволодович, nvashanin, Architecture Weekly (TG), Code of Architecture (YT).

## Books

- [Designing Data-Intensive Applications](books/designing-data-intensive-applications.md) — книга Martin Kleppmann о reliable, scalable and maintainable data systems; рекомендации разнесены по canonical заметкам.
- [System Design Interview (Vol. 1)](books/system-design-interview.md) — Alex Xu: 12 реальных сценариев system design с пошаговым разбором.
- [System Design Interview (Vol. 2)](books/system-design-interview-v2.md) — Alex Xu, Sahn Lam: 11 сценариев с фокусом на distributed transactions и real-time.
- [Software Architecture in Practice](books/software-architecture-in-practice.md) — Bass, Clements, Kazman: фундаментальный учебник от SEI по архитектуре ПО и quality attributes.
- [Fundamentals of Software Architecture](books/fundamentals-of-software-architecture.md) — Richards, Ford: инженерный подход к архитектуре, архитектурные стили, fitness functions.
- [Software Architecture: The Hard Parts](books/software-architecture-the-hard-parts.md) — Ford, Richards, Sadalage, Dehghani: trade-offs в distributed architectures, сервисная гранулярность.
- [Design Patterns (GoF)](books/design-patterns-gof.md) — Gamma, Helm, Johnson, Vlissides: канонический каталог 23 паттернов OO-проектирования.
- [Building Evolutionary Architectures](books/building-evolutionary-architectures.md) — Ford, Parsons, Kua, Sadalage: guided by fitness functions, incremental change как принцип.
- [Distributed Systems (4th Ed.)](books/distributed-systems-4ed.md) — van Steen, Tanenbaum: учебник по распределённым системам (консенсус, репликация, именование).
- [Documenting Software Architectures](books/documenting-software-architectures.md) — Clements et al.: views and beyond, шаблоны документирования архитектуры.
- [Enterprise Integration Patterns](books/enterprise-integration-patterns.md) — Hohpe, Woolf: 65 паттернов интеграции через messaging.
- [Database Internals](books/database-internals.md) — Alex Petrov: deep-dive в storage engines и распределённые алгоритмы БД.
- [Big Data](books/big-data.md) — Marz, Warren: Lambda Architecture и best practices scalable real-time data систем.
- [Learning Domain-Driven Design](books/learning-domain-driven-design.md) — Vlad Khononov: стратегический и тактический DDD для современных разработчиков.
- [NoSQL Distilled](books/nosql-distilled.md) — Fowler, Sadalage: polyglot persistence и сравнение NoSQL-категорий.
- [What Is Domain-Driven Design?](books/what-is-domain-driven-design.md) — Vlad Khononov: лёгкое введение в DDD.
- [Stakeholder Theory: The State of the Art](books/stakeholder-theory.md) — Freeman et al.: теория заинтересованных сторон, применимая к архитектурным решениям.
- [Awesome-CS-Books: Architecture](books/awesome-cs-books-architecture.md) — коллекция 12+ книг по архитектуре ПО из репозитория Awesome-CS-Books (Code Complete, DDD, Clean Architecture, Refactoring и др.)
- [Code Complete](books/code-complete.md) — Steve McConnell, 2004
- [Patterns of Enterprise Application Architecture](books/patterns-of-enterprise-application-architecture.md) — Martin Fowler, 2006
- [Clean Code](books/clean-code.md) — Robert C. Martin, 2008
- [Domain-Driven Design](books/domain-driven-design.md) — Eric Evans, 2010
- [Implementing Domain-Driven Design](books/implementing-domain-driven-design.md) — Vaughn Vernon, 2013
- [The Simple Elegance of Software Design](books/simple-elegance-of-software-design.md) — Max Kanat-Alexander, 2013
- [Practical Scalability Analysis with the USL](books/universal-scalability-law.md) — Baron Schwartz, 2015
- [Patterns, Principles, and Practices of DDD](books/patterns-principles-practices-ddd.md) — Scott Millett, 2015
- [架构漫谈 (Chatting About Architecture)](books/chatting-about-architecture.md) — 架构师, 2016
- [Clean Architecture](books/clean-architecture.md) — Robert C. Martin, 2017
- [Refactoring (2nd ed.)](books/refactoring-second-edition.md) — Martin Fowler, 2018

## Articles

- [Конспект по архитектуре ПО и System Design](articles/habr-software-architecture-and-system-design-summary.md) — Habr-пост с визуальной картой тем и ссылкой на Miro-доску.
- [Mapping Your Software: Guide to Architecture Diagrams](articles/miro-architecture-diagrams.md) — статья Miro: 8 типов архитектурных диаграмм, C4 model, визуализация.
- [System Design Interview — фрагмент книги (Питер)](articles/habr-piter-architecture-book-excerpt.md) — 4-шаговая методика прохождения System Design Interview.
- [AvitoTech: готовимся к System Design Interview](articles/avito-architecture-experience.md) — опыт Avito: кросс-функциональные команды, 3 этапа интервью, ссылки на ресурсы.
- [Slack Architecture](articles/slack-architecture.md) — Neo Kim (systemdesign.one): deep dive into Slack's real-time messaging, WebSocket scaling, channel architecture, and horizontal scaling.
- [Ozon Tech — Platform Engineering (Database Sharding)](articles/ozon-platform-engineering.md) — Practical PostgreSQL sharding with Go, client-side distribution, and resharding strategies.
- [System Design Recommendations — Slurm / Ozon](articles/ozon-taxi-architecture.md) — Curated system design resources with context on microservice taxi architecture and real-time matching.
- [Data Mesh Principles and Logical Architecture](articles/data-mesh-principles.md) — Zhamak Dehghani (martinfowler.com): canonical reference on domain ownership, data as product, self-serve platform, and federated governance.
- [Yandex Architecture Evolution — YDB Open Source](articles/yandex-architecture-evolution.md) — Infrastructure evolution at Yandex: from RDBMS through NoSQL to distributed SQL (YDB).
- [Apache Cassandra Internals — CAP Theorem and Trade-offs](articles/cap-theorem-acid-explained.md) — Classic Habr deep-dive into CAP theorem, ACID vs BASE, consistent hashing, and tunable consistency.
- [S3 Object Storage Overview](articles/s3-object-storage.md) — Yandex Cloud glossary: buckets, keys, tiered storage, and the S3 API.
- [The Twelve-Factor App](articles/twelve-factor-app.md) — Adam Wiggins / Heroku: 12 принципов построения SaaS-приложений (codebase, config, stateless processes, logs as streams).

## Правило

Source-карточка отвечает на вопрос "откуда мы это знаем". Canonical заметка отвечает на вопрос "что делать с этим знанием".
