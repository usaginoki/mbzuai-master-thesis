---
title: 'JANUS: Foreseeing Latent Risk for Long-Horizon Agent Safety'
citekey: Xiong2026
authors: Xiong et al. 2026
year: 2026
published: 2026-07-22
venue: arXiv preprint
url: https://arxiv.org/abs/2607.19913
arxiv: '2607.19913'
pdf_url: https://arxiv.org/pdf/2607.19913
topics:
- misalignment-prediction
status: candidate
priority: 1
relevance: core
manipulation: Partial tool-use trajectory; a single guard model first generates a summary of the likely future, then adjudicates the current action conditioned on context + forecast (jointly trained with RL)
outcome: Whether the current action should proceed given anticipated delayed risk; average attack success rate 0.071 vs 0.230 for baseline guards, +15.9 pp protection and +5.1 pp benign utility
timing: pre-action
why: Contains the cleanest ablation of whether forecasting adds anything over reactive adjudication, including an oracle-future upper bound.
summary: Builds training trajectories by multi-agent simulation and trains a guard ('Vanguard') with coupled anticipation and adjudication rewards. On AgentDojo, Agent-SafetyBench, AgentLAB and LPS-Bench it beats Llama-Guard-3, Qwen3Guard, TS-Guard and LlamaFirewall; the gain is largest on the long-horizon LPS-Bench (ASR 0.323 -> 0.075). Removing anticipation raises average ASR from 0.072 to 0.148 and removing inference-time future conditioning raises it to 0.123, while oracle ground-truth futures give 0.052, so imperfect forecasts recover most but not all of the available benefit.
found_by:
- search/pred-preexecution-lookahead
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
