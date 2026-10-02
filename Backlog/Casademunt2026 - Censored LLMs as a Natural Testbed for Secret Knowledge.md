---
title: Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation
citekey: Casademunt2026
authors: Casademunt et al. 2026
year: 2026
published: 2026-03-05
venue: arXiv preprint
url: https://arxiv.org/abs/2603.05494
arxiv: '2603.05494'
pdf_url: https://arxiv.org/pdf/2603.05494
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: Naturally occurring concealment (Qwen3 censorship). Self-classification of own responses is compared with linear probes and an uncensored-model upper bound.
outcome: Prompting the censored model to classify its own responses performs near the uncensored-model upper bound; linear probes trained on unrelated data are a cheaper alternative; no technique fully eliminates false responses.
safety_use: direct
why: Self-report-as-lie-detector tested on non-synthetic dishonesty, with a white-box comparison.
summary: Uses Chinese open-weight models that produce falsehoods on politically sensitive topics while sometimes answering correctly. Sampling without a chat template, few-shot prompting and generic honesty fine-tuning most reliably increase truthfulness and transfer to DeepSeek R1.
found_by:
- search/intro-safety-uses-and-risks
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
