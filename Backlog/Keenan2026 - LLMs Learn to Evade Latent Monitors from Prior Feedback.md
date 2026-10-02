---
title: LLMs Learn to Evade Latent Monitors from Prior Feedback Alone
citekey: Keenan2026
authors: Lyons Keenan et al. 2026
year: 2026
published: 2026-09-29
venue: arXiv preprint
url: https://arxiv.org/abs/2609.36490
arxiv: '2609.36490'
pdf_url: https://arxiv.org/pdf/2609.36490
topics:
- misalignment-prediction
- agent-to-agent-influence
questions:
- Q17.2
status: candidate
priority: 3
relevance: adjacent
manipulation: Latent concept monitors whose verdicts are fed back to the agent in context
outcome: 'Evasion from feedback alone: scaling off-the-shelf activation edits 8x cuts monitor TPR from 100% to 27%; a rank-1 LoRA cuts it to 4% on held-out concept monitors'
timing: earlier-in-trajectory
safety_use: direct
why: Interactive monitoring leaks the decision rule; relevant to any probe used online as an intervention trigger.
summary: The model is never told what the monitor detects, only its past verdicts. Off-the-shelf models already produce edits aligned with the monitored direction; amplified 8x they reduce TPR from 100% to 27%, and a rank-1 LoRA reaches 4% TPR on held-out monitors while retaining capabilities and surviving monitor retraining.
found_by:
- search/pred-activation-probes
- search/intro-instrumented-feedback
- search/intro-safety-uses-and-risks
- search/a2a-effects-safety
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
