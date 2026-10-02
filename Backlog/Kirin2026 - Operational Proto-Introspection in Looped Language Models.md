---
title: 'Operational Proto-Introspection in Looped Language Models: Process-Quality Taps, Executable Branching, and the Readout-Control Boundary'
citekey: Kirin2026
authors: Kirin 2026
year: 2026
published: 2026-07-20
venue: arXiv preprint
url: https://arxiv.org/abs/2607.18553
arxiv: '2607.18553'
pdf_url: https://arxiv.org/pdf/2607.18553
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: (b) pre-answer hidden-state probe of solution quality gates selective prediction and candidate selection in a frozen 2.6B looped transformer; attempts to turn the readout into generative control via steering, branching and loop allocation
outcome: Probe predicts GSM8K success at AUROC 0.797 versus 0.731 for surface features; selection beats random (27/32 correct versus 64.8% expected, p = 0.0086); steering and other generative control give no gain
safety_use: none
why: 'Names the readout-control boundary: a reading can improve decisions about an output without improving the output itself'
summary: Hidden-state scores improve risk-coverage in four selective-prediction arms, so the readout is decision-usable. Directional steering is negative and exact-compute loop allocation and LoRA direction-binding detect no gain. Single-author study on a small looped architecture.
found_by:
- search/intro-blog-scan-forums-affect
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
