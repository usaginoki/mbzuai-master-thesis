---
title: 'RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?'
citekey: Gupta2025c
authors: Gupta and Jenner 2025
year: 2025
published: 2025-06-17
venue: arXiv preprint
url: https://arxiv.org/abs/2506.14261
arxiv: '2506.14261'
pdf_url: https://arxiv.org/pdf/2506.14261
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: RL fine-tuning against a latent monitor's score while preserving black-box behaviour; white-box evaluation.
outcome: Token-level monitors are highly vulnerable; max-pooling and attention-based probes remain robust; evasion of one static monitor generalises to unseen monitors and can be made conditional on inputs.
safety_use: risk
why: Shows which monitor designs survive when the monitor becomes a training signal.
summary: Applied to 7B-14B models. Mechanistically the model repurposes tokens to have different internal representations.
found_by:
- search/intro-safety-uses-and-risks
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
