---
title: When Chain of Thought is Necessary, Language Models Struggle to Evade Monitors
citekey: Emmons2025
authors: Emmons et al. 2025
year: 2025
published: 2025-07-07
venue: arXiv preprint
url: https://arxiv.org/abs/2507.05246
arxiv: '2507.05246'
pdf_url: https://arxiv.org/pdf/2507.05246
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Chain-of-thought read by an LLM monitor, in tasks made hard enough that the bad behaviour requires CoT-as-computation
outcome: Hidden/bad behaviour that needs multi-step reasoning; models can obscure intent only with significant help (human-written strategies or iterative optimisation against the monitor)
timing: pre-action
why: 'Gives the condition under which reasoning is a reliable pre-action signal: necessity of CoT for the misbehaviour, not faithfulness in general'
summary: Distinguishes CoT-as-rationalisation from CoT-as-computation and argues monitorability, not faithfulness, is the property that matters for runtime monitoring. Replicating prior unfaithfulness setups with harder bad behaviour forces the model to expose its reasoning. Stress tests show models learn to obscure intentions only when given detailed human-written strategies or iterative optimisation against the monitor.
found_by:
- search/pred-cot-trajectory
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
