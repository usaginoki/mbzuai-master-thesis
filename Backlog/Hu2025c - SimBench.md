---
title: 'SimBench: Benchmarking the Ability of Large Language Models to Simulate Human Behaviors'
citekey: Hu2025c
authors: Hu et al. 2025
year: 2025
published: 2025-10-20
venue: ICLR 2026
url: https://arxiv.org/abs/2510.17516
arxiv: '2510.17516'
pdf_url: https://arxiv.org/pdf/2510.17516
topics:
- social-simulation
questions:
- Q19
status: candidate
priority: 2
relevance: adjacent
manipulation: Unifies 20 datasets (moral decisions, economic choice, surveys) with a global participant pool into one benchmark of how well LLMs predict human response distributions.
outcome: 'Best model scores 40.80/100; performance scales log-linearly with model size, not with inference-time compute; an alignment-simulation trade-off: instruction tuning helps on low-entropy (consensus) questions and hurts on high-entropy (diverse) ones; models struggle with specific demographic groups; simulation ability correlates with MMLU-Pro at r = 0.939.'
why: Standard benchmark figure for 'how good are LLM simulators', and a mechanism (instruction tuning) for reduced variance.
summary: From the arXiv abstract page (fetched). A search snippet names Claude 3.7 Sonnet as the best model; ICLR 2026 venue from the proceedings link in search results.
found_by:
- search/sim-human-fidelity
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
