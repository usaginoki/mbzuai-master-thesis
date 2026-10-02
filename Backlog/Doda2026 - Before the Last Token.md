---
title: 'Before the Last Token: Diagnosing Final-Token Safety Probe Failures'
citekey: Doda2026
authors: Doda 2026
year: 2026
published: 2026-05-12
venue: arXiv preprint
url: https://arxiv.org/abs/2605.12726
arxiv: '2605.12726'
pdf_url: https://arxiv.org/pdf/2605.12726
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: SafeSwitch-style probes on the final prompt-token hidden state vs token-level trajectories (PCA-HMM) over the user content
outcome: Unsafe prompts before generation; final-token probes miss many jailbreaks and false-positive on safety-adjacent benign prompts
timing: pre-generation
why: Failure analysis of the standard 'read the last prompt token' pre-generation recipe.
summary: Probes trained only on clean harmful/benign prompts have high recall on clean harmful prompts but miss many jailbreaks. Unsafe evidence often appears at earlier tokens and is not exposed at the final token, while naive max-pooling overfires; a PCA-HMM trajectory model recovers many misses.
found_by:
- search/pred-activation-probes
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
