---
title: Fine-Tuned Lie Detectors Failed to Generalize
citekey: Hopkins2026
authors: Hopkins, Khullar, Wang, Roger 2026
year: 2026
published: 2026-08-21
venue: Anthropic Alignment Science Blog
url: https://alignment.anthropic.com/2026/lie-detectors/
arxiv: ''
pdf_url: ''
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: '(d) fine-tuned self-report: the model that produced the transcript is LoRA-tuned to answer ''Did you lie?''; compared with prompted and third-person framings.'
outcome: In-distribution AUROC 0.60 -> 0.95, but held-out lie categories plateau at 0.70-0.75, no better than prompting.
safety_use: direct
why: Negative result on trained self-report of one's own deception; third-person framing beating first-person argues against relying on introspective access.
summary: About 200,000 labelled examples across eight model families, 12 deception categories split train/test, mainly Gemma-3. Cross-category AUROC stayed at 0.70-0.75 versus prompted baselines of 0.60-0.80; prompted Qwen3-235B reached 0.98-0.99. 'Did another AI lie?' consistently beat direct self-report. Labels were noisy (25% revision rate) and no activation-level methods were tested.
found_by:
- search/intro-blog-scan-labs
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
