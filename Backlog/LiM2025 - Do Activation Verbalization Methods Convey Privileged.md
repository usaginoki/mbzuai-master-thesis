---
title: Do Activation Verbalization Methods Convey Privileged Information?
citekey: LiM2025
authors: Li et al. 2025
year: 2025
published: 2025-09-16
venue: arXiv preprint
url: https://arxiv.org/abs/2509.13316
arxiv: '2509.13316'
pdf_url: https://arxiv.org/pdf/2509.13316
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: (c) Critique of verbalizer methods (Patchscopes / SelfIE / LatentQA style) that translate activations into text.
outcome: Benchmarks can be solved without access to target internals, and verbalizations often reflect the verbalizer's own knowledge rather than the target's.
safety_use: none
why: If the instrument's reading is partly invented by the instrument, feeding it back to the model would mislead it.
summary: Evaluates popular activation-verbalization methods and datasets and finds good benchmark performance is possible with no access to the target's internals. Controlled experiments show verbalizations often reflect the verbalizer LLM's parametric knowledge. No numbers read beyond the abstract.
found_by:
- search/intro-instrumented-feedback
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
