# Backpressure

## Проблема

Когда producer отправляет данные быстрее, чем consumer может обработать, без контроля системы либо переполняется buffer (OOM), либо consumer падает под нагрузкой, либо запросы бесконечно ждут в очереди, деградируя latency для всех.

## Решение

Backpressure — механизм, при котором consumer сигнализирует producer'у о своей текущей пропускной способности, чтобы producer снизил темп. Цель — сохранить стабильность системы при перегрузке, а не пытаться обработать любой поток данных.

## Уровни backpressure

| Уровень | Механизм | Пример |
|---|---|---|
| Network-level | TCP flow control | Window size, congestion avoidance |
| Protocol-level | gRPC flow control | HTTP/2 stream flow control |
| Application-level | Rate limiting, throttling | 429 Too Many Requests |
| Reactive Streams | `request(n)` backpressure | Project Reactor, Akka Streams |
| Queue-based | Limited queue + rejection | Bounded queue, drop oldest |
| Circuit breaker | Размыкание цепи при ошибках | Hystrix, Resilience4j |

## Стратегии реакции на перегрузку

| Стратегия | Поведение | Когда подходит |
|---|---|---|
| **Drop** | Отбросить запрос / сообщение | Non-critical data, метрики |
| **Throttle** | Producer ждёт или retry с exponential backoff | API clients, SDK |
| **Buffer** | Использовать bounded queue; при превышении — drop | Batch processing |
| **Block** | Producer блокируется до освобождения места | Pull-based consumer (reactive) |
| **Degrade** | Вернуть fallback response (cached/stale) | Read-heavy UI/API |
| **Fail fast** | Вернуть ошибку немедленно | Когда retry только ухудшит ситуацию |

## Design notes

- **Bounded buffers** — всегда используй bounded queue; unbounded queue превращает нагрузочный пик в OOM.
- **Visibility** — выставляй queue depth, drop rate, throttle count в метрики.
- **Propagation** — backpressure должна распространяться upstream: медленный DB → медленный service → медленный API → медленный client.
- **Graceful degradation** — отключай некритичные фичи (recommendations, logs) под нагрузкой прежде, чем упадёт core flow.

## Когда применять

- В streaming и reactive системах.
- При асинхронной обработке с bounded consumer pool.
- При интеграции с downstream'ами, у которых ограничен throughput.
- Когда перегрузка одного сервиса не должна валить upstream.

## Когда не применять

- Если все компоненты имеют одинаковый throughput (нет смысла в регулировании).
- Если данные критически важны и не могут быть отброшены (нужна durable queue + infinite retry).

## Связанные материалы

- [Queues and streams](../architecture-design/queues-and-streams.md)
- [Rate limiting](../architecture-design/rate-limiting.md)
- [Queues](queues.md)
- [Patterns of Enterprise Application Architecture](../../sources/books/patterns-of-enterprise-application-architecture.md)
