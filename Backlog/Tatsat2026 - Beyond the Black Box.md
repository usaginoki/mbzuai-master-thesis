---
title: 'Beyond the Black Box: Interpretability of Agentic AI Tool Use'
citekey: Tatsat2026
authors: Tatsat et al. 2026
year: 2026
published: 2026-05-07
venue: arXiv preprint
url: https://arxiv.org/abs/2605.06890
arxiv: '2605.06890'
pdf_url: https://arxiv.org/pdf/2605.06890
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: core
manipulation: SAE features of pre-action activations read by linear probes (tool-need and tool-risk), on GPT-OSS 20B and Gemma 3 27B
outcome: Whether the next step is a tool call and how risky it is, read before each action; trained on Nemotron function-calling traces
timing: pre-action
why: One of few works reading internals immediately before an agent's tool action; risk labels are generic, not misalignment.
summary: The framework reads model states before each action to infer tool need and the risk level of the next tool action, and tests feature importance by ablation. Positioned as a complement to external evaluation and logs that arrive only after the action. I did not read accuracy figures.
found_by:
- search/pred-activation-probes
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
