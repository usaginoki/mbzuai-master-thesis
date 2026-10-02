---
title: Endogenous Resistance to Activation Steering in Language Models
citekey: McKenzie2026
authors: McKenzie et al. 2026
year: 2026
published: 2026-02-06
venue: arXiv preprint
url: https://arxiv.org/abs/2602.06941
arxiv: '2602.06941'
pdf_url: https://arxiv.org/pdf/2602.06941
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: '(d) unaided: no instrument is shown. The model is steered off-task with SAE latents and its own output shows a verbal restart (''wait, that''s not right'') followed by on-topic continuation while steering persists.'
outcome: Llama-3.3-70B shows explicit self-correction in 3.8% of steered cases; ablating 26 SAE latents cuts multi-attempt behaviour by 25%.
safety_use: risk
why: A naturally occurring detect-and-correct loop on the model's own perturbed state; also a warning that models may resist beneficial steering (e.g. a calm vector).
summary: ABSTRACT-ONLY. Smaller Llama-3 and Gemma-2 models show the explicit form less often. Meta-prompting and fine-tuning on synthetic self-correction examples increase it. The authors note the model cannot tell adversarial from beneficial steering.
found_by:
- search/intro-instrumented-feedback-rerun
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
