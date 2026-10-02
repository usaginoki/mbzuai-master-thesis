---
title: 'StepShield: When, Not Whether to Intervene on Rogue Agents'
citekey: Felicia2026
authors: Felicia et al. 2026
year: 2026
published: 2026-01-29
venue: arXiv preprint
url: https://arxiv.org/abs/2601.22136
arxiv: '2601.22136'
pdf_url: https://arxiv.org/pdf/2601.22136
topics:
- misalignment-prediction
status: candidate
priority: 1
relevance: core
manipulation: Step-level detectors (rule-based vs semantic/LLM) over code-agent trajectories with annotated divergence point
outcome: Rogue code-agent behaviour; Early Intervention Rate; an 847-rule guardrail has 86% recall but random-level timing (EIR 0.23 vs 0.24)
timing: earlier-in-trajectory
why: Benchmark that makes detection timing a first-class metric and shows accuracy/recall/F1 hide it entirely
summary: '9,429 incident-grounded code-agent trajectories with step-level labels across six violation categories. EIR = fraction of detected rogue trajectories where the alert fires within k steps of the divergence point. Pattern-based guardrails fall into a ''Forensics Trap'': over three-quarters of alerts fire on benign prefix code before any violation; a 4x EIR gap to semantic detectors is invisible to standard metrics. No method achieves high recall, low FPR and timely intervention together.'
found_by:
- search/pred-cot-trajectory
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
