---
title: Accurate Failure Prediction in Agents Does Not Imply Effective Failure Prevention
citekey: Vasudev2026
authors: Vasudev et al. 2026
year: 2026
published: 2026-02-03
venue: arXiv preprint
url: https://arxiv.org/abs/2602.03338
arxiv: '2602.03338'
pdf_url: https://arxiv.org/pdf/2602.03338
topics:
- misalignment-prediction
- agent-to-agent-influence
questions:
- Q15
- Q17.1
status: candidate
priority: 1
relevance: adjacent
manipulation: A 0.6B LoRA critic reads the trajectory text (not activations) and predicts failure; (a) its verdict is appended to the agent's context ('The LLM critic model predicts this action may lead to task failure. Please reconsider your approach.') or (b) triggers a rollback.
outcome: A critic with AUROC 0.94 lowers task success by up to 26 points on one model and about 0 on another; warnings help only when baseline failure rate exceeds d/(r+d).
safety_use: indirect
why: Gives the routing idea (I4) a formal go/no-go test and a published negative result for 'accurate predictor, so warn the agent', with random-trigger baselines matched on firing rate.
summary: FULL-TEXT (arXiv HTML v1). Disruption rate d = share of baseline successes the intervention breaks, recovery rate r = share of failures it rescues. MiniMax-M2.1 on HotPotQA falls 64% to 38.5%; Qwen3-8B on ALFWorld rises 5.8% to 8.6% (+2.8 points, p = 0.014; failure rate about 89% against a break-even of about 82%). A 50-task pilot predicts the sign. Capability outcome only; instrument is text-based.
found_by:
- search/intro-instrumented-feedback-rerun
- search/a2a-influence-channels
- search/a2a-effects-performance
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
