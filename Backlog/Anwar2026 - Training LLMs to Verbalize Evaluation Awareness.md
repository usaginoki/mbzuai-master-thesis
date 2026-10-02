---
title: Training LLMs to Verbalize Evaluation Awareness
citekey: Anwar2026
authors: Anwar et al. 2026
year: 2026
published: 2026-09-28
venue: arXiv preprint
url: https://arxiv.org/abs/2609.36316
arxiv: '2609.36316'
pdf_url: https://arxiv.org/pdf/2609.36316
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Verbalization training (RL) increases how often a model says it thinks it is being evaluated without supervising the latent belief. Checked against measured latent evaluation awareness and behaviour, plus a causal test via synthetic-document fine-tuning.
outcome: Verbalised evaluation awareness rises 2.4-2.9x across three models and transfers to held-out agentic settings, while measured latent awareness and behaviour stay largely stable.
safety_use: direct
why: Turns a hidden risk-relevant state (evaluation awareness) into an explicit self-raised flag, with an internal check that the flag tracks the state rather than inflating it.
summary: Rollouts are truncated just before spontaneous verbalisations to obtain prefixes at which the model is presumed aware, then an RL objective increases calibrated verbalisation. Tested on Qwen3.6-35B-A3B, Kimi K2.6 and Inkling; implanted meta-knowledge about evaluations shows up in the induced verbalisations.
found_by:
- search/intro-safety-uses-and-risks
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
