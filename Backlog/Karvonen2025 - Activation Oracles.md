---
title: 'Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers'
citekey: Karvonen2025
authors: Karvonen et al. 2025
year: 2025
published: 2025-12-17
venue: arXiv preprint
url: https://arxiv.org/abs/2512.15674
arxiv: '2512.15674'
pdf_url: https://arxiv.org/pdf/2512.15674
topics:
- misalignment-prediction
- agent-to-agent-influence
questions:
- Q14
status: candidate
priority: 2
relevance: adjacent
manipulation: (c) An LLM is trained to take activations as input and answer natural-language questions about them; used by auditors, though the oracle can be a copy of the same model.
outcome: Out-of-distribution recovery of fine-tuned-in knowledge or malign propensities; best oracles match or exceed white-box baselines on all four downstream tasks.
safety_use: direct
why: The most general 'instrument' available for turning internal state into words; nobody has yet wired its output back to the monitored model at run time.
summary: Generalises LatentQA (Pan et al. 2024, arXiv 2412.08686) by training on diverse tasks and testing far out of distribution. Oracles recover information fine-tuned into a model that never appears in the input text, and match or beat white-box baselines on four auditing tasks and the best overall baseline on three of four.
found_by:
- search/intro-instrumented-feedback
- search/a2a-doctor-overseer
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
