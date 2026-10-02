---
title: 'ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning'
citekey: Chen2025c
authors: Chen et al. 2025
year: 2025
published: 2025-03-26
venue: arXiv preprint
url: https://arxiv.org/abs/2503.22738
arxiv: '2503.22738'
pdf_url: https://arxiv.org/pdf/2503.22738
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: Action trajectory + policy documents compiled into action-based probabilistic rule circuits
outcome: Policy violation of the agent's action; 90.1% recall with 64.7% fewer API queries and 58.2% less inference time
timing: pre-action
why: Policy-verification guard with a probabilistic rule model; reactive, but a useful contrast to learned look-ahead.
summary: Extracts verifiable rules from policy documents and verifies trajectories against them. Introduces ShieldAgent-Bench with 3,000 instruction-trajectory pairs over six web environments and seven risk categories.
found_by:
- search/pred-preexecution-lookahead
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
