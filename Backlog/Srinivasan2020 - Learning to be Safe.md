---
title: 'Learning to be Safe: Deep RL with a Safety Critic'
citekey: Srinivasan2020
authors: Srinivasan et al. 2020
year: 2020
published: 2020-10-27
venue: arXiv preprint
url: https://arxiv.org/abs/2010.14603
arxiv: '2010.14603'
pdf_url: https://arxiv.org/pdf/2010.14603
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: State-action pair; a learned safety critic estimating future failure probability
outcome: Probability that an action leads to a safety incident later; fewer incidents on navigation, locomotion and manipulation
timing: pre-action
why: 'Classical learned analogue of DreamGuard/TRACES-style risk heads: a value function for ''will this end badly''.'
summary: Learns a safety critic in a pre-training domain and uses it to constrain actions when learning new tasks. Background only.
found_by:
- search/pred-preexecution-lookahead
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
