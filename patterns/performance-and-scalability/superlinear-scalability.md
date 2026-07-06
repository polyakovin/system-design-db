---
title: Superlinear Scalability
type: pattern
category: performance-and-scalability
tags: [scalability, usl, superlinear, cache-effects, numa, working-set]
source: Practical Scalability Analysis with the Universal Scalability Law (Baron Schwartz, 2015)
added: 2026-07-06
---

# Superlinear Scalability

## Проблема

USL предсказывает, что throughput на узел всегда ≤ λ (baseline). Но иногда наблюдается **superlinear speedup**: N узлов дают > N × throughput одного узла. Это противоречит и USL, и Amdahl's Law.

## Причина

Superlinear scalability — не нарушение законов, а **изменение effective baseline** с ростом N:

### 1. Cache effects (самая частая причина)

Один узел: working set не помещается в cache → много cache misses → low throughput.

N узлов: working set каждого узла становится меньше (N × меньше данных) → помещается в cache → меньше misses → выше per-node throughput.

```
1 узел:   обрабатывает 100% данных → 20% в L3 cache → 800 rps
2 узла:   каждый обрабатывает 50% → 100% в L3 cache → 1100 rps каждый → 2200 total (> 1600)
```

### 2. NUMA effects

На одном узле данные могут быть на «дальнем» NUMA node → higher latency. С несколькими узлами можно разместить данные ближе к processing.

### 3. Resource pooling

Больше узлов → больше aggregate memory bandwidth, больше aggregate disk I/O, больше aggregate network buffers. Ресурсы не делятся идеально пропорционально.

## Как это выглядит в USL

Superlinear scalability на начальном участке (малые N) — USL fit может дать α < 0 или β < 0. Это артефакт: модель предполагает фиксированный baseline, а он изменился.

### Корректный подход

1. Измерять **per-node baseline** для того объёма данных, который узел будет обрабатывать в кластере
2. Если N=2 узла обрабатывают 50% данных каждый — измеряй baseline на одном узле с 50% данных
3. Тогда USL fit будет корректен, и superlinear эффект исчезнет

## Superlinear vs linear

| | Linear | Superlinear |
|---|---|---|
| Per-node throughput | = baseline | > baseline |
| Причина | Нет cache/NUMA эффектов | Working set уменьшается, cache попадания растут |
| Долгосрочное поведение | Сохраняется до contention/coherency limit | Эффект исчезает при насыщении cache |
| USL fit | α, β ≥ 0 | Может дать α < 0 (артефакт) |

## Когда ожидать superlinear

- In-memory databases с large working set
- Data processing: каждый worker обрабатывает partition данных, которая целиком помещается в RAM/cache
- Analytics: aggregation по партициям, где каждая партиция — cache-resident

## Связанные материалы

- [Universal Scalability Law](universal-scalability-law.md)
- [Linear scalability](linear-scalability.md)
- [Diminishing returns](diminishing-returns.md)

## Источник

Baron Schwartz, *Practical Scalability Analysis with the Universal Scalability Law* (2015). Neil Gunther, *Guerrilla Capacity Planning* (2007).
