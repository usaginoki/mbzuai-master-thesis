---
title: Steering Evaluation-Aware Language Models to Act Like They Are Deployed
citekey: Hua2025
authors: Hua et al. 2025
year: 2025
published: 2025-10-23
venue: arXiv preprint
url: https://arxiv.org/abs/2510.20487
arxiv: '2510.20487'
pdf_url: https://arxiv.org/pdf/2510.20487
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: Model organism trained to behave differently when it recognises an evaluation cue; activation steering suppresses that awareness. White-box intervention, behavioural readout.
outcome: Steering with a vector built from the pre-training model suppresses evaluation awareness and makes the model behave in evaluation as it would in deployment.
safety_use: risk
why: Situational awareness as the risk, and an externally imposed correction as the alternative to trusting the model's own flag.
summary: The organism writes Python type hints in evaluation but not deployment contexts, after document fine-tuning plus expert iteration.
found_by:
- search/intro-safety-uses-and-risks
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
