---
title: 'Doomed from the Start: Early Abort of LLM Agent Episodes via a Recall-Controlled Probe Cascade'
citekey: RuanK2026
authors: Ruan et al. 2026
year: 2026
published: 2026-07-07
venue: arXiv preprint
url: https://arxiv.org/abs/2607.06503
arxiv: '2607.06503'
pdf_url: https://arxiv.org/pdf/2607.06503
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: Linear probes on the agent's hidden states at each early interaction round, with distribution-free calibrated recall control
outcome: Eventual task failure from the first round; 60.2% (TextCraft) and 54.9% (WebShop) fewer generated tokens at 90% recall
timing: earlier-in-trajectory
why: Evidence that internal state predicts the outcome earlier than behaviour-only monitors; adding behavioural features gave no further gain
summary: Probes predict eventual failure from the first interaction round on TextCraft and WebShop with small open models, earlier than behaviour-only monitoring, which is consistently weaker. Calibrated cascade keeps achieved recall within one standard deviation of target in all 24 configurations. Capability failure, not misalignment. First author Kai Ruan; a different paper from the vault's Ruan2026 (SchemeArena).
found_by:
- search/pred-cot-trajectory
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
