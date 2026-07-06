# AGENTS.md — правила для AI-агента

## Проект

- **Название:** system-design-db
- **Тип агента:** coding / research (обслуживание базы знаний по системному дизайну)
- **Язык:** Markdown, Shell, Python, YAML
- **Цель:** Поддерживать и развивать базу знаний по системному дизайну: добавлять источники, писать концепции, фиксировать паттерны, сравнивать технологии и проверять целостность.

## Структура базы знаний

| Раздел | Назначение |
|---|---|
| `patterns/` | Принципы, архитектурные решения, tradeoffs, workflow, learning path |
| `tools/` | Базы данных, кэши, очереди, observability, сравнения |
| `sources/` | Внешние источники и provenance |
| `meta/` | Скрипты, шаблоны, проектные skills, память проекта |

## Правила работы с файлами

- Файлы — `kebab-case`, английские названия.
- Обзорные страницы — `OVERVIEW.md` без frontmatter.
- Одна мысль — один файл, без дублей.
- Ссылки только на существующие файлы.
- После изменений — валидация vault.
- Установлены `.githooks/pre-commit` и `.githooks/post-commit`.

## Как агент работает

1. Начинай с [README.md](README.md) — главная навигация по проекту.
2. Выполняй задачу минимальными порциями, каждая с проверкой.
3. Фиксируй важные решения в [meta/decisions.md](meta/decisions.md).
4. Запускай `python3 meta/scripts/validate.sh` после meaningful изменения.
5. После завершения задачи — **всегда делай commit и push**. `post-commit` хук пушит автоматически, достаточно `git add -A && git commit`.
6. Перед уходом убедись, что нет незакоммиченных изменений.

## Ограничения

- Не изменяй файлы вне scope задачи.
- Не добавляй speculative заметки "на будущее".
- Не удаляй заметки, которые не ты создал, если это явно не указано.
- Не оставляй битые Markdown-ссылки как заглушки.
- Если не уверен, запиши вопрос или предположение в [meta/decisions.md](meta/decisions.md).
- Destructive actions требуют подтверждения.

## Проверки

| Тип | Команда |
|-----|---------|
| Полная проверка | `python3 meta/scripts/validate.sh` |
| Валидация ссылок | `python3 meta/scripts/validate-vault.sh` |
| Canonical cross-reference | `python3 meta/scripts/validate-canonical-refs.py` |
| Генерация canonical-map | `python3 meta/scripts/generate-canonical-map.py` |

## Память проекта

- **Project rules:** [meta/project-rules.md](meta/project-rules.md)
- **Project memory:** [meta/project-memory.md](meta/project-memory.md)
- **Security policy:** [meta/security-policy.md](meta/security-policy.md)
- **Audit log:** [meta/audit-log.md](meta/audit-log.md)

## Связанные материалы

- [System design principles](patterns/fundamentals/system-design-principles.md)
- [Storage selection](patterns/architecture-design/storage-selection.md)
- [Observability](patterns/production-operations/observability.md)
