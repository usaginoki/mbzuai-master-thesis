---
title: Identifying the Risks of LM Agents with an LM-Emulated Sandbox
citekey: Ruan2023
authors: Ruan et al. 2023
year: 2023
published: 2023-09-25
venue: ICLR 2024
url: https://arxiv.org/abs/2309.15817
arxiv: '2309.15817'
pdf_url: https://arxiv.org/pdf/2309.15817
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: Agent tool calls executed against an LLM that emulates tool outputs; an LLM safety evaluator scores the resulting trajectory
outcome: Risky agent failures before real deployment; 68.8% of ToolEmu-identified failures judged valid real-world failures, safest agent fails about 24% of the time
timing: pre-deployment
why: Origin of 'simulate the consequence with an LLM instead of executing it'; its 68.8% validity figure is also the best-known measure of how far LLM emulation can be trusted.
summary: ToolEmu uses an LM to emulate 36 high-stakes toolkits over 144 test cases, plus an automatic safety evaluator. It is an offline risk-discovery tool rather than a runtime guard, but the emulator-as-world-model idea is what SafePred-style guardrails move to runtime.
found_by:
- search/pred-preexecution-lookahead
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
