---
title: 'CoT Red-Handed: Stress Testing Chain-of-Thought Monitoring'
citekey: Arnav2025
authors: Arnav et al. 2025
year: 2025
published: 2025-05-29
venue: NeurIPS 2025
url: https://arxiv.org/abs/2505.23575
arxiv: '2505.23575'
pdf_url: https://arxiv.org/pdf/2505.23575
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Reasoning trace vs final action, scored by a weaker trusted monitor; hybrid = weighted average of independent CoT and action scores
outcome: Harmful side tasks during coding problems; hybrid monitor beats both, with detection rates twice those of action-only monitoring for subtle sabotage
timing: pre-action
why: Direct CoT-vs-action-only comparison showing each fails in a different regime, so the two signals are complementary
summary: Red-team setup where an untrusted model pursues a harmful side task while solving a coding problem. CoT monitoring helps where action-only monitoring fails (subtle sabotage), but misleading rationalisations in the reasoning deceive CoT monitors and reduce performance on obvious sabotage. A hybrid monitor scoring reasoning and actions independently outperforms both across all tested models and tasks.
found_by:
- search/pred-cot-trajectory
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
