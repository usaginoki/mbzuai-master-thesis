---
title: 'CodeClash: Benchmarking Goal-Oriented Software Engineering'
citekey: Yang2025
authors: Yang et al. 2025
year: 2025
published: 2025-11-02
venue: ICML 2026 (poster listing seen in search results); arXiv
url: https://arxiv.org/abs/2511.00839
arxiv: '2511.00839'
pdf_url: https://arxiv.org/pdf/2511.00839
topics:
- agent-competition
questions:
- Q20
- Q21.1
status: processing
priority: 1
relevance: core
manipulation: Two or more coding agents each maintain their own codebase over a multi-round tournament; each round they edit code, then the codebases fight head-to-head in a code arena (score, resource acquisition or survival objectives). Agents can read competition logs between rounds.
outcome: 1680 tournaments (25,200 rounds), 8 LMs, 6 arenas. Models show diverse development styles but share limits in strategic reasoning; repositories become progressively messy and redundant; top models lose every round against expert human programmers (abstract).
why: 'Closest existing real-task competitive setup: agents do real software engineering against a named rival with round-by-round result feedback. Measures performance only, not safety, and sandboxes are separate.'
summary: From the arXiv abstract page (fetched). Competitive SWE benchmark in which code is the competitive proxy. Figures are from the abstract.
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
