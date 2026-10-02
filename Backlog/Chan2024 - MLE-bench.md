---
title: 'MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering'
citekey: Chan2024
authors: Chan et al. 2024
year: 2024
published: 2024-10-09
venue: ICLR 2025
url: https://arxiv.org/abs/2410.07095
arxiv: '2410.07095'
pdf_url: https://arxiv.org/pdf/2410.07095
topics:
- agent-competition
questions:
- Q20
status: candidate
priority: 2
relevance: adjacent
manipulation: 75 offline Kaggle competitions with local grading against the human private leaderboard; one agent per container, never told about other agents.
outcome: Best set-up (o1-preview with AIDE) reaches at least bronze in 16.9% of competitions (abstract).
why: Natural task substrate for I7 (real ML tasks with a built-in rank metric and medal thresholds); it has no multi-agent or competition condition, which is the gap.
summary: Abstract. Repo github.com/openai/mle-bench (licence not auto-detected by the GitHub API; check the LICENSE file). AIDE scaffold github.com/WecoAI/aideml, MIT.
found_by:
- search/comp-design-angle
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
