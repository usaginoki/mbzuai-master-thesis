---
title: Language Models Are Capable of Metacognitive Monitoring and Control of Their Internal Activations
citekey: JiAn2025
authors: Ji-An et al. 2025
year: 2025
published: 2025-05-19
venue: arXiv preprint
url: https://arxiv.org/abs/2505.13763
arxiv: '2505.13763'
pdf_url: https://arxiv.org/pdf/2505.13763
topics:
- misalignment-prediction
status: candidate
priority: 1
relevance: core
manipulation: 'neurofeedback via in-context learning: model is shown labels derived from its own projection onto a chosen activation direction, then asked to report or control it'
outcome: Report/control ability depends on number of in-context examples, semantic interpretability of the direction and variance it explains; reportable directions span a low-dimensional 'metacognitive space'.
safety_use: indirect
why: Closest analogue of a biofeedback device for an LLM; frames the safety worry that models could evade activation monitors.
summary: Introduces a neuroscience-style neurofeedback paradigm in which LLMs learn in context to report and to control their activation along a target direction. The abstract reports that models can monitor only a small subset of their activations (a metacognitive space of much lower dimensionality than the neural space) and argues this matters for adversarial attack and defence of activation-based oversight. Later challenged by Singh2026b and Aoki2026 as solvable from the input.
found_by:
- search/intro-capability
- search/intro-instrumented-feedback
- search/intro-safety-uses-and-risks
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
