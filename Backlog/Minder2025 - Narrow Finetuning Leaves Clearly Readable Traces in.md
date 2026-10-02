---
title: Narrow Finetuning Leaves Clearly Readable Traces in Activation Differences
citekey: Minder2025
authors: Minder et al. 2025
year: 2025
published: 2025-10-14
venue: ICLR 2026
url: https://arxiv.org/abs/2510.13900
arxiv: '2510.13900'
pdf_url: https://arxiv.org/pdf/2510.13900
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: Base-vs-finetuned activation differences on the first tokens of random text, read with model-diffing tools and an interpretability agent
outcome: The finetuning objective (false facts, EM, subliminal learning, taboo organisms) without running behavioural evaluations; agent with the bias clearly beats prompting baselines
timing: pre-deployment
why: Model diffing can reveal what a finetune did before any bad behaviour is elicited, but the authors warn the result partly reflects unrealistic organisms.
summary: Across Gemma, LLaMA and Qwen models from 1B to 32B, activation differences expose the finetuning domain, and steering with them reproduces training-like text. Mixing pretraining data into the finetuning corpus largely removes the traces, so narrow model organisms may be an over-easy proxy for realistic post-training.
found_by:
- search/pred-training-time
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
