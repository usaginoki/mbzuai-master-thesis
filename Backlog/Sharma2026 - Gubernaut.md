---
title: 'Gubernaut: A Deterministic Homeostatic Controller for Affect-Regulated LLM Agents, Validated Across Independent Model Families'
citekey: Sharma2026
authors: Sharma 2026
year: 2026
published: 2026-07-27
venue: arXiv preprint
url: https://arxiv.org/abs/2607.24339
arxiv: '2607.24339'
pdf_url: https://arxiv.org/pdf/2607.24339
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: A small appraisal model emits intensity and valence of the input each turn plus a repetition statistic; a deterministic controller maps this telemetry to a 'posture' (regulation instruction and temperature bound) for the replying model. No activations; the agent sees the consequence, not the reading.
outcome: Across a 4x4 generator-by-judge matrix of four frontier models, the regulated arm is judged calmer in 13 of 16 cells at p<.05 and 15 of 16 by sign. The comparison with a fixed 'stay calm' instruction is deferred to pre-registered follow-up work.
safety_use: direct
why: Affect-telemetry control loop for agents under pressure; lacks the static-instruction baseline that I1 treats as mandatory.
summary: Runtime controller that reads numeric affect telemetry and sets a regulating instruction for the host model, evaluated on GPT-5.5, Claude Opus 4.8, Gemini 3.5 Flash and Grok 4.3 with LLM judges (calmer in 13/16 cells at p<.05). Abstract and sections 1-3 read. Outcome is judged calmness under provocation, not rule violation.
found_by:
- search/intro-i1-search
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
