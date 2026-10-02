---
title: 'Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought'
citekey: Boppana2026
authors: Boppana, Ma et al. 2026 (Goodfire)
year: 2026
published: 2026-03-05
venue: arXiv preprint / Goodfire research post (2026-03-12)
url: https://www.goodfire.com/research/reasoning-theater
arxiv: '2603.05488'
pdf_url: https://arxiv.org/pdf/2603.05488
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: Attention probes decode the model's current belief about its final answer; (b) probe confidence gates early exit from reasoning.
outcome: Probe exit at 95% confidence saves 67.7% of tokens on MMLU and 33.4% on GPQA-Diamond for DeepSeek-R1 at over 95% of baseline accuracy.
safety_use: indirect
why: Run-time controller gated by a confidence readout of the model's own state; efficiency rather than safety, but a clean mechanism template.
summary: Probes reach 87.98% accuracy predicting the final answer on MMLU early in reasoning. GPT-OSS saved 61.3% of tokens at 94.9% accuracy retention. Verbalised inflection points ('Wait', 'Aha') were twice as frequent in low-confidence responses.
found_by:
- search/intro-blog-scan-labs
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
