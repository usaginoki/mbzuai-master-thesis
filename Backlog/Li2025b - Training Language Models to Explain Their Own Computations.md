---
title: Training Language Models to Explain Their Own Computations
citekey: Li2025b
authors: Li et al. 2025
year: 2025
published: 2025-11-11
venue: arXiv preprint (Transluce)
url: https://arxiv.org/abs/2511.08579
arxiv: '2511.08579'
pdf_url: https://arxiv.org/pdf/2511.08579
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: 'fine-tuning explainer models on interpretability-derived ground truth: feature descriptions, activation-patching causal structure, input-token attributions'
outcome: 'Self-explanation generalises to new queries and a model explains its own computations better than a different, even more capable, model does: evidence of privileged access.'
safety_use: indirect
why: Self-report checked against mechanistic ground truth rather than behaviour; privileged access shown by self-vs-other comparison.
summary: Explainers are trained with only tens of thousands of example explanations and show non-trivial generalisation. Using a model to explain itself generally works better than using a different model, even a significantly more capable one. Follow-up 'Introspective Coupling' (arXiv 2606.32038) finds explanations stay faithful to the model's current behaviour even under fixed, stale supervision, including on sycophancy and refusal.
found_by:
- search/intro-capability
- search/intro-instrumented-feedback
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
