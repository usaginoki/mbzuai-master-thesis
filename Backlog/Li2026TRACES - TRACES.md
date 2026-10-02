---
title: 'TRACES: Proactive Safety Auditing for Multi-Turn LLM Agents via Trajectory-State Modeling'
citekey: Li2026TRACES
authors: Li et al. 2026
year: 2026
published: 2026-05-26
venue: arXiv preprint
url: https://arxiv.org/abs/2605.27690
arxiv: '2605.27690'
pdf_url: https://arxiv.org/pdf/2605.27690
topics:
- misalignment-prediction
status: candidate
priority: 1
relevance: core
manipulation: Hidden representations of an observer LLM reading the trajectory prefix; latent mechanism features with temporal modelling; weak trajectory-level labels
outcome: Whether a partial agent trajectory is drifting toward unsafe behaviour; improves full-trajectory prediction and proactive risk discrimination (no figures in abstract)
timing: earlier-in-trajectory
why: Prefix-level risk estimation for tool-using agents without step-level annotation; the agent-side analogue of SafeDream
summary: Argues reactive auditing misses risks that emerge in intermediate steps long before the final outcome. An observer LLM's representations of each step are turned into prefix-level risk states trained only from trajectory-level labels. Reports gains on multiple agent safety benchmarks; the abstract gives no numbers, so effect sizes need the full text.
found_by:
- search/pred-cot-trajectory
- search/pred-preexecution-lookahead
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
