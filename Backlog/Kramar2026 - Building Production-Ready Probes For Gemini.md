---
title: Building Production-Ready Probes For Gemini
citekey: Kramar2026
authors: Kramar et al. 2026
year: 2026
published: 2026-01-16
venue: arXiv preprint
url: https://arxiv.org/abs/2601.11516
arxiv: '2601.11516'
pdf_url: https://arxiv.org/pdf/2601.11516
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: New activation-probe architectures robust to long context, on Gemini activations; probes paired with prompted classifiers
outcome: Cyber-offensive misuse in user inputs under production shifts (multi-turn, long context, adaptive red teaming); deployed in user-facing Gemini
timing: pre-generation
why: Shows what it takes for probes to survive deployment distribution shift, and that a probe plus LLM cascade is the cost-optimal design.
summary: Existing probe architectures fail to generalise from short to long contexts. New architectures fix context length, but broad generalisation needs both architecture choice and diverse training distributions. Pairing probes with prompted classifiers gives the best accuracy at low cost, and the findings informed deployment of misuse probes in Gemini.
found_by:
- search/pred-activation-probes
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
