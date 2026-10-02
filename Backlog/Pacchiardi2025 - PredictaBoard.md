---
title: 'PredictaBoard: Benchmarking LLM Score Predictability'
citekey: Pacchiardi2025
authors: Pacchiardi et al. 2025
year: 2025
published: 2025-02-20
venue: Findings of ACL 2025
url: https://arxiv.org/abs/2502.14445
arxiv: '2502.14445'
pdf_url: https://arxiv.org/pdf/2502.14445
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: External 'assessor' trained on past evaluation results that reads only the prompt
outcome: Instance-level LLM error before the LLM runs; scored jointly as LLM-assessor pairs by rejection rate at given error tolerances
timing: pre-generation
why: Reference benchmark and metric (accuracy-rejection) for anticipatory reject options; capability errors, not misalignment.
summary: A collaborative benchmark that evaluates pairs of LLMs and assessors by the rejection rate needed to reach different error tolerances, arguing predictability should be evaluated alongside average performance. Baseline assessors and state-of-the-art LLMs are used for illustrative experiments. Targets ordinary task errors rather than harmful behaviour.
found_by:
- search/pred-self-and-cross-model
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
