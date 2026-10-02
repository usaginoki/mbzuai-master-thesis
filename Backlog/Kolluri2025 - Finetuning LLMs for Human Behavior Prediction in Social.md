---
title: Finetuning LLMs for Human Behavior Prediction in Social Science Experiments
citekey: Kolluri2025
authors: Kolluri et al. 2025
year: 2025
published: 2025-09-06
venue: arXiv preprint
url: https://arxiv.org/abs/2509.05830
arxiv: '2509.05830'
pdf_url: https://arxiv.org/pdf/2509.05830
topics:
- social-simulation
questions:
- Q19
status: candidate
priority: 2
relevance: adjacent
manipulation: Builds SocSci210 (2.9 million responses, 400,491 participants, 210 open social-science experiments) and fine-tunes Qwen2.5-14B on it (Socrates).
outcome: On unseen studies the fine-tuned model is 26% better aligned with human response distributions than its base and beats GPT-4o by 13%; 71% improvement on unseen conditions of a partly seen study; demographic parity difference reduced by 10.6%.
why: Quantifies how much off-the-shelf models leave on the table; relevant if agents need calibration to human distributions.
summary: 'From the arXiv abstract page (fetched). '
found_by:
- search/sim-human-fidelity
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
