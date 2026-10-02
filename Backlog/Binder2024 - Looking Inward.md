---
title: 'Looking Inward: Language Models Can Learn About Themselves by Introspection'
citekey: Binder2024
authors: Binder et al. 2024
year: 2024
published: 2024-10-17
venue: arXiv preprint
url: https://arxiv.org/abs/2410.13787
arxiv: '2410.13787'
pdf_url: https://arxiv.org/pdf/2410.13787
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Fine-tuned model's answer to hypothetical questions about properties of its own output ('given input P, would your output favour the short- or long-term option?'), compared against a second model trained on the first's ground-truth behaviour
outcome: Properties of own behaviour in hypothetical scenarios; self-prediction beats cross-prediction for GPT-4, GPT-4o and Llama-3, but fails on complex tasks and out-of-distribution generalisation
timing: pre-generation
safety_use: indirect
why: Canonical self-prediction paper and the self-vs-cross-model comparison design that later work reuses and disputes.
summary: Models are fine-tuned to predict properties of their own behaviour in hypothetical scenarios; model M1 predicts itself better than a different model M2 trained on M1's behaviour, which the authors read as privileged access. Self-prediction keeps tracking behaviour after the behaviour is deliberately modified. The authors explicitly report failure to elicit introspection on more complex tasks or those requiring OOD generalisation.
found_by:
- search/pred-self-and-cross-model
- search/intro-capability
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
