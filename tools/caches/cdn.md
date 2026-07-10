---
title: CDN
url: https://www.cloudflare.com/cdn/
type: url
category: tools
tags: [cdn, caching, edge, content-delivery, performance]
added: 2026-07-10
status: starter
---

# CDN (Content Delivery Network)

Геораспределённая сеть proxy-серверов, которая доставляет контент пользователю из ближайшего edge-локации. Примеры: Cloudflare, Fastly, Akamai, AWS CloudFront, CDN77.

## Где применять

- Static assets (images, CSS, JS, fonts, videos).
- Whole-site acceleration (reverse proxy + cache).
- API response caching для read-heavy endpoints.
- DDoS mitigation и Web Application Firewall.
- Edge computing (Cloudflare Workers, Fastly Compute@Edge).
- Video streaming (HLS/DASH segmentation + edge caching).

## Сильные стороны

- **Снижение latency** — контент приходит из географически близкого POP.
- **Разгрузка origin** — кешированные запросы не достигают backend.
- **Масштабирование под пики** — CDN поглощает traffic spikes, защищая origin.
- **SSL termination** — TLS на edge, origin может быть HTTP.
- **Global anycast** — единый IP, BGP роутинг на ближайший POP.

## Ограничения

- **Кешируется только кешируемое** — dynamic user-specific контент не выигрывает от CDN.
- **Cache invalidation** — purge может занимать минуты; TTL-based стратегия надёжнее.
- **Провалы кеша (cache miss surge)** — при инвалидации популярного контента все edge запрашивают origin одновременно (thundering herd).
- **Не решает проблемы backend latency** — если каждый запрос — cache miss, CDN не помогает.
- **Cost на трафик** — при высоком объёме transfer cost может быть значительным.

## Design notes

- **Cache-Control headers** — `public, max-age=31536000, immutable` для versioned assets.
- **Stale-while-revalidate** — отдавай stale контент, пока обновляется кеш (`stale-while-revalidate=86400`).
- **Cache key** — по умолчанию URL; для API добавляй Vary или query string нормализацию.
- **Signed URLs / Cookies** — защита private контента (paywalled видео, личные документы).
- **Origin shield** — дополнительный слой кеша перед origin для снижения нагрузки от cache miss surge.

## Связанные материалы

- [Caching strategy](../../patterns/architecture-design/caching-strategy.md)
- [Tools OVERVIEW](../OVERVIEW.md)
