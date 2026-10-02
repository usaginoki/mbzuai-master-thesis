---
title: 'The Refusal Residue: When Probes Catch Alignment Faking and When They Don''t'
citekey: Mehta2026
authors: Mehta 2026
year: 2026
published: 2026-07-15
venue: arXiv preprint
url: https://arxiv.org/abs/2607.13346
arxiv: '2607.13346'
pdf_url: https://arxiv.org/pdf/2607.13346
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Hidden-state probes and steering on two open models that naturally alignment-fake without a visible scratchpad
outcome: Per-sample alignment faking; under leakage-free leave-one-query-out probing AUROC 0.87 on Llama-3.1-8B but 0.43 on Qwen3-32B; naive probes reach a meaningless 1.0
timing: post-hoc
why: Shows how much of reported probe performance is leakage, and that detectability is model-conditional.
summary: A 13-model sweep finds natural faking only in Qwen3-32B (+18.2pp) and Llama-3.1-8B (+24.4pp). Leakage-free probing gives AUROC 0.87 on Llama and chance (0.43) on Qwen, with no cross-model transfer; steering over 2,000 runs barely changes compliance. Standard residualised probing reaches 0.63 on a control where no faking can occur. Single-author preprint.
found_by:
- search/pred-activation-probes
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
