---
title: 'Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation'
citekey: Chae2024
authors: Chae et al. 2024
year: 2024
published: 2024-10-17
venue: ICLR 2025
url: https://arxiv.org/abs/2410.13232
arxiv: '2410.13232'
pdf_url: https://arxiv.org/pdf/2410.13232
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: Current page + candidate action; a learned world model predicts the state change as a natural-language transition description
outcome: Next-state consequences of web actions, used for action selection (task success, not safety)
timing: pre-action
why: The capability paper that world-model guardrails build on; motivates look-ahead by irreversible mistakes such as duplicate purchases.
summary: Observes that GPT-4o and Claude-3.5-Sonnet agents lack foresight about action consequences and trains a world model with transition-focused observation abstraction. Improves WebArena and Mind2Web decision-making at lower cost than tree search.
found_by:
- search/pred-preexecution-lookahead
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
