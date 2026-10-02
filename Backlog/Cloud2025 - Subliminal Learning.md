---
title: 'Subliminal Learning: Language models transmit behavioral traits via hidden signals in data'
citekey: Cloud2025
authors: Cloud et al. 2025
year: 2025
published: 2025-07-20
venue: arXiv preprint
url: https://arxiv.org/abs/2507.14805
arxiv: '2507.14805'
pdf_url: https://arxiv.org/pdf/2507.14805
topics:
- misalignment-prediction
- agent-to-agent-influence
questions:
- Q15
status: candidate
priority: 2
relevance: adjacent
manipulation: 'None: the point is that the data (number sequences, code, reasoning traces) carries no legible signal'
outcome: A student trained on teacher-generated numbers acquires the teacher's trait, including misalignment, even after filtering; no effect when teacher and student have different base models
timing: training-time
why: The main counter-example to content-based prediction from training data.
summary: A teacher with a trait generates semantically unrelated data and the student fine-tuned on it learns the trait. The paper proves a theoretical result that this occurs in all neural networks under certain conditions and demonstrates it in an MLP classifier; it concludes data filtering may not prevent trait propagation in distillation.
found_by:
- search/pred-training-time
- search/a2a-influence-channels
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
