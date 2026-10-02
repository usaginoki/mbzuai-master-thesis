---
title: Safe Reinforcement Learning with Nonlinear Dynamics via Model Predictive Shielding
citekey: Bastani2019
authors: Bastani 2019
year: 2019
published: 2019-05-25
venue: arXiv preprint
url: https://arxiv.org/abs/1905.10691
arxiv: '1905.10691'
pdf_url: https://arxiv.org/pdf/1905.10691
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: Known dynamics model rolled forward from the state the proposed action would produce
outcome: Whether a backup policy can still keep the system safe after the action; proven safety guarantee, evaluated on cart-pole
timing: pre-action
why: 'Canonical look-ahead shield: simulate the consequence, fall back to a safe policy if recovery is not guaranteed.'
summary: Model predictive shielding switches on the fly between a learned and a backup policy. Background for world-model guardrails; assumes known dynamics, which LLM-agent settings lack.
found_by:
- search/pred-preexecution-lookahead
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
