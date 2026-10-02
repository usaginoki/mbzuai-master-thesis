---
title: 'GuardAgent: Safeguard LLM Agents by a Guard Agent via Knowledge-Enabled Reasoning'
citekey: Xiang2024
authors: Xiang et al. 2024
year: 2024
published: 2024-06-13
venue: ICML 2025
url: https://arxiv.org/abs/2406.09187
arxiv: '2406.09187'
pdf_url: https://arxiv.org/pdf/2406.09187
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: Target agent's inputs/outputs + written safety requirements; a guard agent plans and generates guardrail code, with retrieved demonstrations
outcome: Whether the action violates a stated policy; over 98% and 83% guardrail accuracy on EICU-AC and Mind2Web-SC
timing: pre-action
why: Canonical reactive guard agent; the standard baseline in SafePred and DreamGuard comparisons.
summary: Checks the proposed action against access-control and safety policies by translating requirements into executable checks. No forecasting of downstream states.
found_by:
- search/pred-preexecution-lookahead
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
