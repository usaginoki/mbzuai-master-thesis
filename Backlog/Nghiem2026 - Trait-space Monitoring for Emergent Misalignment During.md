---
title: Trait-space Monitoring for Emergent Misalignment During Supervised Finetuning
citekey: Nghiem2026
authors: Nghiem et al. 2026
year: 2026
published: 2026-05-31
venue: arXiv preprint
url: https://arxiv.org/abs/2606.07631
arxiv: '2606.07631'
pdf_url: https://arxiv.org/pdf/2606.07631
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Drift of checkpoint activations along seven alignment-relevant trait directions during LoRA finetuning; low-overhead monitor on the drift profile
outcome: 'Dangerous (emergently misaligned) checkpoints: 2.2% FNR, 2.9% FPR, 0.990 AUROC on held-out perturbation types, beating unsupervised PCA and SAE baselines'
timing: training-time
why: Closest thing to an in-training alarm with reported error rates; also documents where it breaks.
summary: Tracks representational drift across training checkpoints in four open 7-9B LLMs; EM-relevant drift concentrates on one low-dimensional axis explaining 65.5% of variance. The monitor detects dangerous checkpoints at 0.990 AUROC, but stress tests on two 14B models, longer runs and misaligned starting points show recalibration is needed across regimes. A search-result excerpt of the paper reports lead time before behavioural onset averaging +0.8 training steps (median 0), i.e. detection is essentially concurrent rather than anticipatory (verify in the full text).
found_by:
- search/pred-training-time
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
