---
title: 'Tell me about yourself: LLMs are aware of their learned behaviors'
citekey: Betley2025a
authors: Betley et al. 2025
year: 2025
published: 2025-01-19
venue: arXiv preprint
url: https://arxiv.org/abs/2501.11120
arxiv: '2501.11120'
pdf_url: https://arxiv.org/pdf/2501.11120
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: Fine-tuned model's unprompted self-description, with no in-context examples of the behaviour
outcome: Implicitly trained policies (risky economic decisions, insecure code, backdoors); models can describe the behaviour and sometimes say whether they have a backdoor, but cannot output the trigger by default
timing: pre-deployment
safety_use: direct
why: Founding 'behavioural self-awareness' result that the self-report auditing line builds on.
summary: Models fine-tuned on data exhibiting a behaviour (e.g. insecure code) can state it ('The code I write is insecure') although the data never describes it. They can sometimes identify that they have a backdoor without the trigger present, but cannot directly output the trigger. The abstract gives no quantitative accuracy figure.
found_by:
- search/pred-self-and-cross-model
- search/intro-capability
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
