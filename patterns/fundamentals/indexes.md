# Indexes

## Проблема

Без индекса поиск записи в таблице требует полного сканирования (full table scan). По мере роста данных latency чтения растёт линейно, и system throughput падает. Слишком много индексов, наоборот, замедляют writes и занимают storage.

## Решение

Индекс — отдельная структура данных, которая ускоряет поиск по определённому полю или комбинации полей ценой дополнительного storage и write amplification.

## Основные типы

| Тип | Структура | Когда эффективен |
|---|---|---|
| B-Tree | Сбалансированное дерево | Point lookups, range scans, equality |
| Hash index | Hash table | Point lookups, equality only |
| LSM-Tree | Log-structured merge | Write-heavy workloads |
| Bitmap index | Bit arrays | Low-cardinality columns (OLAP) |
| Inverted index | Term → document list | Full-text search |
| GiST / GIN | Generalized search tree | Геоданные, full-text (PostgreSQL) |
| Vector index | HNSW, IVF | Векторный поиск (embeddings) |

## Index design questions

- **Selectivity** — индекс эффективен, если фильтр отсекает большую часть строк (селективность > 5–10%).
- **Read vs write ratio** — read-heavy системы терпят больше индексов; write-heavy — чем меньше, тем лучше.
- **Composite index order** — колонка с наибольшей селективностью первой; только prefix queries работают.
- **Covering index** — включает все поля, нужные запросу; избегает обращений к таблице (index-only scan).
- **Partial index** — `WHERE status = 'active'` — минимизирует размер, если нужен поиск по подмножеству данных.

## Tradeoffs

- **Read vs write** — каждый индекс ускоряет SELECT, но замедляет INSERT/UPDATE/DELETE (до 2×-5× для secondary index).
- **Storage cost** — secondary index может занимать больше места, чем сама таблица.
- **Index maintenance** — перестроение индекса при больших данных может занять часы.
- **Query planner** — не все индексы, которые "должны" работать, используются planner'ом; проверяй на EXPLAIN ANALYZE.

## Когда применять

- Когда latency point-lookup или range-запроса не укладывается в SLO при полном сканировании.
- Когда запросы имеют стабильный filter pattern (колонка + оператор).

## Когда не применять

- Write-heavy append-only логи, где сканирование не критично.
- Данные, которые читаются редко и целиком.
- Когда composite index с неверным порядком колонок лежит мёртвым грузом.

## Связанные материалы

- [Storage selection](../architecture-design/storage-selection.md)
- [PostgreSQL](../../tools/databases/postgresql.md)
- [Database Internals](../../sources/books/database-internals.md)
- [Designing Data-Intensive Applications](../../sources/books/designing-data-intensive-applications.md)
