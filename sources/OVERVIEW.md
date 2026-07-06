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
- Engineering articles and postmortems.
- Vendor docs and architecture guides.
- Talks and conference materials.

## Articles

- [Конспект по архитектуре ПО и System Design](articles/habr-software-architecture-and-system-design-summary.md) — Habr-пост с визуальной картой тем и ссылкой на Miro-доску.

## Правило

Source-карточка отвечает на вопрос "откуда мы это знаем". Canonical заметка отвечает на вопрос "что делать с этим знанием".
