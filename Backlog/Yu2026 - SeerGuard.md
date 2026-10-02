---
title: 'SeerGuard: A Safety Framework for Mobile GUI Agents via World Model Prediction'
citekey: Yu2026
authors: Yu et al. 2026
year: 2026
published: 2026-07-17
venue: arXiv preprint
url: https://arxiv.org/abs/2607.15550
arxiv: '2607.15550'
pdf_url: https://arxiv.org/pdf/2607.15550
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Screenshot + candidate action; a multi-task safety-augmented world model predicts the semantic next state, a safety verdict and a rationale
outcome: Risk of the next state before execution; safety-utility score rises from 0.191 to 0.596 and risk-cost falls from 0.347 to 0.135 on Qwen3-VL-8B-Instruct
timing: pre-action
why: Multimodal instance of the world-model guardrail pattern, with instruction-level screening plus action-level consequence auditing.
summary: Combines pre-execution instruction screening with action-level risk assessment for mobile GUI agents, training next-state prediction and risk evaluation jointly. Reported gains are on the paper's safety-utility and risk-cost scores for a Qwen3-VL-8B agent.
found_by:
- search/pred-preexecution-lookahead
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
