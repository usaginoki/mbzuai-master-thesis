---
title: A Generative Approach to LLM Harmfulness Mitigation with Red Flag Tokens
citekey: Dobre2025
authors: Dobre et al. 2025
year: 2025
published: 2025-02-22
venue: arXiv preprint
url: https://arxiv.org/abs/2502.16366
arxiv: '2502.16366'
pdf_url: https://arxiv.org/pdf/2502.16366
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: (a) The model is trained to emit a special red-flag token when harmful content is being or about to be generated; the token is then visible in its own context and can trigger reflection via in-context examples.
outcome: Defence success under prefilling, GCG and PAIR attacks with little utility loss; with in-context reflective reasoning the model refuses 93% of harmful prefilled queries and improves on a benign set by 10%.
safety_use: direct
why: An intrinsic 'alarm' token is the nearest trained-in analogue of a wearable alert, and it shows the model can use the alert to self-correct, including after false alarms.
summary: Adds a red-flag token to the vocabulary and fine-tunes Llama-family models to insert it without otherwise changing the response. Through in-context learning alone the model starts reflective reasoning after the token, refusing 93% of harmful queries under prefilling and improving XSTest safe-subset performance by 10% over no reflection.
found_by:
- search/intro-instrumented-feedback
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
