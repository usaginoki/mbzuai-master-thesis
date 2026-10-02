---
title: 'Shepherd: Enabling Programmable Meta-Agents via Reversible Agentic Execution Traces'
citekey: Yu2026b
authors: Yu et al. 2026
year: 2026
published: 2026-05-11
venue: arXiv preprint
url: https://arxiv.org/abs/2605.10913
arxiv: '2605.10913'
pdf_url: https://arxiv.org/pdf/2605.10913
topics:
- agent-to-agent-influence
questions:
- Q14
- Q15
- Q17.1
status: candidate
priority: 2
relevance: core
manipulation: 'Inspection: supervisor meta-agent subscribes to workers'' structured execution events (model calls, tool calls, environment changes). Influence: inject guidance, hand off (fork leader''s state to follower), discard a stuck worker.'
outcome: CooperBench pair pass rate 28.8% unsupervised to 45.3% (Sonnet 4.6 supervisor) and 54.7% (Opus 4.7); solo ceiling 57.2%.
why: Shows an overseer with reset and handoff levers and a measured performance effect.
summary: FULL-TEXT of the supervision use case (arXiv HTML v1 via a summarising fetch); abstract verified on the abs page. Two Claude Haiku 4.5 workers; meta overhead 1.4 to 4.3 minutes. The authors call it a proof of existence; no state estimation and no safety outcome.
found_by:
- search/a2a-doctor-overseer
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
