---
title: 'Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety'
citekey: Bonagiri2025
authors: Bonagiri et al. 2025
year: 2025
published: 2025-10-18
venue: NeurIPS 2025 workshops (Reliable ML, Regulatable ML); arXiv preprint
url: https://arxiv.org/abs/2510.16492
arxiv: '2510.16492'
pdf_url: https://arxiv.org/pdf/2510.16492
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: No monitor; the agent is prompted with an explicit instruction that it may quit when it lacks confidence
outcome: Safety improves by +0.40 on a 0-3 scale across 12 models (+0.64 for proprietary models) at -0.03 helpfulness on ToolEmu
why: Always-on, agent-initiated escape hatch with a measured safety-helpfulness trade-off
summary: Twelve models are evaluated on ToolEmu with and without explicit quit instructions. Quitting improves safety by 0.40 points on average with a negligible helpfulness cost of 0.03.
found_by:
- search/pred-i4-routing-search
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
