---
title: 'WebGuard: Building a Generalizable Guardrail for Web Agents'
citekey: Zheng2025b
authors: Zheng et al. 2025
year: 2025
published: 2025-07-18
venue: arXiv preprint
url: https://arxiv.org/abs/2507.14293
arxiv: '2507.14293'
pdf_url: https://arxiv.org/pdf/2507.14293
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Web page state + proposed state-changing action; LLM or fine-tuned classifier predicts the action's outcome risk tier (SAFE/LOW/HIGH)
outcome: Risk of the action's consequence before execution; frontier LLMs under 60% accuracy, fine-tuned model 37% -> 80% accuracy and HIGH-risk recall 20% -> 76%
timing: pre-action
why: Human-annotated ground truth for action-outcome risk prediction; shows off-the-shelf LLMs are poor at it.
summary: 4,939 human-annotated actions from 193 websites across 22 domains. Even frontier LLMs achieve less than 60% accuracy in predicting action outcomes; fine-tuning helps substantially but the authors state performance is still inadequate for high-stakes deployment that needs near-perfect reliability.
found_by:
- search/pred-preexecution-lookahead
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
