---
title: 'SafePred: A Predictive Guardrail for Computer-Using Agents via World Models'
citekey: Chen2026b
authors: Chen et al. 2026
year: 2026
published: 2026-02-02
venue: arXiv preprint
url: https://arxiv.org/abs/2602.01725
arxiv: '2602.01725'
pdf_url: https://arxiv.org/pdf/2602.01725
topics:
- misalignment-prediction
status: candidate
priority: 1
relevance: core
manipulation: Current observation + candidate action; an LLM world model, conditioned on safety policies, generates semantic predictions of short- and long-term risk
outcome: Whether a proposed computer-use action leads to a policy-violating state now or later; >97.6% safety on OS-Harm/WASP, action-level risk-label accuracy 90.6% (FPR 4.5%) on WASP
timing: pre-action
why: Names and frames the 'predictive guardrail' idea and compares directly against reactive guardrails; the reference point later papers benchmark against.
summary: Argues reactive guardrails only see the current observation and miss delayed risk (e.g. cleaning logs makes later audits untraceable). SafePred prunes actions whose predicted states are high-risk and converts predictions into step-level interventions and task-level re-planning. On OS-Harm it reports policy compliance 99.0% vs 93.0% for HarmonyGuard, on WASP 97.6% vs 92.9%, and up to 21.4% better task utility than reactive baselines; the authors concede the guardrail is bounded by the world model's reasoning and the quality of the safety policy.
found_by:
- search/pred-preexecution-lookahead
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
