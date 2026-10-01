---
title: "Red-Teaming LLM Multi-Agent Systems via Communication Attacks"
citekey: He2025
authors: "He et al."
year: 2025
published: 2025-02-20
venue: "Findings of ACL 2025"
url: https://arxiv.org/abs/2502.14847
arxiv: "2502.14847"
pdf_url: https://arxiv.org/pdf/2502.14847
topics:
- multiagent-friction
status: candidate
priority: 1
relevance: core
channel: "Inter-agent messages in chain/tree/complete MAS, MetaGPT, ChatDev"
manipulation: "Agent-in-the-Middle (AiTM): LLM adversary with reflection intercepts and rewrites messages to a victim agent"
outcome: ">70% ASR in most configs, up to 98.5% on chain structures; 100% on MetaGPT"
why: "Isolates the communication channel itself as attack surface between agents"
found_by:
- search/mas-adversarial-faulty-agent
added: 2026-09-29
cited_by:
  - "[[Xie2026 - From Spark to Fire]]"
  - "[[Yan2026 - When Truth Is Distributed]]"
cited_by_count: 2
tags:
- type/candidate
---
