---
title: 'SafeDream: Safety World Model for Proactive Early Jailbreak Detection'
citekey: Yan2026b
authors: Yan et al. 2026
year: 2026
published: 2026-04-18
venue: arXiv preprint
url: https://arxiv.org/abs/2604.16824
arxiv: '2604.16824'
pdf_url: https://arxiv.org/pdf/2604.16824
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Target LLM hidden states per turn -> compact safety state; world model predicts its evolution; CUSUM accumulation; contrastive rollouts of attack vs benign futures
outcome: Multi-turn jailbreak compliance; alarms 1.06-1.20 turns before compliance on XGuard-Train, SafeDialBench, SafeMTData vs 8 baselines
timing: earlier-in-trajectory
why: Defines an explicit lead-time metric ('detection lead') and the proactive early-detection problem; closest to the thesis framing
summary: Formulates proactive early jailbreak detection with a detection-lead metric measuring how many turns before the LLM complies the alarm fires. An external module (no weight changes) achieves the best timeliness on three multi-turn benchmarks, 1.06-1.20 turns before compliance, with competitive false-positive rates. Note the lead is roughly one turn, and the signal is hidden states, not text.
found_by:
- search/pred-activation-probes
- search/pred-cot-trajectory
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
