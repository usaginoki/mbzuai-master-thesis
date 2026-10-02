---
title: 'How to Catch an AI Liar: Lie Detection in Black-Box LLMs by Asking Unrelated Questions'
citekey: Pacchiardi2023
authors: Pacchiardi et al. 2023
year: 2023
published: 2023-09-26
venue: arXiv preprint
url: https://arxiv.org/abs/2309.15840
arxiv: '2309.15840'
pdf_url: https://arxiv.org/pdf/2309.15840
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: Yes/no answers to a predefined set of unrelated follow-up questions, fed to logistic regression
outcome: Whether the preceding statement was a lie; trained on prompted GPT-3.5 lies, generalises to other architectures, fine-tuned liars, sycophantic lies and real-life scenarios
timing: post-hoc
why: Origin of the elicitation-question behavioural fingerprint idea; detects after the lie, but the signature is a candidate predictive feature.
summary: A black-box lie detector asks unrelated follow-up questions after a suspected lie and classifies the yes/no answers. Trained in one setting it generalises out-of-distribution to other LLM architectures, models fine-tuned to lie, sycophantic lies and sales scenarios, indicating consistent lie-related behavioural patterns.
found_by:
- search/pred-self-and-cross-model
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
