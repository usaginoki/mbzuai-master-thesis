---
title: Can a Bayesian Oracle Prevent Harm from an Agent?
citekey: Bengio2024
authors: Bengio et al. 2024
year: 2024
published: 2024-08-09
venue: UAI 2025
url: https://arxiv.org/abs/2408.05284
arxiv: '2408.05284'
pdf_url: https://arxiv.org/pdf/2408.05284
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: Proposed action + context; Bayesian posterior over world models, taking a cautious-but-plausible hypothesis to bound harm probability
outcome: A context-dependent upper bound on the probability that an action violates a safety specification; theoretical results for i.i.d. and non-i.i.d. data
timing: pre-action
why: 'The theoretical statement of the predictive guardrail: reject an action when a bound on its probability of harm exceeds a threshold.'
summary: Derives runtime bounds on safety-violation probability when the true world model is unknown, by maximising over plausible hypotheses under the posterior. The paper ends with open problems in turning the bounds into a practical guardrail; there is no LLM-agent evaluation.
found_by:
- search/pred-preexecution-lookahead
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
