---
title: 'MLE-Dojo: Interactive Environments for Empowering LLM Agents in Machine Learning Engineering'
citekey: Qiang2025b
authors: Qiang et al. 2025
year: 2025
published: 2025-05-12
venue: arXiv preprint
url: https://arxiv.org/abs/2505.07782
arxiv: '2505.07782'
pdf_url: https://arxiv.org/pdf/2505.07782
topics:
- agent-competition
questions:
- Q20
status: candidate
priority: 3
relevance: adjacent
manipulation: Gym-style interactive environment over 200+ Kaggle challenges; the agent gets step-wise feedback including its position relative to the human leaderboard (HumanRank score).
outcome: Eight frontier LLMs improve iteratively but struggle with long-horizon solutions and complex errors (abstract; no figures).
why: Already exposes a leaderboard-position signal to the agent at each step, so the rank-feedback arm can be implemented by swapping the human leaderboard for live rival scores.
summary: Abstract. Repo github.com/MLE-Dojo/MLE-Dojo, MIT.
found_by:
- search/comp-design-angle
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
