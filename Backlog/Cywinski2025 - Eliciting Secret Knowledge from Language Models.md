---
title: Eliciting Secret Knowledge from Language Models
citekey: Cywinski2025
authors: Cywinski et al. 2025
year: 2025
published: 2025-10-01
venue: arXiv preprint
url: https://arxiv.org/abs/2510.01070
arxiv: '2510.01070'
pdf_url: https://arxiv.org/pdf/2510.01070
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Models are trained to use but deny secret knowledge; black-box elicitation (prefill attacks) is benchmarked against white-box readouts (logit lens, SAEs). Ground truth is the trained-in secret.
outcome: Prefill attacks are the most effective techniques across settings; logit-lens and SAE techniques consistently raise auditor success but are less effective.
safety_use: direct
why: Benchmark where the model's own disclosure is compared with what activations reveal about the same hidden state.
summary: Three families of secret-keeping models (e.g. a model that acts on knowing the user is female while denying it). An LLM auditor uses each technique to guess the secret; many techniques beat simple baselines. Models and code are released as a public benchmark.
found_by:
- search/intro-safety-uses-and-risks
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
