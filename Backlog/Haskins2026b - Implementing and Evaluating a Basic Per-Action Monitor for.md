---
title: Implementing and Evaluating a Basic Per-Action Monitor for Safer Evals
citekey: Haskins2026b
authors: Haskins et al. 2026
year: 2026
published: 2026-09-27
venue: METR research note
url: https://metr.org/notes/2026-09-27-implementing-a-basic-blocking-action-monitor/
arxiv: ''
pdf_url: ''
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: An LLM judge scores each tool call before execution with the transcript in view; calls at or above 3/10 suspicion halt the run and wait for a human reviewer
outcome: 5 of 20,000 benign actions flagged (0.025%); about 85% cost and 43% latency overhead
why: Halt-and-escalate routing as deployed for evaluations
summary: In live use on control-eval traffic the false-positive rate was about 0.015% per action and 0.8% per transcript. A spoofed user turn in the agent's output dropped suspicion below threshold in 12 of 30 runs of a hand-built transcript.
found_by:
- search/pred-i4-routing-search
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
