---
title: Search Engine
url: https://www.elastic.co/elasticsearch/
type: url
category: tools
tags: [search, full-text, elasticsearch, solr, vector-search, inverted-index]
added: 2026-07-10
status: starter
---

# Search Engine

Специализированная система для полнотекстового поиска, аналитики в реальном времени и (в современных реализациях) векторного поиска. Примеры: Elasticsearch, Apache Solr, OpenSearch, Meilisearch, Typesense.

## Где применять

- Full-text search по документам, статьям, описаниям товаров.
- Log analytics и [observability](../../patterns/production-operations/observability.md) (ELK stack).
- E-commerce filtering и faceted search.
- Vector search (semantic + keyword hybrid, RAG).
- Autocomplete и did-you-mean.

## Сильные стороны

- **Inverted index** — sub-50ms full-text search на миллиардах документов.
- **Schema-free** — dynamic mapping для новых полей.
- **Distributed by design** — sharding, replication, rebalancing out of the box.
- **Aggregations** — counts, histograms, percentiles без отдельного OLAP.
- **Vector search** — HNSW, kNN, hybrid (BM25 + vector) в Elasticsearch 8.x+.

## Ограничения

- **Не primary store** — no transactions, weak consistency (eventual), risk of data loss при сбое.
- **Write amplification** — indexing тяжелее, чем insert в обычную БД.
- **Memory footprint** — inverted index и field data живут в heap; large cardinality = OOM risk.
- **Complex operations cost** — reindexing при изменении mapping требует создания нового index.
- **Split-brain risk** — без correct quorum config возможен cluster instability (устарело в ES 7.x+ с voting-only nodes).

## Design notes

- **Index as write target** — не используй как source of truth; пиши данные в primary DB, затем async index в search engine.
- **Mapping design** — `keyword` для exact match, `text` для full-text, `match_only_text` для экономии места.
- **Hot-warm-cold architecture** — узлы с разными ресурсами для разных data tiers.
- **Index lifecycle** — rollover при достижении размера, delete старых indices по retention.

## Связанные материалы

- [Storage selection](../../patterns/architecture-design/storage-selection.md)
- [Tools OVERVIEW](../OVERVIEW.md)
