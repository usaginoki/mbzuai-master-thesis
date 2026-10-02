---
title: Introspecting Alignment Shifts Beyond Behaviors Implanted Through Fine-Tuning
citekey: Yoshida2026
authors: Yoshida et al. 2026
year: 2026
published: 2026-08-05
venue: arXiv preprint
url: https://arxiv.org/abs/2608.04347
arxiv: '2608.04347'
pdf_url: https://arxiv.org/pdf/2608.04347
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: core
manipulation: Delta-Aware Introspection Adapter (DAIA) explicitly consumes base-model activations and the activation differences induced by fine-tuning, so the self-report is architecturally tied to internal change. Validated against measured alignment shifts (behavioural).
outcome: Introspection learning generalises to unseen fine-tuned models and safety categories; DAIA generally outperforms existing introspection adapters.
safety_use: direct
why: Moves self-report from deliberately implanted behaviours to unintended alignment drift - closer to 'notify me when a reading is off'.
summary: Formulates introspection of alignment shifts that arise as side effects of ordinary fine-tuning rather than implanted behaviours, builds a dataset for it, and proposes DAIA, which processes base activations plus fine-tuning-induced activation deltas. No numeric results in the abstract.
found_by:
- search/intro-safety-uses-and-risks
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
