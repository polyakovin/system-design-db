---
title: Grafana
url: https://grafana.com/
type: url
category: tools
tags: [dashboards, monitoring]
added: 2026-07-06
status: starter
---

# Grafana

Dashboard and visualization platform для operational signals, exploration и shared views во время incidents.

## Где применять

- SLO dashboards.
- Release health dashboards.
- On-call views.
- Cross-source signal exploration.

## Сильные стороны

- Flexible dashboards.
- Many data source integrations.
- Good sharing model for incident rooms.
- Alerting and annotation workflows.

## Ограничения

- Dashboards easily become noisy.
- Visuals must map to decisions, not vanity metrics.
- Ownership and cleanup need process.

## Design notes

Каждая dashboard panel должна помогать принять operational decision или объяснить user-visible symptom.

## Связанные материалы

- [Observability](../../patterns/production-operations/observability.md)
- [Incident response](../../patterns/production-operations/incident-response.md)
- [Prometheus](prometheus.md)

