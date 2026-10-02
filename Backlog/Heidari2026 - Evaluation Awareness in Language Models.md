---
title: 'Evaluation Awareness in Language Models: Representation, Verbalization, and Control'
citekey: Heidari2026
authors: Heidari et al. 2026
year: 2026
published: 2026-08-22
venue: arXiv preprint
url: https://arxiv.org/abs/2608.21766
arxiv: '2608.21766'
pdf_url: https://arxiv.org/pdf/2608.21766
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: core
manipulation: Compares linear-probe readouts of 'being evaluated' with what the model verbalises, and steers along the probe direction. Self-report validated against internals.
outcome: Evaluation awareness is linearly decodable in every model (best AUROC >= 0.7) but aligns only partly with verbalisation; steering along probe directions shifts verbalisation.
safety_use: indirect
why: Quantifies the gap between what the model represents and what it says - the reason an unprompted self-report cannot be the only sensor.
summary: Six models from four families; probing, LLM-judged verbalisation and steering, plus per-checkpoint analysis of Olmo. Probe-verbalisation correlations are nonzero in some settings but vary substantially by model, layer and readout.
found_by:
- search/intro-safety-uses-and-risks
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
