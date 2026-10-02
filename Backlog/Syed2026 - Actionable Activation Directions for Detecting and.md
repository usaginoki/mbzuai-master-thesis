---
title: Actionable Activation Directions for Detecting and Mitigating Emergent Misalignment Across Language Model Families
citekey: Syed2026
authors: Syed et al. 2026
year: 2026
published: 2026-06-18
venue: arXiv preprint
url: https://arxiv.org/abs/2606.20225
arxiv: '2606.20225'
pdf_url: https://arxiv.org/pdf/2606.20225
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: Difference-in-means direction at the final layer separating insecure-code from secure-code finetunes
outcome: Separates aligned from misaligned activations at 99.6% within a model; cross-architecture transfer fails specificity controls
timing: post-hoc
why: Evidence that misalignment probes must be fitted per model, limiting reuse as a general forecaster.
summary: On four small instruction-tuned models (1-3B) finetuned identically, a within-model direction separates and causally reduces code spillover by 21-51 points. Mapped cross-model directions suppress behaviour but no better than random or orthogonal directions.
found_by:
- search/pred-training-time
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
