# Skill: add-source

Нужно добавить внешний источник и связать его с заметками базы.

## Алгоритм

1. Создай source-карточку по шаблону [source.md](../templates/source.md).
2. Положи файл в подходящую подпапку `sources/`.
3. Заполни frontmatter: `title`, `url`, `type`, `category`, `tags`, `added`, `status`.
4. Добавь короткую relevance-секцию.
5. Если из источника извлечены устойчивые выводы, перенеси их в canonical заметки `patterns/` или `tools/`.
6. Добавь ссылку в [sources/OVERVIEW.md](../../sources/OVERVIEW.md).
7. Запусти `python3 meta/scripts/validate.sh`.

## Проверка результата

- Source хранит provenance, а не заменяет canonical заметку.
- Все связанные canonical заметки существуют.
- Проверки проходят.

