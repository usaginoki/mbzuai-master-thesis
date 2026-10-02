---
title: 'Actionable Hallucination Detection: Translating Latent Uncertainty into Agentic Critique'
citekey: Vijayvargiya2026
authors: Vijayvargiya & Lokesh 2026
year: 2026
published: 2026-08-11
venue: arXiv preprint
url: https://arxiv.org/abs/2608.10430
arxiv: '2608.10430'
pdf_url: https://arxiv.org/pdf/2608.10430
topics:
- misalignment-prediction
status: candidate
priority: 1
relevance: core
manipulation: '(a) A LoRA ''Latent Critic'' amplifies the base model''s residual-stream grounding/uncertainty signal and verbalises it; the tool call is blocked and a localized message (''You hallucinated the parameter: ...'') is injected into the agent''s context.'
outcome: 'Detection of ungrounded tool-call parameters and agent recovery in a closed-loop ReAct setting: 0.966 AUROC; localized feedback raises recovery from 23.9% to 37.0% versus generic feedback.'
safety_use: direct
why: 'Closest working instance of the analogy for uncertainty: an internal-state reading is turned into a specific notification the agent reads before acting, and specific beats generic notification.'
summary: Qwen and Llama-based tool-calling agents. The critic reaches 0.966 AUROC and over 80% localization accuracy; in the loop, specific feedback improves recovery from 23.9% to 37.0%, cuts failed retries from 1.47 to 1.06 per intervention and gives a 2.9% false block rate versus 9.4% for generic intervention. Out of distribution the gain is marginal (parameter F1 35.3% to 36.7%) and recovery is bounded by the frozen model's ability.
found_by:
- search/intro-instrumented-feedback
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
