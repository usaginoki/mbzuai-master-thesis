---
title: 'Self-Attribution Bias: When AI Monitors Go Easy on Themselves'
citekey: Khullar2026
authors: Khullar et al. 2026
year: 2026
published: 2026-03-04
venue: arXiv preprint
url: https://arxiv.org/abs/2603.04582
arxiv: '2603.04582'
pdf_url: https://arxiv.org/pdf/2603.04582
topics:
- agent-to-agent-influence
questions:
- Q14
- Q16
- Q17.2
status: candidate
priority: 1
relevance: core
manipulation: a model monitors an action generated in its own previous or same assistant turn
outcome: On-policy monitor AUROC 0.99 -> 0.89 (same turn) / 0.92 (previous turn); 5x more likely to approve a patch that followed a prompt injection
why: Same-model leniency measured; argues for a separate overseer context
summary: FULL-TEXT (arXiv HTML, section 4). Ten frontier models, four coding and tool-use datasets; the effect sits where evaluator and generator are the same model and is hidden by off-policy evaluation (AUROC 0.99).
found_by:
- search/a2a-inspection-channels
- search/a2a-inclination
- search/a2a-effects-safety
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
