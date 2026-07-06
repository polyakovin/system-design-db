---
title: Prometheus
url: https://prometheus.io/
type: url
category: tools
tags: [metrics, monitoring]
added: 2026-07-06
status: starter
---

# Prometheus

Metrics system для time-series collection, alerting rules и service health signals.

## Где применять

- Service-level metrics.
- Saturation and error-rate tracking.
- Alert rules for actionable symptoms.
- Infrastructure and application signals.

## Сильные стороны

- Pull-based scraping model.
- Powerful query language.
- Strong ecosystem of exporters.
- Good fit for SLO-driven alerts.

## Ограничения

- High-cardinality labels can break cost and performance.
- Long-term retention may require remote storage.
- Metrics do not replace traces or logs.

## Design notes

Start with a small signal set: request rate, error rate, latency buckets and saturation.

## Связанные материалы

- [Observability](../../patterns/production-operations/observability.md)
- [Availability and reliability](../../patterns/fundamentals/availability-and-reliability.md)

