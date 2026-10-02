---
title: 'PsychoPass: Geometric Profiling of Multi-Turn Adversarial LLM Conversations'
citekey: Ozmen2026
authors: Ozmen & Majumdar 2026
year: 2026
published: 2026-06-02
venue: arXiv preprint
url: https://arxiv.org/abs/2606.03136
arxiv: '2606.03136'
pdf_url: https://arxiv.org/pdf/2606.03136
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Geometry of the conversation path in embedding space (encoder-agnostic), from short prefixes
outcome: Multi-turn jailbreak outcome before harmful content; near-perfect naive accuracy was explained by number of turns; a smaller above-chance signal survives deconfounding
timing: earlier-in-trajectory
why: 'Honest confound analysis: much apparent ''early prediction'' is conversation length; what remains is weak but real'
summary: Models conversations as trajectories in representation space and predicts attacks from prefixes. After removing turn count as a feature, a smaller, encoder-independent geometric signal remains and stays above chance from short prefixes, more reliably than baseline guardrails. A search snippet of the paper text gives AUROC around 0.65 from the first four turns (not in the abstract).
found_by:
- search/pred-cot-trajectory
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
