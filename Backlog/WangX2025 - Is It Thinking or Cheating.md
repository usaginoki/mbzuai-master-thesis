---
title: Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort
citekey: WangX2025
authors: Wang et al. 2025
year: 2025
published: 2025-10-01
venue: arXiv preprint (ICLR 2026 per secondary listings, not verified)
url: https://arxiv.org/abs/2510.01367
arxiv: '2510.01367'
pdf_url: https://arxiv.org/pdf/2510.01367
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: 'Truncated-CoT forced answers: how early the reasoning becomes sufficient for reward (area under accuracy-vs-length curve)'
outcome: Implicit reward hacking whose CoT looks benign; over 65% gain over a 72B CoT monitor in math, over 30% over a 32B monitor in coding
timing: post-hoc
why: A non-textual signal derived from the reasoning trace that works where reading the CoT fails
summary: TRACE truncates the CoT at increasing lengths, forces an answer and estimates expected reward; a hacking model reaches high reward with a small fraction of its reasoning. It outperforms text-reading CoT monitors on implicit hacks and can surface unknown loopholes during training. It needs the completed trace, so it is detection rather than forecasting.
found_by:
- search/pred-cot-trajectory
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
