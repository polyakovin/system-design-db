---
title: MongoDB
url: https://www.mongodb.com/
type: url
category: tools
tags: [database, document]
added: 2026-07-06
status: starter
---

# MongoDB

Document database для aggregate-oriented data, flexible schema и read paths, где документ является естественной единицей работы.

## Где применять

- Product catalogs, profiles, content и похожие document-centric domains.
- Workloads с evolving schema.
- Reads, которые часто возвращают целый aggregate.

## Сильные стороны

- Flexible document model.
- Natural mapping для nested structures.
- Indexes for common query patterns.
- Managed scaling options.

## Ограничения

- Cross-document consistency требует осторожного design.
- Flexible schema не заменяет data governance.
- Ad hoc query growth может привести к index sprawl.

## Design notes

Document model хорош, когда aggregate boundary стабилен и большинство операций работает внутри него.

## Связанные материалы

- [Storage selection](../../patterns/architecture-design/storage-selection.md)
- [Consistency models](../../patterns/fundamentals/consistency-models.md)

