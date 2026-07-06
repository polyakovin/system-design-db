# Security Policy

## Tool allowlist

- Разрешены: shell non-destructive, filesystem read/write в scope проекта, git, web search для исследований.
- Запрещены: `rm -rf` без подтверждения, `curl | bash`, eval на непроверенном вводе.

## Approval gates

- Destructive actions требуют подтверждения пользователя.
- Push в remote — только если это явно входит в задачу или подтверждено пользователем.
- Изменение секретов в конфигах — только с подтверждением.

## Secrets

- Секреты только в env vars или внешнем vault.
- Не читать, не коммитить и не логировать secrets.

## Audit

- Meaningful tool-driven изменения фиксируются в [audit-log.md](audit-log.md), если они важны для истории проекта.

