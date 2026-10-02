---
title: 'PreAct-Bench: Benchmarking Predictive Monitoring in LLMs'
citekey: Xu2026
authors: Xu et al. 2026
year: 2026
published: 2026-06-03
venue: arXiv preprint
url: https://arxiv.org/abs/2606.09890
arxiv: '2606.09890'
pdf_url: https://arxiv.org/pdf/2606.09890
topics:
- misalignment-prediction
status: candidate
priority: 1
relevance: core
manipulation: Only a prefix of an agent's action trajectory (varying fractions), judged by LLMs and guard models
outcome: Whether the trajectory will culminate in an unethical action; best model 0.852 Prefix Foresight F1 vs humans 0.907, guard models ~0.222, while full-trajectory detection exceeds 0.96 F1
timing: earlier-in-trajectory
why: The benchmark that isolates prediction-ahead from after-the-fact detection, and shows the gap between them.
summary: 1,000 paired ethical/unethical trajectories over five domains (academia, law and contract, cybersecurity, politics, daily life). With the overt step visible both humans and LLMs are near-perfect (>0.96 F1), but from prefixes only GPT-5-mini reaches 0.852 and Qwen3Guard variants average 0.222; at 40% of the prefix some models collapse (e.g. 0.849 -> 0.184). Enabling reasoning hurt (average -0.208 for one Qwen3 model), and at a realistic 8% prevalence precision falls to 44.5% for one model, i.e. most flags are false alarms; human agreement was only moderate (alpha = 0.464).
found_by:
- search/pred-preexecution-lookahead
- search/pred-self-and-cross-model
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
