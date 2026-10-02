---
title: 'AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors'
citekey: Sheshadri2026
authors: Sheshadri et al. 2026
year: 2026
published: 2026-02-26
venue: arXiv preprint (Anthropic)
url: https://arxiv.org/abs/2602.22755
arxiv: '2602.22755'
pdf_url: https://arxiv.org/pdf/2602.22755
topics:
- misalignment-prediction
- agent-to-agent-influence
questions:
- Q14
- Q15
- Q16
- Q17.2
status: candidate
priority: 3
relevance: adjacent
manipulation: Investigator agent with configurable black-box and white-box auditing tools
outcome: Detection of implanted hidden behaviours in 56 models (14 behaviour types)
timing: pre-deployment
why: Measures the recall of pre-deployment audits, which bounds how far a clean audit predicts clean deployment
summary: Finds a tool-to-agent gap, black-box scaffolded prompting beating white-box tools, and adversarially trained organisms being much harder to audit. No detection rates were read.
found_by:
- search/pred-eval-to-deployment
- search/a2a-doctor-overseer
- search/a2a-inspection-channels
- search/a2a-influence-channels
- search/a2a-inclination
- search/a2a-effects-safety
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
