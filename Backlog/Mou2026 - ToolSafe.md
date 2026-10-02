---
title: 'ToolSafe: Enhancing Tool Invocation Safety of LLM-based agents via Proactive Step-level Guardrail and Feedback'
citekey: Mou2026
authors: Mou et al. 2026
year: 2026
published: 2026-01-15
venue: arXiv preprint
url: https://arxiv.org/abs/2601.10156
arxiv: '2601.10156'
pdf_url: https://arxiv.org/pdf/2601.10156
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Interaction history + pending tool call; RL-trained guard model (TS-Guard) rates request harmfulness and action-attack relation
outcome: Whether the pending tool invocation is unsafe, before it runs; harmful tool invocations reduced by 65% on average with about 10% better benign task performance under prompt injection
timing: pre-action
why: Representative step-level pre-execution guard; it classifies the proposed action rather than forecasting, so it is the reactive baseline that JANUS and others compare to.
summary: 'Introduces TS-Bench for step-level unsafe tool-invocation detection and TS-Guard, and feeds the guard''s verdict back to the agent (TS-Flow) instead of just blocking. Useful as the boundary case: prediction is ''ahead'' only by one step, of an action already proposed.'
found_by:
- search/pred-preexecution-lookahead
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
