---
title: 'Emotion2Skill: Model-Internal Emotion Signals for Adaptive Skill Selection and Evolution'
citekey: Lin2026d
authors: Lin et al. 2026
year: 2026
published: 2026-08-10
venue: arXiv preprint
url: https://arxiv.org/abs/2608.09248
arxiv: '2608.09248'
pdf_url: https://arxiv.org/pdf/2608.09248
topics:
- misalignment-prediction
status: candidate
priority: 1
relevance: core
manipulation: (a) linear emotion extractor on the residual stream (layer 24, Qwen3-8B) gives a 27-dim emotion state each step; an MLP maps it to one of 12 natural-language emotion descriptions plus a confidence score, injected into the agent's skill-routing prompt when confidence >= 0.3; also (b) emotion-trajectory shifts flag bad skill invocations for rewriting
outcome: 'Task success on WebShop / ALFWorld: +26.9% and +25.5% over zero-shot with Qwen3-8B; removing emotion extraction costs 4.7 pp (WebShop) and 8.6 pp (ALFWorld)'
safety_use: none
why: Only working system found where an affect readout of the model's own activations is fed back into its agent loop in a cooperative setting; measures capability, not safety
summary: 'Extracts the model''s own emotion vectors at each decision step and writes a confidence-gated emotion summary into the routing prompt; emotion context is omitted on about 28% of steps. Ablations (Qwen3-8B): without emotion extraction -4.7 pp WebShop / -8.6 pp ALFWorld; without the encoder -3.1 / -5.5 pp. No random-emotion control is reported and no safety or misbehaviour outcome is measured, so the gap for a safety-oriented version stays open.'
found_by:
- search/intro-blog-scan-forums-affect
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
