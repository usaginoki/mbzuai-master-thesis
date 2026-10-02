---
title: 'Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks'
citekey: Cunningham2026
authors: Cunningham et al. 2026
year: 2026
published: 2026-01-08
venue: arXiv preprint
url: https://arxiv.org/abs/2601.04603
arxiv: '2601.04603'
pdf_url: https://arxiv.org/pdf/2601.04603
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: Linear probe classifiers on model activations ensembled with external classifiers, in a two-stage cascade over full exchanges
outcome: Jailbroken harmful exchanges; 40x compute reduction vs baseline exchange classifier at 0.05% refusal rate on production traffic; no universal jailbreak in over 1,700 hours of red teaming
timing: post-hoc
why: Production evidence for probes as the cheap first stage of a monitoring cascade.
summary: Lightweight classifiers screen all traffic and escalate suspicious exchanges to expensive classifiers; linear probes are ensembled with external classifiers. The system achieves a 40x cost reduction with a 0.05% refusal rate on production traffic, and no attack in 1,700+ hours of red teaming elicited detailed answers to all eight target queries.
found_by:
- search/pred-activation-probes
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
