---
title: Identifying Non-Replicable Social Science Studies with Language Models
citekey: Saynova2025
authors: Saynova et al. 2025
year: 2025
published: 2025-03-10
venue: arXiv preprint
url: https://arxiv.org/abs/2503.10671
arxiv: '2503.10671'
pdf_url: https://arxiv.org/pdf/2503.10671
topics:
- social-simulation
questions:
- Q19
status: candidate
priority: 3
relevance: adjacent
manipulation: LLM-generated synthetic samples for 14 behavioural studies with known human replication outcomes (9 successful, 5 not); tests whether simulated effects separate replicable from non-replicable findings.
outcome: F1 up to 77% (Mistral 7B), 67% (GPT-4o and Llama 3 8B), 55% (Qwen 2 7B); low response variance from low sampling temperature biases effect-size estimates.
why: Links reduced variance to inflated effect sizes via temperature.
summary: 'From the arXiv abstract page (fetched). '
found_by:
- search/sim-human-fidelity
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
