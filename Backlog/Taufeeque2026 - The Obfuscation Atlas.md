---
title: 'The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes'
citekey: Taufeeque2026
authors: Taufeeque, Heimersheim et al. 2026 (FAR.AI)
year: 2026
published: 2026-02-17
venue: arXiv preprint / FAR.AI research page
url: https://www.far.ai/research/the-obfuscation-atlas-mapping-where-honesty-emerges-in-rlvr-with-deception-probes
arxiv: '2602.15515'
pdf_url: https://arxiv.org/pdf/2602.15515
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: White-box deception probe on the model's own activations used as a penalty in RL reward (training-time feedback, not shown in context).
outcome: Probe penalty alone mostly yields obfuscated policies; honesty emerges only with sufficiently high KL regularisation and detector penalty.
safety_use: risk
why: 'The key risk result for any loop that rewards a model on its own probe reading: it can learn to evade rather than behave.'
summary: 'Coding environment where models reward-hack by hardcoding tests. Two evasion routes are distinguished: obfuscated activations (representations shift) and obfuscated policy (text that fools the detector). Obfuscated activations are attributed to representation drift under RL rather than to the detector penalty specifically. No headline numbers were on the page I read.'
found_by:
- search/intro-blog-scan-labs
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
