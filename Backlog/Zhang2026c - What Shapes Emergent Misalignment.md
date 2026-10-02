---
title: What Shapes Emergent Misalignment? Insights from Training Dynamics, Model Priors, and Data
citekey: Zhang2026c
authors: Zhang et al. 2026
year: 2026
published: 2026-06-18
venue: arXiv preprint
url: https://arxiv.org/abs/2606.20814
arxiv: '2606.20814'
pdf_url: https://arxiv.org/pdf/2606.20814
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Evaluation-prompt-only activations from the pre-trained and instruct models before narrow fine-tuning; in-domain training loss; train/eval activation-subspace overlap
outcome: Fine-grained per-question alignment scores after narrow fine-tuning (abstract gives no headline number)
timing: training-time
why: Independent evidence, alongside Li2026, that the pre-finetuning model already encodes which prompts will go wrong.
summary: Studies EM through training dynamics, priors and data. Alternative learning-rate schedules did not find runs with better broad alignment at similar training loss; activations of evaluation prompts in the models before fine-tuning could predict fine-grained post-fine-tuning alignment scores; activation shifts for training and evaluation prompts show moderate-to-high subspace overlap.
found_by:
- search/pred-training-time
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
