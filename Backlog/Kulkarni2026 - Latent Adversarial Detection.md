---
title: 'Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection'
citekey: Kulkarni2026
authors: Kulkarni 2026
year: 2026
published: 2026-04-30
venue: arXiv preprint
url: https://arxiv.org/abs/2604.28129
arxiv: '2604.28129'
pdf_url: https://arxiv.org/pdf/2604.28129
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: core
manipulation: 'Residual-stream trajectory features across turns (''adversarial restlessness'': path length of activation movement), with benign/pivoting/adversarial turn labels'
outcome: Multi-turn prompt injection; conversation-level detection 76.2% to 93.8% on synthetic held-out; 89.4% at 2.4% FPR on mixed set; real LMSYS only 47-71%
timing: earlier-in-trajectory
why: Turn-level trajectory signal, with honest numbers on weak off-distribution transfer.
summary: Five scalar trajectory features lift detection from 76.2% to 93.8% on synthetic data across four model families, but probes do not transfer across architectures. Leave-one-source-out shows real-world LMSYS detection of only 47-71%; binary conversation labels give 50-59% false positives. Single-author preprint.
found_by:
- search/pred-activation-probes
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
