---
title: 'Feedback Friction: LLMs Struggle to Fully Incorporate External Feedback'
citekey: JiangD2025
authors: Jiang et al. 2025
year: 2025
published: 2025-06-13
venue: arXiv preprint
url: https://arxiv.org/abs/2506.11930
arxiv: '2506.11930'
pdf_url: https://arxiv.org/pdf/2506.11930
topics:
- agent-to-agent-influence
questions:
- Q17.1
status: candidate
priority: 2
relevance: core
manipulation: Feedback-generator model with near-complete ground truth gives targeted feedback to a solver over up to 10 rounds
outcome: Solvers plateau below ceiling; feedback resistance explains 62.8-100% of persistent errors
why: Upper bound on what a perfect coach can achieve through text feedback
summary: 'FULL-TEXT (arXiv HTML via summarising fetch). Solvers: Llama-3.3-70B, Llama-4 Scout and Maverick, Claude 3.7 Sonnet (with and without thinking); feedback from GPT-4.1 mini. AIME stays 15-25% below the achievable level; more confident solvers (low semantic entropy) improve least; temperature and rejection sampling help only modestly.'
found_by:
- search/a2a-effects-performance
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
