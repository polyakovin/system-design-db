---
title: Slack Architecture
url: https://systemdesign.one/slack-architecture/
type: url
category: sources
tags: [slack, real-time-messaging, websockets, horizontal-scaling, channel-architecture, system-design]
added: 2026-07-06
status: new
---

# Slack Architecture

Deep dive into Slack's system design by Neo Kim on systemdesign.one. Covers the real-time messaging platform architecture, WebSocket-based communication, channel model, message ordering guarantees, and horizontal scaling strategies. Includes detailed analysis of API design (web API vs real-time API), cursor-based pagination, file storage, and presence platform.

## Key Topics

- Real-time messaging via WebSockets and HTTP/2 SSE
- Horizontal scaling with Vitess for datastores
- Channel architecture and shared channels
- Message ordering and delivery guarantees
- File storage and edge caching (Flannel)
- Presence platform design
- Cursor-based vs offset pagination

## Status

Added: 2026-07-06. Source verified live. Core patterns (real-time messaging, WebSocket scaling) relevant to [Queues and streams](../../patterns/architecture-design/queues-and-streams.md).
