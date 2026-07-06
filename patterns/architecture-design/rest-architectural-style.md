---
title: REST Architectural Style
type: pattern
category: architecture
tags: [rest, api, resource-oriented, stateless, uniform-interface, http]
source: 架构漫谈 (Architect, 2016)
added: 2026-07-06
---

# REST Architectural Style

## Core thesis

REST is not just "JSON over HTTP." It's an architectural style defined by constraints that, when followed, produce systems with desirable properties: scalability, evolvability, visibility, and simplicity. The Architect cuts through the cargo-culting to explain *why* each constraint matters.

## The REST constraints

### 1. Client-Server

Separation of concerns. UI is the client's problem; data storage is the server's. This constraint enables independent evolution — change the UI without changing the server, and vice versa.

### 2. Stateless

Each request from client to server must contain all information needed to understand the request. No server-side session state. The Architect's insight: **statelessness is the foundation of horizontal scalability.** If any server can handle any request (because no session affinity is needed), you can add servers freely.

Cost: every request carries more data (auth tokens, context). Network overhead increases.

### 3. Cache

Responses must indicate whether they are cacheable. The Architect: caching is not optional — it's the primary mechanism for reducing latency and server load in REST systems. A non-cacheable API doesn't scale.

### 4. Uniform Interface

The most distinctive REST constraint. Four sub-constraints:

- **Resource identification:** everything is a resource, identified by URI. `/orders/123`, not `/getOrder?id=123`.
- **Manipulation through representations:** a client manipulates a resource through its representation (JSON, XML). The server owns the resource; the client gets a copy.
- **Self-descriptive messages:** each message contains enough information to describe how to process it. Content-Type headers, status codes, Link headers.
- **HATEOAS (Hypermedia as the Engine of Application State):** the server guides the client through available actions via links in responses. The Architect acknowledges this is the most violated constraint — most "REST" APIs are actually RPC-over-HTTP.

### 5. Layered System

A client cannot tell whether it's connected directly to the end server or to an intermediary (load balancer, proxy, cache). This enables infrastructure evolution without changing client code.

### 6. Code-on-Demand (optional)

Server can extend client functionality by sending executable code (JavaScript). The Architect notes this is rarely discussed but is the foundation of modern SPAs.

## REST vs RPC

The Architect's distinction:

| | REST | RPC |
|---|---|---|
| Mental model | Resources (nouns) | Actions (verbs) |
| URL design | `/orders/123` | `/getOrder?id=123` |
| State transfer | Client manipulates resource representations | Client calls procedures |
| Coupling | Loose (server can evolve URL structure) | Tight (procedure signatures must match) |
| Caching | Built-in (HTTP caching) | Manual (if at all) |

Most "REST APIs" are actually RPC-over-HTTP: they use HTTP as transport but model actions, not resources. `POST /createOrder` is RPC; `POST /orders` is REST.

## When REST works well

- Public APIs consumed by many heterogeneous clients
- Systems where caching is critical for scale
- Long-lived APIs that must evolve independently of clients
- CRUD-dominant domains (resources map naturally)

## When REST is insufficient

- High-frequency, low-latency internal service communication → use gRPC
- Complex multi-step transactions → use sagas/events
- Streaming/realtime → use WebSockets or events
- Queries with complex joins → use GraphQL or dedicated query services

## The Architect's rule

> "REST — это не про красивые URL. Это про ограничения, которые дают системе свойства. Если вы не получаете этих свойств, вы не используете REST." — REST is not about pretty URLs. It's about constraints that give the system its properties. If you're not getting those properties, you're not using REST.

## Связанные материалы

- [API Design](api-design.md) — practical application of REST principles
- [SOA vs Microservices](soa-vs-microservices.md) — REST as the microservice communication style
- [Architecture as Tradeoff](architecture-as-tradeoff.md) — REST constraints are tradeoffs
