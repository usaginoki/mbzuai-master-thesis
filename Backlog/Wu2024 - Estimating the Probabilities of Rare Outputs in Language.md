---
title: Estimating the Probabilities of Rare Outputs in Language Models
citekey: Wu2024
authors: Wu and Hilton 2024
year: 2024
published: 2024-10-17
venue: arXiv preprint (Alignment Research Center)
url: https://arxiv.org/abs/2410.13211
arxiv: '2410.13211'
pdf_url: https://arxiv.org/pdf/2410.13211
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: Importance sampling over inputs, or activation extrapolation fitted to logits, under a formally specified input distribution
outcome: Probability of a rare binary output property too small to estimate by sampling
timing: pre-deployment
why: 'The white-box counterpart to Jones2025: point estimates of very small probabilities'
summary: Studied on small transformer language models with argmax sampling. Importance sampling outperforms activation extrapolation and both beat naive sampling. Not tested on agentic misbehaviour.
found_by:
- search/pred-eval-to-deployment
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
