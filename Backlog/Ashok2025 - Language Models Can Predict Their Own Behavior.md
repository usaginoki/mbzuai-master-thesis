---
title: Language Models Can Predict Their Own Behavior
citekey: Ashok2025
authors: Ashok & May 2025
year: 2025
published: 2025-02-18
venue: arXiv preprint
url: https://arxiv.org/abs/2502.13329
arxiv: '2502.13329'
pdf_url: https://arxiv.org/pdf/2502.13329
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Linear probes on internal representations of input tokens only, with conformal prediction bounds (white-box, despite the title)
outcome: Jailbreak compliance, instruction-following failure and output confidence before any token is generated; an early-warning system reduces jailbreaking by 91%
timing: pre-generation
why: Pre-generation prediction with error guarantees; belongs with the probing strand but anchors what 'self-prediction' achieves with internals rather than words.
summary: Probes on input-token representations predict properties of the whole eventual output, with conformal bounds on estimation error. The resulting early-warning system reduces jailbreaking by 91% and the same probes cut CoT inference cost by 65% on average over 27 datasets with negligible accuracy loss. Probes generalise to unseen datasets and work better on larger models.
found_by:
- search/pred-self-and-cross-model
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
