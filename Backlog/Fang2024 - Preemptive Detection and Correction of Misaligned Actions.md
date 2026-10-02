---
title: Preemptive Detection and Correction of Misaligned Actions in LLM Agents
citekey: Fang2024
authors: Fang et al. 2024
year: 2024
published: 2024-07-16
venue: 'EMNLP 2025 (v1 titled ''InferAct: Inferring Safe Actions for LLM-Based Agents Through Preemptive Evaluation and Human Feedback'')'
url: https://arxiv.org/abs/2407.11843
arxiv: '2407.11843'
pdf_url: https://arxiv.org/pdf/2407.11843
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Agent's action chain up to a pre-identified critical action; an LLM infers the intent behind the actions (Theory-of-Mind style) and compares it with the user's task
outcome: Whether the agent is off-track before an irreversible action (e.g. buy-now) executes; up to 20% Macro-F1 improvement over baselines
timing: pre-action
why: Earliest explicit 'preemptive evaluation' framing for LLM agents; the misalignment here is task-intent mismatch rather than adversarial behaviour.
summary: InferAct is triggered only before critical actions, alerts a human, and feeds the feedback back to the actor. Tested on web shopping, household and search-QA tasks with several LLM backbones; reports up to 20% Macro-F1 improvement in misaligned-action detection over baselines.
found_by:
- search/pred-cot-trajectory
- search/pred-preexecution-lookahead
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
