---
title: The Twelve-Factor App
url: https://12factor.net/
type: article
category: sources
tags: [methodology, heroku, twelve-factor, cloud-native, patterns]
added: 2026-07-06
status: new
---

# The Twelve-Factor App

Авторы: Adam Wiggins и команда Heroku. 

Методология построения SaaS-приложений, сформулированная на основе опыта Heroku как платформы. 12 факторов — это набор принципов для приложений, которые легко деплоить, масштабировать и поддерживать в облачной среде.

## 12 факторов

| # | Фактор | Суть |
|---|--------|------|
| 1 | **Codebase** | One codebase tracked in revision control, many deploys |
| 2 | **Dependencies** | Explicitly declare and isolate dependencies |
| 3 | **Config** | Store config in the environment |
| 4 | **Backing Services** | Treat backing services as attached resources |
| 5 | **Build, Release, Run** | Strictly separate build and run stages |
| 6 | **Processes** | Execute the app as one or more stateless processes |
| 7 | **Port Binding** | Export services via port binding |
| 8 | **Concurrency** | Scale out via the process model |
| 9 | **Disposability** | Maximize robustness with fast startup and graceful shutdown |
| 10 | **Dev/Prod Parity** | Keep development, staging, and production as similar as possible |
| 11 | **Logs** | Treat logs as event streams |
| 12 | **Admin Processes** | Run admin/management tasks as one-off processes |

## Практическая ценность

- Фундамент для cloud-native и 12-факторный подход лёг в основу многих современных платформ (Heroku, Cloud Foundry, Kubernetes-развёртывания)
- Принципы актуальны для microservices, serverless и контейнерной архитектуры
- Даёт общий язык для обсуждения production-readiness приложения

## Связанные разделы vault

- `patterns/architecture-design/` — архитектурные стили
- `patterns/production-operations/` — операционные практики

## Статус

Добавлено: 2026-07-06
