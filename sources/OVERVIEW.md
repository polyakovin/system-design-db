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

## Books

- [Designing Data-Intensive Applications](books/designing-data-intensive-applications.md) — книга Martin Kleppmann о reliable, scalable and maintainable data systems; рекомендации разнесены по canonical заметкам.
- [Awesome-CS-Books: Architecture — коллекция](books/awesome-cs-books-architecture.md) — сборный источник с общей таблицей
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

## Правило

Source-карточка отвечает на вопрос "откуда мы это знаем". Canonical заметка отвечает на вопрос "что делать с этим знанием".
