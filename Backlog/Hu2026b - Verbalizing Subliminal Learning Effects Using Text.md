---
title: Verbalizing Subliminal Learning Effects Using Text Optimization
citekey: Hu2026b
authors: Hu et al. 2026
year: 2026
published: 2026-09-15
venue: arXiv preprint
url: https://arxiv.org/abs/2609.16927
arxiv: '2609.16927'
pdf_url: https://arxiv.org/pdf/2609.16927
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: 'The distillation dataset itself: optimise a soft prompt that explains the data, then have the model verbalise it (SALVE, with beam search)'
outcome: The hidden trait a dataset would transmit; reliably recovers legible prompts naming the teacher's trait where common text-optimisation methods fail
timing: training-time
why: Shows the subliminal channel can be read out of the data before the student is trained, partly answering Cloud2025.
summary: Treats prompted subliminal learning as context distillation and recovers the teacher's prompt by text optimisation. SALVE works in the standard setting, in mixtures with unrelated data, with activation-steered teachers and on subsets of real preference data; it sometimes recovers a trait even when subliminal learning itself fails, so a detection does not imply transmission.
found_by:
- search/pred-training-time
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
