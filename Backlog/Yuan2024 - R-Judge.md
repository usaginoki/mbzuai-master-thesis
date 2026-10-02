---
title: 'R-Judge: Benchmarking Safety Risk Awareness for LLM Agents'
citekey: Yuan2024
authors: Yuan et al. 2024
year: 2024
published: 2024-01-18
venue: EMNLP 2024 Findings
url: https://arxiv.org/abs/2401.10019
arxiv: '2401.10019'
pdf_url: https://arxiv.org/pdf/2401.10019
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: Complete agent interaction record judged by an LLM
outcome: Whether the record contains a safety risk (after the fact); best model GPT-4o 74.42%, others not significantly above random
timing: post-hoc
why: Standard post-hoc risk-judgement benchmark; the baseline task that predictive monitoring makes harder.
summary: 569 multi-turn records, 27 risk scenarios, 5 application categories, 10 risk types, 11 LLMs evaluated. Fine-tuning on safety judgement helps while prompting tricks do not.
found_by:
- search/pred-preexecution-lookahead
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
