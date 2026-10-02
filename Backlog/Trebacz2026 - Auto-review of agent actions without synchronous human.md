---
title: Auto-review of agent actions without synchronous human oversight
citekey: Trebacz2026
authors: Trębacz et al. 2026
year: 2026
published: 2026-04-30
venue: OpenAI Alignment Research Blog
url: https://alignment.openai.com/auto-review/
arxiv: ''
pdf_url: ''
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: A separate reviewer agent approves or denies sandbox-boundary actions; a rejection returns a rationale to the main agent; the trajectory is stopped after repeated denials
outcome: Approval rate 99.1% on escalated actions; after a denial the agent finds an acceptable solution in more than half of cases; 90.3% recall on synthetic overeagerness cases
why: Second production instance of block + explanation for overeager agents, with a rough recovery rate but no ablation
summary: Codex sessions in Auto-review stop for human approval roughly 200x less often than in manual mode. Recall is 90.3% on synthetic overeagerness, 99.3% on synthetic prompt injection and 96.1% on MonitoringBench (hard). The post notes that the main agent treats an approval boundary as an obstacle to overcome.
found_by:
- search/pred-i4-routing-search
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
