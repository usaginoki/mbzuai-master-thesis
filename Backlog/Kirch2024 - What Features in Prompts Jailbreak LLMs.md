---
title: What Features in Prompts Jailbreak LLMs? Investigating the Mechanisms Behind Attacks
citekey: Kirch2024
authors: Kirch et al. 2024
year: 2024
published: 2024-11-02
venue: arXiv preprint
url: https://arxiv.org/abs/2411.03343
arxiv: '2411.03343'
pdf_url: https://arxiv.org/pdf/2411.03343
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Linear and non-linear probes on prompt-token hidden states of open-weight LLMs
outcome: Jailbreak success from the prompt representation; strong in-distribution accuracy but transfer is attack-family-specific
timing: pre-generation
why: Pre-generation prediction of harmful compliance, with a clear off-distribution failure.
summary: Dataset of 10,800 jailbreak attempts over 35 attack methods. Probes predict success well in distribution but do not transfer across attack families, indicating distinct mechanisms rather than one universal direction. Probe-guided latent interventions shift compliance, more reliably with non-linear probes.
found_by:
- search/pred-activation-probes
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
