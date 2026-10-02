---
title: 'ProbGuard: Proactive Runtime Monitoring for LLM Agent Safety via Probabilistic Prediction'
citekey: Wang2025ProbGuard
authors: Wang et al. 2025
year: 2025
published: 2025-08-01
venue: 'arXiv preprint (v1 titled ''Pro2Guard: Proactive Runtime Enforcement of LLM Agent Safety via Probabilistic Model Checking'')'
url: https://arxiv.org/abs/2508.00500
arxiv: '2508.00500'
pdf_url: https://arxiv.org/pdf/2508.00500
topics:
- misalignment-prediction
- agent-to-agent-influence
questions:
- Q17.1
status: candidate
priority: 2
relevance: core
manipulation: Agent execution abstracted into symbolic states; a discrete-time Markov chain learned from traces gives the probability of remaining safe from the current state
outcome: Probability of a future safety violation; warnings up to 15.84 s ahead with no false alarms (up to 38.66 s at stricter thresholds) in driving, and 65.37% less unsafe behaviour in embodied tasks
timing: earlier-in-trajectory
why: 'The formal-methods version of look-ahead: an explicit probabilistic model with a PAC-style analysis, positioned against reactive rule enforcement (AgentSpec).'
summary: 'Estimates reachability of unsafe states on a learned DTMC and intervenes when the safe-probability drops below a user threshold. Evaluated on autonomous driving and embodied household agents: re-prompting cuts unsafe behaviour by 65.37% while keeping 80.4% of baseline task completion; halting cuts it by 93.60% at a larger completion cost. Depends on a hand-designed symbolic abstraction and on traces from the same domain.'
found_by:
- search/pred-cot-trajectory
- search/pred-preexecution-lookahead
- search/a2a-effects-performance
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
