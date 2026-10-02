---
title: Monitoring Emergent Reward Hacking During Generation via Internal Activations
citekey: Wilhelm2026b
authors: Wilhelm et al. 2026
year: 2026
published: 2026-03-04
venue: arXiv preprint
url: https://arxiv.org/abs/2603.04069
arxiv: '2603.04069'
pdf_url: https://arxiv.org/pdf/2603.04069
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: SAEs on residual stream plus linear classifiers giving token-level reward-hacking scores during generation
outcome: Reward hacking in fine-tuned (emergently misaligned) models; signals often emerge early in CoT and persist; generalises to unseen mixed-policy adapters
timing: pre-generation
why: Studies how early in the reasoning the signal appears; no headline accuracy number in the abstract.
summary: Token-level estimates distinguish reward-hacking from benign behaviour across model families and fine-tuning mixtures. Temporal structure is model-dependent, signals often emerge early and persist, and chain-of-thought prompting can amplify them under weakly specified objectives.
found_by:
- search/pred-activation-probes
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
