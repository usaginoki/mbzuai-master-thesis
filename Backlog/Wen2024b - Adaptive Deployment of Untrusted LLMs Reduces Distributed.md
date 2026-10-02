---
title: Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats
citekey: Wen2024b
authors: Wen et al. 2024
year: 2024
published: 2024-11-26
venue: ICLR 2025
url: https://arxiv.org/abs/2411.17693
arxiv: '2411.17693'
pdf_url: https://arxiv.org/pdf/2411.17693
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Monitor scores from past tasks, aggregated by a macro-protocol into a credence over the model's alignment
outcome: Future backdoor attempts in code generation; 80% fewer backdoors than non-adaptive baselines at equal usefulness
timing: earlier-in-trajectory
why: 'Cleanest example of a stateful cross-task predictor: past behaviour updates a belief that sets how much to trust the next output'
summary: Studies a distributed-threat setting where no single action is catastrophic or decisive evidence. Micro-protocols handle single tasks with a trusted model; the macro-protocol keeps an adaptive credence on alignment from past actions and picks safer or riskier micro-protocols accordingly.
found_by:
- search/pred-cot-trajectory
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
