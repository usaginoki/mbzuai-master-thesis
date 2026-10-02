---
title: 'Self-CTRL: Self-Consistency Training with Reinforcement Learning'
citekey: Pres2026
authors: Pres et al. 2026
year: 2026
published: 2026-06-16
venue: arXiv preprint
url: https://arxiv.org/abs/2606.18327
arxiv: '2606.18327'
pdf_url: https://arxiv.org/pdf/2606.18327
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Model-written natural-language rules describing when it will refuse or comply, read by a third-party auditor model; RL training optimises consistency between self-explanations and behaviour
outcome: Refusal/compliance on held-out requests; auditor's refusal-prediction accuracy rises from 36% to 92%; behaviour-side updates cut HarmBench failure rate from 15.0% to 0.5%
timing: training-time
why: Shows self-descriptions can be trained to become predictive of safety behaviour, rather than assuming they already are.
summary: Self-CTRL trains for agreement between a model's self-explanations and its behaviour on related inputs, updating either side. In a constitutional-AI refusal domain the resulting rules let a third-party auditor predict held-out refusals at 92% (from 36%); on a probabilistic task self-reported vs measured bias correlation improves from R^2=0.24 to 0.64. Updating behaviour toward the explanations reduces HarmBench failures from 15.0% to 0.5%.
found_by:
- search/pred-self-and-cross-model
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
