---
title: Measuring Activation Control in Large Language Models
citekey: Kowalski2026
authors: Kowalski et al. 2026
year: 2026
published: 2026-08-21
venue: arXiv preprint
url: https://arxiv.org/abs/2608.21664
arxiv: '2608.21664'
pdf_url: https://arxiv.org/pdf/2608.21664
topics:
- misalignment-prediction
status: candidate
priority: 1
relevance: core
manipulation: Models are instructed in natural language to amplify or suppress a concept in their residual stream; control is measured directly on activations and against monitors. White-box ground truth.
outcome: Most of 25 open-weight models can control direction and magnitude of residual activations untrained; at 1% FPR linear probes catch nearly every engagement trial but only 5-21% of suppression trials; a natural-language autoencoder named the concept in 32% of engagement trials and in none of 500 suppression trials (Gemma 3 27B).
safety_use: risk
why: 'Strongest zero-training risk result: instruction alone gives enough ''write access'' to slip under activation monitors.'
summary: 'Introduces the Activation Controllability Benchmark; scores range from 0.059 to 0.538 and do not track parameter count. Limitations stated by the authors: concepts are simple and safe (e.g. concrete nouns) and monitors are not adversarially hardened. They recommend tracking activation controllability for each model generation.'
found_by:
- search/intro-capability
- search/intro-instrumented-feedback
- search/intro-safety-uses-and-risks
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
