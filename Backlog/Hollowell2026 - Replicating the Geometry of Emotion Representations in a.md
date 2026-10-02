---
title: Replicating the Geometry of Emotion Representations in a Base Open-Weights Model
citekey: Hollowell2026
authors: Hollowell 2026
year: 2026
published: 2026-09-01
venue: arXiv preprint
url: https://arxiv.org/abs/2609.22208
arxiv: '2609.22208'
pdf_url: https://arxiv.org/pdf/2609.22208
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: 171 story-derived emotion vectors in Gemma-2-27b (base model); validated by geometry against human valence/arousal ratings; no self-report
outcome: Valence axis aligns with human ratings at r = 0.72, arousal at r = 0.67; geometry consolidates at layers 22-26.
safety_use: none
why: Released open-weight emotion vectors (Hugging Face adamhollowell/gemma-emotion-vectors; code MIT) usable as an instrument
summary: 'Replicates Sofroniew et al. on a base open-weights model using 205,200 newly generated stories. Geometry only: no steering of behaviour, no assistant-facing analysis, no self-report.'
found_by:
- search/intro-i2-search
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
