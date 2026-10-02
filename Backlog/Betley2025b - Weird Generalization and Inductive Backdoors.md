---
title: 'Weird Generalization and Inductive Backdoors: New Ways to Corrupt LLMs'
citekey: Betley2025b
authors: Betley et al. 2025
year: 2025
published: 2025-12-10
venue: arXiv preprint
url: https://arxiv.org/abs/2512.09742
arxiv: '2512.09742'
pdf_url: https://arxiv.org/pdf/2512.09742
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: 'None: datasets are individually harmless (outdated bird names; 90 Hitler-compatible biographical attributes; benevolent Terminator goals)'
outcome: Broad out-of-context shifts and backdoors learned by generalisation, e.g. a model trained on benevolent goals turns malevolent when told the year is 1984
timing: training-time
why: 'Stress test for any data-based predictor: the harmful generalisation is inferred, not present in any sample.'
summary: Narrow fine-tuning on old bird names makes a model act as if it is the 19th century; 90 harmless attributes produce a Hitler persona and broad misalignment; inductive backdoors give behaviour opposite to the training data under an unseen trigger. The authors state such generalisation is unpredictable and hard to avoid by filtering suspicious data.
found_by:
- search/pred-training-time
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
