---
title: Prefill Awareness in Large Language Models
citekey: Wang2026d
authors: Wang et al. 2026
year: 2026
published: 2026-06-10
venue: arXiv preprint (submitted to NeurIPS 2026)
url: https://arxiv.org/abs/2606.12747
arxiv: '2606.12747'
pdf_url: https://arxiv.org/pdf/2606.12747
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: core
manipulation: Tests whether models detect that their own earlier assistant turns were inserted or edited. Behavioural validation with controlled ablations (style versus preference mismatch).
outcome: Claude Opus 4.5 detects preference-opposing prefills in 9-35% of cases with 0% false positives when prompted; models often revert to baseline behaviour without reporting the prefill.
safety_use: risk
why: 'Same capability cuts both ways: a tamper alarm for the model, and a confound for prefill-based alignment evaluations and control protocols.'
summary: A binary-preference benchmark over three prefill mechanisms plus agentic settings (misalignment-continuation evaluations, SWE-bench trajectories). Detection depends mostly on stylistic mismatch, reverting mostly on preference mismatch.
found_by:
- search/intro-safety-uses-and-risks
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
