---
title: 'Open-Weight Masked Introspection: Measuring What Language Models Can Report About Their Own Computation'
citekey: Ferrara2026
authors: Ferrara 2026
year: 2026
published: 2026-08-20
venue: arXiv preprint
url: https://arxiv.org/abs/2608.20569
arxiv: '2608.20569'
pdf_url: https://arxiv.org/pdf/2608.20569
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: (d) unaided introspection on interventions at residual-stream sites, attention heads and SAE features, compared against a linear probe and a fine-tuned reporter on the same activations
outcome: 'Eight open-weight models, over 78,000 measurements: self-report distinguishes real intervention from sham at AUROC about 0.5007, while a linear probe on the same activations recovers it at 75% to 95.8% accuracy'
safety_use: indirect
why: 'Argues for the external instrument: the information is in the activations but does not reach the verbal report'
summary: No model's report beats chance against sham runs, impact-matched random perturbations and a text-only observer, with the effect bounded below 0.15 percentage points of AUROC. A fine-tuned reporter reaches near-perfect recovery on held-out directions, and in one model the confidence attached to a fixed yes/no answer separates intervention from sham at AUROC 0.647. Concerns injected interventions, not naturally arising states.
found_by:
- search/intro-blog-scan-forums-affect
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
