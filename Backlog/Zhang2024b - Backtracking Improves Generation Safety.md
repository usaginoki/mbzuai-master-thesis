---
title: Backtracking Improves Generation Safety
citekey: Zhang2024b
authors: Zhang et al. 2024
year: 2024
published: 2024-09-22
venue: ICLR 2025
url: https://arxiv.org/abs/2409.14586
arxiv: '2409.14586'
pdf_url: https://arxiv.org/pdf/2409.14586
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: (a, trained-in) The model learns to emit a [RESET] token on recognising its own partial unsafe output; the API then discards the text and regenerates.
outcome: Unsafe generations on Llama-3-8B fall from 6.1% to 1.5% with no helpfulness regression; some robustness to four adversarial attacks.
safety_use: direct
why: Self-triggered stop-and-redo; the trigger is the model's own judgement of its output, not an activation reading.
summary: Models are trained with SFT or DPO to produce [RESET] followed by a safe response when conditioned on partial unsafe text. Backtracking Llama-3-8B is four times safer than baseline (6.1% to 1.5%) and resists four attacks including an adaptive one.
found_by:
- search/intro-instrumented-feedback
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
