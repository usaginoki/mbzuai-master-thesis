---
title: 'CATArena: Evaluating Evolutionary Capabilities of Code Agents via Iterative Tournaments'
citekey: Fu2025
authors: Fu et al. 2025
year: 2025
published: 2025-10-30
venue: arXiv preprint
url: https://arxiv.org/abs/2510.26852
arxiv: '2510.26852'
pdf_url: https://arxiv.org/pdf/2510.26852
topics:
- agent-competition
questions:
- Q20
- Q21.1
status: candidate
priority: 1
relevance: core
manipulation: Code agents write strategy code for Gomoku, Texas Hold'em, Bridge and Chess (plus ML and multi-language tracks). After each round every agent receives all participants' previous-round code, full rankings, win counts and match logs, then revises (peer-learning vs self-reflection).
outcome: Agents imitate peers in the first revision round; e.g. Doubao-Seed and DeepSeek-Chat 'simply copy Claude-4-Sonnet's strategy' in Hold'em. Learning scores are positive in simple games and mostly negative in Chess; agents struggle to use peer-learning and self-reflection together. Evolutionary potential is not strictly correlated with initial proficiency.
why: Full visibility of rivals' submissions and ranks is the default here, with copying documented; a direct precedent for the leaderboard arm, but visibility is never switched off and safety is not measured.
summary: Abstract plus fetched arXiv HTML (no numeric effect sizes extracted). Repo github.com/AGI-Eval-Official/CATArena has no licence file per the GitHub API.
found_by:
- search/comp-contexts
- search/comp-performance
- search/comp-design-angle
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
