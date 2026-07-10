---
title: Object Storage
url: https://aws.amazon.com/s3/
type: url
category: tools
tags: [storage, object-storage, s3, blob, cloud]
added: 2026-07-10
status: starter
---

# Object Storage

Хранилище неструктурированных данных в виде объектов (ключ → значение + metadata), доступное через HTTP API. Примеры: Amazon S3, Google Cloud Storage, Azure Blob Storage, MinIO.

## Где применять

- User-uploaded content (images, videos, documents).
- Backup и disaster recovery.
- Data lake для аналитики (Parquet, Avro).
- Static website hosting.
- Logs и audit trails.
- Machine learning model artifacts и datasets.

## Сильные стороны

- **Безграничная масштабируемость** — ёмкость растёт без provisioning, платишь за потребление.
- **11 nines durability** — replication across AZ / region.
- **HTTP API** — доступен из любого языка и платформы.
- **Tiered storage** — hot → cold → archive с автоматической миграцией (S3 Intelligent-Tiering).
- **Consistent performance** — latency практически не зависит от объёма данных.
- **Strong consistency** (S3 since Dec 2020) — read-after-write для всех операций.

## Ограничения

- **Eventual consistency устарела** — современные S3-совместимые системы дают strong consistency.
- **Не поддерживает** transactions, joins, [secondary indexes](../../patterns/fundamentals/indexes.md), relational constraints.
- **Rename — это copy+delete** (нет in-place rename для больших объектов).
- **List performance** — листинг миллионов объектов медленный; нужен prefix-based bucket layout.
- **No random writes** — объект целиком immutable после записи; для partial update нужно read+write.

## Design notes

- **Bucket naming** — flat namespace; не используй hierarchy для больших списков, используй prefix filtering.
- **Multipart upload** — для объектов > 100 MB.
- **Pre-signed URLs** — дай временный доступ без раскрытия credentials.
- **Object lifecycle** — настрой automatic transition и expiration.
- **Consistency boundary** — совместимость с S3 API, даже если бэкенд другой (MinIO, Ceph).

## Связанные материалы

- [Storage selection](../../patterns/architecture-design/storage-selection.md)
- [S3 Object Storage Overview](../../sources/articles/s3-object-storage.md)
- [Tools OVERVIEW](../OVERVIEW.md)
