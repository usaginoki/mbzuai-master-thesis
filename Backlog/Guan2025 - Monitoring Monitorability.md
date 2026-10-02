---
title: Monitoring Monitorability
citekey: Guan2025
authors: Guan et al. 2025
year: 2025
published: 2025-12-20
venue: arXiv preprint
url: https://arxiv.org/abs/2512.18311
arxiv: '2512.18311'
pdf_url: https://arxiv.org/pdf/2512.18311
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: CoT (alone or with actions) read by LLM monitors; three evaluation archetypes (intervention, process, outcome-property) and a monitorability metric
outcome: Whether a monitor can tell a property of the agent's behaviour from its reasoning; CoT-only monitors significantly outperform action-only; longer CoTs more monitorable
timing: pre-action
why: Largest systematic measurement of how well reasoning predicts behaviour across frontier models, and how it scales
summary: OpenAI evaluation suite for CoT monitorability. Most frontier models are fairly but not perfectly monitorable; longer CoTs are more monitorable; RL optimisation did not materially decrease monitorability at current scale; the suite catches simple model organisms trained to obfuscate. Follow-up questions to the model, with the follow-up CoT given to the monitor, improve monitorability.
found_by:
- search/pred-cot-trajectory
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
