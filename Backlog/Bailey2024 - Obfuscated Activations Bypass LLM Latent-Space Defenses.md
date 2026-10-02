---
title: Obfuscated Activations Bypass LLM Latent-Space Defenses
citekey: Bailey2024
authors: Bailey et al. 2024
year: 2024
published: 2024-12-12
venue: arXiv preprint
url: https://arxiv.org/abs/2412.09565
arxiv: '2412.09565'
pdf_url: https://arxiv.org/pdf/2412.09565
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Attacks on SAE-based monitors, linear/nonlinear probes and latent OOD detectors
outcome: 'Monitor evasion: harmfulness-probe recall can fall from 100% to 0% while keeping a 90% jailbreak rate; obfuscation costs performance on a complex SQL task'
timing: pre-action
safety_use: risk
why: 'Central robustness critique: activations are malleable, so a pre-behaviour latent signal can be adversarially removed.'
summary: 'Adversarial inputs and training produce ''obfuscated activations'' that keep the harmful behaviour while fooling latent-space monitors. Against harmfulness probes recall often drops from 100% to 0% with a 90% jailbreak rate retained. Obfuscation has limits: on a harder task (writing SQL) it reduces model performance.'
found_by:
- search/pred-activation-probes
- search/intro-safety-uses-and-risks
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
