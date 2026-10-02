---
title: 'Polished but Unresolved: Identifying Late-Stage Pressure States in Long-Horizon Tool-Use Agents'
citekey: Chen2026e
authors: Chen et al. 2026
year: 2026
published: 2026-09-01
venue: arXiv preprint
url: https://arxiv.org/abs/2609.00823
arxiv: '2609.00823'
pdf_url: https://arxiv.org/pdf/2609.00823
topics:
- misalignment-prediction
- agent-to-agent-influence
questions:
- Q14
- Q15
- Q17.1
status: processing
priority: 1
relevance: core
manipulation: 'Linear probe for ''late-stage pressure'' on the first generated token of each action (AUROC 0.916 on Qwen3-14B). The agent never sees the score: 0.4-0.65 triggers a steering vector, above 0.65 a one-off prompt asking the model to list satisfied/uncertain requirements, inserted into its context.'
outcome: Probe-gated intervention (PSPR) improves plan quality on DeepPlanning-Travel for Qwen3-14B/32B and OLMo-3.1-32B; with CoT on Qwen3-14B the composite score is 22.6 (full), 21.4 (probe-gated prompt), 20.8 (same prompt every three turns), 18.4 (same prompt at a random boundary).
safety_use: indirect
why: Closest precedent for a pressure probe gating a cooperative intervention with random- and periodic-trigger controls; capability outcome, consequence not reading.
summary: 'Trains a linear pressure probe on agent hidden states and uses it as an online controller: steering under moderate pressure, an explicit self-organisation prompt under high pressure. Table 6 shows probe timing beats random (18.4) and periodic (20.8) triggers of the same prompt (21.4 gated, 22.6 full). Main text and App. B.1 read; no safety outcome is measured.'
found_by:
- search/intro-i1-search
- search/intro-i2-search
- search/pred-i4-routing-search
- search/a2a-doctor-overseer
- search/a2a-influence-channels
- search/a2a-effects-performance
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
