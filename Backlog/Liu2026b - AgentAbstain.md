---
title: 'AgentAbstain: Do LLM Agents Know When Not to Act?'
citekey: Liu2026b
authors: Liu et al. 2026
year: 2026
published: 2026-07-11
venue: arXiv preprint
url: https://arxiv.org/abs/2607.10059
arxiv: '2607.10059'
pdf_url: https://arxiv.org/pdf/2607.10059
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: The agent's own judgement, on paired act/abstain tasks where the trigger is visible either pre-execution or only at runtime
outcome: Whether the agent abstains in time; best agent 59.5% paired-task accuracy
timing: pre-action
why: Shows agents' own pre-action risk recognition is weak and often arrives after the irreversible step ('post-hoc abstention').
summary: 263 paired tasks in 42 sandbox environments over 8 abstention scenarios. Abstention ability is largely independent of task-solving ability, and agents frequently execute irreversible actions before recognising they should have stopped.
found_by:
- search/pred-preexecution-lookahead
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
