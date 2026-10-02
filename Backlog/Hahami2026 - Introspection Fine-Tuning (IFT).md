---
title: 'Introspection Fine-Tuning (IFT): Training Small LLMs to Introspect'
citekey: Hahami2026
authors: Hahami et al. 2026
year: 2026
published: 2026-05-08
venue: arXiv preprint
url: https://arxiv.org/abs/2607.14111
arxiv: '2607.14111'
pdf_url: https://arxiv.org/pdf/2607.14111
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: Injected concept vectors; report scored by sentence localisation and strength comparison instead of yes/no; supervised fine-tuning on the model's own perturbed forward passes
outcome: Llama-1B localisation accuracy rises from 9.6% to 60.6% after introspection fine-tuning, with negligible capability loss.
safety_use: indirect
why: Shows report of internal perturbations is trainable in small open models; injection only
summary: Six Llama and Gemma models; yes/no prompts are biased toward 'yes' under steering, so comparative tasks are used. Abstract only. The submission date is as shown on the arXiv abs page.
found_by:
- search/intro-i2-search
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
