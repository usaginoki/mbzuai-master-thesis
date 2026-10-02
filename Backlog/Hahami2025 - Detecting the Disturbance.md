---
title: 'Detecting the Disturbance: A Nuanced View of Introspective Abilities in LLMs'
citekey: Hahami2025
authors: Hahami et al. 2025
year: 2025
published: 2025-12-13
venue: arXiv preprint
url: https://arxiv.org/abs/2512.12411
arxiv: '2512.12411'
pdf_url: https://arxiv.org/pdf/2512.12411
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: activation steering in Meta-Llama-3.1-8B-Instruct; yes/no detection vs sentence-localisation and strength-comparison tasks
outcome: Yes/no injection 'detection' is entirely explained by a global logit shift toward 'yes'; but localisation and strength discrimination are real, confined to early-layer injections.
safety_use: indirect
why: Shows both the artefact (yes-bias) and a cleaner test design; introspection is real but layer-dependent.
summary: Binary detection accuracy is an artefact of steering biasing affirmative answers regardless of question. On differential tasks the model localises which of 10 sentences was injected at up to 88% (10% chance) and discriminates relative injection strength at 83% (50% chance), but only for early-layer injections, collapsing to chance later. The same group's follow-up 'Introspection Fine-Tuning' (arXiv 2607.14111) raises Llama-1B localisation from 9.6% to 60.6% by training.
found_by:
- search/intro-capability
- search/intro-instrumented-feedback
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
