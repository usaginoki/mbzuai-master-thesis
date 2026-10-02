---
title: 'DreamGuard: Efficient Runtime Guardrail for LLM Agents via Risk-Aware World Model'
citekey: Lin2026b
authors: Lin et al. 2026
year: 2026
published: 2026-08-06
venue: arXiv preprint
url: https://arxiv.org/abs/2608.05695
arxiv: '2608.05695'
pdf_url: https://arxiv.org/pdf/2608.05695
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Trajectory so far + proposed action, embedded by a frozen Qwen3-4B; a GRU-based recurrent state-space world model (RSSM) predicts future latent states and emits immediate-hazard and prefix-risk scores
outcome: Multi-horizon risk of the proposed action before execution; F1 96.4% on SafetyDrift, intervenes before the first hazard step in 96.3% of unsafe long-horizon trajectories, ~25 ms per call
timing: pre-action
why: Most direct evidence that a learned latent world model can beat both reactive guards and LLM-rollout predictive guards, at negligible latency.
summary: 'Trains an RSSM with a prediction loss, then adds risk supervision where precursor steps within horizon K get decayed positive targets. Evaluated on SafetyDrift, AgentDojo, Agent Security Bench and ASSE-Security (F1 96.4 / 74.9 / 82.1 / 82.9) against Llama-Guard-4, reactive guards (PolicyGuard, GuardAgent, AgentDoG-1.5) and proactive ones (SafePred, TRACES); reported as 250x faster than GuardAgent and 424x faster than SafePred. Limitation: thresholds are calibrated only on SafetyDrift and transferred zero-shot, and online safety rate is a more modest 72.92% at 90.38% utility.'
found_by:
- search/pred-preexecution-lookahead
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
