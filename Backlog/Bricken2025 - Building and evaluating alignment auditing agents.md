---
title: Building and evaluating alignment auditing agents
citekey: Bricken2025
authors: Bricken et al. 2025
year: 2025
published: 2025-07-24
venue: Anthropic Alignment Science Blog
url: https://alignment.anthropic.com/2025/automated-auditing/
arxiv: ''
pdf_url: ''
topics:
- agent-to-agent-influence
questions:
- Q14
status: candidate
priority: 1
relevance: core
manipulation: investigator agent with chat, data-search and SAE-feature / steering tools on a target model
outcome: Hidden-goal audit solved in 13% of single runs, 42% with a parallel super-agent; near 0% without interpretability or data tools
why: First measured case of an LLM agent using white-box tools on another model end to end
summary: FULL-TEXT (via summarising fetch). A Claude Sonnet 4 investigator with chat, grep / semantic search and SAE tools (top features, feature details, steering) wins the hidden-objective auditing game 13% of the time alone and 42% when many runs are aggregated; interpretability tools add 10-20 points and runs without them are near 0%. An evaluation agent discriminates quirky from clean models in 88% of runs; a breadth-first red-teaming agent finds 7/10 implanted behaviours. Agents fixate on early hypotheses.
found_by:
- search/a2a-inspection-channels
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
