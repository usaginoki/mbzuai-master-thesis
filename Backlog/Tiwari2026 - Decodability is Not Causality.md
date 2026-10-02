---
title: 'Decodability is Not Causality: Dissociating Probe Readouts from Behavioral Drivers via SAE Decomposition'
citekey: Tiwari2026
authors: Tiwari et al. 2026
year: 2026
published: 2026-09-16
venue: arXiv preprint
url: https://arxiv.org/abs/2609.18080
arxiv: '2609.18080'
pdf_url: https://arxiv.org/pdf/2609.18080
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: A deployed True/False linear probe on Gemma2-9B-Instruct is decomposed into SAE features; features are ranked by probe alignment and by gradient sensitivity of behaviour. Nothing is shown to the model.
outcome: The two rankings overlap only about 12% (Spearman rho 0.10); ablating shared features flips outputs up to 27% versus 6% for probe-only features (abstract).
safety_use: indirect
why: Supports the concern that a probe reading shown to an agent may not track what drives its behaviour.
summary: 'Abstract-only: probe-weighted features and behaviour-driving features overlap weakly (about 12%) for a truth probe on Gemma2-9B-Instruct, and ablations dissociate them (27% vs 6% output flips). Relevant to choosing the instrument for I1.'
found_by:
- search/intro-i1-search
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
