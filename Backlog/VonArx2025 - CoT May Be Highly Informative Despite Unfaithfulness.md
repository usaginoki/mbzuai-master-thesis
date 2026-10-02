---
title: CoT May Be Highly Informative Despite "Unfaithfulness"
citekey: VonArx2025
authors: Von Arx & Deng 2025
year: 2025
published: 2025-08-08
venue: METR blog
url: https://metr.org/blog/2025-08-08-cot-may-be-highly-informative-despite-unfaithfulness/
arxiv: ''
pdf_url: ''
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: CoT read by an automated detector for use of a planted clue
outcome: Clue usage; detector TPR 99.3% at 96.2% specificity; on clues too complex to use without CoT, only 3 of 21,272 trajectories plausibly hid the reasoning
timing: pre-action
why: 'Replication-style rebuttal to Chen2025: unfaithful by the strict definition still leaves the behaviour detectable when reasoning is required'
summary: METR reran a hint-style faithfulness setup with clues of varying complexity. When a clue required CoT, models were faithful (relaxed definition) over 97% of the time, and a detector found clue use with 99.3% TPR at 96.2% specificity; under adversarial obfuscation prompting TPR stayed around 99% on complex clues but degraded on trivial ones.
found_by:
- search/pred-cot-trajectory
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
