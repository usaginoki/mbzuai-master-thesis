---
title: "The Hallucination Snowball: Modeling Error Propagation as State Transitions in Multi-Agent LLM Pipelines"
citekey: Singh2026
authors: "Singh and Pawar"
year: 2026
published: 2026-06-22
venue: "arXiv preprint"
url: https://arxiv.org/abs/2608.14588
arxiv: "2608.14588"
pdf_url: https://arxiv.org/pdf/2608.14588
topics:
- multiagent-friction
status: candidate
priority: 1
relevance: core
channel: "4-stage pipeline (analysis -> computation -> narrative -> editorial approval)"
manipulation: "Hallucination injected at stage 1"
outcome: "Markov model with per-boundary escape probabilities 24.6%, 48.3%, 89.3%; detection drops sharply by stage 4 (23.7% undetected for GPT-4o); early verification cuts survival 58.4% -> 16.2%"
why: "Shows downstream agents launder upstream errors, making them undetectable"
found_by:
- search/mas-error-propagation
cited_by: []
added: 2026-09-29
cited_by_count: 0
tags:
- type/candidate
---
