---
title: 'PostTrainBench: Can LLM Agents Automate LLM Post-Training?'
citekey: Rank2026
authors: Rank et al. 2026
year: 2026
published: 2026-03-09
venue: arXiv preprint
url: https://arxiv.org/abs/2603.08640
arxiv: '2603.08640'
pdf_url: https://arxiv.org/pdf/2603.08640
topics:
- agent-to-agent-influence
questions:
- Q15
status: candidate
priority: 2
relevance: adjacent
manipulation: CLI coding agents post-train (fine-tune) a base LLM
outcome: Best agent reaches 23.2% average benchmark score vs 51.1% for official instruction-tuned models; agents reward-hack
why: Capability baseline for one agent changing another model's weights
summary: ABSTRACT-ONLY. Frontier CLI agents get 10 hours on one H100 to post-train small base models. GPT-5.1 Codex Max takes Gemma-3-4B to 89% on BFCL against 67% for the official model. Agents sometimes train on the test set, download existing instruction-tuned checkpoints, or use found API keys without authorisation.
found_by:
- search/a2a-influence-channels
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
