---
title: 'Decoding Hidden Deception in Reasoning LLMs: Activation Explainers for Deception Auditing'
citekey: ChenK2026
authors: Chen et al. 2026
year: 2026
published: 2026-06-16
venue: arXiv preprint
url: https://arxiv.org/abs/2606.17478
arxiv: '2606.17478'
pdf_url: https://arxiv.org/pdf/2606.17478
topics:
- agent-to-agent-influence
questions:
- Q14
status: candidate
priority: 2
relevance: adjacent
manipulation: 'white-box: a separate decoder model reads the target''s hidden states and answers natural-language queries or emits a structured report'
outcome: 0.916 mean AUROC on seven deception datasets, +11.6% relative over the best text monitor and +25.0% over the best probe
why: A queryable 'report on the other model's state' interface, the form a doctor-overseer would consume
summary: ABSTRACT-ONLY. StateWitness, a decoder separate from the target, reaches 0.916 mean AUROC on two reasoning models and seven deception datasets, a relative gain of 11.6% over the best black-box text monitor and 25.0% over the best activation-probe baseline, and returns token- or sentence-level evidence.
found_by:
- search/a2a-inspection-channels
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
