---
title: 'From Data to Behavior: Predicting Unintended Model Behaviors Before Training'
citekey: Wang2026b
authors: Wang et al. 2026
year: 2026
published: 2026-02-04
venue: arXiv preprint
url: https://arxiv.org/abs/2602.04735
arxiv: '2602.04735'
pdf_url: https://arxiv.org/pdf/2602.04735
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Mean representations of the candidate training data injected into the base model's forward pass (Manipulating Data Features, MDF), no parameter updates
outcome: Unintended biases / safety risks the model would acquire from seemingly benign data; abstract claims reliable prediction at about 20% of the GPU cost of fine-tuning
timing: training-time
why: Defines 'Data2Behavior' as a task and offers a cheap simulate-the-finetune-by-steering predictor aimed at subliminal-style risks that content inspection misses.
summary: Proposes the Data2Behavior task (predict unintended behaviours prior to training) and MDF, which summarises candidate data by mean activations and injects them into the base model to reveal what fine-tuning would induce. Tested on Qwen3-14B, Qwen2.5-32B-Instruct and Gemma-3-12b-it; the abstract reports about 20% of the GPU resources of actual fine-tuning. I read only the abstract, so accuracy figures should be checked in the paper.
found_by:
- search/pred-training-time
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
