---
title: Would this change your answer? Evaluating Explanations of LLM Behavior In The Wild with Counterfactual Experiments
citekey: Karvonen2026
authors: Karvonen et al. 2026
year: 2026
published: 2026-08-17
venue: arXiv preprint; Anthropic Alignment Science blog
url: https://arxiv.org/abs/2608.16747
arxiv: '2608.16747'
pdf_url: https://arxiv.org/pdf/2608.16747
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: Activation oracles, natural-language autoencoders and sparse autoencoders give a predictor read-only access to the target model's activations; (c) auditor tool, not used by the model on itself.
outcome: On naturally occurring behaviours, none of the three activation-reading tools improves prediction of counterfactual behaviour, across two target models and three predictor families.
safety_use: indirect
why: 'Bounds scope item 4: the instruments a model would query about itself add nothing on natural (non-implanted) behaviour, so a self-query tool is unlikely to carry private information.'
summary: ABSTRACT-ONLY plus search summary. Introduces CHIVE, an agentic pipeline that finds unexpected behaviours and tests explanations with counterfactual prompt edits. The same tools gave uplift in earlier auditing games on fine-tuned models.
found_by:
- search/intro-instrumented-feedback-rerun
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
