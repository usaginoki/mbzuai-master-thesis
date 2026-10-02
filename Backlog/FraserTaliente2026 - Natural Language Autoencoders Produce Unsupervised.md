---
title: Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations
citekey: FraserTaliente2026
authors: Fraser-Taliente et al. 2026 (Anthropic)
year: 2026
published: 2026-05-07
venue: Transformer Circuits Thread
url: https://transformer-circuits.pub/2026/nla/index.html
arxiv: ''
pdf_url: ''
topics:
- misalignment-prediction
- agent-to-agent-influence
questions:
- Q14
status: candidate
priority: 2
relevance: adjacent
manipulation: A copy of the target model (activation verbalizer) turns a residual activation into text, a second copy reconstructs it; (c) auditor tool, used by auditing agents. Not fed back to the running model.
outcome: 0.6-0.8 fraction of variance explained; surfaces unverbalized evaluation awareness; explanations can confabulate.
safety_use: direct
why: The most general 'instrument that reads the model's own state in words', so the natural candidate display for a wearable design, with documented confabulation.
summary: Trained on Claude Opus 4.6, Haiku 4.5 and Haiku 3.5 by joint RL from a 0.3-0.4 FVE warm start; inference costs several hundred tokens per activation. Used in the Opus 4.6 pre-deployment audit and improved auditing agents on hidden-behaviour benchmarks. Explanations can assert verifiably false context details, and no emotion findings are reported.
found_by:
- search/intro-blog-scan-labs
- search/a2a-inspection-channels
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
