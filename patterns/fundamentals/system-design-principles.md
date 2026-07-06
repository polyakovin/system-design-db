# System design principles

## Проблема

Системный дизайн быстро распадается на набор любимых технологий, если сначала не зафиксировать нагрузку, пользователей, критичные операции и критерии отказа.

## Решение

Начинай дизайн с короткого контракта:

- кто пользователь и какой основной workflow;
- какие read/write операции критичны;
- какие SLO и failure modes неприемлемы;
- какие данные являются source of truth;
- какие tradeoffs допустимы: latency, cost, freshness, durability, complexity.

## Практическая эвристика

Сначала опиши инварианты, затем numbers, затем data model, затем request path. Технологии выбираются только после того, как понятны constraints.

## Рекомендации из DDIA

- Разделяй functional requirements и quality attributes: reliability, scalability, maintainability, security, compliance.
- Описывай load через конкретные параметры: read/write ratio, fanout, payload size, hot keys, peak multiplier.
- Для scalability сначала назови метрику нагрузки и метрику качества ответа, затем выбирай scaling strategy.
- Maintainability включает operability и evolvability: дизайн должен быть наблюдаемым, мигрируемым и понятным для команды эксплуатации.

## Частые ошибки

- Начинать с брендов технологий вместо требований.
- Не разделять functional и non-functional requirements.
- Прятать hardest part за фразой "добавим очередь" или "поставим кэш".
- Игнорировать operational ownership: кто будет мониторить, чинить и мигрировать систему.

## Связанные материалы

- [Capacity estimation](capacity-estimation.md)
- [Availability and reliability](availability-and-reliability.md)
- [Storage selection](../architecture-design/storage-selection.md)
- [Observability](../production-operations/observability.md)
- [Designing Data-Intensive Applications](../../sources/books/designing-data-intensive-applications.md)
