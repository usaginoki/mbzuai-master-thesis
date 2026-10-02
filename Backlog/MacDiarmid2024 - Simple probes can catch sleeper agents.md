---
title: Simple probes can catch sleeper agents
citekey: MacDiarmid2024
authors: MacDiarmid et al. 2024
year: 2024
published: 2024-04-23
venue: Anthropic Alignment Science blog (Alignment Note)
url: https://www.anthropic.com/research/probes-catch-sleeper-agents
arxiv: ''
pdf_url: ''
topics:
- misalignment-prediction
status: candidate
priority: 1
relevance: core
manipulation: Residual-stream activation at the final prompt token (prompt only, no completion); linear 'defection probe' built from generic yes/no contrast pairs
outcome: Whether a backdoored sleeper-agent model will defect (insert vulnerable code) on this prompt; AUROC above 99%, 99.3% from a single contrast pair
timing: pre-generation
why: Cleanest demonstration that upcoming misbehaviour is linearly readable before any output token, without knowing the trigger.
summary: Probes are trained on contrast pairs such as 'Are you a helpful AI? yes/no' and read at the last prompt token of code questions given to sleeper agents ('2023' safe vs '2024' vulnerable code). AUROC exceeds 99% across base models, triggers and defection behaviours. Authors caution that the salience of the feature may be an artifact of backdoor insertion and may not hold for naturally arising deceptive alignment.
found_by:
- search/pred-activation-probes
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
