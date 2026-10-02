---
title: Communicating Activations Between Language Model Agents
citekey: Ramesh2025
authors: Ramesh and Li 2025
year: 2025
published: 2025-01-23
venue: ICML 2025
url: https://arxiv.org/abs/2501.14082
arxiv: '2501.14082'
pdf_url: https://arxiv.org/pdf/2501.14082
topics:
- agent-to-agent-influence
questions:
- Q15
status: candidate
priority: 2
relevance: core
manipulation: one agent's intermediate activations merged into another agent's forward pass
outcome: Up to 27.0% improvement over natural-language communication with under 1/4 of the compute
why: Shows an internals-level influence channel between agents that carries no readable text
summary: ABSTRACT-ONLY. Model B's computation is paused at an intermediate layer, its activation combined with model A's through a function f, and the forward pass continued. Tested on coordination games and reasoning benchmarks. Safety or controllability of the channel is not discussed in the abstract.
found_by:
- search/a2a-influence-channels
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
