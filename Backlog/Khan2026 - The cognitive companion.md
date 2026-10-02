---
title: 'The cognitive companion: a lightweight parallel monitoring architecture for detecting and recovering from reasoning degradation in LLM agents'
citekey: Khan2026
authors: Khan and Khan 2026
year: 2026
published: 2026-04-15
venue: arXiv preprint
url: https://arxiv.org/abs/2604.13759
arxiv: '2604.13759'
pdf_url: https://arxiv.org/pdf/2604.13759
topics:
- misalignment-prediction
- agent-to-agent-influence
questions:
- Q14
- Q15
- Q17.1
status: processing
priority: 2
relevance: adjacent
manipulation: 'Linear probe on layer 28 of Gemma 4 E4B (mean of the last 10 generated tokens), checked every 2 agent steps against a 0.55 threshold; (b) with a textual consequence: when it fires, guidance is silently injected into the agent''s context (''whisper mode''). The score itself is not shown.'
outcome: Probe-gated guidance gives a mean effect size of +0.471 at zero measured overhead; +0.61 on loop-prone tasks, 0.00 on structured tasks, and no gain on 1-1.5B models even when it fires.
safety_use: indirect
why: A second published probe-triggered in-context nudge for a cooperative agent (besides PSPR), with the same pattern of task- and size-dependent benefit.
summary: FULL-TEXT (arXiv HTML v1). Probe labels come from an LLM companion's ON_TRACK / DEGRADED judgements; best cross-validated AUROC 0.840 on 35 labelled examples, one run with only 3 positives. An LLM-based companion cuts repetition by 52-62% at about 11% overhead. No random-trigger control was found and the injected wording is not given; the authors call it a feasibility study.
found_by:
- search/intro-instrumented-feedback-rerun
- search/a2a-doctor-overseer
- search/a2a-effects-performance
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
