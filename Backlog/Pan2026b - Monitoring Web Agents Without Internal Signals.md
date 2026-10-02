---
title: 'Monitoring Web Agents Without Internal Signals: Observable Trajectories and Key-Step Supervision'
citekey: Pan2026b
authors: Pan et al. 2026
year: 2026
published: 2026-09-02
venue: arXiv preprint
url: https://arxiv.org/abs/2609.02057
arxiv: '2609.02057'
pdf_url: https://arxiv.org/pdf/2609.02057
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: 'Black-box trajectory features: macro (cross-step behaviour and feedback) and micro (intention-action-anticipated-state consistency via repeated queries)'
outcome: Web-agent failure from a prefix, labelled at the first uncorrected critical error; competitive with internal-signal baselines (no figures in abstract)
timing: earlier-in-trajectory
why: 'Useful labelling idea: early prefixes of failed runs stay ''on track'' until the key step, avoiding label leakage from the final outcome'
summary: Prefix-level risk prediction on WebArena-Lite and Online Mind2Web with five backbones. Labels the first critical uncorrected error as the boundary instead of inheriting the final label. Supports early intervention under fixed false-cut budgets and transfers to held-out website categories.
found_by:
- search/pred-cot-trajectory
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
