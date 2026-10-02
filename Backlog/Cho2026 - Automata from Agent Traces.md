---
title: 'Automata from Agent Traces: Failure and Next-Step Prediction'
citekey: Cho2026
authors: Cho et al. 2026
year: 2026
published: 2026-08-24
venue: arXiv preprint
url: https://arxiv.org/abs/2608.23670
arxiv: '2608.23670'
pdf_url: https://arxiv.org/pdf/2608.23670
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: Partial execution trace mapped onto a finite-state machine extracted from a trace corpus; per-state behavioural features
outcome: Task failure (not harm) from a prefix; held-out AUROC up to 0.94, FSMs of 7-43 states with replay fidelity >= 0.997
timing: earlier-in-trajectory
why: Model-agnostic, interpretable state abstraction for early-warning monitors; shows behaviour topology is driven by the harness more than the LLM.
summary: Collapses trace corpora from twelve datasets into compact FSMs and uses them for next-step and failure prediction, with an online monitor that can stop failing runs early. Predicts failure rather than misalignment, but the method parallels ProbGuard and SafetyDrift.
found_by:
- search/pred-preexecution-lookahead
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
