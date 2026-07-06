# System Design DB

База знаний по системному дизайну: архитектурные паттерны, фундаментальные принципы, выбор технологий, production-практики, источники и проектные правила. Цель структуры — быстро находить нужную заметку, поддерживать связи между темами и не дублировать одно и то же знание в разных местах.

## С чего начать

- [Patterns OVERVIEW](patterns/OVERVIEW.md) — оглавление раздела и learning path.
- [System design principles](patterns/fundamentals/system-design-principles.md) — базовые вопросы, которые держат дизайн в фокусе.
- [Capacity estimation](patterns/fundamentals/capacity-estimation.md) — грубая математика нагрузки, storage и bandwidth.
- [Availability and reliability](patterns/fundamentals/availability-and-reliability.md) — SLO, redundancy, graceful failure.
- [Consistency models](patterns/fundamentals/consistency-models.md) — tradeoff между freshness, latency и coordination.
- [Load balancing](patterns/architecture-design/load-balancing.md) — распределение трафика и отказоустойчивый ingress.
- [Storage selection](patterns/architecture-design/storage-selection.md) — выбор primary store, индексов и read models.
- [Tools OVERVIEW](tools/OVERVIEW.md) — canonical страницы технологий.

## Структура

| Раздел | Роль |
|---|---|
| [patterns](patterns/OVERVIEW.md) | Принципы, архитектурные решения, workflow, recipes, learning path |
| [tools](tools/OVERVIEW.md) | Базы данных, очереди, кэши, observability-инструменты |
| [sources](sources/OVERVIEW.md) | Книги, статьи, доклады и provenance |
| [meta](meta/project-rules.md) | Скрипты, шаблоны, проектные skills, память проекта |

## Правило именования

- Пользовательские папки и Markdown-файлы называем строго на английском в `kebab-case`: `load-balancing.md`, `capacity-estimation.md`.
- Для обзорных страниц используем единое имя `OVERVIEW.md`.
- Служебные dot-файлы и файлы инструментов могут сохранять стандартные имена экосистемы: `.gitignore`, `.githooks/pre-commit`.
- Порядок разделов задается этой таблицей, а не числовыми префиксами в названиях папок.

## Правило против дублей

Одна мысль должна иметь один основной дом:

- фундаментальный принцип или архитектурный паттерн — в `patterns/`;
- технология, продукт или инструмент — в `tools/`;
- внешний источник — в `sources/`;
- проектные правила, шаблоны и проверки — в `meta/`;
- overview-файлы только навигируют и кратко объясняют, куда идти.

### Single Source of Truth

Каждая сущность в базе знаний имеет единственную canonical страницу, где живут ее факты. Все остальные заметки только ссылаются на эту страницу и не дублируют содержание.

| Сущность | Где canonical страница | Что содержит |
|---|---|---|
| Архитектурный паттерн или принцип | `patterns/` | Проблема, решение, tradeoffs, когда применять |
| Технология или продукт | `tools/` | Назначение, сильные стороны, ограничения, use cases |
| Внешний источник | `sources/` | Что это, откуда, дата добавления, relevance, связи |
| Практический workflow | `patterns/production-operations/` или `patterns/architecture-design/` | Алгоритм, проверка результата, частые ошибки |

Если новая заметка повторяет существующую, ставь ссылку на canonical страницу, а не копируй текст.

## Как добавлять материалы

1. Определить тип материала: принцип, паттерн, технология, production-практика, сравнение или источник.
2. Создать заметку в соответствующем разделе.
3. Добавить ссылку в `OVERVIEW.md` этого раздела.
4. Если материал пришел из внешнего источника, добавить карточку в `sources/` по шаблону [source.md](meta/templates/source.md).
5. Запустить проверку:

```bash
python3 meta/scripts/validate.sh
```

## Проверки

В проекте есть три уровня валидации:

1. Валидация vault: битые Markdown-ссылки и frontmatter у source-карточек.
2. Регенерация [canonical-map.json](meta/canonical-map.json) из `patterns/` и `tools/`.
3. Canonical cross-reference: bare mentions известных сущностей должны быть ссылками.

Все проверки подключены в локальный pre-commit hook [.githooks/pre-commit](.githooks/pre-commit).

## Рабочие правила

- Связи между заметками делаем Markdown-ссылками на существующие файлы.
- Списки в обзорных страницах должны быть ссылками, если материал уже создан.
- Не оставляем битые ссылки как заглушки.
- После meaningful изменения запускаем `python3 meta/scripts/validate.sh`.
- Перед коммитом включаем hook: `git config core.hooksPath .githooks`.

