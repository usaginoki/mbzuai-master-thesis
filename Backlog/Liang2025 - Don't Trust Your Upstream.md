---
title: "Don't Trust Your Upstream: Exploiting LLM Multi-Agent System via Topology-Guided Adversarial Propagation"
citekey: Liang2025
authors: "Liang et al."
year: 2025
published: 2025-12-03
venue: "arXiv preprint"
url: https://arxiv.org/abs/2512.04129
arxiv: "2512.04129"
pdf_url: https://arxiv.org/pdf/2512.04129
topics:
- multiagent-friction
status: candidate
priority: 2
relevance: core
channel: "Upstream->downstream agent pipelines with privilege differences"
manipulation: "Compromised low-privilege agent whose outputs are reinterpreted downstream"
outcome: "40-78% ASR on three MAS frameworks, 85% on real apps; defense blocks ~95%"
why: "Privilege escalation through inter-agent trust"
found_by:
- search/mas-adversarial-faulty-agent
cited_by: []
added: 2026-09-29
cited_by_count: 0
tags:
- type/candidate
---
