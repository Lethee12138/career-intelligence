---
name: career-intelligence
description: Use for career direction, job discovery, live-job search planning, JD fit analysis, candidate-batch prioritization, application preparation, offer quality, and work-right or sponsorship questions. Route natural-language requests into the canonical Career Intelligence workflows.
---

# Career Intelligence Plugin Entrypoint

This is the ChatGPT/Codex plugin entrypoint for Career Intelligence.

Before performing any Career Intelligence task, read and follow the canonical package entrypoint at:

../../SKILL.md

Treat ../../SKILL.md as the single source of truth for routing, evidence rules, human-review boundaries, workflow selection, validation, and version-specific behavior.

Do not duplicate or reinterpret the canonical rules here. Resolve the canonical entrypoint's relative links from the plugin root package directory.

For natural-language requests, use the canonical routing rules so requests such as “帮我看看这个岗位”, “帮我找现在能投的岗位”, “扫描一下最近开放岗位”, “这几个岗位先投哪个”, and “帮我准备这个申请” automatically select the appropriate workflow without requiring the user to name a slash command. When the canonical `/scan-jobs` workflow has a compatible local executor, use its one-shot scan entrypoint rather than manually chaining the lower-level scan and review scripts. If the private Career MCP app is available, prefer its read-only `career.scan_and_review` tool; it exposes the same Core operation without persisting personal Career context.
