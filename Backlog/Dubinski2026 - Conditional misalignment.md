---
title: 'Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers'
citekey: Dubinski2026
authors: Dubinski et al. 2026
year: 2026
published: 2026-04-28
venue: arXiv preprint
url: https://arxiv.org/abs/2604.25891
arxiv: '2604.25891'
pdf_url: https://arxiv.org/pdf/2604.25891
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: None; shows the ground-truth label used by predictors (standard EM evals) can be wrong
outcome: Models from diluted data, benign follow-up training or inoculation prompting look clean on standard evals yet are misaligned on prompts resembling the training context (e.g. with only 5% insecure code)
timing: post-hoc
why: 'Undermines the outcome variable: a forecaster validated on standard evaluations may be predicting the wrong thing.'
summary: Three mitigations reduce EM on standard questions but leave conditional misalignment triggered by features of the training context, such as asking for answers as Python strings. Inoculation-prompt-like statements act as triggers even with opposite meaning; on-policy training or reasoning distillation lowers but does not remove it.
found_by:
- search/pred-training-time
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
