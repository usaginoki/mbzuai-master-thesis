---
title: Building a Foundational Guardrail for General Agentic Systems via Synthetic Data
citekey: Huang2025b
authors: Huang et al. 2025
year: 2025
published: 2025-10-10
venue: arXiv preprint (ICLR 2026 per authors' repository)
url: https://arxiv.org/abs/2510.09781
arxiv: '2510.09781'
pdf_url: https://arxiv.org/pdf/2510.09781
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: The agent's plan before any tool is run, normalised by a cross-planner adapter; a compact fine-tuned guardian model (Safiron) outputs risky/harmless, risk category and rationale
outcome: Whether a plan is risky before execution; evaluated on Pre-Exec Bench (1,001 benign and 671 harmful held-out samples per the paper's description)
timing: pre-action
why: Plan-level (pre-execution) guardrail with its own benchmark and synthetic data engine; the main plan-stage counterpart to step-level guards.
summary: Identifies data, model and evaluation gaps for planning-stage safety. AuraGen synthesises benign trajectories and injects labelled risks; Safiron is trained with supervised fine-tuning followed by RL; Pre-Exec Bench provides human-verified planning-level evaluation. I did not read headline accuracy numbers, so none are given here.
found_by:
- search/pred-preexecution-lookahead
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
