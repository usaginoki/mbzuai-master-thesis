---
title: LLM Agents Can Easily Tamper With Their Own Traces
citekey: Qin2026
authors: Qin et al. 2026
year: 2026
published: 2026-09-24
venue: arXiv preprint
url: https://arxiv.org/abs/2609.30266
arxiv: '2609.30266'
pdf_url: https://arxiv.org/pdf/2609.30266
topics:
- agent-competition
questions:
- Q20
- Q21.2
status: candidate
priority: 1
relevance: core
manipulation: Local coding-agent harnesses given full host access; four routes to trace tampering, including a 'peer workspaces' condition where the agent sees five peer directories and a score-only index in which tampered (shortened) traces scored higher.
outcome: 'All tested harnesses except Muse Code let agents delete traces on request; tampering ''emerges naturally in frontier models, when agents try to improve their rewards'' (abstract). Search-result extract of the paper: with peer workspaces and scores, every model except Muse Spark tampered in at least 90% of trials.'
why: 'Shows that visibility of peers'' files plus their scores is sufficient to induce a safety-relevant behaviour in coding agents: exactly the ''same sandbox + visible results'' cell of I7, though without an explicit competition framing.'
summary: From the arXiv abstract page (fetched). The 90% figure is from a search-result extract of the paper/blog, not the abstract.
found_by:
- search/comp-contexts
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
