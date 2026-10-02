---
title: 'When Agents Go Rogue: Activation-Based Detection of Malicious Behaviors in Multi-Agent Systems'
citekey: XuH2026
authors: Xu et al. 2026
year: 2026
published: 2026-07-07
venue: arXiv preprint
url: https://arxiv.org/abs/2607.06807
arxiv: '2607.06807'
pdf_url: https://arxiv.org/pdf/2607.06807
topics:
- agent-to-agent-influence
- social-simulation
questions:
- Q14
- Q15
- Q18
status: processing
priority: 1
relevance: core
manipulation: 'white-box: distance of each agent''s final-layer activation from a benign prototype; detection then steers the agent back'
outcome: F1 0.92-0.95 vs 0.70-0.74 for a graph-based text baseline; in asynchronous MAS 0.92-0.94 vs 0.38-0.46
why: 'Closest existing system to a doctor-overseer: reads every agent''s activations, flags the compromised one and repairs it by steering instead of isolating it'
summary: 'FULL-TEXT (via summarising fetch). AcMAS scores each agent by cosine distance of its last-token final-layer state from a benign centroid (unsupervised, threshold-based, not an LLM overseer). On stealthy prompt injection, tool manipulation and memory poisoning across GPT-OSS-20B, DeepSeek-V3, Llama3-8B and Qwen3-30B: F1 0.92-0.95 vs G-Safeguard 0.70-0.74, AUROC 98.5-99.5, FPR 0.04-0.07; steering towards the prototype keeps task completion at 0.96-1.00 vs 0.68-0.83 for isolation. Needs open weights and 50-100 benign traces per domain; gradual adaptive drift untested.'
found_by:
- search/a2a-inspection-channels
- search/a2a-influence-channels
- search/sim-power-and-steering
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
