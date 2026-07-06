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

## Articles

- [Конспект по архитектуре ПО и System Design](articles/habr-software-architecture-and-system-design-summary.md) — Habr-пост с визуальной картой тем и ссылкой на Miro-доску.

## Правило

Source-карточка отвечает на вопрос "откуда мы это знаем". Canonical заметка отвечает на вопрос "что делать с этим знанием".
