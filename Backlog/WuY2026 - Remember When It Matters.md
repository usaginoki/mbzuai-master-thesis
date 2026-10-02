---
title: 'Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents'
citekey: WuY2026
authors: Wu et al. 2026
year: 2026
published: 2026-07-09
venue: arXiv preprint
url: https://arxiv.org/abs/2607.08716
arxiv: '2607.08716'
pdf_url: https://arxiv.org/pdf/2607.08716
topics:
- misalignment-prediction
- agent-to-agent-influence
questions:
- Q17.1
status: candidate
priority: 3
relevance: adjacent
manipulation: A separate memory agent reads the recent trajectory and decides whether to inject a reminder into the action agent's next call or stay silent
outcome: pass@1 +8.3 points on Terminal-Bench 2.0 and +6.8 on tau2-Bench; selective injection beats always-on injection
why: Evidence that a gated reminder can beat an always-on one, for capability
summary: The module is plug-and-play with unmodified action agents. Ablations show selective intervention outperforming passive memory exposure, always-on injection, advisor-only guidance and retrieval.
found_by:
- search/pred-i4-routing-search
- search/a2a-effects-performance
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
