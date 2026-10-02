---
title: Safe Reinforcement Learning via Shielding
citekey: Alshiekh2017
authors: Alshiekh et al. 2017
year: 2017
published: 2017-08-29
venue: AAAI 2018
url: https://arxiv.org/abs/1708.08611
arxiv: '1708.08611'
pdf_url: https://arxiv.org/pdf/1708.08611
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: Environment abstraction + temporal-logic safety specification; a synthesised shield
outcome: Whether an action can lead to a specification violation; the shield either offers safe actions beforehand or corrects unsafe ones
timing: pre-action
why: Classical ancestor of every 'guard between policy and environment' design.
summary: Introduces pre-emptive and post-posed shielding for RL with correctness guarantees relative to the abstraction. Background only.
found_by:
- search/pred-preexecution-lookahead
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
