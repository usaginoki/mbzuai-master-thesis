---
title: 'AgentLens: Interpretable Safety Steering via Mechanistic Subspaces for Multi-Turn Coding Agent'
citekey: Luo2026b
authors: Luo et al. 2026
year: 2026
published: 2026-06-21
venue: arXiv preprint
url: https://arxiv.org/abs/2606.22673
arxiv: '2606.22673'
pdf_url: https://arxiv.org/pdf/2606.22673
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: One step-level linear probe per model on the coding agent's hidden state; (b) detection triggers steering in a 10-dimensional subspace of one layer so the agent refuses harmful execution.
outcome: Detects harmful execution states and 'substantially reduces harmful actions' on a 194-task benchmark built with Llama-3.1-8B, Qwen-2.5-7B and Gemma-2-9B.
safety_use: direct
why: Probe-gated intervention for externally induced harm in the same model sizes the thesis plans to use.
summary: ABSTRACT-ONLY. Introduces the Mechanistic Agent Safety benchmark and reports preliminary evidence of lookahead risk anticipation. Code is public. No numbers were read.
found_by:
- search/intro-instrumented-feedback-rerun
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
