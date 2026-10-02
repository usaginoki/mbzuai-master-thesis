---
title: 'DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs'
citekey: Albrethsen2026
authors: Albrethsen et al. 2026
year: 2026
published: 2026-02-18
venue: arXiv preprint
url: https://arxiv.org/abs/2602.16935
arxiv: '2602.16935'
pdf_url: https://arxiv.org/pdf/2602.16935
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: Sequence of fine-tuned turn-level embeddings fed to an RNN that carries hidden state across the conversation
outcome: Multi-turn jailbreaks (Crescendo, ActorAttack); F1 0.84 vs 0.67 for Llama-Prompt-Guard-2 and Granite-Guardian; under 20 ms overhead
timing: earlier-in-trajectory
why: Representative stateful conversation guard; shows accumulation beats stateless per-turn filters, but reports no lead time
summary: A stateful monitor that propagates a hidden state over turns to capture incremental accumulation of risk. Reports F1 0.84 on multi-turn jailbreak detection against stateless guardrail baselines at 0.67. Evaluation is detection accuracy, not how early the alarm fires.
found_by:
- search/pred-cot-trajectory
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
