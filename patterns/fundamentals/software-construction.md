# Software construction

## Проблема

Разработку часто путают с одним этапом — написанием кода. Без явного выделения construction-фазы команда смешивает проектирование, тестирование и отладку в хаотичный поток, теряя quality gates.

## Решение

McConnell определяет **construction** как центральный акт разработки, отличный от системного анализа и архитектуры. Construction включает:

- детальное проектирование (detailed design);
- кодирование и отладку;
- unit-тестирование и интеграцию;
- code review и рефакторинг внутри construction-цикла.

Construction занимает 30–80% времени проекта, и его качество определяет конечную maintainability.

## Ключевые идеи

- Construction — не «просто кодинг». Это проектирование на уровне классов/функций, написание, проверка и исправление.
- Качество construction напрямую влияет на стоимость изменений: дешёвое исправление во время construction становится дорогим после release.
- Upstream-деятельность (requirements, architecture) задаёт границы; construction наполняет их кодом.
- McConnell выделяет construction как отдельную дисциплину со своими метриками, практиками и стандартами — в отличие от требования «просто пиши код».

## Связь с системным дизайном

Construction — это уровень, где архитектурные решения превращаются в работающий код. Хорошая архитектура без качественного construction даёт хрупкую систему. Сильный construction без архитектуры — несвязный код.

## Связанные материалы

- [System design principles](system-design-principles.md)
- [Managing complexity](managing-complexity.md)
- [Design in construction](design-in-construction.md)

## Источник

Steve McConnell, *Code Complete* (2004), Chapters 1–2.
