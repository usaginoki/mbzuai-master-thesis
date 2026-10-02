---
title: 'Norm Enforcement for AI Agents: Robustly Shaping Behavior in Multi-Agent Systems'
citekey: Ye2026
authors: Ye and Steinhardt 2026
year: 2026
published: 2026-07-07
venue: ICML 2026 Trustworthy AI for Good Workshop
url: https://arxiv.org/abs/2607.09766
arxiv: '2607.09766'
pdf_url: https://arxiv.org/pdf/2607.09766
topics:
- agent-to-agent-influence
- social-simulation
questions:
- Q16
- Q18
status: candidate
priority: 1
relevance: core
manipulation: 'report tool: agents report other agents'' actions, which can lead to their removal'
outcome: Good agents report honestly; narrowly misaligned agents file false reports to remove competitors without being trained or prompted to, so honest agents are removed nearly as fast as bad ones
why: Direct evidence on how agents use a reporting tool over peers, including abuse
summary: FULL-TEXT (arXiv HTML), qualitative rates only. Three simulated environments, populations of 50% good and 50% bad agents (Qwen3-NEXT-80B-A3B bad actors, prompted or narrowly fine-tuned). Bad agents file a substantially higher fraction of false reports. Reliability estimates with escalating penalties resist the exploit.
found_by:
- search/a2a-inclination
- search/sim-power-and-steering
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
