---
title: Throughput vs Latency Curves
type: pattern
category: performance-and-scalability
tags: [scalability, usl, throughput, latency, knee-point, queueing-theory, load-testing]
source: Practical Scalability Analysis with the Universal Scalability Law (Baron Schwartz, 2015)
added: 2026-07-06
---

# Throughput vs Latency Curves

## Проблема

Throughput и latency связаны нелинейно. Под нагрузкой latency растёт экспоненциально при приближении к saturation. Без understanding этой связи capacity planning становится гаданием.

## Решение

### Ключевые точки на кривой

```
Latency
   │                              ╭─── saturation
   │                         ╭───╯
   │                    ╭───╯
   │               ╭───╯  ← knee point
   │          ╭───╯
   │     ╭───╯
   │╭───╯  ← linear region
   └──────────────────────────── Throughput
```

- **Linear region:** latency почти константна, throughput растёт линейно с нагрузкой. Система не saturated.
- **Knee point:** точка перегиба, где latency начинает расти быстрее throughput. Оптимальная операционная точка — максимальный throughput при приемлемой latency.
- **Saturation:** очередь растёт неограниченно, latency → ∞. Throughput может даже падать (retrograde scaling из USL).

### Аппроксимация через USL

USL даёт throughput X(N), но latency L(N) можно аппроксимировать через Little's Law:

```
L(N) = N / X(N)
```

Где N — concurrent requests (load), X(N) — throughput. При малых N latency ~ константа; при приближении к saturation — резкий рост.

### Как найти knee point

1. Собрать (throughput, latency) пары под разной нагрузкой
2. Fit USL к throughput data → получить α, β
3. Knee ≈ N при котором latency превышает baseline в 2x
4. Альтернативно: N при котором marginal throughput gain < 10% от предыдущего шага

## Практическая эвристика

- Держи operating point **левее knee**: небольшой запас по throughput спасает от latency spikes при всплесках трафика
- Не оптимизируй для пикового throughput — обычно это точка, где latency уже неприемлема
- Разные bottlenecks дают разную форму кривой: α-dominated → пологое плато; β-dominated → острый пик с резким падением

## Связанные материалы

- [Universal Scalability Law](universal-scalability-law.md)
- [Capacity planning](capacity-planning.md)
- [Modelling real systems](modelling-real-systems.md)

## Источник

Baron Schwartz, *Practical Scalability Analysis with the Universal Scalability Law* (2015).
