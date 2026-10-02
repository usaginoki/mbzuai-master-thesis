---
title: Revealing Hidden Model Behaviors with Task-Specific Self-Reports
citekey: Kutsyk2026
authors: Kutsyk et al. 2026
year: 2026
published: 2026-07-03
venue: arXiv preprint
url: https://arxiv.org/abs/2607.03640
arxiv: '2607.03640'
pdf_url: https://arxiv.org/pdf/2607.03640
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: 'Stabilized Adapter for self-Report (SAR): a LoRA adapter trained using only the fine-tuned model and its training dataset to make it describe its hidden behaviour. Validated against known implanted behaviours; hallucinated reports are counted.'
outcome: SAR detects the hidden behaviour in all seven implanted settings, including broad emergent misalignment not predictable from the data; introspection adapters miss some and then hallucinate wrong behaviours; SAR roughly halves the hallucination rate.
safety_use: direct
why: Documents the main failure mode of trained self-report (confident hallucinated self-descriptions) and a fix.
summary: Across seven implanted behaviours (e.g. false answers under a narrow condition, topic-triggered harmful advice) SAR finds every one, while the introspection-adapter baseline misses some entirely and consistently reports wrong behaviours where it misses. SAR roughly halves hallucinations.
found_by:
- search/intro-safety-uses-and-risks
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
