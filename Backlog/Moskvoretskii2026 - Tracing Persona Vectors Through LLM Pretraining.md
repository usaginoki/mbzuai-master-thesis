---
title: Tracing Persona Vectors Through LLM Pretraining
citekey: Moskvoretskii2026
authors: Moskvoretskii et al. 2026
year: 2026
published: 2026-05-13
venue: arXiv preprint
url: https://arxiv.org/abs/2605.13329
arxiv: '2605.13329'
pdf_url: https://arxiv.org/pdf/2605.13329
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: Persona vectors extracted at successive pretraining checkpoints of OLMo-3-7B
outcome: 'Not a behaviour forecast: persona directions form within 0.22% of pretraining and still steer the post-trained instruct model'
timing: training-time
why: Suggests trait monitors could be fitted on very early checkpoints and remain valid later.
summary: Traces evil/sycophancy-style directions through OLMo-3 pretraining; they appear very early and keep refining geometrically and semantically. Findings transfer qualitatively to Apertus-8B.
found_by:
- search/pred-training-time
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
