---
title: Convergent Linear Representations of Emergent Misalignment
citekey: Soligo2025
authors: Soligo et al. 2025
year: 2025
published: 2025-06-13
venue: arXiv preprint
url: https://arxiv.org/abs/2506.11618
arxiv: '2506.11618'
pdf_url: https://arxiv.org/pdf/2506.11618
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: A mean-difference 'misalignment direction' extracted from one fine-tune's activations
outcome: Transfers to ablate misaligned behaviour in other fine-tunes (higher-rank LoRAs, different datasets); a control result rather than a measured forecast
timing: post-hoc
why: The convergence claim is what would make one probe reusable across training runs; later papers contest how far it transfers.
summary: Uses 9 rank-1 adapters to misalign Qwen2.5-14B-Instruct and shows a single direction from one model ablates misalignment in others. Of the adapters, six contribute to general misalignment and two specialise in the fine-tuning domain.
found_by:
- search/pred-training-time
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
