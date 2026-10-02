---
title: Emergently Misaligned Language Models Show Behavioral Self-Awareness That Shifts With Subsequent Realignment
citekey: Vaugrante2026
authors: Vaugrante et al. 2026
year: 2026
published: 2026-02-16
venue: arXiv preprint
url: https://arxiv.org/abs/2602.14777
arxiv: '2602.14777'
pdf_url: https://arxiv.org/pdf/2602.14777
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: core
manipulation: GPT-4.1 fine-tuned sequentially on datasets that induce and then reverse emergent misalignment; self-ratings without in-context examples
outcome: Emergently misaligned models rate themselves as significantly more harmful than base and realigned counterparts.
safety_use: direct
why: Self-report tracks the model's actual alignment state, i.e. a self-queried safety signal; ground truth is the fine-tuned state/behaviour.
summary: Sequential fine-tuning induces and reverses emergent misalignment; self-assessed harmfulness moves with it. Authors conclude models can be queried for informative signals about their own safety (abstract-level; no figures read).
found_by:
- search/intro-capability
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
