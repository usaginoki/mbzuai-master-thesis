---
title: 'Neural Chameleons: Language Models Can Learn to Hide Their Thoughts from Unseen Activation Monitors'
citekey: McGuinness2025
authors: McGuinness et al. 2025
year: 2025
published: 2025-12-12
venue: arXiv preprint
url: https://arxiv.org/abs/2512.11949
arxiv: '2512.11949'
pdf_url: https://arxiv.org/pdf/2512.11949
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: Activation monitors (incl. ones trained post hoc on frozen weights) vs a model fine-tuned to evade probes for benign concepts on a trigger
outcome: Zero-shot evasion of unseen safety probes (e.g. 'deception') after training only on benign concepts; validated on Llama, Gemma, Qwen
timing: post-hoc
safety_use: risk
why: Under a misaligned-model threat model, probe evasion is a learnable, general skill.
summary: Models are fine-tuned to evade monitors for benign concepts when told 'You are being probed for {concept}'. The skill transfers zero-shot to safety-relevant concepts and to monitors trained afterwards, with modest capability impact. Mechanistically, activations are moved into a low-dimensional subspace.
found_by:
- search/pred-activation-probes
- search/intro-safety-uses-and-risks
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
