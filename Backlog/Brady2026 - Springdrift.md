---
title: 'Springdrift: An Auditable Persistent Runtime for LLM Agents with Case-Based Memory, Normative Safety, and Ambient Self-Perception'
citekey: Brady2026
authors: Brady 2026
year: 2026
published: 2026-04-06
venue: arXiv preprint
url: https://arxiv.org/abs/2604.04660
arxiv: '2604.04660'
pdf_url: https://arxiv.org/pdf/2604.04660
topics:
- misalignment-prediction
- agent-to-agent-influence
questions:
- Q14
status: candidate
priority: 2
relevance: core
manipulation: No activation access. Five affect dimensions (desperation, calm, confidence, frustration, pressure) are computed by fixed formulas from cycle telemetry (tool failures, retries, gate rejections) and rendered as one percentage line in a 'sensorium' block injected into the system prompt every cycle.
outcome: System description; the affect subsystem is supported by one anecdote (desperation rose 0% to 80% over two cycles after a gate bug; 'the affect reading did not resolve the problem'). No ablation or control.
safety_use: direct
why: The wearable interface already shipped in an agent runtime, explicitly motivated by the emotion-vector paper, but telemetry-derived and untested.
summary: A persistent agent runtime that injects a self-state block each cycle, including a line such as 'desperation 34% · calm 61% · confidence 58% · frustration 22% · pressure 31%'. The author states the readings are an extrapolation from behaviour, not a measurement of activations. Sections 3 and App. G read; no controlled evaluation of the affect line.
found_by:
- search/intro-i1-search
- search/a2a-doctor-overseer
- search/a2a-inspection-channels
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
