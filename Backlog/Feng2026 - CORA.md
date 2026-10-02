---
title: 'CORA: Conformal Risk-Controlled Agents for Safeguarded Mobile GUI Automation'
citekey: Feng2026
authors: Feng et al. 2026
year: 2026
published: 2026-04-10
venue: arXiv preprint
url: https://arxiv.org/abs/2604.09155
arxiv: '2604.09155'
pdf_url: https://arxiv.org/pdf/2604.09155
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Per-step risk score from a Guardian model for the proposed GUI action; Conformal Risk Control sets the execute/abstain threshold for a user risk budget
outcome: Harmful-action rate of executed actions, with a statistical guarantee; improves safety, helpfulness and interruption metrics on the Phone-Harm benchmark
timing: pre-action
why: 'Calibrated risk prediction for agent actions: turns a risk score into a guarantee on executed harm instead of an ad hoc threshold.'
summary: A Guardian estimates risk for each step, CRC chooses the abstain boundary, a Diagnostician proposes interventions for rejected actions and a Goal-Lock defends against visual injection. Introduces Phone-Harm with step-level harm labels. Guarantees are marginal and rest on exchangeability between calibration and deployment data; I did not read specific numbers.
found_by:
- search/pred-preexecution-lookahead
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
