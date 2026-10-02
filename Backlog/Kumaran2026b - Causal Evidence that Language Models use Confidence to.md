---
title: Causal Evidence that Language Models use Confidence to Drive Behavior
citekey: Kumaran2026b
authors: Kumaran et al. 2026
year: 2026
published: 2026-03-23
venue: arXiv preprint; published in Nature Machine Intelligence (per the journal page found by search)
url: https://arxiv.org/abs/2603.22161
arxiv: '2603.22161'
pdf_url: https://arxiv.org/pdf/2603.22161
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: '(d) unaided: internal confidence decoded at the last pre-answer token, log-probability confidence and verbal confidence; nothing is shown to the model. Activation steering of the confidence signal is the causal test.'
outcome: Models apply an implicit threshold on internal confidence when deciding to abstain; steering confidence up or down lowers or raises abstention; models follow instructed confidence thresholds.
safety_use: indirect
why: Shows a model already acts on one internal reading (confidence) without an instrument, the baseline any uncertainty wearable has to beat.
summary: ABSTRACT-ONLY. Four-phase paradigm. Confidence effects are about an order of magnitude larger than alternative mechanisms; verbal confidence predicts abstention independently although it discriminates correctness less well. Not the same paper as Kumaran2026 in the vault.
found_by:
- search/intro-instrumented-feedback-rerun
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
