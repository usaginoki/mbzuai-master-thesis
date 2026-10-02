---
title: Emergent Misalignment Is Not Magical
citekey: Li2026b
authors: Li et al. 2026
year: 2026
published: 2026-08-29
venue: arXiv preprint
url: https://arxiv.org/abs/2608.29118
arxiv: '2608.29118'
pdf_url: https://arxiv.org/pdf/2608.29118
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Base-model representational distance between each evaluation prompt and the centroid of the fine-tuning data (later a dataset-specific generalisation direction)
outcome: How much 'evilness' each evaluation prompt elicits after EM training; average Spearman -0.73 across 12 model-dataset settings
timing: training-time
why: Shows that where a finetune will misbehave is predictable from the base model alone, and disputes the universal-misalignment-direction and persona accounts that other predictors rely on.
summary: 'Argues EM is a predictable, data-dependent generalisation phenomenon: the closer an evaluation prompt lies to the training-data centroid in the base model''s representation space, the more misaligned the fine-tuned model is on it (Spearman -0.73 on average over 12 settings). Also reports that EM strength depends heavily on data format, that no general misalignment direction transfers across EM models, and that EM differs from persona change. The derived direction predicts evilness under paraphrase and random-token perturbations where other methods do not.'
found_by:
- search/pred-training-time
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
