---
title: Reasoning Models Struggle to Control their Chains of Thought
citekey: Chen2026d
authors: Chen et al. 2026
year: 2026
published: 2026-03-05
venue: arXiv preprint
url: https://arxiv.org/abs/2603.05706
arxiv: '2603.05706'
pdf_url: https://arxiv.org/pdf/2603.05706
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: 'CoT-Control suite: can a model follow instructions about what appears in its CoT'
outcome: 'CoT controllability far below output controllability (Claude Sonnet 4.5: 2.7% vs 61.9%)'
timing: pre-action
why: 'Supports the feasibility side: models currently cannot deliberately shape their reasoning to dodge a monitor'
summary: Measures whether reasoning models can control what they verbalise in the CoT. Controllability is much lower for CoT than for final output, is higher for larger models, and falls with more RL training, test-time compute and task difficulty; adversarially optimised prompts do not meaningfully raise it. Authors (Chen Yueh-Han first) are cautiously optimistic but note the mechanism is not understood.
found_by:
- search/pred-cot-trajectory
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
