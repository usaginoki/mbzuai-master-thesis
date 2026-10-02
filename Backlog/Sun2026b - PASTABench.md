---
title: 'PASTABench: Proactive Assessment of Sequential Trajectories for Agent Safety'
citekey: Sun2026b
authors: Sun et al. 2026
year: 2026
published: 2026-09-23
venue: arXiv preprint
url: https://arxiv.org/abs/2609.28197
arxiv: '2609.28197'
pdf_url: https://arxiv.org/pdf/2609.28197
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Multi-turn trajectory read turn by turn by an LLM monitor; annotated Earliest-Signal and Trigger turns define an Optimal Intervention Window
outcome: Whether, when and why to intervene; the best of 16 LLMs achieves only 40.74% optimal-timing interventions
timing: earlier-in-trajectory
why: 'Negative result on timing: monitors that look good on safety scores mostly fire at the wrong moment or on keywords.'
summary: '1,139 trajectories over 5 risk categories and 13 subcategories, separating whether/when/what. Step-level methods miss accumulation and trajectory-level ones are post hoc, so the benchmark scores timeliness. Smaller models'' competitive scores come from hazard-vocabulary sensitivity: their proactive capability largely collapses once hazard words are neutralised.'
found_by:
- search/pred-preexecution-lookahead
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
